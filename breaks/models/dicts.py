from common.models.mixins import BaseDictModelMixin


class ReplacementStatus(BaseDictModelMixin):
    """Модель статуса смены"""

    class Meta:
        verbose_name = 'Статус смены'
        verbose_name_plural = 'Статусы смены'
