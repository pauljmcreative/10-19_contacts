from django.urls import path

from . import views

urlpatterns = [
  path('', views.contacts_index, name='contacts'),
  path('<int:contact_id>/', views.contacts_show, name='contact'),
]
