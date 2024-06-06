from django.db import models

class PetitionSignup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    signed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} '
