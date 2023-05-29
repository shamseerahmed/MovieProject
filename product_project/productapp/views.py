from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import product
from . forms import MovieForms
# Create your views here.
def index(request):
    Product=product.objects.all()
    context={
        'product_list':Product
    }
    return render(request,'index.html',context)

def detail(request,product_id):
    pro=product.objects.get(id=product_id)
    return render(request,"details.html",{'product':pro})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie=product(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movie=product.objects.get(id=id)
    form=MovieForms(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form, 'movie':movie })

def delete(request,id):
    if request.method=='POST':
        movie=product.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

