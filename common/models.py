from django.utils import timezone
from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)


class DeleteMixin(models.Model):
    deleted_at = models.DateTimeField('记录删除时间', null=True, blank=True, default=None)

    objects = DeleteManager()
    allobjects = models.Manager()

    @property
    def is_deleted(self):
        return True if self.deleted_at else False

    class Meta:
        abstract = True

    def _delete(self, using=None, keep_parents=False):
        super(DeleteMixin, self).delete()

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()
