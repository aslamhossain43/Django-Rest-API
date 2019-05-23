from rest_framework import serializers

from User_App.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','user_date','user_name', 'user_photo')




