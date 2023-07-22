from django.db import models
from users.models import Member

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    publisher = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    book_image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    document = models.FileField(upload_to='book_documents/', blank=True, null=True)

    def __str__(self):
        return self.title
class Member(models.Model):
    member_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    books_borrowed = models.ManyToManyField('Book', through='Transaction')
    outstanding_debt = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return str(self.member_id)

class Transaction(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)  # Set default value to None
    issue_date = models.DateField()
    return_date = models.DateField()
    is_returned = models.BooleanField(default=False)
    rent_fee = models.DecimalField(max_digits=8, decimal_places=2, default=200)

    def __str__(self):
        return f"Transaction ID: {self.pk}, Book: {self.book.title}, Member: {self.member.name}"

    # Override the save method to set a default value for the member field if it is not provided
    def save(self, *args, **kwargs):
        if not self.member_id:
            # Use get_or_create to retrieve an existing member or create a new one with a default ID
            self.member, _ = Member.objects.get_or_create(member_id=0, defaults={'name': 'Default Member'})
        super().save(*args, **kwargs)

        