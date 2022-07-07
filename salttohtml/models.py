from django.db import models


class SaltCodeModel(models.Model):
    salt_code = models.TextField()
    def __str__(self):
        return self.salt_code
