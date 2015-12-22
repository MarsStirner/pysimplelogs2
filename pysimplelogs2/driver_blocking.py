# -*- coding: utf-8 -*-
import requests

__author__ = 'viruzzz-kun'


def send(url, data):
    requests.post(
        url,
        data=data,
        headers={
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        }
    )