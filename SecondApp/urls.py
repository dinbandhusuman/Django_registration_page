from django.urls import path
from SecondApp import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('',views.home,name='registration'),
]
