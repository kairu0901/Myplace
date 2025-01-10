from django import template

register = template.Library()

@register.simple_tag
def is_active(request, url):
    """現在のリクエストが指定されたURLと一致しているか判定"""
    if url == request.path:
        return "active"
    return ""
