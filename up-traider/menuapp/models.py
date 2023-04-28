from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=100)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Пункт меню MPTT'
        verbose_name_plural = 'Пункты меню MPTT'

    def __str__(self):
        return self.name
