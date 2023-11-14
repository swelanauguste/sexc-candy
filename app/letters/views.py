from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import (
    LetterCommentCreateForm,
    LetterCommentUpdateForm,
    LetterCreateForm,
    LetterUpdateForm,
)
from .models import Action, Correspondence, Letter, LetterComment

# class HomeView(TemplateView):
#     template_name = "home.html"


class LetterCommentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = LetterComment
    fields = ["comment"]
    success_message = "Updated"
    # template_name_suffix = "_update_form"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        comment = LetterComment.objects.get(pk=self.kwargs["pk"])
        return comment.letter.get_absolute_url()


class ActionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Action
    fields = ["name"]
    success_url = "/"


class CorrespondenceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Correspondence
    fields = ["name"]
    success_url = "/"


def my_custom_page_not_found_view(request, exception):
    return render(request, "404.html", status=404)


@login_required
def letter_list_view(request):
    """
    List all letters.
    """
    form = LetterCreateForm()
    comment_form = LetterCommentCreateForm()
    query = request.GET.get("letters")
    if query:
        letters = Letter.objects.filter(
            Q(edrms_id__icontains=query)
            | Q(to__name__icontains=query)
            | Q(subject__icontains=query)
        ).distinct()
    else:
        letters = Letter.objects.all().order_by('-received')
    return render(
        request,
        "letters/letter_list.html",
        {"letters": letters, "form": form, "comment_form": comment_form},
    )


@login_required
def letter_create_view(request):
    """
    Create a new letter.
    """
    letters = Letter.objects.all()
    if request.method == "POST":
        form = LetterCreateForm(request.POST)
        if form.is_valid():
            letter = form.save()
            letter.created_by = request.user
            letter.updated_by = request.user
            messages.success(
                request,
                f"{letter.edrms_id} was added.",
            )
            return redirect("letter-list")
    else:
        form = LetterCreateForm()
        return render(request, "letters/letter_list.html", {"form": form})
    return render(
        request, "letters/letter_list.html", {"form": form, "letters": letters}
    )


class LetterUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Letter
    form_class = LetterUpdateForm
    success_message = "Updated"
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


@login_required
def letter_detail_view(request, slug):
    """
    Show a letter.
    """
    letter = Letter.objects.get(slug=slug)
    comment_form = LetterCommentCreateForm()
    # comments = LetterComments.objects.filter(letter=letter)
    return render(
        request,
        "letters/letter_detail.html",
        {"letter": letter, "comments": "comments", "comment_form": comment_form},
    )


@login_required
def letter_comment_create_view(request, slug):
    letter = get_object_or_404(Letter, slug=slug)
    if request.method == "POST":
        form = LetterCommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.letter = letter
            comment.save()
            comment.created_by = request.user
            comment.updated_by = request.user
            messages.success(
                request,
                f"Your comment was added.",
            )
            letter_detail_url = reverse("letter-detail", args=[letter.slug])
            return redirect(letter_detail_url)
    else:
        form = LetterCreateForm()
    return render(request, "letters/letter_list.html", {"form": form, "letter": letter})
