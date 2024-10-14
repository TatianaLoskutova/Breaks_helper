from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models.users import User


class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'full_name',
        )


class UserEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'full_name',
            'email',
            'phone_number',
            'is_corporate_account',
        )
