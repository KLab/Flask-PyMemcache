# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import pymemcache.client
import flask
import flask.ext.pymemcache


def test_simple():
    pymc = pymemcache.client.Client(('localhost', 11211))
    memcache = flask.ext.pymemcache.FlaskPyMemcache()
    app = flask.Flask(__name__)
    app.config['PYMEMCACHE'] = {
        'server': ('localhost', 11211),
        'prefix': b'px'}
    memcache.init_app(app)

    with app.app_context():
        memcache.client.set(b'foo', b'bar')
        assert memcache.client.get(b'foo') == b'bar'

    assert pymc.get(b'pxfoo') == b'bar'