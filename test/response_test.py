from restfulie.response import Response
from mockito import *

def trivial_test():

    response = ({'status': 200}, "Hello")

    r = Response(response)
    assert r.body == "Hello"
    assert r.code == 200

def resource_test():

    response = ({'status': 200, 'content-type':'text/plain; charset=utf-8'}, "Hello")

    r = Response(response)
    assert r.resource() == "Hello"
