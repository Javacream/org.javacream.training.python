def trace(f):
    def tracer(*args, **kwargs):
        print ("entering " +  f.__name__)
        for arg in args:
            print (arg)
        try:    
            result= f(*args, **kwargs)
            print ("exiting from " +  f.__name__ + ", result=" + str(result))
            return result
        except BaseException as e:
            print ("throwing from " +  f.__name__ + ", exception=" + str(e))
            raise e
    tracer.__name = f.__name__
    tracer.__doc__ = f.__doc__
    return tracer

def decorate(obj, decorator_function):
    for function in [a for a in dir(obj) if not a.startswith('__') and callable(getattr(obj,a))]:
        setattr(obj, function, decorator_function(getattr(obj, function)))
                    