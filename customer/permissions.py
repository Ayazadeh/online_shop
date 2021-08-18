from rest_framework import permissions
from customer.models import Customer


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class UserDetailOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_ptr_id == request.user.id


class AddressDetailOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner.user_ptr_id == request.user.id

