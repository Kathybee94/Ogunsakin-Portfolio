from django.urls import path
from portapp import views

app_name= 'portapp'

urlpatterns= [
    path('index/', views.index, name='index'),
    path('download/', views.download, name='download'),
   
]