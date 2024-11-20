from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('trainers/', views.trainers, name='trainers'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('course/<slug:slug>/', views.course_details, name='course-details'),
]