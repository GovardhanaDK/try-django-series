"""prog_first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from gun.views import home_view,actual_home_view,childu
from just_trying.views import detail_view
from db_related.views import productview_db

urlpatterns = [
    path('template/',home_view),
    path('child/',childu),
    path('',actual_home_view),
    path('admin/', admin.site.urls),
    path('db_first/',detail_view),
    path('create/<int:my_id>/update', productview_db),

]
