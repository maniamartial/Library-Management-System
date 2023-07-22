from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from .form import BookForm, BookUpdateForm, TransactionForm, TransactionUpdateForm, MemberForm
from .models import Book, Transaction, Member


def home_page(request):
    return render(request, 'library/home.html')


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_listing')  # Redirect to a view to display the list of books
    else:
        form = BookForm()
    
    return render(request, 'library/add_book.html', {'form': form})


# def all_books(request):
#     try:
#         books = Book.objects.all()
#     except Book.DoesNotExist:
#         books = []  # If no books exist, initialize books as an empty list
#     return render(request, 'library/book_listing.html', {'books': books})

def all_books(request):
    query = request.GET.get('q')  # Get the query parameter from the URL
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'library/book_listing.html', {'books': books})

def update_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookUpdateForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_listing')  # Redirect to a view to display all books
    else:
        form = BookUpdateForm(instance=book)
    
    return render(request, 'library/update_book_details.html', {'form': form})


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_listing')  # Redirect to a view to display all books

    return render(request, 'library/confirm_delete_book.html', {'book': book})

from datetime import date

# def create_transaction(request, book_id):
#     # Retrieve the book using the provided book_id
#     book = get_object_or_404(Book, pk=book_id)

#     if request.method == 'POST':
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             member_id = form.cleaned_data['member_id']
#             member_name = form.cleaned_data['member_name']
#             rent_fee = form.cleaned_data['rent_fee']
#             return_date = form.cleaned_data['return_date']

#             # Check if the member with the given member_id exists
#             try:
#                 member = Member.objects.get(member_id=member_id)
#             except Member.DoesNotExist:
#                 # If member does not exist, create a new one
#                 member = Member.objects.create(member_id=member_id, name=member_name)

#             # Calculate the outstanding debt for the member
#             member.outstanding_debt += rent_fee
#             member.save()

#             # Create the transaction and link it to the member and book
#             transaction = Transaction.objects.create(
#                 book=book,
#                 member=member,
#                 issue_date=date.today(),
#                 return_date=return_date,
#                 rent_fee=rent_fee,
#             )

#             return redirect('transaction_list')  # Redirect to a view to display the list of transactions
#     else:
#         form = TransactionForm()

#     return render(request, 'library/create_transaction.html', {'form': form})
def create_transaction(request, book_id):
    # Retrieve the book using the provided book_id
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            member_id = form.cleaned_data['member'].member_id
            rent_fee = form.cleaned_data['rent_fee']
            return_date = form.cleaned_data['return_date']

            # Check if the member with the given member_id exists
            try:
                member = Member.objects.get(member_id=member_id)
            except Member.DoesNotExist:
                # If member does not exist, create a new one
                return redirect('add_member')  # Redirect to the add_member view

            # Calculate the outstanding debt for the member
            member.outstanding_debt += rent_fee
            member.save()

            # Create the transaction and link it to the member and book
            transaction = Transaction.objects.create(
                book=book,
                member=member,
                issue_date=date.today(),
                return_date=return_date,
                rent_fee=rent_fee,
            )

            return redirect('transaction_list')  # Redirect to a view to display the list of transactions
        else:
            # Print the form errors and choices to the console for debugging
            print(form.errors)
            print(form.fields['member'].choices)
            print("Submitted member ID:", form.data['member'])
    else:
        form = TransactionForm()

    return render(request, 'library/create_transaction.html', {'form': form, 'book': book})


    #Show transaction
def transaction_list(request):
    try:
        transactions = Transaction.objects.all()
    except Transaction.DoesNotExist:
        transactions = []  # If no transactions exist, initialize transactions as an empty list

    return render(request, 'library/transaction_list.html', {'transactions': transactions})



# View for updating a transaction
def update_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'library/update_transaction.html', {'form': form})


# View for deleting a transaction
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)

    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')  # Redirect to a view to display the updated list of transactions

    return render(request, 'library/delete_transaction.html', {'transaction': transaction})


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_listing')
    else:
        form = MemberForm()
    return render(request, 'library/add_member.html', {'form': form})