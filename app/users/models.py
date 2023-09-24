import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    pass
    # is_buyer = models.BooleanField(default=False)
    # is_seller = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)


class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    gender = models.ForeignKey(
        Gender,
        on_delete=models.PROTECT,
        related_name="user_gender_list",
        null=True,
        blank=True,
    )
    phone = models.TextField(null=True, default="+1")
    bio = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})

    def get_profile_initials(self):
        if self.first_name and self.last_name:
            return f"{self.first_name[0]} {self.last_name[0]}"
        return self.user.email[0]

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.email
