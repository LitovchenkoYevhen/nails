from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'services'
urlpatterns = [
   #  path('', views.index, name='home'),
    path('', views.HomeServices.as_view(), name='home'),
    path('show_visit/<int:visit_pk>', views.show_visit, name='show_visit'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('works/', views.show_works, name='works_list'),
    path('prices/', views.show_prices, name='prices'),
    path('contacts/', views.show_contacts, name='contacts'),
    path('cleaning/', views.show_cleaning, name='cleaning'),
    path('show_work/<int:work_pk>', views.show_work, name='show_work'),
]
