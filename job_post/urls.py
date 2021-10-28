from django.conf.urls.static import static
from django.urls import path

from upwork import settings
from . import views


app_name = 'upwork'

urlpatterns = [
    path('search_results', views.SearchResultsView.as_view(), name='search_results'),
    path('', views.HomeView.as_view(), name='home'),
    path('profile/', views.user_profile, name='profile'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)