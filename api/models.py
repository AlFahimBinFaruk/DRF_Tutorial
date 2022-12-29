from django.db import models
import uuid

# Testmodel
class TestModel(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    title = models.CharField(max_length=200,null=False)
    desc = models.TextField(null=True)