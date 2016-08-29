# coding: utf-8
# __author__: u"John"
from django.conf.urls import url

from . import views

urlpatterns = [
    url(ur"^$", views.index, name=u"index"),
]