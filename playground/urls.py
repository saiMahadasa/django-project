from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.sayHello, name='say_hello'),
]
