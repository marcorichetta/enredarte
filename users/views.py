from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from users.forms import UserRegisterForm

# Create your views here.


def register(request):

    # Redirect to index
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    """ Register a new user """
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Retrieve username from cleaned_data to show it on message
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'{username}, tu usuario fue creado. Por favor, inicia sesión')
            return redirect('login')
    # GET Request
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
