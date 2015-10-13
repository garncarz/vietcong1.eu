from core.views import LocalizedTemplateView

class FAQView(LocalizedTemplateView):
    template_name = 'vietcong/faq-%(lang)s.html'
