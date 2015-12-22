# -*- coding: utf-8 -*-
import json
import requests
import logging
from pysimplelogs2.apiencoder import APIEncoder

__author__ = 'viruzzz-kun'


logger = logging.getLogger('simplelog-fallback')
logger.setLevel(logging.DEBUG)


class Simplelog(object):
    """Basic class for lib users.

    Keyword arguments:
    url -- simplelogs server URI.

    """

    CONNECTION_TIMEOUT = 2

    def __init__(self, url):
        self.url = url.rstrip('/')

    def get_levels_list(self):
        """Returns levels from server or default-list if server is unavailable."""
        try:
            levels = json.loads(requests.get(self.url + "/api/level/", timeout=self.CONNECTION_TIMEOUT).content)
        except:
            levels = {u'level': [u'critical', u'error', u'warning', u'notice', u'info', u'debug']}
        return levels

    def get_owners(self):
        try:
            response = requests.get(
                self.url + "/api/owners/",
                timeout=self.CONNECTION_TIMEOUT
            )
        except requests.ConnectionError:
            logger.exception('Cannot connect to Simplelog server')
        else:
            if response.status_code == requests.codes.ok:
                try:
                    result = response.json()
                except ValueError:
                    logger.exception('Malformed JSON from Simplelog server')
                else:
                    return result

    def get_list(self, **kwargs):
        params = dict()
        if kwargs:
            if 'find' in kwargs:
                params['find'] = kwargs['find']
            if 'sort' in kwargs:
                params['sort'] = kwargs['sort']
            if 'limit' in kwargs:
                params['limit'] = kwargs['limit']
            if 'skip' in kwargs:
                params['skip'] = kwargs['skip']
            try:
                response = requests.post(
                    self.url + "/api/list/",
                    headers={'content-type': 'application/json'},
                    data=json.dumps(params, cls=APIEncoder),
                    timeout=self.CONNECTION_TIMEOUT
                )
            except requests.ConnectionError:
                logger.exception('Cannot connect to Simplelog server')
                return
        else:
            try:
                response = requests.get(
                    self.url + "/api/list/",
                    headers={'content-type': 'application/json'},
                    timeout=self.CONNECTION_TIMEOUT
                )
            except requests.ConnectionError:
                logger.exception('Cannot connect to Simplelog server')
                return
        if response.status_code == requests.codes.ok:
            try:
                result = response.json()
            except ValueError:
                logger.exception('Malformed JSON from Simplelog server')
            else:
                return result

    def count(self, **kwargs):
        params = dict()
        if kwargs:
            if 'find' in kwargs:
                params['find'] = kwargs['find']
            if 'sort' in kwargs:
                params['sort'] = kwargs['sort']
            if 'limit' in kwargs:
                params['limit'] = kwargs['limit']
            try:
                response = requests.post(
                    self.url + "/api/count/",
                    headers={'content-type': 'application/json'},
                    data=json.dumps(params, cls=APIEncoder),
                    timeout=self.CONNECTION_TIMEOUT
                )
            except requests.ConnectionError:
                logger.exception('Cannot connect to Simplelog server')
                return
        else:
            try:
                response = requests.get(
                    self.url + "/api/count/",
                    headers={'content-type': 'application/json'},
                    timeout=self.CONNECTION_TIMEOUT
                )
            except requests.ConnectionError:
                logger.exception('Cannot connect to Simplelog server')
                return
        if response.status_code == requests.codes.ok:
            try:
                result = response.json()
            except ValueError:
                logger.exception('Malformaed JSON from Simplelog server')
            else:
                return result
