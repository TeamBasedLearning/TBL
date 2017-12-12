from rolepermissions.permissions import register_object_checker
from django.contrib.auth import get_user_model
from groups.models import Group

User = get_user_model()


@register_object_checker()
def change_own_group(permission, user, view):
    """
    Function to verify if user is the discipline owner.
    Admin user can change all disciplines
    """

    discipline = view.get_discipline()

    if user == discipline.teacher:
        return True

    return False


@register_object_checker()
def show_discipline_groups_permission(permission, user, view):
    """
    Permission that allows only students, monitors and teacher of specific
    discipline to see discipline groups features.
    """

    discipline = view.get_discipline()

    if not Group.is_released():
        return False

    if user in discipline.students.all() or \
       user in discipline.monitors.all() or \
       user == discipline.teacher:
        return True

    return False
