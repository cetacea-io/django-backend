from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

import object_tools

urlpatterns = [
    path('', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('admin/', admin.site.urls),
    path('object_tools/', object_tools.tools.urls), # needed for django categories
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
