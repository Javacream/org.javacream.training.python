import logging
def debug(f):
    def debug(*args, **kwargs):
        logging.debug ("entering " +  f.__name__)
        for arg in args:
            print (arg)
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
    for function in [a for a in dir(obj) if not a.startswith('__') and callable(getattr(obj,a))]:
        setattr(obj, function, decorator_function(getattr(obj, function)))
    return obj    