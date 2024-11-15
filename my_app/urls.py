from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('' ,views.MainView.as_view()),
    path('signup/' ,views.IndexView.as_view()),
    path('signin/' ,views.AddData.as_view()),
    path('home/' ,views.HomeView.as_view()),
    path('signout/' ,views.SignOutView.as_view()),
    path('data/' ,views.DataView.as_view()),
    path('data2/' ,views.DataView2.as_view()),
    path('home2/' ,views.HomeView2.as_view()),
    path('learn/' ,views.LearnView.as_view()),
    
   
]