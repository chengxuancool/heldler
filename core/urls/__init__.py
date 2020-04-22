from django.conf.urls import url, include

app_name = 'core'

index_patterns = [
    url(r'^', include('core.urls.archives')),
]

archive_patterns = (index_patterns) # can add new pattern into this tuple

urlpatterns = archive_patterns