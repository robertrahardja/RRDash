"""RRDash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rrdashapp import views
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('restaurant/sign-in', auth_views.login, {'template_name': 'restaurant/sign_in.html'}, name='restaurant-sign-in'),
    path('restaurant/sign-in/', LoginView.as_view(template_name='restaurant/sign_in.html'), name="restaurant-sign-in"),
    # path('restaurant/sign-out', auth_views.logout, {'next_page': '/'}, name='restaurant-sign-out'),
    path('restaurant/sign-out/', LogoutView.as_view(next_page='/'), name="restaurant-sign-out"),
    path('restaurant/', views.restaurant_home, name='restaurant-home'),

]
