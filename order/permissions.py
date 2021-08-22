from rest_framework import permissions


class OrderOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.id == view.owner_id)
        return request.user.id == view.owner_id
