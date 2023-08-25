from django import template

register = template.Library()

@register.filter(name='is_teacher')
def is_teacher(user):
    return user.user_type == 'teacher'