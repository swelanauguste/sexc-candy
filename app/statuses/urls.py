from django.urls import path

from .views import StatusCreateView, StatusListView, StatusUpdateView

urlpatterns = [
    path("", StatusListView.as_view(), name="status-list"),
    path("add/", StatusCreateView.as_view(), name="status-create"),
    path("update/<int:pk>/", StatusUpdateView.as_view(), name="status-update"),
]
