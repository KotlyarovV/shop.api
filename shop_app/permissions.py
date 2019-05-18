from rest_framework import permissions


class IsLoggedInUser(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user

    def has_object_permission(self, request, view, obj):
        result = obj == request.user
        return result


class NON(permissions.BasePermission):

    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False