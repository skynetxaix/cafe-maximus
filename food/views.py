from django.shortcuts import render ,redirect , get_object_or_404
from .forms import ItemForm
from django.http import HttpResponse
from . models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.
def index (request):
    item_list=Item.objects.all()

    context={
        'item_list':item_list
        }
    return render(request,'food/index.html',context)

class IndexClassView(ListView):
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'


def items (request):
    return HttpResponse('<h1>this is an item i dont know why i type it?!</h1>')

def detail(request,item_id):
    item=get_object_or_404(Item,pk=item_id)
    return render(request,'food/detail.html',{'item':item})

class FoodDetail (DetailView):
    model=Item
    template_name='food/detail.html'
    context_object_name = 'item'

def home(request):
    return render(request,'food/home.html')

def add_item (request):
    if request.method=='POST':
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ("food:index")
    else:
        form=ItemForm()
    return render(request, 'food/add_item.html',{'form':form})
# this is a class base view (cbv)
class CreateItem(CreateView):
    model=Item
    fields=['item_name','item_desc','item_price','item_image']
    template_name='food/item_form.html'
    success_url = reverse_lazy('food:index')  # ← این رو اضافه کن

    def form_valid(self,form):
        form.instance.user_name=self.request.user

        return super().form_valid(form)

def update_item(request,id):
    
    item=Item.objects.get(id=id)
    form= ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item_forms.html',{'form':form,'item':item})

def delete_item (request, id):


    item=Item.objects.get(id=id)

    if request.method=="POST":
        item.delete()
        return redirect ('food:index')
    return render (request,'food/item_delete.html',{'item':item})

        

