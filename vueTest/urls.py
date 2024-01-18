from django.urls import path

from vueTest import views

urlpatterns = [
    path('', views.HomePage, name='home'),
]