from django.shortcuts import render ,redirect , get_object_or_404
from .models import Item ,Order
from .forms import ItemForm
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Sum
# Create your views here.
# def index (request):
#     item_list=Item.objects.all()

#     context={
#         'item_list':item_list
#         }
#     return render(request,'food/index.html',context)


@method_decorator(never_cache, name='dispatch')
class IndexClassView(ListView):
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'


def items (request):
    return HttpResponse('<h1>this is an item i dont know why i type it?!</h1>')

def detail(request,item_id):
    item=get_object_or_404(Item,pk=item_id)
    return render(request,'food/detail.html',{'item':item})


class detailview():
    model=Item
    template_name='food/detail.html'
    context_object_name='item'

class FoodDetail (DetailView):
    model=Item
    template_name='food/detail.html'
    context_object_name = 'item'

def home(request):
    return render(request,'food/home.html')

# def add_item (request):
#     if request.method=='POST':
#         form=ItemForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect ("food:index")
#     else:
#         form=ItemForm()
#     return render(request, 'food/add_item.html',{'form':form})
# # this is a class base view (cbv)

class CreateItem(CreateView):
    model=Item
    fields=['item_name','item_desc','item_price','item_image']
    tampalte_name= 'food/add_item.html'
    success_url=reverse_lazy ('food:index')
    def form_valid(self,form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)


# def update_item(request,id):
    
#     item=Item.objects.get(id=id)
#     form= ItemForm(request.POST or None, instance=item)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
    
#     return render(request,'food/item_form.html',{'form':form,'item':item})

class UpdateItem(UpdateView):
    model=Item
    fields=['item_name','item_desc','item_price','item_image']
    template_name='food/item_form.html'
    success_url=reverse_lazy('food:index' )


# def delete_item (request, id):


#     item=Item.objects.get(id=id)

#     if request.method=="POST":
#         item.delete()
#         return redirect ('food:index')
#     return render (request,'food/item_delete.html',{'item':item})

        
class DeleteItem (DeleteView):
    model=Item
    template_name='food/item_delete.html'
    success_url= reverse_lazy ('food:index')


@login_required
def Order_item(request, pk):
    item= get_object_or_404(Item, pk=pk)
    Order.objects.create(
        user=request.user,
        orderd_item=item
    )
    return redirect('food:index')

class IndexClassView (ListView):
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'
    
    
class Order_list (ListView):
    model=Order
    template_name='food/orders.html'
    context_object_name= 'order_list'
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
from django.db.models import Count, Sum

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            orders = Order.objects.filter(
                user=self.request.user
            ).values('orderd_item_id').annotate(count=Count('id'))
            
            context['orders_per_item'] = {o['orderd_item_id']: o['count'] for o in orders}
        else:
            context['orders_per_item'] = {}
        return context



# class Delete_order(DeleteView):
#     model=Order
#     template_name='food/orders.html'
#     success_url=reverse_lazy ('food:orders')

def delete_order(request,pk):
    order=get_object_or_404(Order,pk=pk,user=request.user)
    order.delete()
    return redirect('food:Orders')