from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL


class Correspondence(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Letter(models.Model):
    edrms_id = models.CharField("EDRMS ID", max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True, blank=True, null=True)
    subject = models.TextField()
    dated = models.DateField()
    received = models.DateField()
    rec_from = models.ForeignKey(
        Correspondence,
        on_delete=models.PROTECT,
        related_name="rec_from_list",
        verbose_name="received from",
    )
    to = models.ForeignKey(
        Correspondence,
        on_delete=models.PROTECT,
        related_name="sent_to_list",
        verbose_name="sent to",
    )
    copied = models.ManyToManyField(
        Correspondence,
        blank=True,
        related_name="copied_to_list",
    )
    action = models.ForeignKey(
        Action, on_delete=models.PROTECT, related_name="action_list", default=1
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="created_by_list", null=True
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="updated_by_list", null=True
    )

    class meta:
        ordering = ["-created"]

    def get_absolute_url(self):
        return reverse("letter-detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("letter-update", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.edrms_id)
        super(Letter, self).save(*args, **kwargs)

    def __str__(self):
        return self.edrms_id


class LetterComment(models.Model):
    letter = models.ForeignKey(
        Letter, on_delete=models.CASCADE, related_name="letter_comments"
    )
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="comment_created_by_list",
        null=True,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="comment_updated_by_list",
        null=True,
    )

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.comment


# class LetterAttachments(models.Model):
#     letter = models.ForeignKey(
#         Letter, on_delete=models.PROTECT, related_name="letter_attachments"
#     )
