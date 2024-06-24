from django.urls import path ,re_path
from . import views
app_name = 'menu'
urlpatterns = [
    #path(r'<int:menu_id>', views.menu_num),
    re_path(r'^(?P<menu_id>\d+)/$', views.menu_num, name='name_menu_num'),
    path('index', views.index, name='menu_index'),
    path('dummy', views.dummy ,name= 'dummy_page'),
    path('redirect_other_app', views.redirect_other_app, name='redirect')
]