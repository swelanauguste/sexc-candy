from django.urls import path

from .views import (
    ActionCreateView,
    CorrespondenceCreateView,
    # HomeView,
    letter_comment_create_view,
    letter_create_view,
    letter_detail_view,
    letter_list_view,
)

urlpatterns = [
    # path("", HomeView.as_view(), name="home"),
    path("", letter_list_view, name="letter-list"),
    path("create/", letter_create_view, name="letter-create"),
    path("letter/detail/<int:slug>/", letter_detail_view, name="letter-detail"),
    path("add/comment/<int:slug>/", letter_comment_create_view, name="add-comment"),
    path("create/action", ActionCreateView.as_view(), name="action-create"),
    path(
        "create/correspondence",
        CorrespondenceCreateView.as_view(),
        name="correspondence-create",
    ),
]
