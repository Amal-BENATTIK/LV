from django import template

register = template.Library()

@register.filter
def masked_password(password):
    print(f"masked_password: input: {password}")
    masked = '*' * len(password)
    print(f"masked_password: output: {masked}")
    return masked
