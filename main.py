import endpoints
from endpoints import message_types
from endpoints import messages
from endpoints import remote
import logging


class KeyValuePair(messages.Message):
    key = messages.StringField(1)
    value = messages.StringField(2)


class UserPairs(messages.Message):
    userId = messages.StringField(1)
    keyValuePairs = messages.MessageField(KeyValuePair, 2, repeated=True)


class UserPairSingle(messages.Message):
    userId = messages.StringField(1)
    keyValuePair = messages.MessageField(KeyValuePair, 2)


class UserPairsCollection(messages.Message):
    items = messages.MessageField(UserPairs, 1, repeated=True)


LIST_PAIRS_RESOURCE = endpoints.ResourceContainer(userId=messages.StringField(1),
                                                  key=messages.StringField(2),
                                                  value=messages.StringField(3))

GET_PAIR_RESOURCE = endpoints.ResourceContainer(userId=messages.StringField(1, required=True))

GET_KEY_RESOURCE = endpoints.ResourceContainer(userId=messages.StringField(1, required=True),
                                               key=messages.StringField(2, required=True))


@endpoints.api(name='alicia', version='v1', base_path="/api/")
class AliciaAPI(remote.Service):
    def __init__(self):
        pass

    @endpoints.method(
        LIST_PAIRS_RESOURCE,
        UserPairsCollection,
        path='/',
        http_method='GET',
        name='listPairs'
    )
    def listPairs(self, request):
        pairs = [UserPairs(userId='1', keyValuePairs=[KeyValuePair(key='hello', value='world')])]
        return UserPairsCollection(items=pairs)

    @endpoints.method(
        UserPairs,
        UserPairs,
        path='/',
        http_method='POST',
        name='addPair'
    )
    def addPair(self, request):
        return UserPairs(userId=request.userId, keyValuePairs=[KeyValuePair(key=p.key, value=p.value)
                                                               for p in request.keyValuePairs])

    @endpoints.method(
        GET_PAIR_RESOURCE,
        UserPairs,
        path='/{userId}',
        http_method='GET',
        name='getPair'
    )
    def getPair(self, request):
        pairs = [KeyValuePair(key='foo', value='bar')]
        return UserPairs(userId=request.userId, keyValuePairs=[KeyValuePair(key=p.key, value=p.value) for p in pairs])

    @endpoints.method(
        GET_KEY_RESOURCE,
        UserPairSingle,
        path='/{userId}/{key}',
        http_method='GET',
        name='getKey'
    )
    def getKey(self, request):
        pair = KeyValuePair(key=request.key, value='bar')
        return UserPairSingle(userId=request.userId, keyValuePair=pair)

    @endpoints.method(
        GET_KEY_RESOURCE,
        message_types.VoidMessage,
        path='/{userId}/{key}',
        http_method='DELETE',
        name='deleteKey'
    )
    def deleteKey(self, request):
        return message_types.VoidMessage()

api = endpoints.api_server([AliciaAPI])
