from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from language.link import TranslatablePageMixin


class HomePage(Page, TranslatablePageMixin):
    content_panels = [
        MultiFieldPanel(TranslatablePageMixin.panels, 'Language links')
    ]
