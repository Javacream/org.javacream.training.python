def checkNoneOrEmptyParameter(param, name):
            if param == None or len(str(param).strip()) == 0:
                raise IllegalParameterException("Illegal parameter: %s" % (name))

class IllegalParameterException(BaseException):
    def __init__(self, cause):
        self.cause = cause