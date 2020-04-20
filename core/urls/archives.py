from django.conf.urls import url

from heldler.core.views.archives import EntryIndex

index_patterns = [
    url(r'^$',
        EntryIndex.as_view(),
        name='entry_index_archive'),
]