# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences
import uwsgidecorators

__author__ = 'viruzzz-kun'


@uwsgidecorators.mulefunc
def send(url, data, timeout=10):
    import requests
    requests.post(
        url,
        data=data,
        headers={
            'Content-type': 'application/json',
            'Accept': 'application/json; text/plain',
        },
        timeout=timeout,
    )
