from django import template

register= template.Library()

"""Either use this or register.filter to register:"""
"""@register.filter(name="cut_arg")"""
def cut(value,arg):
    "This cuts out all values of arg from string"
    return value.replace(arg,"test")

# approach two to register:
register.filter("cut_arg",cut)
