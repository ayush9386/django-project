"""
URL configuration for new_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('user/<name>/<id>', views.get_info_url ),
    path('info_using_query', views.get_info_query),
    path('menu/', include('menu.urls')),
    path('anotherapp/' , include('myapp.urls')),
    path('dummy_view' , views.dummy_view, name='dummy_view'),
    path('admin_view' , views.admin_view),
    path('user_view', views.user_view),
    path('testapp/', include('testapp.urls')),
    path('crudapp/', include('crudapp.urls')),
    path('restapi/', include('restapi.urls')),
]

#handler404 = 'new_project.views.handler404'
