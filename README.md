[toc]

# 제주코딩베이스캠프 강의 노트

## 1. 환경설정

```python
pip3 install django==2.1.5
django-admin startproject config .
python manage.py migrate
```

## 2. url 연결

- 서버를 실행시켰으니 앱을 만들어보자.

  > python manage.py startapp main

- 앱을 만들었으면 INSTALLED_APPS에 등록해줘야 한다.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',			<<<<<----------------------------등록방법
]
```

- 이제 간단한 (M)VT 구조를 이용하여 띄워보자.

### 2.1 먼저 뷰를 작성해보자.

```python
# main/views.py

from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main/index.html')
```

- 원래는 `config/urls`에서 관리하는게 맞지만, `config/urls.py`는 각 앱의 url을 묶어주는 총괄의 역할을 수행하도록 하고, 깔끔한 관리를 위해 각각의 앱마다  `urls.py`를 생성하여 관리해준다.

```python
# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    # '' : 주소를 의미
	# views.index : 주소로 접근 시 호출할 뷰.
	# name='index' : 원하는 곳에서 이 이름을 가지고 주소를 호출해 출력
]
```

- 여기서 나는 `name=` 옵션을 쓰는 이유를 잘 몰랐었는데 생각보다 괭장히 편리한 기능인 것 같아서 놀랐다. 다행히 답변도 잘 달려있었다.

![image](https://user-images.githubusercontent.com/26649731/75942657-59279500-5ed6-11ea-9fd5-6e8fcc8edab2.png)



```python
# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('main.urls'))
    # main/urls 를 가져온다.
]
```

### 2.2 이제 template를 작성하여 사용자가 볼 수 있도록 하자.

- template는 다음과 같은 구조로 작성하는 것이 좋은데, 다른 앱에서 똑같은 template가 나오는 것을 방지하기 위해서이다.

![image](https://user-images.githubusercontent.com/26649731/75942493-d4d51200-5ed5-11ea-9db3-05cd88b66e29.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>hello, this is main/index page</h1>
</body>
</html>
```

> python manage.py runserver 로 실행시켜 확인해보자.

![image](https://user-images.githubusercontent.com/26649731/75941916-52981e00-5ed4-11ea-8b7e-dc7c40209281.png)

- 잘 나타나는 것을 볼 수 있다!

## 3. 이미지 삽입해보기

### 3.1 앱 디랙토리에 `static` 넣기

- 넣고 이미지도 넣어준다.

- 이미지는 주로 [픽사베이](https://pixabay.com/ko/)를 사용한다고 한다.

![image](https://user-images.githubusercontent.com/26649731/75962021-62305a80-5f06-11ea-98a5-8dfa04477915.png)

### 3.2 static 설정

- `config/settings.py`에 static 설정을 한다.

```python
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
```

### 3.3 html 설정

```html
{% load staticfiles %}
<img src="{% static 'jeju.jpg' %}">
```

![image](https://user-images.githubusercontent.com/26649731/75962150-93a92600-5f06-11ea-9a90-c8a1dd18bb54.png)

- 이미지가 잘 등록되었다.

## 4. Model 이용하기

- 이제는 MVT 구조를 이용하여 웹을 설계해보자

### 4.1 Model(모델) 작성하기

- 맨 처음에는 무조건 모델을 설계한다. 간단하게 카페 이름과 카페 설명을 골자로 하는 모델을 생성해보았다.
- \__str\__은 관리자권한에서 보여줄 단어를 나타낸다.

```python
# main/models.py

from django.db import models

# Create your models here.
class Cafe(models.Model):
    cafeName = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.cafeName
```

- 모델을 작성했으면 URL 로 이어준다.

```python
from django.urls import path
from . import views

urlpatterns = [
    ...
    path('cafeList/',views.cafeList,name='cafeList')
]
```

- 모델을 작성한 뒤 주의점은 __마이그레이션을 진행해야한다는 점__이다.

- 다음 명령어로 꼭 모델을 DB에 적용시키자

```bash
python manage.py makemigrations main
python manage.py migrate main
```

### 4.2 뷰(View) 작성하기

- 모델에서 작성한 것을 어떤 것이 보여줄 것인지 지정한다.
- main/cafeList.html에서 보여주기로 하자.

```python
from django.shortcuts import render

# Create your views here.

def cafeList(request):
    return render(request,'main/cafeList.html')
```

### 4.3 템플릿(Templates) 작성하기

- html로 사용자들이 볼 수 있도록 한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>hello, this is cafeList</h1>
</body>
</html>
```

![image](https://user-images.githubusercontent.com/26649731/76037870-75d1d480-5f8b-11ea-8c49-c4a40afbc040.png)

- 잘 작성된 것을 볼 수 있었다.

## 5. list 띄우기

- 이제 관리자페이지에서 등록한 카페이름과 설명을 사용자에게 보여주도록 하자.
- 뷰에서 모델 부분을 파라메터로 넘기고 템플릿에서 보여주는 작업을 하면 된다.(2가지)

### 5.1 뷰(View) 작업

```python
from django.shortcuts import render
from .models import Cafe	# <---- 모델에서 가져온다.

# Create your views here.

def cafeList(request):
    cafeList = Cafe.objects.all()# <---- 전체로 가져오고 이걸 파라메타로 넘긴다.
    return render(request,'main/cafeList.html',{'cafeList':cafeList})
```

### 5.2 탬플릿(templates) 작업

```html
<h1>hello, this is cafeList</h1>
{% for elem in cafeList %}
    <h2>{{elem.cafeName}}</h2>
    <p>{{elem.description}}</p>
{% endfor %}
```

- 변수는 `{{}}`으로 작업하고 문법은 `{%%}`로 작업한다.

![image](https://user-images.githubusercontent.com/26649731/76039797-d7487200-5f90-11ea-8601-64f40424b71e.png)

- 리스트가 잘 출력되었다!

## 6. 디테일 보여주기

- 이제 제목을 클릭하면 디테일을 보여주고, 디테일에 들어가면 목록으로 나갈 수 있도록 하도록 구현한다.
- 그러자면 먼저 details를 구현해야한다.
- 마찬가지로 뷰와 템플릿에 적절하게 적용해보자.

### 6.1 뷰(view) 코딩

```python
from django.shortcuts import render
from .models import Cafe

# Create your views here.

def cafeDetail(request,pk):
    cafeObj = Cafe.objects.get(pk=pk)	#<-------pk값을 기준으로 가져온다.
    return render(request,'main/cafeDetails.html',{'cafeObj':cafeObj})
```

```python
from django.urls import path
from . import views

urlpatterns = [
	...
    path('cafeList/<int:pk>/',views.cafeDetail,name='cafeDetails'),
]
```

### 6.2 탬플릿(templates) 코딩

- 이제 `name=`옵션의 위력이 나온다.

```html
<!--main/cafeDetails.html-->

<h1>hello, this is cafeDetails</h1>
<h2>{{cafeObj.cafeName}}</h2>
<p>{{cafeObj.description}}</p>
<a href="{% url 'cafeList' %}">목록으로</a>
```

```html
<!--main/cafeList.html-->

<h1>hello, this is cafeList</h1>
{% for elem in cafeList %}
    <h2><a href="{% url 'cafeDetails' elem.pk %}">{{elem.cafeName}}</a></h2>
    <p>{{elem.description}}</p>
{% endfor %}
```

![image](https://user-images.githubusercontent.com/26649731/76043912-38297780-5f9c-11ea-8d1a-dd5366706f6b.png)

- detail 도 id값에 따라 잘 구현 되었다.

## 7. 사진(media) 넣기

- 사진을 넣어보자. 약간 세팅이 어려울 수 있지만 따라하기만 하면 된다.
- 먼저 project-name > media 폴더를 생성하자. 여기에 사진이 들어가게 된다.

### 7.1 config 코딩

- settings.py에 다음을 추가한다. 미디어 관련 파일을 넣겠다는 말이다.

```python
# config/settings.py

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
```

- urls.py에 다음을 추가하면서 미디어를 추가해준다.

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ....
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 7.2 모델(Model) 코딩

- 이제 이미지를 넣기위한 작업을 추가해보자. 이미지 영역을 추가하면 된다.

```python
from django.db import models

# Create your models here.
class Cafe(models.Model):
    cafeName = models.CharField(max_length=50)
    cafeImg = models.ImageField(blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.cafeName
```

- **모델 수정시 반드시 마이그레이션 해줘야 한다.**

```bash
python manage.py makemigrations main
python manage.py migrate main
```

- 뷰는 따로 변경 안해줘도 된다. 어짜피 객체를 가져오는 것이기 때문이다.
  이제 템플릿을 수정해보자

### 7.3 탬플릿(templates) 코딩

- 사진이 없는 글도 있기 때문에 if 문을 적용시킨다.

```python
<h2>{{cafeObj.cafeName}}</h2>
<p>{{cafeObj.description | linebreaks }}</p>
{% if cafeObj.cafeImg %}
<img src="{{cafeObj.cafeImg.url}}">
{% endif %}
<a href="{% url 'cafeList' %}">목록으로</a>
```

![image](https://user-images.githubusercontent.com/26649731/76051333-c6f2c000-5fad-11ea-8e6a-644598244c97.png)

- 이미지가 짤렸지만 잘 적용된 것을 볼 수 있다.



## 8. 댓글 구현 및 태그 구현

- 댓글 구현은 Disqus라는걸 이용한다. 따로 코딩할 필요 없음.

  - 튜토리얼 보면서 나오는 코드를 details 하단에 붙여넣으면 된다.

- 태그 구현은 먼저 패키지를 설치해보자

  > pip3 install django-taggit

- INSTALLED_APPS 추가

  ```python
  INSTALLED_APPS = [
      ...
      'taggit',
  ]
  ```

  

### 8.1 모델(Model) 구현

- 모델 싹 뜯어고쳤다.

```python
from django.db import models
from taggit.managers import TaggableManager

class Cafe(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    mainphoto = models.ImageField(blank=True, null=True)
    subphoto = models.ImageField(blank=True, null=True)
    publishedDate = models.DateTimeField(blank=True, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    locate = models.TextField(null=True)
    phone = models.TextField(null=True)
    insta = models.TextField(null=True)
    tag = TaggableManager(blank=True)

    def __str__(self):
        return self.name
```

```bash
python manage.py makemigrations main
python manage.py migrate main
```

### 8.2 탬플릿(template) 코딩

- 구조와 변수명을 바꾸었기 때문에 templates에서 받는 변수명도 바뀌어야 한다.

```html
{% for elem in cafeList %}
    <h2><a href="{% url 'cafeDetails' elem.id %}">{{elem.name}}</a></h2>
    <p>{{elem.content}}</p>
{% endfor %}
```

```html
<h2>{{cafeObj.name}}</h2>
<p>{{cafeObj.content | linebreaks }}</p>
<p>{{cafeObj.publishedDate | linebreaks }}</p>
<p>{{cafeObj.insta | linebreaks }}</p>
<p>{{cafeObj.tag.names | linebreaks }}</p>
{% if cafeObj.mainphoto %}
<img src="{{cafeObj.mainphoto.url}}">
{% endif %}
<a href="{% url 'cafeList' %}">목록으로</a>
```

![image](https://user-images.githubusercontent.com/26649731/76054855-5f407300-5fb5-11ea-9821-87d0d1c14d87.png)

- 댓글기능까지 구현 된 것을 볼 수 있다.



