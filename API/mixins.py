from .permissions import IsStaffEditorPermission
from rest_framework import permissions

class StaffEditorPermissionMixin():
    """
        this enables the permissions to be added as views arguments
    """
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    
    # using mixin for queryset. it is added to the view
class UserQuerySetMixin():
    user_field = "user"
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data ={}
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args, **kwargs)
        if user.is_staff:
            return qs
        return qs.filter(**lookup_data)