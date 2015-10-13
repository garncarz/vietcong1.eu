from django.views.generic.base import TemplateView
from django.utils.translation import get_language

class LocalizedTemplateView(TemplateView):
    """
    Children have to define:
    template_name = 'template-%(lang)s.html'
    """

    def get_template_names(self):
        return [self.template_name % {'lang': get_language()}]
