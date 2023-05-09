from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('emp_record/', views.emp_record, name='emp_record'),
    path('catalog/', views.catalog, name='catalog'),
    path('offer/', views.offer, name='offer'),
    path('services/', views.services, name='services'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
]
