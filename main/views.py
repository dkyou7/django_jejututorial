from django.shortcuts import render
from .models import Cafe

# Create your views here.
def main(request):
    return render(request,'main/index.html')

def cafeList(request):
    cafeList = Cafe.objects.all()
    return render(request,'main/cafeList.html',{'cafeList':cafeList})

def cafeDetail(request,pk):
    cafeObj = Cafe.objects.get(pk=pk)
    return render(request,'main/cafeDetails.html',{'cafeObj':cafeObj})