from django.shortcuts import render
from .models import Cafe

# Create your views here.
def main(request):
    return render(request,'main/index.html')

def index(request):
    if request.method == "POST":
        # print(request)
        # print(request.POST.keys())

        keys = list(request.POST.keys())
        keys.remove('csrfmiddlewaretoken')
        # print(keys[0])

        cafelistobj = []
        cafelistobjall = Cafe.objects.all()
        # print(cafelistobj)
        # print(type(cafelistobj))
        # print(dir(cafelistobj))

        for key in keys:
            for cafelist in cafelistobjall:
                # print(cafelist['tag'], key, cafelist.tag == key)
                cafetag = list(cafelist.tag.values())
                print(cafetag[0]['name'], key, cafetag[0]['name'] == key)
                if cafetag[0]['name'] == key:
                    cafelistobj.append(cafelist)
        print(cafelistobj)
        return render(request, 'main/cafelist.html', {'cafelistobj': cafelistobj})
    return render(request, 'main/index.html')

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