from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # instance =
            form.save()
            # instance.author = request.user
            # instance.save()
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context=context)
