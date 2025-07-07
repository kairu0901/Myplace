from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def parent_menu_open(context,children):
    request = context.get('request')
    for child in children:
        """現在のリクエストが指定されたURLと一致しているか判定"""
        if child['url'] == request.path:
            return "menu-open"
    return ""

@register.simple_tag(takes_context=True)
def parent_menu_is_active(context,children):
    request = context.get('request')
    for child in children:
        """現在のリクエストが指定されたURLと一致しているか判定"""
        if child['url'] == request.path:
            return "active"
    return ""

@register.simple_tag(takes_context=True)
def child_menu_is_active(context, child_url):
    request = context.get('request')
    """現在のリクエストが指定されたURLと一致しているか判定"""
    if child_url == request.path:
        return "active"
    return ""
