from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and \
               not request.user.is_superuser and \
               not request.user.groups.filter(name='moderator').exists()

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
