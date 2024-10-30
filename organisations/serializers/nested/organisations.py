from common.serializers.mixins import ExtendedModelSerializer
from organisations.models.organisations import Organisation


class OrganisationShortSerializer(ExtendedModelSerializer):
    """Сериализатор краткой информации об организации."""

    class Meta:
        model = Organisation
        fields = (
            'id',
            'name',
        )
