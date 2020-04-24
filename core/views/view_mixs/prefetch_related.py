from django.core.exceptions import ImproperlyConfigured


class PrefetchRelatedMixin(object):
    relation_names = None

    def get_queryset(self):
        if self.relation_names is None:
            raise ImproperlyConfigured(
                "'%s' must a avaiable 'relation_names'".format(self.__class__.__name__)
            )

        if not isinstance(self.relation_names, (tuple, list)):
            raise ImproperlyConfigured(
                "%s's relation_names must be tuple or list."
            )

        return super(PrefetchRelatedMixin, self).get_queryset().prefetch_related(*self.relation_names)


class PrefetchCategoriesAuthorsMixin(PrefetchRelatedMixin):
    relation_names = ('categories', 'authors')