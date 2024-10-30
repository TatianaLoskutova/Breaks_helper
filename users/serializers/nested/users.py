from rest_framework import serializers

from users.models.users import User


class UserShortSerializer(serializers.ModelSerializer):
    """Сокращенный сериализатор юзера."""

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'full_name',
        )


class UserEmployeeSerializer(serializers.ModelSerializer):
    """Сокращенный сериализатор юзера-сотрудника."""

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
