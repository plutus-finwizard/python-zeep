class Error(Exception):
    def __init__(self, message=''):
        super(Exception, self).__init__(message)
        self.message = message

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.message)


class XMLSyntaxError(Error):
    pass


class XMLParseError(Error):
    def __init__(self, *args, **kwargs):
        self.filename = kwargs.pop('filename', None)
        self.sourceline = kwargs.pop('sourceline', None)
        super(XMLParseError, self).__init__(*args, **kwargs)

    def __str__(self):
        location = None
        if self.filename and self.sourceline:
            location = '%s:%s' % (self.filename, self.sourceline)
        if location:
            return '%s (%s)' % (self.message, location)
        return self.message


class UnexpectedElementError(Error):
    pass


class WsdlSyntaxError(Error):
    pass


class TransportError(Error):
    pass


class LookupError(Error):
    def __init__(self, *args, **kwargs):
        self.qname = kwargs.pop('qname', None)
        self.item_name = kwargs.pop('item_name', None)
        self.location = kwargs.pop('location', None)
        super(LookupError, self).__init__(*args, **kwargs)


class NamespaceError(Error):
    pass


class Fault(Error):
    def __init__(self, message, code=None, actor=None, detail=None, subcodes=None):
        super(Fault, self).__init__(message)
        self.message = message
        self.code = code
        self.actor = actor
        self.detail = detail
        self.subcodes = subcodes


class ZeepWarning(RuntimeWarning):
    pass


class ValidationError(Error):
    def __init__(self, *args, **kwargs):
        self.path = kwargs.pop('path', [])
        super(ValidationError, self).__init__(*args, **kwargs)

    def __str__(self):
        if self.path:
            path = '.'.join(str(x) for x in self.path)
            return '%s (%s)' % (self.message, path)
        return self.message


class SignatureVerificationFailed(Error):
    pass
