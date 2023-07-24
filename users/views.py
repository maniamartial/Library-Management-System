from django.urls import reverse
from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
# from users.decorators import unauthenticated_user
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
# from django.forms.widgets import EmailInput
from .form import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import MemberForm

def member_registration(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created successfully for " + username)
            return redirect('login')
        else:
            # Print the form errors to the console for debugging
            print(form.errors)

    context = {'form': form}
    return render(request, "users/register.html", context)

import logging



logger = logging.getLogger(__name__)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect(reverse('book_listing'))
        else:
            messages.error(request, 'Username or Password is incorrect')
            logger.error(f"Failed login attempt for user: {username}")

    context = {'next': request.GET.get('next')}
    return render(request, "users/login.html", context)


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_listing')  # Redirect to a view to display the list of members
    else:
        form = MemberForm()
    
    return render(request, 'users/member_form.html', {'form': form})

