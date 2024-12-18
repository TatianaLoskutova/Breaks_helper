from django.db.models import Q
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import get_object_or_404

from breaks.models.breaks import Break
from breaks.serializers.api import breaks as breaks_s
from common.views.mixins import ExtendedCRUAPIView


@extend_schema_view(
    get=extend_schema(
        summary='Деталка обеда', tags=['Обеды: Обеды пользователя']
    ),
    post=extend_schema(
        summary='Резерв обеда', tags=['Обеды: Обеды пользователя']
    ),
    patch=extend_schema(
        summary='Измемение резерва обеда', tags=['Обеды: Обеды пользователя']
    ),
)
class BreakMeView(ExtendedCRUAPIView):
    """Представление моего обеденного перерыва."""

    queryset = Break.objects.all()
    serializer_class = breaks_s.BreakMeUpdateSerializer
    multi_serializer_class = {
        'GET': breaks_s.BreakMeRetrieveSerializer,
    }
    http_method_names = ('get', 'post', 'patch')

    def get_object(self):
        user = self.request.user
        replacement_id = self.request.parser_context['kwargs'].get('pk')

        return get_object_or_404(
            Break, Q(
                replacement_id=replacement_id,
                member__member__employee__user=user,
            )
        )
