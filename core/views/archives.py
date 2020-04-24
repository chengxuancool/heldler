from django.views.generic.dates import BaseArchiveIndexView
from django.views.generic.base import TemplateView
from core.models.entry import Entry
from core.views.view_mixs.entry import EntryMixin, EntryQuerysetArchiveTemplateResponseMixin
from core.views.view_mixs.callable_queryset import CallableQuerysetViewMixin
from core.views.view_mixs.prefetch_related import PrefetchCategoriesAuthorsMixin


class EntryIndex(EntryMixin,
                 PrefetchCategoriesAuthorsMixin,
                 CallableQuerysetViewMixin,
                 EntryQuerysetArchiveTemplateResponseMixin,
                 BaseArchiveIndexView):
    """
    This is the archive index View
    """
    # context_object_name = 'entry_list'
    queryset = Entry.published.all