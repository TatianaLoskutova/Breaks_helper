from rest_framework import serializers

from users.models.profile import Profile


class ProfileShortSerializer(serializers.ModelSerializer):
    """Сокращенный сериализатор профиля юзера."""

    class Meta:
        model = Profile
        fields = (
            'telegram_id',
        )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    """Сокращенный сериализатор обновления профиля юзера."""

    class Meta:
        model = Profile
        fields = (
            'telegram_id',
        )
