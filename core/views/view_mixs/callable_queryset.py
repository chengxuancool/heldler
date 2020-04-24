from django.core.exceptions import ImproperlyConfigured


class CallableQuerysetViewMixin(object):
    queryset = None

    def get_queryset(self):
        if self.queryset is None:
            raise ImproperlyConfigured(
                "'%s' must a available 'queryset'".format(self.__class__.__name__)
            )

        return self.queryset()