from django.conf.urls import url

from core.views.archives import EntryIndex

urlpatterns = [
    url(r'^$',
        EntryIndex.as_view(),
        name='entry_index_archive'),
]