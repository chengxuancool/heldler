from django.views.generic.dates import BaseArchiveIndexView


class EntryIndex(BaseArchiveIndexView):
    """
    This is the archive index View
    """
    context_object_name = 'entry_list'