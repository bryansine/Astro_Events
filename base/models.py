from django.db import models

class PetitionSignup(models.Model):
    # Define fields for a petition signup
    name = models.CharField(max_length=100)  # Name of the person signing the petition
    email = models.EmailField()  # Email address of the person signing the petition
    message = models.TextField(blank=True, null=True)  # Optional message from the signer
    signed_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the petition was signed

    def __str__(self):
        # Return the name of the person signing the petition
        return f'{self.name}'

