from django import forms 
from .models import Book, Transaction, Member

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity_in_stock', 'publisher', 'book_image', 'document']

    # Add form field widget attributes to control the appearance and behavior of fields
    widgets = {
        'book_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        'document': forms.FileInput(attrs={'class': 'form-control-file'}),
    }

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity_in_stock', 'publisher', 'book_image', 'document']

    # Add form field widget attributes to control the appearance and behavior of fields
    widgets = {
        'book_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        'document': forms.FileInput(attrs={'class': 'form-control-file'}),
    }

class TransactionForm(forms.ModelForm):
    return_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    member = forms.ModelChoiceField(
        queryset=Member.objects.all(),  # Query all Member objects
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,  # Set to False to make it optional in the form
    )

    class Meta:
        model = Transaction
        fields = ['member', 'rent_fee', 'return_date']


class TransactionUpdateForm(forms.ModelForm):
    return_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    member = forms.ModelChoiceField(
        queryset=Member.objects.all(),  # Query all Member objects
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,  # Set to False to make it optional in the form
    )
    class Meta:
        model = Transaction
        fields = ['member', 'rent_fee', 'return_date']
# Use 'member' instead of 'member_name' and 'member_id'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_id', 'name']  # Include 'member_id' and 'name' fields only

class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_id', 'name']