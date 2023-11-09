from django.urls import path

from .views import StatusCreateView, StatusDetailView, StatusListView, StatusUpdateView

urlpatterns = [
    path("", StatusListView.as_view(), name="status-list"),
    path("add/", StatusCreateView.as_view(), name="status-create"),
    path("detail/<int:pk>/", StatusDetailView.as_view(), name="status-detail"),
    path("update/<int:pk>/", StatusUpdateView.as_view(), name="status-update"),
]
