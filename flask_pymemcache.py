# -*- coding: utf-8 -*-
"""
pymemcache_ integration for Flask
=================================

.. _pymemcache: https://github.com/pinterest/pymemcache

Initialize
----------

::

    memcache = FlaskPyMemcache(app)

or::

    memcache = FlaskPyMemcache()
    memcache.init_app(app)


Configuration
-------------

Put kwargs for pymemcache to `PYMEMCACHE` in your Flask configuration.

::

    PYMEMCACHE = {
        'server': ('localhost', 11211),
        'connect_timeout': 1.0,
        'timeout': 0.5,
        'no_delay': True,
        'key_prefix': b'myapp-',
    }

You can use different config key with `conf_key` keyword::

    session = FlaskPyMemcache(conf_key='MEMCACHE_SESSION')
    cache = FlaskPyMemcache(conf_key='MEMCACHE_CACHE')

    session.init_app(app)
    cache.init_app(app)

In addition to normal pymemcache kwargs, Flask-PyMemcache provides following
configuration options.

* `close_on_teardown` -- Close connection to memcached when app teardown.

Use
---

::

    memcache.client.set('foo', 'bar')

"""
from __future__ import absolute_import, division, print_function
import flask
import pymemcache.client


class FlaskPyMemcache(object):

    def __init__(self, app=None, conf_key=None):
        """
        :type app: flask.Flask
        :parm str conf_key: Key of flask config.
        """
        self.conf_key = conf_key
        if app is not None:
            self.init_app(app, conf_key)

    def init_app(self, app, conf_key=None):
        """
        :type app: flask.Flask
        :parm str conf_key: Key of flask config.
        """
        conf_key = conf_key or self.conf_key or 'PYMEMCACHE'
        self.conf_key = conf_key
        conf = app.config[conf_key]
        if not isinstance(conf, dict):
            raise TypeError("Flask-PyMemcache conf should be dict")

        close_on_teardown = conf.pop('close_on_teardown', False)
        client = pymemcache.client.Client(**conf)
        app.extensions.setdefault('pymemcache', {})
        app.extensions['pymemcache'][self] = client

        if close_on_teardown:
            @app.teardown_appcontext
            def close_connection(exc=None):
                client.disconnect_all()

    @property
    def client(self):
        """
        :rtype: pymemcache.client.Client
        """
        return flask.current_app.extensions['pymemcache'][self]
