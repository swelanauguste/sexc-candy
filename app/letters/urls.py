from django.urls import path

from .views import letter_create_view, letter_list_view, letter_detail_view, letter_comment_create_view, CorrespondenceCreateView, ActionCreateView

urlpatterns = [
    path("", letter_list_view, name="letter-list"),
    path("create/", letter_create_view, name="letter-create"),
    path("letter/detail/<str:letter_id>/", letter_detail_view, name="letter-detail"),
    path("add/comment/<int:pk>/", letter_comment_create_view, name="add-comment"),
    path('create/action', ActionCreateView.as_view(), name='action-create'),
    path('create/correspondence', CorrespondenceCreateView.as_view(), name='correspondence-create'),
]
