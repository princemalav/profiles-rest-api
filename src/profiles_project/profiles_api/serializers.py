from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    '''create a serializers for api'''

    name = serializers.CharField(max_length=10)
