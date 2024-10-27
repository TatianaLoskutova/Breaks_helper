from common.serializers.mixins import DictMixinSerializer
from organisations.models.dicts import Position


class PositionShortSerializer(DictMixinSerializer):
    """Сериализатор краткой информации о позиции."""

    class Meta:
        model = Position
