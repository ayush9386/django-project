from . import views
from django.urls import path

urlpatterns=[
    path('home/',views.form_view),
    path('home_post/', views.form_view_post),
    path('about/',views.about),
    path('menu/' , views.menu),
    path('menu_card/', views.menu_by_id),
    path('menu_extend/' , views.menu_extend),
    path('about_extend/',views.about_extend),
    path('home_extend/',views.home_extend),

]

