from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'services'
urlpatterns = [


    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    #  path('', views.index, name='home'),
    path('', views.HomeServices.as_view(), name='home'),
    path('prices/', views.Prices.as_view(), name='prices'),
    path('cleaning/', views.CleaningList.as_view(), name='cleaning'),

    # path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('make_appointment/', views.CreateVisit.as_view(), name='make_appointment'),
    path('show_visit/<int:visit_pk>', views.show_visit, name='show_visit'),

    path('statictic/', views.Statistic.as_view(), name='statistic'),

    path('works/', views.AllVisits.as_view(), name='all_visits'),
    path('works/<int:category_id>', views.WorksByCategory.as_view(), name='show_works_by_category'),
    # path('works/<int:category_id>', views.WorksByCategory, name='show_works_by_category'),
    # path('show_work/<int:work_pk>', views.show_work, name='show_work'),
    path('show_work/<int:pk>', views.ShowWork.as_view(), name='show_work'),

    path('contacts/', views.show_contacts, name='contacts'),
    path('contact/', views.send_message, name='contact')

]
