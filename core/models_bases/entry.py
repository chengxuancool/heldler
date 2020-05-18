from django.db import models
from django.utils import timezone
from core.managers import EntryPublishedManager


class BaseEntry(models.Model):
    """
    Abstract entry model class providing
    the main fields and methods for content
    publishing.
    """
    STATUS_CHOICES = ((0, 'draft'),
                      (1, 'hidden'),
                      (2, 'published'))

    title = models.CharField('title', max_length=255)
    slug = models.SlugField(
        'slug', max_length=255,
        unique_for_date='publication_date',
        help_text="Used to build the entry's URL."
    )
    status = models.IntegerField(
        'status', db_index=True,
        choices=STATUS_CHOICES, default=0
    )

    publication_date = models.DateTimeField(
        'publication date',
        db_index=True, default=timezone.now,
        help_text="Used to build the entry's URL.")

    last_update = models.DateTimeField(
        'last update date', default=timezone.now())

    object = models.Manager()
    published = EntryPublishedManager()

    class Meta:
        """
        base entry meta info
        """
        abstract = True
        ordering = ['-publication_date']
        get_latest_by = 'publication_date'
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
        # index_together = []
        permissions = (('can_view_all', 'Can view all entries'),
                       ('can_change_status', 'Can change status'),
                       ('can_change_author', 'Can change authors(s)'))


class ContentEntry(models.Model):
    """
    Abstract content model class defined fields and methods
    """
    content = models.TextField('content', blank=True)

    class Meta:
        abstract = True

class AbstractEntry(
        BaseEntry,
        ContentEntry):
    """
    abstract entry model class assembling
    all the abstract entry model in this class

    In this manner we can override some fields without
    reimplement all the Abstract Entries.
    """

    class Meta(BaseEntry.Meta):
        abstract = True