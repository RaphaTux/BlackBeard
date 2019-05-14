from django.contrib import admin
from django.urls import path , include
from .views import hello
from home import urls as home_urls
from clientes import urls as clientes_urls
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path( '',include(home_urls),name='home'),
    path( 'clientes/',include(clientes_urls),name='clientes'),
    path( 'hello/',hello),
    path( 'admin/', admin.site.urls),
    path( 'login/', auth_views.LoginView.as_view(), name='login'),
    # path( 'logout/', auth_views.LogoutView.as_view(), name='logout'),

]
