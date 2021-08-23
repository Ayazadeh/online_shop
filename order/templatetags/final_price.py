from django import template
from order.models import Order

register = template.Library()


def final_price(value, arg):
    return Order.total_price(value, arg)


register.filter('final_price', final_price)