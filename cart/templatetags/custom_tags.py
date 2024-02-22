from django.template import Library
register = Library()

@register.filter
def subtotal(order_detail):
    return sum([item.product.price * item.quantity for item in order_detail])
