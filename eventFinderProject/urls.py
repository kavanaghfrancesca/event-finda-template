from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('event-finder/', include('eventFinderApp.urls'), name='eventFinderApp'),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls'), name='users'),
]