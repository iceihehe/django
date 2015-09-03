# -*- coding=utf-8 -*-

from django.conf.urls import url, patterns

import views


urlpatterns = patterns(
    '',

    url(
        r'^(?P<appid>wx[0-9a-z]{16})/interface$',
        views.WechatInterface.as_view()
    ),
)
