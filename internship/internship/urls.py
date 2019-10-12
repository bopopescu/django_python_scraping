from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url


urlpatterns = [
    path('', include('mywebsite.urls')),
    # path('signup/', include('mywebsite.urls')),
    # url('scraping_admin', include('scraping_admin.urls')),
    path('admin/', admin.site.urls),
]


