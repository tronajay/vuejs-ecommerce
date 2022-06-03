from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
    