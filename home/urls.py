from django.urls import path , include
from .views import home,Systemlogout

urlpatterns = [
    path( '',home,name='home'),
    path( 'logout/',Systemlogout,name='logout'),


]
