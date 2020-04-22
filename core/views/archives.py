from django.views.generic.dates import BaseArchiveIndexView
from core.models.entry import Entry
from core.views.view_mixs.entry import EntryMixin


class EntryIndex(EntryMixin, BaseArchiveIndexView):
    """
    This is the archive index View
    """
    context_object_name = 'entry_list'
    queryset = Entry.new_object.all()