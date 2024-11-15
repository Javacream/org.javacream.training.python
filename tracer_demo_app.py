from tracer import decorate, trace
import publishing_service

decorate(publishing_service, trace)
publishing_service.create_publisher('Springer')

class Object:
    def do_something(self):
        pass
o = Object()
o.do_something()
decorate(o, trace)
o.do_something()
