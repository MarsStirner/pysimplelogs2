# -*- coding: utf-8 -*-
import datetime
import json

__author__ = 'viruzzz-kun'


class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, datetime.date):
            return datetime.date.strftime(obj, "%Y-%m-%d")
        else:
            return super(APIEncoder, self).default(obj)