from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

from common.constants import roles
from common.serializers.mixins import DictMixinSerializer


class ExtendedView:
    """
    "Расширенный класс представлений с многоуровневыми разрешениями и
    сериализаторами.
    """

    multi_permission_classes = None
    multi_serializer_class = None
    request = None

    def get_serializer_class(self):
        assert self.serializer_class or self.multi_serializer_class, (
            '"%s" should either include `serializer_class`, '
            '`multi_serializer_class`, attribute, or override the '
            '`get_serializer_class()` method.' % self.__class__.__name__
        )
        if not self.multi_serializer_class:
            return self.serializer_class

        # define request action or method
        if hasattr(self, 'action') and self.action:
            action = self.action
        else:
            action = self.request.method

        # Trying to get action serializer or default
        return self.multi_serializer_class.get(action) or self.serializer_class

    def get_permissions(self):
        # define request action or method
        if hasattr(self, 'action'):
            action = self.action
        else:
            action = self.request.method

        if self.multi_permission_classes:
            permissions = self.multi_permission_classes.get(action)
            if permissions:
                return [permission() for permission in permissions]

        return [permission() for permission in self.permission_classes]


class ExtendedGenericViewSet(ExtendedView, GenericViewSet):
    """Расширенный граничный класс для работы с набором представлений."""

    pass


class ListViewSet(ExtendedGenericViewSet, mixins.ListModelMixin):
    """Набор представлений для получения списка объектов."""

    pass


class UpdateViewSet(ExtendedGenericViewSet, mixins.UpdateModelMixin):
    """Набор представлений для обновления объектов."""

    pass


class DictListMixin(ListViewSet):
    """Смешанный класс для представления списка словарей."""

    serializer_class = DictMixinSerializer
    pagination_class = None
    model = None

    def get_queryset(self):
        assert self.model, (
            '"%s" should either include attribute `model`' % self.__class__.__name__
        )
        return self.model.objects.filter(is_active=True)


class LCRUViewSet(ExtendedGenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin, ):
    """Набор представлений для создания, получения и обновления объектов."""

    pass


class LCRUDViewSet(LCRUViewSet,
                   mixins.DestroyModelMixin, ):
    """
    Набор представлений для создания, получения, обновления и удаления
    объектов.
    """

    pass


class LCUViewSet(ExtendedGenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin, ):
    """
    Набор представлений для получения списка, создания и обновления объектов.
    """

    pass


class LCDViewSet(ExtendedGenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.DestroyModelMixin, ):
    """
    Набор представлений для получения списка, создания и удаления объектов.
    """

    pass


class ExtendedGenericAPIView(ExtendedView, GenericAPIView):
    """Расширенный класс представлений для обработки общих запросов."""

    pass


class ExtendedRetrieveUpdateAPIView(mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    ExtendedGenericAPIView,
                                    ):
    """
    Расширенный класс для получения и обновления объектов через различные
    HTTP-методы.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ExtendedCRUAPIView(mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         ExtendedGenericAPIView):
    """
    Представление для обработки операций создания, получения и обновления
    модели.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
