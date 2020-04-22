from django.conf import settings

ENTRY_BASIC_MODEL = getattr(settings, 'BASIC_MODEL',
                            'heldler.core.models_bases.entry.AbstractEntry')