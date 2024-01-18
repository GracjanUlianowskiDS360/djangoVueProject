from django.urls import path

from vueTest import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('create_worker/', views.create_worker, name='create worker')
]
