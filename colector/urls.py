from django.conf.urls import url
from colector import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^error_list/', views.error_list, name='error_list'),
    url(r'^online_detail/(?P<pk>[\w\-]+)/$', views.online_detail, name='online_detail'),
    url(r'^new_config/(?P<pk>[\w\-]+)/$', views.new_config, name='new_config'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
#url(r'^online_list/', views.online_list, name='online_list'),

