import endpoints
from endpoints import message_types
from endpoints import messages
from endpoints import remote
import logging


class JsonField(messages.StringField):
    type = dict


class KeyValuePair(messages.Message):
    key = messages.StringField(1)
    value = messages.StringField(2)


class UserPairs(messages.Message):
    userId = messages.StringField(1)
    keyValuePairs = messages.MessageField(KeyValuePair, 2, repeated=True)


class ListUserPairs(messages.Message):
    data = messages.MessageField(UserPairs, 1, repeated=True)


WRITE_USER_RESOURCE = endpoints.ResourceContainer(foo=messages.StringField(1))

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
        ListUserPairs,
        path='/',
        http_method='GET',
        name='listPairs'
    )
    def listPairs(self, request):
        return ListUserPairs(data=[UserPairs(userId='1', keyValuePairs=[KeyValuePair(key='hello', value='world')])])

    @endpoints.method(
        UserPairs,
        UserPairs,
        path='/',
        http_method='POST',
        name='addPair'
    )
    def addPair(self, request):
        """This works if you:
         curl --request POST --url http://localhost:8080/api/alicia/v1/ --header 'content-type: application/json' --data '{"foo": "bar"}'"""
        logging.info(request.userId)
        logging.info(request.keyValuePairs)
        return UserPairs(userId=request.userId, keyValuePairs=[KeyValuePair(key=p.key, value=p.value) for p in request.keyValuePairs])
# {
#   "userId": "string",
#   "keyValuePairs": [
#     {
#       "key": "string",
#       "value": "string"
#     }
#   ]
# }


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

api = endpoints.api_server([AliciaAPI])
