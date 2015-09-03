# -*- coding=utf-8 -*-

from __future__ import print_function

import sys

from django.http import HttpResponse
from django.views.generic import View
from wechat_extend.basic import WechatExtend
from const import pn


class WechatInterface(View):
    def get(self, request, *args, **kwargs):
        appid = kwargs.get('appid')
        print('appid:\t{0}'.format(appid), file=sys.stderr)

        data = request.GET
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')

        wechat = WechatExtend(token=appid)

        # 验证是否来自微信服务器
        if not wechat.check_signature(
                signature=signature,
                timestamp=timestamp,
                nonce=nonce
                ):
            return HttpResponse('')

        return HttpResponse(echostr)

    def post(self, request, *args, **kwargs):
        appid = kwargs.get('appid')
        print('appid:\t{0}'.format(appid), file=sys.stderr)

        data = request.GET
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')

        wechat = WechatExtend(appid=appid, appsecret=pn.get(appid))

        # 验证是否来自微信服务器
        if not wechat.check_signature(
                signature=signature,
                timestamp=timestamp,
                nonce=nonce
                ):
            return HttpResponse('')

        # 解析xml
        wechat.parse_data(request.body)
        # message = wechat.get_message()

        print('request.body:\t{0}'.format(request.body), file=sys.stderr)

        res = wechat.response_text(u'Welcome~')

        return HttpResponse(res)
