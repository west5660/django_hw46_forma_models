from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
# def index(req):
#     forma = Personforma()
#     bd = Person.objects.all()
#     data = {'forma':forma, 'database':bd}
#     return render(req,'index.html', context=data)
#     pass
#
# def add1(req):
#     man = Person()
#     man.name='Igor'
#     man.age = 22
#     man.save()
#     man2 = Person.objects.create(name='Vlad', age=13)
#     return redirect('home')    #назввание маршрута
#
# def create(req):
#     if req.POST:
#         man = Person()
#         man.name = req.POST.get('name1')
#         man.age = req.POST.get('age1')
#         man.save()
#         return redirect('home')
#     pass
#
# def delete(req,ids):
#     man = Person.objects.get(id=ids)
#     man.delete()
#     return redirect('home')

def indexx(req):
    forma = Carforma()
    bd = Car.objects.all()
    data = {'forma':forma, 'database':bd}
    return render(req,'index.html', context=data)
    pass

def add2(req):
    avto = Car()
    avto.marka='M3'
    avto.proizv='BMW'
    avto.age = 2015
    avto.gn = 'M364MM'
    avto.save()
    avto2 = Car.objects.create(marka='ELIS', proizv='LOTUS', age=2018, gn='C896AA')
    return redirect('home')    #назввание маршрута

def create2(req):
    if req.POST:
        avto = Car()
        avto.marka = req.POST.get('marka1')
        avto.proizv = req.POST.get('proizv1')
        avto.age = req.POST.get('age1')
        avto.gn = req.POST.get('gn1')
        avto.save()
        return redirect('home')
    pass

def delete2(req,ids):
    avto = Car.objects.get(id=ids)
    avto.delete()
    return redirect('home')