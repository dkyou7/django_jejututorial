from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main/index.html')

def cafeList(request):
    return render(request,'main/cafeList.html')