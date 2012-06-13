from django.test import TestCase
from django.template import Context, Template, TemplateSyntaxError
from django.core.cache import cache

from chunks.models import Chunk

class ChuckTemplateTagTestCase(TestCase):

    def setUp(self):
        self.home_page_left = Chunk.objects.create(
            key='home_page_left',
            content='This is the content for left box')
        cache.delete('cache_home_page_left')


    def test_should_render_content_from_key(self):
        result = self.render_template('{% load chunks %}'
                                      '<div>{% chunk "home_page_left" %}</div>')

        self.assertEquals('<div>This is the content for left box</div>', result)


    def test_should_render_empty_string_if_key_not_found(self):
        result = self.render_template('{% load chunks %}'
                                      '<div>{% chunk "key_not_found" %}</div>')

        self.assertEquals('<div></div>', result)


    def test_should_cache_rendered_content(self):
        cache_key = 'chunk_home_page_left'
        self.assertFalse(cache.get(cache_key), "key %r should NOT be cached" % cache_key)

        self.render_template("{% load chunks %}"
                             "<div>{% chunk 'home_page_left' 10 %}</div>")
        cached_result = cache.get(cache_key)

        self.assertTrue(cached_result, "key %r should be cached" % cache_key)
        self.assertEquals('This is the content for left box', cached_result.content)


    def test_should_fail_if_wrong_number_of_arguments(self):
        with self.assertRaisesRegexp(TemplateSyntaxError, "'chunk' tag should have either 2 or 3 arguments"):
            self.render_template('{% load chunks %}'
                                 '{% chunk %}')

        with self.assertRaisesRegexp(TemplateSyntaxError, "'chunk' tag should have either 2 or 3 arguments"):
            self.render_template('{% load chunks %}'
                                 '{% chunk "home_page_left" 10 "invalid" %}')

        with self.assertRaisesRegexp(TemplateSyntaxError, "'chunk' tag should have either 2 or 3 arguments"):
            self.render_template('{% load chunks %}'
                                 '{% chunk "home_page_left" 10 too much invalid arguments %}')


    def test_should_fail_if_key_not_quoted(self):
        with self.assertRaisesRegexp(TemplateSyntaxError, "'chunk' tag's argument should be in quotes"):
            self.render_template('{% load chunks %}'
                                 '{% chunk home_page_left %}')

        with self.assertRaisesRegexp(TemplateSyntaxError, "'chunk' tag's argument should be in quotes"):
            self.render_template('{% load chunks %}'
                                 '{% chunk "home_page_left\' %}')


    def render_template(self, content_string, context={}):
        template = Template(content_string)
        return template.render(Context(context))
