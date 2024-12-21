from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db.models import Sum
from .models import Pedido

@receiver(m2m_changed, sender=Pedido.produtos.through)
def update_pedido_total(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.total = instance.produtos.aggregate(total=Sum('preco'))['total'] or 0.0
        instance.save()
