from rest_framework import serializers
from . import models
class HelloSerializers(serializers.Serializer):
    '''create a serializers for api'''

    name = serializers.CharField(max_length=10)

class UserProfileSerializers(serializers.ModelSerializer):
    '''Create a serailizer for user profile'''

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self , validated_data):
        '''create a new new user and return it'''

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
