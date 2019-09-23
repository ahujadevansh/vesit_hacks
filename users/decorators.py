from django.core.exceptions import PermissionDenied


def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            print (request.user.role)

            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                print ("hii", request.user.role)
                print (allowed_roles)
                raise PermissionDenied
        return wrap
    return decorator
