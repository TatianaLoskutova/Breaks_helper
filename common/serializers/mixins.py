from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from users.serializers.nested.users import UserShortSerializer


class ExtendedModelSerializer(serializers.ModelSerializer):
    """
    Сериализатор, расширяющий функциональность стандартного сериализатора
    моделей.
    """

    class Meta:
        abstract = True

    def get_from_url(self, lookup_field):
        assert 'view' in self.context, (
            'No view context in "%s". '
            'Check parameter context on function calling.' % self.__class__.__name__
        )
        assert self.context['view'].kwargs.get(lookup_field), (
            'Got no data from url in  "%s". '
            'Check lookup field on function calling.'
        )
        value = self.context['view'].kwargs.get(lookup_field)
        return value

    def get_object_from_url(self, model, lookup_field='pk', model_field='pk'):
        obj_id = self.get_from_url(lookup_field)
        obj = get_object_or_404(
            queryset=model.objects.all(), **{model_field: obj_id}
        )
        return obj


class InfoModelSerializer(ExtendedModelSerializer):
    """Сериализатор для моделей с информацией о создателе и обновителе."""

    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

    class Meta:
        abstract = True


class DictMixinSerializer(serializers.Serializer):
    """Сериализатор для представления словарных данных."""

    code = serializers.CharField()
    name = serializers.CharField()
