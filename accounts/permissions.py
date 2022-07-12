from django.core.exceptions import PermissionDenied


def user_is_employee(function):  # If the user is not the employee, it will show the 403 error page.
    def wrap(request, *args, **kwargs):
        if request.user.is_active and request.user.is_employee:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def user_is_customer(function):  # If the user is not the customer, it will show the 403 error page.
    def wrap(request, *args, **kwargs):
        if request.user.is_active and request.user.is_customer:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
