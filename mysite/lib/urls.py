# lib/urls.py
from django.urls import path
from . import views1
from . import views

app_name = 'lib'    #添加这行 命名空间

urlpatterns = [
    path('', views1.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('addBook/', views.addBook, name='addBook'),
    path('update_info/<int:book_id>', views.update_info, name='update_info'),
    path('updateBook/<int:book_id>', views1.updateBook, name='updateBook'),
    path('delBook/<int:book_id>', views.delBook, name='delBook'),
]