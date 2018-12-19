import endpoints
from endpoints import message_types
from endpoints import messages
from endpoints import remote


class JsonField(messages.StringField):
    type = dict


class KeyValuePair(messages.Message):
    key = message_types.StringField(1)
    value = message_types.StringField(2)


class UserPairs(messages.Message):
    userId = message_types.StringField(1)
    keyValuePairs = messages.MessageField(KeyValuePair, 2, repeated=True)


class ListUserPairs(messages.Message):
    data = messages.MessageField(UserPairs, 1, repeated=True)


LIST_PAIRS_RESOURCE = endpoints.ResourceContainer(userId=messages.StringField(1),
                                                  key=messages.StringField(2),
                                                  value=messages.StringField(3))

# TODO: this is supposed to be a json body, but should we give it a more specific schema?
ADD_PAIR_RESOURCE = endpoints.ResourceContainer(body=JsonField(1))

GET_PAIR_RESOURCE = endpoints.ResourceContainer(userId=messages.StringField(1, required=True))

GET_KEY_RESOURCE = endpoints.ResourceContainer(userId=messages.StringField(1, required=True),
                                               key=messages.StringField(2, required=True))


@endpoints.api(name='link', version='v1', base_path="/api/")
class AliciaAPI(remote.Service):
    def __init__(self):
        pass

    @endpoints.method(
        LIST_PAIRS_RESOURCE,
        ListUserPairs,
        path='/',
        http_method='GET',
        name='listPairs'
    )
    def listPairs(self, request):
        pass

    @endpoints.method(
        ADD_PAIR_RESOURCE,
        message_types.VoidMessage,
        path='/',
        http_method='POST',
        name='addPair'
    )
    def addPair(self, request):
        pass

    @endpoints.method(
        GET_PAIR_RESOURCE,
        UserPairs,
        path='/{userId}',
        http_method='GET',
        name='getPair'
    )
    def getPair(self, request):
        pass

    @endpoints.method(
        GET_KEY_RESOURCE,
        UserPairs,
        path='/{userId}/{key}',
        http_method='GET',
        name='getKey'
    )
    def getKey(self, request):
        pass

    @endpoints.method(
        GET_KEY_RESOURCE,
        message_types.VoidMessage,
        path='/{userId}/{key}',
        http_method='DELETE',
        name='deleteKey'
    )
    def deleteKey(self, request):
        pass
