from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit the their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check  user try to edit the own profile """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id