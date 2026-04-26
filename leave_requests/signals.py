from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

from balances.models import LeaveBalance
from leave_requests.choices import LeaveStatus
from leave_requests.models import LeaveRequest


@receiver (post_save, sender=LeaveRequest)
def update_leave_balance_on_approval(sender, instance, created, **kwargs):

    if instance.status == LeaveStatus.APPROVED and not instance.is_processed:
        .
        try:
            balance = LeaveBalance.objects.get(employee=instance.employee)

            if balance.annual_leave_remaining < instance.duration_off:
                raise ValueError(f'You don\'t have enough days off!')

            balance.annual_leave_remaining -= instance.duration_off
            balance.save()
            LeaveRequest.objects.filter(pk=instance.pk).update(is_processed=True)

        except LeaveBalance.DoesNotExist:
            raise ValueError(f'No balance found for the employee {instance.employee}')
