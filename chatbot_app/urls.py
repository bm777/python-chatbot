from django.conf.urls import url
from chatbot_app import views


urlpatterns = [
    # url(r'^$', views.Bot, name='bot'),
    url(r'^$', views.Home, name='home'),
    url(r'^post/$', views.Post, name='post'),

]
