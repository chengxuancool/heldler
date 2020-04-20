from django.conf.urls import url, include
from heldler.core import views

index_patterns = [
    url(r'^', include('heldler.core.urls.archives')),
]