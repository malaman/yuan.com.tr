from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from modelcluster.fields import ParentalKey
from common.models import CarouselItem, AppStreamBlock
from language.link import TranslatablePageMixin


class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('HomePage', related_name='carousel_items')

class HomePage(Page, TranslatablePageMixin):
    body = StreamField(AppStreamBlock())
    content_panels = [
        FieldPanel('title', classname="full title"),
        MultiFieldPanel(TranslatablePageMixin.panels, 'Language links'),
        StreamFieldPanel('body'),
        InlinePanel('carousel_items', label="Carousel items"),
    ]
