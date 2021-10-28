from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from job_post.views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    # path('register/*', CompleteRegisterView.as_view(), name='complete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('job_post.urls')),
]
