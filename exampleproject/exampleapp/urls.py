
from django.urls import path, include

from exampleapp import views

urlpatterns = [
    path('',views.home,name="home")

]