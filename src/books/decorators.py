import logging


def trace(f):
    def debug(*args, **kwargs):
        logging.debug ("entering " +  f.__name__)
        for arg in args:
            logging.debug (arg)
        try:    
            result= f(*args, **kwargs)
            logging.debug  ("exiting from " +  f.__name__ + ", result=" + str(result))
            return result
        except BaseException as e:
            logging.debug  ("throwing from " +  f.__name__ + ", exception=" + str(e))
            raise e
    debug.__name = f.__name__
    debug.__doc__ = f.__doc__
    return debug

def decorate(obj, decorator_function):
    for function_name in [a for a in dir(obj) if not a.startswith('__') and callable(getattr(obj,a))]:
        setattr(obj, function_name, decorator_function(getattr(obj, function_name)))
    return obj    