from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='作成日時',
        null=False,
        blank=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='更新日時',
        null=False,
        blank=True,
    )
    delete_flag = models.BooleanField(
        verbose_name='削除フラグ',
        null=False,
        blank=True,
        default=False
    )
    class Meta:
        abstract = True