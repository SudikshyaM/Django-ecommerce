from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.auth import admin_only
from users.models import Order
from django.contrib.auth.models import User
# Create your views here.

@login_required
@admin_only
def dashboard(request):
    return render(request,'admins/dashboard.html')

@login_required
@admin_only
def order(request):
    items=Order.objects.all()
    context={
        'items':items
    }
    return render(request,'admins/order.html',context)

@login_required
@admin_only
def users(request):
    users=User.objects.all()
    context={
        'users':users
    }
    return render(request,'admins/users.html',context)
