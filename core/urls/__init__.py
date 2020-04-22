from django.conf.urls import url, include

app_name = 'core'

urlpatterns = [
    url(r'^', include('core.urls.archives')),
]