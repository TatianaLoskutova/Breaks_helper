from common.models.mixins import BaseDictModelMixin


class Position(BaseDictModelMixin):
    """Модель позиции."""

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
