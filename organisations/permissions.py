from rest_framework.permissions import SAFE_METHODS, IsAuthenticated


class IsMyOrganisation(IsAuthenticated):
    """Разрешение для работы с организациями."""

    def has_permission(self, request, view):
        try:
            org_id = request.parser_context['kwargs']['pk']
            user = request.user
            return user.organisations_info.filter(
                organisation_id=org_id
            ).exists()
        except KeyError:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.director == request.user:
            return True

        if request.method in SAFE_METHODS:
            return request.user in obj.employees.all()

        return False


class IsColleagues(IsAuthenticated):
    """Разрешение для доступа коллег к объектам."""

    def has_object_permission(self, request, view, obj):
        if obj.organisation.director == request.user:
            return True

        if request.method in SAFE_METHODS:
            return request.user in obj.organisation.employees.all()
        return False


class IsMembers(IsAuthenticated):
    """Разрешение для участников группы для доступа к объектам."""

    def has_object_permission(self, request, view, obj):
        if (
            obj.group.organisation.director == request.user
            or obj.group.manager.user == request.user
        ):
            return True

        if request.method in SAFE_METHODS:
            return request.user in obj.group.organisation.employees.all()
        return False


class IsMyGroup(IsAuthenticated):
    """Разрешение для участников группы для выполнения операций с объектами."""

    def has_object_permission(self, request, view, obj):
        if obj.organisation.director == request.user:
            return True

        if request.method in SAFE_METHODS:
            return request.user in obj.organisation.employees.all()

        if obj.manager.user == request.user:
            return True
        return False


class IsOfferManager(IsAuthenticated):
    """
    Разрешение для директора организации на доступ к объектам предложений.
    """

    def has_object_permission(self, request, view, obj):
        if obj.organisation.director == request.user:
            return True
        return False
