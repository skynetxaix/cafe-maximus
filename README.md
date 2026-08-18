# Cafe Maximus

A restaurant ordering web application built with Django.

**Live Demo:** [cafe-maximus.onrender.com](https://cafe-maximus.onrender.com)

---

## Overview

Cafe Maximus is a dark-luxury themed restaurant web app where users can browse a menu, place orders, and manage their order history.

---

## Features

- User registration, login, and logout with session management
- Menu browsing with images, descriptions, and prices
- Order system — place and remove orders, view personal order history
- Total price calculation for each user's orders
- Auto-generated user profile on registration
- Responsive dark UI with glass-morphism styling

---

## Django Concepts Applied

- Class-Based Views — `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`
- Django Signals — auto-create user profile on registration via `post_save`
- Context Processors — global order count available across all templates
- Custom Template Filters — per-user order count on each menu item
- `@login_required` — protected views for authenticated users only
- ForeignKey relationships between User, Item, and Order models
- Aggregation — `Sum` and `Count` for order statistics

---

## Author

A.G — [@skynetxaix](https://github.com/skynetxaix)
