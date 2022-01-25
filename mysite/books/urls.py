from django.urls import path
from . import views

urlpatterns = [  
    path('', views.home, name='index'), 
    path('home', views.home, name='home'),
    path('create', views.create_view, name='create_view'),  
    path('update/<id>', views.update_view, name='update_view'),
    path('delete/<id>', views.delete_view, name='delete_view'),
]