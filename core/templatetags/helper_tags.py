from django.template import Library
from django.core.urlresolvers import resolve, reverse
from django.utils.translation import activate, get_language

LANGUAGE_FLAGS = {
    'en': 'us',
    'cs': 'cz',
}

register = Library()

@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}

    https://djangosnippets.org/snippets/2875/
    """

    path = context['request'].path
    url_parts = resolve(path)

    url = path
    cur_language = get_language()
    try:
        activate(lang)
        url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
    finally:
        activate(cur_language)

    return url


@register.simple_tag
def language_flag(code):
    return LANGUAGE_FLAGS[code]
