from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site

DRAFT = 0
HIDDEN = 1
PUBLISHED = 2


# def entries_published(queryset):
#     now = timezone.now()
#     query_set = queryset.filter(
#         models.Q(start_publication__lte=now) |
#         models.Q(start_publication=None),
#         models.Q(end_publication__gt=now) |
#         models.Q(end_publication=None),
#         status=PUBLISHED, site=Site.objects.get_current())
#
#     return query_set


def entries_published(queryset):
    now = timezone.now()
    query_set = queryset.filter(
        models.Q(publication_date__lte=now)
    )

    return query_set


class EntryPublishedManager(models.Manager):
    def get_queryset(self):
        return entries_published(super(EntryPublishedManager, self).get_queryset())