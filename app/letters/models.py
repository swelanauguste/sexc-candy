from django.conf import settings
from django.db import models

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
    subject = models.TextField()
    date_on_doc = models.DateField("date on document")
    date_received = models.DateField()
    rec_from = models.ForeignKey(
        Correspondence,
        on_delete=models.PROTECT,
        related_name="rec_from_list",
        verbose_name="received from",
    )
    sent_to = models.ForeignKey(
        Correspondence,
        on_delete=models.PROTECT,
        related_name="sent_to_list",
        verbose_name="sent to",
    )
    copied_to = models.ManyToManyField(
        Correspondence, blank=True,
        related_name="copied_to_list",
    )
    action = models.ForeignKey(
        Action, on_delete=models.PROTECT, related_name="action_list", default=1
    )

    def __str__(self):
        return self.edrms_id


class LetterComment(models.Model):
    letter = models.ForeignKey(
        Letter, on_delete=models.CASCADE, related_name="letter_comments"
    )
    comment = models.TextField()
    
    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return self.comment


# class LetterAttachments(models.Model):
#     letter = models.ForeignKey(
#         Letter, on_delete=models.PROTECT, related_name="letter_attachments"
#     )
