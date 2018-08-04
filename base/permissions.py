from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.is_staff if request.user else False
