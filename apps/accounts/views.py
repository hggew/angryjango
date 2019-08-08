from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .serializer import UserSerializer

from .models import User


class RegistrationAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_pk'

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['user_pk'])

    def update(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_superuser is False:
            raise PermissionDenied('This user is not authenticated to update an user.')

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
