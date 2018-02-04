from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url,include

from MeetingRoom import views

urlpatterns = [
    #url('', views.RoomList.as_view()),
    url(r'', views.RoomList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.RoomDetails.as_view()),
                       ]

#data conversion api/1/json or api/1/xml

urlpatterns = format_suffix_patterns(urlpatterns)