from django.urls import path
from . import views

urlpatterns = [
    path('add', views.form, name='addSite'),
    path('edit/<int:idSite>', views.form, name='editSite'),
    path('delete/<int:idSite>', views.delete, name='deleteSite'),
    path('', views.index, name='index')
]
