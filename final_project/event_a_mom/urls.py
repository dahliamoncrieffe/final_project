from django.conf.urls import url
from event_a_mom import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_event/$', views.add_event, name='add_event'),
    # url(r'^register/$', views.register, name='register'),
]
