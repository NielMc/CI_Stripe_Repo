from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
