from django.db.models import Q
from rest_framework.filters import BaseFilterBackend


class OwnedByOrganisation(BaseFilterBackend):
    """Фильтрация queryset по организации."""

    def filter_queryset(self, request, queryset, view):
        org_id = request.parser_context['kwargs'].get('pk')
        return queryset.filter(organisation_id=org_id)


class OwnedByGroup(BaseFilterBackend):
    """Фильтрация queryset по группе."""

    def filter_queryset(self, request, queryset, view):
        group_id = request.parser_context['kwargs'].get('pk')
        return queryset.filter(group_id=group_id)


class MyOrganisation(BaseFilterBackend):
    """
    Фильтрация queryset по тем организациям где юзер директор или сотрудник.
    """

    def filter_queryset(self, request, queryset, view):
        user = request.user
        return queryset.filter(
            Q(director=user) | Q(employees=user)
        ).distinct()


class MyGroup(BaseFilterBackend):
    """Фильтрация queryset по тем группам где юзер директор или сотрудник."""

    def filter_queryset(self, request, queryset, view):
        user = request.user
        return queryset.filter(
            Q(organisation__director=user) | Q(organisation__employees=user)
        ).distinct()
