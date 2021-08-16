from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Sale


@receiver(m2m_changed, sender=Sale.positions.through)
def calculate_total_price(sender, instance, action, **kwargs):
    if action in ('post_add', 'post_remove'):
        prices = [position.price for position in instance.get_positions()]
        instance.total_price = sum(prices)
        instance.save()
