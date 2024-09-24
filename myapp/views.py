from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Product,Chai,Category
from .forms import ProductForm,CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.auth import admin_only
# Create your views here.

def all_chai(request):
    chais=Chai.objects.all()
    context={
        'chais':chais
    }
    return render(request,'myapp/all_chai.html',context)

def chaistore(request):
    return render(request,'myapp/ChaiStores.html')

@login_required
@admin_only
def index(request):
    # fetch data from the table
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'myapp/product.html',context)

def desc(request,chai_id):
    chai=get_object_or_404(Chai,pk=chai_id)
    return render(request,'myapp/details.html',{'chais':chai})

@login_required
@admin_only
def post_product(request):
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Product added successfylly')
            return redirect('/myapp/product')
        else:
            messages.add_message(request,messages.ERROR,'Failed to add product')
            return render(request,'myapp/addProduct.html',{'form':form})
    context={
        'form':ProductForm
    }
    return render(request,'myapp/addProduct.html',context)

@login_required
@admin_only
def update(request,product_id):
    instances=Product.objects.get(pk=product_id)
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES,instance=instances)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Product updated successfylly')
            return redirect('/myapp/product')
        else:
            messages.add_message(request,messages.ERROR,'Failed to update product')
            return render(request,'myapp/updateProduct.html',{'form':form})
    context={
        'form':ProductForm(instance=instances)
    }
    return render(request,'myapp/updateProduct.html',context)

@login_required
@admin_only
def delete(request,product_id):
    product=Product.objects.get(pk=product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'deleted successfully')
    return redirect('/myapp/product')

@login_required
@admin_only
def post_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category added successfylly')
            return redirect('/myapp/addcategory')
        else:
            messages.add_message(request,messages.ERROR,'Failed to add category')
            return render(request,'myapp/addCategory.html',{'form':form})
    context={
        'form':CategoryForm
    }
    return render(request,'myapp/addCategory.html',context)

@login_required
@admin_only   
def show_category(request):
    category=Category.objects.all()
    context={
        'category':category
    }
    return render(request,'myapp/showCategory.html',context)

@login_required
@admin_only
def update_category(request,category_id):
    instances=Category.objects.get(pk=category_id)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=instances)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category updated successfylly')
            return redirect('/myapp/showCategory')
        else:
            messages.add_message(request,messages.ERROR,'Failed to update category')
            return render(request,'myapp/updateCategory.html',{'form':form})
    context={
        'form':CategoryForm(instance=instances)
    }
    return render(request,'myapp/updateCategory.html',context)

@login_required
@admin_only
def delete_category(request,category_id):
    product=Category.objects.get(pk=category_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'deleted successfully')
    return redirect('/myapp/showCategory')



