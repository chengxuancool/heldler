from importlib import import_module

from django.core.exceptions import ImproperlyConfigured


def load_model_class(model_path):
    mod = model_path.rindex('.')
    module_name = model_path[:mod]
    class_name = model_path[mod + 1:]

    try:
        _class = getattr(import_module(module_name), class_name)
        return _class
    except (ImportError, AttributeError):
        raise ImproperlyConfigured('%s cannot be imported' % model_path)