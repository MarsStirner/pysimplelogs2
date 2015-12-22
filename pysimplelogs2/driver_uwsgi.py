# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences
import uwsgidecorators

__author__ = 'viruzzz-kun'


@uwsgidecorators.mulefunc
def send(url, data):
    import requests
    requests.post(
        url,
        data=data,
        headers={
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        }
    )
