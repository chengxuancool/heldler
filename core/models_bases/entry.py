from django.db import models


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