from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    # '' : 주소를 의미
	# views.index : 주소로 접근 시 호출할 뷰.
	# name='index' : 원하는 곳에서 이 이름을 가지고 주소를 호출해 출력
    path('cafeList/',views.cafeList,name='cafeList'),
    path('cafeList/<int:pk>/',views.cafeDetail,name='cafeDetails'),
    path('about/',views.about,name='about'),
    path('write/',views.write,name='wirte'),
]