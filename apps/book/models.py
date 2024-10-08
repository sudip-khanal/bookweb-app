from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pdf_file = models.FileField(
        upload_to="books/", validators=[FileExtensionValidator(allowed_extensions=["pdf"])]
    )   
    description = models.TextField(max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Model representing a user's favorite book
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    #  a user can not favorite the same book more than once
    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.book.title}"

