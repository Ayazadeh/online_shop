from rest_framework import permissions
from customer.models import Customer


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class UserDetailOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class AddressDetailOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.owner.user)
        print(request.user)
        return obj.owner.user == request.user
