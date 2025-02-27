from rest_framework.permissions import BasePermission
from .models import Bucketlist


class IsOwner(BasePermission):
    """
    Custom permissions class to allow only bucketlist owners to edit them
    """

    def has_object_permission(self, request, view, obj) -> bool:
        """
        :return: True if permission is granted to the bucketlist owner
        """
        if isinstance(obj, Bucketlist):
            return obj.owner == request.user
        return obj.owner == request.user
