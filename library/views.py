from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from .form import BookForm, BookUpdateForm, TransactionForm, TransactionUpdateForm, MemberForm, MemberUpdateForm
from .models import Book, Transaction, Member
from django.contrib import messages


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_listing')  # Redirect to a view to display the list of books
    else:
        form = BookForm()
    
    return render(request, 'library/add_book.html', {'form': form})


#list of  available
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

#process transaction, will be called inside create transaction
def process_transaction_form(request, book, form):
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

        # Check if the member's outstanding debt will be more than 500 after the transaction
        if member.outstanding_debt + rent_fee > 500:
            extra_debt = member.outstanding_debt + rent_fee - 500
            messages.error(request, f"Member will surpass the expected debt by {extra_debt}. They must pay to continue with transactions.")
            return None

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

        # Reduce the book quantity in stock by 1
        book.quantity_in_stock -= 1
        book.save()

        return transaction

    return None


def create_transaction(request, book_id):
    # Retrieve the book using the provided book_id
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        transaction = process_transaction_form(request, book, form)
        if transaction:
            return redirect('transaction_list')  # Redirect to a view to display the list of transactions
        else:
            # Print the form errors and choices to the console for debugging
            print(form.errors)
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

#Members list
def members_list(request):
    members = Member.objects.all()
    return render(request, 'library/members_list.html', {'members': members})

#Update members
def update_member(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        form = MemberUpdateForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members_list')  # Redirect to the member list view after successful update
    else:
        form = MemberUpdateForm(instance=member)

    return render(request, 'library/update_member_details.html', {'form': form})

#Delete members
def delete_member(request, member_id):  # Use 'member_id' here to match the URL parameter
    member = get_object_or_404(Member, id=member_id)  # Use 'id' to match the primary key field in the Member model

    if request.method == 'POST':
        member.delete()
        return redirect('members_list')  # Redirect to a view to display the list of members

    return render(request, 'library/confirm_delete_member.html', {'member': member})



#Return teh book
def mark_transaction_returned(transaction_id):
    # Get the transaction using the provided transaction_id
    transaction = get_object_or_404(Transaction, pk=transaction_id)

    # Check if the transaction is not already marked as returned
    if not transaction.is_returned:
        # Mark the transaction as returned and save it
        transaction.is_returned = True
        transaction.save()

        # Retrieve the member and book related to the transaction
        member = transaction.member
        book = transaction.book

        # Increase the book quantity in stock by 1
        book.quantity_in_stock += 1
        book.save()

        # Reduce the outstanding debt of the member by the rent_fee of the transaction
        member.outstanding_debt -= transaction.rent_fee
        member.save()


def return_book(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)

    if request.method == 'POST':
        
        if request.POST.get('returned') == 'yes':
            # Call the mark_transaction_returned function to update book, transaction, and member
            mark_transaction_returned(transaction_id)

            # Check if the transaction amount is paid
            if request.POST.get('paid') == 'yes':
                # Reduce the member's outstanding debt by the book's rent fee
                member = transaction.member
                member.outstanding_debt -= transaction.rent_fee
                member.save()

        return redirect('transaction_list')  # Redirect to a view to display the list of transactions
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'library/return_book.html', {'form': form, 'transaction': transaction})
