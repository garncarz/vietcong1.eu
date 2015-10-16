from django.core.urlresolvers import reverse
import django.test

class TestCase(django.test.TestCase):
    def get(self, path, kwargs=None):
        return self.client.get(reverse(path, kwargs=kwargs))

    def assert200(self, response, template_used=None):
        self.assertEqual(response.status_code, 200)
        if template_used:
            self.assertTemplateUsed(response, template_used)
