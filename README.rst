pymemcache_ integration for Flask
=================================

.. _pymemcache: https://github.com/pinterest/pymemcache

Install
-------

Install from https://pypi.org/project/Flask-PyMemcache/

.. code:: bash

   pip install Flask-PyMemcache


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


