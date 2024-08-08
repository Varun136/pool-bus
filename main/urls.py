from django.urls import path
from .views import SearchRoutesView, ListStopView

urlpatterns = [
    path('search-routes', SearchRoutesView.as_view(), name='search-routes'),
    path('all-stops', ListStopView.as_view(), name='all-stops')
]