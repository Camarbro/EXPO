from django.conf.urls import url,  include
from .views import home, post_list, post_detail, post_new, post_edit, signup, delete_post
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^$', home, name="home_view"),
    url(r'^postlist$', post_list, name = 'post_list_view'),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name = 'post_detail_view'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', delete_post, name = 'delete_post'),
    url(r'^post/new/$',post_new, name = 'post_new_view'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
    url(r'^signup/$', signup.as_view(),name = 'signup' ),
    url(r'^login/$', login , {'template_name': 'ParraCity/login.html'}, name='login_city'),
	url(r'^logout/$', logout_then_login, name='logout'),

]
