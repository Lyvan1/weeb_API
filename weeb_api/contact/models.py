from django.db import models


class Contact(models.Model):
    """Contact entity for storing contact form submissions."""
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return f"{self.full_name} <{self.email}>"


