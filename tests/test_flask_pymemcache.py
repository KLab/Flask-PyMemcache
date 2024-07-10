from unittest import TestCase

import pymemcache.client
import flask
import flask_pymemcache


class TestFlaskPyMemcache(TestCase):
    def test_simple(self):
        pymc = pymemcache.client.Client(("localhost", 11211))
        memcache = flask_pymemcache.FlaskPyMemcache()
        app = flask.Flask(__name__)
        app.config["PYMEMCACHE"] = {
            "server": ("localhost", 11211),
            "key_prefix": b"px",
            "close_on_teardown": False,
        }
        memcache.init_app(app)

        with app.app_context():
            memcache.client.set(b"foo", b"bar")

        with app.app_context():
            assert memcache.client.get(b"foo") == b"bar"

        assert pymc.get(b"pxfoo") == b"bar"

    def test_pool(self):
        memcache = flask_pymemcache.FlaskPyMemcache()
        app = flask.Flask(__name__)
        app.config["PYMEMCACHE"] = {
            "server": ("localhost", 11211),
            "key_prefix": b"px",
            "close_on_teardown": False,
        }
        memcache.init_app(app, client_class=pymemcache.PooledClient)

        with app.app_context():
            assert memcache.client.get(b"foo") is None
            assert isinstance(memcache.client, pymemcache.PooledClient)
