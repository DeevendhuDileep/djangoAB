
from django.shortcuts import render

#load first page
def firstpage(request):
    return render(request,'first.html',{'animal':'cat','flower':'rose','color':'yellow'})

def load_add_page(request):
    return render(request,'add.html')

def add_num(request):
    n1=int(request.GET['num1'])
    n2=int(request.GET['num2'])
    sum = n1+n2
    return render(request,'result.html',{'result':sum})
