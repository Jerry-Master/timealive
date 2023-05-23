from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, '')

@register.filter
def get_item_nested(dictionary, key):
    return dictionary.get(key, {})

@register.simple_tag
def get_nested_color(color_dict, appointments, day, hour):
    appointment_day = appointments.get(day, {})
    appointment_hour = appointment_day.get(hour, 'None')
    color = color_dict.get(appointment_hour, 'None')
    return color