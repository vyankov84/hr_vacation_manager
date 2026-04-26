from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

from leave_requests.choices import TypeLeave, LeaveStatus


class LeaveRequest(models.Model):

    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='leave_requests'
    )

    start_date = models.DateField()
    end_date = models.DateField()

    leave_type = models.CharField(
        max_length=20,
        choices=TypeLeave.choices,
        default=TypeLeave.PAID
    )

    reason = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=15,
        choices=LeaveStatus.choices,
        default=LeaveStatus.PENDING
    )

    is_processed = models.BooleanField(default=False)

    @property
    def duration_off(self) -> int:
        if self.start_date and self.end_date:
            delta = (self.end_date - self.start_date).days
            return delta + 1
        return 0


    def clean(self):
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError({
                    "end_date": "This not a time machine, the end date is before the start date!!!"
                })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} ({self.start_date} - {self.end_date})"
