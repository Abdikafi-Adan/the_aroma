from django import template


register = template.Library()
"""adjusts the subtotal price in shopping cart to update
 to right price on added quantiy """


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
