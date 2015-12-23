# -*- coding: utf-8 -*-
import requests

__author__ = 'viruzzz-kun'


def send(url, data, timeout=10):
    requests.post(
        url,
        data=data,
        headers={
            'Content-type': 'application/json',
            'Accept': 'application/json; text/plain',
        },
        timeout=timeout,
    )
