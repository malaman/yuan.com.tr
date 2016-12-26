from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel, PageChooserPanel


class TranslatablePageMixin(models.Model):
    # One link for each alternative language
    # These should only be used on the main language page (english)
    turkish_link = models.ForeignKey(Page, null=True, on_delete=models.SET_NULL, blank=True, related_name='+')

    panels = [
        PageChooserPanel('turkish_link'),
    ]

    def get_language(self):
        """
        This returns the language code for this page.
        """
        # Look through ancestors of this page for its language homepage
        # The language homepage is located at depth 3
        language_homepage = self.get_ancestors(inclusive=True).get(depth=3)

        # The slug of language homepages should always be set to the language code
        return language_homepage.slug


    # Method to find the main language version of this page
    # This works by reversing the above links

    def english_page(self):
        """
        This finds the english version of this page
        """
        language = self.get_language()

        if language == 'en':
            return self
        elif language == 'tr':
            return type(self).objects.filter(turkish_link=self).first().specific


    # We need a method to find a version of this page for each alternative language.
    # These all work the same way. They firstly find the main version of the page
    # (english), then from there they can just follow the link to the correct page.

    def turkish_page(self):
        """
        This finds the turkish version of this page
        """
        english_page = self.english_page()

        if english_page and english_page.turkish_link:
            return english_page.turkish_link.specific

    class Meta:
        abstract = True
