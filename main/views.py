from django.shortcuts import render
from .models import Cafe

# Create your views here.
def main(request):
    return render(request,'main/index.html')

def cafeList(request):
    cafeList = Cafe.objects.all()
    return render(request,'main/cafelist.html',{'cafeList':cafeList})

def cafeDetail(request,pk):
    cafeObj = Cafe.objects.get(pk=pk)
    return render(request,'main/cafeDetails.html',{'cafeObj':cafeObj})

def about(request):
    return render(request,'main/about.html')

def write(request):
    return render(request,'main/write.html')