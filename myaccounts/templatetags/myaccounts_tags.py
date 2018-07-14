from django import template
from myaccounts import utils

register = template.Library()


@register.filter
def available_username(name):
    return utils.available_username(name)