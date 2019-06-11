from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('3Ton/', views.threeTon, name='3ton'),
    path('5Ton/', views.fiveTon, name='5ton'),
    path('Giraffe/', views.giraffe, name='giraffe'),
    path('About/', views.about, name='about'),
    path('Contact/', views.contact, name='contact'),
]
