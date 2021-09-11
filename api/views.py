from django.http import Http404, JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser


def index(request):
    try:
        if request.user.is_authenticated:
            response = {str(request.user): f'hello {request.user.first_name}!'}
        else:
            raise
    except Exception:
        raise Http404("Document does not exist")
    return JsonResponse(response)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
