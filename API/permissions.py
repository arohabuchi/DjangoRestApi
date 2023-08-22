from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET':['%(app_label)s.view_%(model_name)s'],
        'OPTIONS':[],
        'HEAD':[],
        'POST':['%(app_label)s.add_%(model_name)s'],
        'PUT':['%(app_label)s.change_%(model_name)s'],
        'PATCH':['%(app_label)s.change_%(model_name)s'],
        'DELETE':['%(app_label)s.delete_%(model_name)s'],
    }
    
    # ##this is use if we have another type or group that is not listed in the admin page eg E-commerce site with state rep, local rep etc
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
   
    #     print(request.user.get_all_permissions())
    