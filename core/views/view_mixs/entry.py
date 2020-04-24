from django.views.generic.base import TemplateResponseMixin


class EntryMixin(object):
    allow_future = True
    allow_empty = True
    date_field = 'publication_date'


class EntryQuerysetArchiveTemplateResponseMixin(TemplateResponseMixin):

    def get_template_names(self):
        templates = []
        template_name = 'core/entry_index.html'
        templates.append(template_name)

        return templates