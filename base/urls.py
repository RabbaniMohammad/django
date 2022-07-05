from django.urls import URLPattern, path 
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    # str slug int whatever
    path('rooms/<str:pk>',views.rooms, name='room' ),
    path('create-room/', views.createRoom, name='create-room'),
]