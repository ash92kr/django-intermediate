from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    # path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/edit/', views.edit, name='edit'),  # GET 방식은 edit, POST 방식은 update
    path('<int:pk>/delete/', views.delete, name='delete'),  # POST일 때만 delete 작동하기
    path('<int:pk>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),  # GET으로 들어오면 NEW, POST로 들어오면 CREATE -> if문 사용
    path('', views.index, name='index'),  # GET으로 들어오면 form을 보여주고 POST로 들어오면 정보를 저장한다
]


