import logging

file = logging.FileHandler('./books.log')
console = logging.StreamHandler()#Standard: Streaming auf die Konsole
file.setLevel(logging.DEBUG)
console.setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG, handlers=[file, console])


def trace(f):
    def tracer(*args, **kwargs):
        logging.info ("entering " +  f.__name__)
        for arg in args:
            print (arg)
        try:    
            result= f(*args, **kwargs)
            logging.info ("exiting from " +  f.__name__ + ", result=" + str(result))
            return result
        except BaseException as e:
            logging.info ("throwing from " +  f.__name__ + ", exception=" + str(e))
            raise e
    tracer.__name = f.__name__
    tracer.__doc__ = f.__doc__
    return tracer

def decorate(obj, decorator_function):
    for function in [a for a in dir(obj) if not a.startswith('__') and callable(getattr(obj,a))]:
        setattr(obj, function, decorator_function(getattr(obj, function)))
    return obj    