from rest_framework import permissions 

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
    
        # Check the requeat user is the author of the object
        return obj.author == request.user