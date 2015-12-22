# -*- coding: utf-8 -*-
import json
import logging

from pysimplelogs2.apiencoder import APIEncoder

__author__ = 'viruzzz-kun'


class SimplelogHandler(logging.Handler):
    url = None
    send_func = None
    owner = None
    fallback = logging.StreamHandler()

    def emit(self, record):
        """
        :type record: logging.LogRecord
        :param record:
        :return:
        """
        if self.send_func and self.url:
            data = json.dumps({
                'level': record.levelname.lower(),
                'owner': self.owner,
                'data': self.format(record),
                'tags': sorted(getattr(record, 'tags', []))
            },
                cls=APIEncoder,
                encoding='utf-8',
                ensure_ascii=False
            )
            try:
                self.send_func(self.url + '/api/entry/', data)
                return
            except:
                pass
        if self.fallback:
            self.fallback.emit(record)

    def setFormatter(self, fmt):
        if self.fallback:
            self.fallback.setFormatter(fmt)
        super(SimplelogHandler, self).setFormatter(fmt)

    def set_url(self, url, glob=False):
        if glob:
            self.__class__.url = url.rstrip('/')
        else:
            self.url = url.rstrip('/')


def __configure_default_send():
    try:
        from pysimplelogs2.driver_uwsgi import send
    except ImportError:
        from pysimplelogs2.driver_blocking import send
    SimplelogHandler.send_func = staticmethod(send)

__configure_default_send()
del __configure_default_send
