from django.db import models

class LeaveStatus(models.TextChoices):
    PENDING = 'pending','Pending'
    APPROVED = 'approved','Approved'
    REJECTED = 'rejected','Rejected'

class TypeLeave(models.TextChoices):
    PAID = 'paid','Paid'
    UNPAID = 'unpaid','Unpaid'
    NATIONAL_HOLIDAY = 'national','National'