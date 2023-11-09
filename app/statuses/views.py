from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.db.models import Q
from .forms import StatusForm
from .models import Status


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    success_message = "%(name)s was added"
    success_url = reverse_lazy("status-list")


class StatusDetailView(LoginRequiredMixin, DetailView):
    model = Status


class StatusListView(LoginRequiredMixin,ListView):
    model = Status
    extra_context = {"form": StatusForm}

    def get_queryset(self):
        query = self.request.GET.get("statuses")
        if query:
            return Status.objects.filter(
                Q(name__icontains=query) | Q(uid__icontains=query)
            ).distinct()
        else:
            return Status.objects.all()


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin,UpdateView):
    model = Status
    form_class = StatusForm
    success_message = "%(name)s was edited"
    success_url = reverse_lazy("status-list")
