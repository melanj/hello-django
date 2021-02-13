from rest_framework.permissions import BasePermission


class IsCoach(BasePermission):
    """
    Allows access only to coach users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='Coach').exists())


class IsPlayer(BasePermission):
    """
    Allows access only to coach users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='Player').exists())
