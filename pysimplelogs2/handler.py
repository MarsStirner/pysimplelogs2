# -*- coding: utf-8 -*-
import json
import logging

from pysimplelogs2.apiencoder import APIEncoder

__author__ = 'viruzzz-kun'


fallback_handler = logging.StreamHandler()
fallback_handler.setFormatter(logging.Formatter('%(asctime)s [pid:%(process)d|%(name)s|%(levelname)s] - %(message)s'))
error_logger = logging.getLogger('PySimplelogs')
error_logger.addHandler(fallback_handler)


class SimplelogHandler(logging.Handler):
    url = None
    send_func = None
    owner = None
    fallback = fallback_handler

    def emit(self, record):
        """
        :type record: logging.LogRecord
        :param record:
        :return:
        """
        if self.fallback:
            self.fallback.emit(record)
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
            ).encode('utf-8')
            try:
                self.send_func(self.url + '/api/entry/', data)
                return
            except:
                error_logger.exception()
                error_logger.error('Error connecting to %s. Passing...', self.url)

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
