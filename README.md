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
