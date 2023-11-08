from django.urls import path

from .views import CorrespondenceCreateView  # HomeView,
from .views import (
    ActionCreateView,
    LetterCommentUpdateView,
    LetterUpdateView,
    letter_comment_create_view,
    letter_create_view,
    letter_detail_view,
    letter_list_view,
)

urlpatterns = [
    # path("", HomeView.as_view(), name="home"),
    path("", letter_list_view, name="letter-list"),
    path("create/", letter_create_view, name="letter-create"),
    path("letter/detail/<slug:slug>/", letter_detail_view, name="letter-detail"),
    path(
        "letter/update/<slug:slug>/", LetterUpdateView.as_view(), name="letter-update"
    ),
    path("add/comment/<slug:slug>/", letter_comment_create_view, name="add-comment"),
    path(
        "update/comment/<int:pk>/",
        LetterCommentUpdateView.as_view(),
        name="update-comment",
    ),
    path("create/action", ActionCreateView.as_view(), name="action-create"),
    path(
        "create/correspondence",
        CorrespondenceCreateView.as_view(),
        name="correspondence-create",
    ),
]
