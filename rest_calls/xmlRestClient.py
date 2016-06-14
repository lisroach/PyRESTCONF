from rest_calls.restClient import RestCalls


class XMLRestCalls(RestCalls):
    Format = 'xml'

    def __repr__(self):
        return '%s(Session Object%s, Host = %s, Format = %s)' % (
            self.__class__.__name__,
            self._session.headers.items(),
            self._host,
            self.Format
        )
