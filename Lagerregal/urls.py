from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from devices.views import *
from network.views import *
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name="home"),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', }),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),

    url(r'^devices/$', login_required(DeviceList.as_view()), name="device-list"),
    url(r'^devices/add$', login_required(DeviceCreate.as_view()), name="device-add"),
    url(r'^devices/edit/(?P<pk>.*)$', login_required(DeviceUpdate.as_view()), name="device-edit"),
    url(r'^devices/delete/(?P<pk>.*)$', login_required(DeviceDelete.as_view()), name="device-delete"),
    url(r'^devices/(?P<pk>[0-9]*)$', login_required(DeviceDetail.as_view()), name="device-detail"),
    url(r'^devices/(?P<pk>[0-9]*)/history/$', login_required(DeviceHistoryList.as_view()), name="device-history-list"),
    url(r'^devices/(?P<pk>[0-9]*)/history/(?P<revision>[0-9]*)$', login_required(DeviceHistory.as_view()), name="device-history"),

    url(r'^types/$', login_required(TypeList.as_view()), name="type-list"),
    url(r'^types/add$', login_required(TypeCreate.as_view()), name="type-add"),
    url(r'^types/edit/(?P<pk>.*)$', login_required(TypeUpdate.as_view()), name="type-edit"),
    url(r'^types/delete/(?P<pk>.*)$', login_required(TypeDelete.as_view()), name="type-delete"),
    url(r'^types/(?P<pk>.*)$', login_required(TypeDetail.as_view()), name="type-detail"),

    url(r'^rooms/$', login_required(RoomList.as_view()), name="room-list"),
    url(r'^rooms/add$', login_required(RoomCreate.as_view()), name="room-add"),
    url(r'^rooms/edit/(?P<pk>.*)$', login_required(RoomUpdate.as_view()), name="room-edit"),
    url(r'^rooms/delete/(?P<pk>.*)$', login_required(RoomDelete.as_view()), name="room-delete"),
    url(r'^rooms/(?P<pk>.*)$', login_required(RoomDetail.as_view()), name="room-detail"),

    url(r'^buildings/$', login_required(BuildingList.as_view()), name="building-list"),
    url(r'^buildings/add$', login_required(BuildingCreate.as_view()), name="building-add"),
    url(r'^buildings/edit/(?P<pk>.*)$', login_required(BuildingUpdate.as_view()), name="building-edit"),
    url(r'^buildings/delete/(?P<pk>.*)$', login_required(BuildingDelete.as_view()), name="building-delete"),
    url(r'^buildings/(?P<pk>.*)$', login_required(BuildingDetail.as_view()), name="building-detail"),

    url(r'^manufacturers/$', login_required(ManufacturerList.as_view()), name="manufacturer-list"),
    url(r'^manufacturers/add$', login_required(ManufacturerCreate.as_view()), name="manufacturer-add"),
    url(r'^manufacturers/edit/(?P<pk>.*)$', login_required(ManufacturerUpdate.as_view()), name="manufacturer-edit"),
    url(r'^manufacturers/delete/(?P<pk>.*)$', login_required(ManufacturerDelete.as_view()), name="manufacturer-delete"),
    url(r'^manufacturers/(?P<pk>.*)$', login_required(ManufacturerDetail.as_view()), name="manufacturer-detail"),

    url(r'^ipaddresses/$', login_required(IpAddressList.as_view()), name="ipaddress-list"),
    url(r'^ipaddresses/add$', login_required(IpAddressCreate.as_view()), name="ipaddress-add"),
    url(r'^ipaddresses/edit/(?P<pk>.*)$', login_required(IpAddressUpdate.as_view()), name="ipaddress-edit"),
    url(r'^ipaddresses/delete/(?P<pk>.*)$', login_required(IpAddressDelete.as_view()), name="ipaddress-delete"),
    url(r'^ipaddresses/(?P<pk>.*)$', login_required(IpAddressDetail.as_view()), name="ipaddress-detail"),

    url(r'^search/$', login_required(Search.as_view()), name="search"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns += format_suffix_patterns(patterns('',
    url(r'^api/$', api_root),
))