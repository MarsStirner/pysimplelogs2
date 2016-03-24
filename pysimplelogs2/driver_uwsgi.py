# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences
import uwsgidecorators

import logging

__author__ = 'viruzzz-kun'


error_logger = logging.getLogger('PySimplelogs')


@uwsgidecorators.mulefunc
def send(url, data, timeout=10):
    import requests
    try:
        result = requests.post(
            url,
            data=data,
            headers={
                'Content-type': 'application/json',
                'Accept': 'application/json; text/plain',
            },
            timeout=timeout,
        )
        if result.status_code >= 400:
            result.raise_for_status()
    except:
        error_logger.exception(u'Error communicating with Simplelogs server')

