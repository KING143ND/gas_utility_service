from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from .models import Customer
from django.http import HttpResponse, Http404
from django.conf import settings
import os


@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(customer__user=request.user)
    return render(request, 'customer_service/request_list.html', {'requests': requests})


@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    context = {
        'request': service_request
    }
    return render(request, 'customer_service/request_detail.html', context)

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/request_form.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                user=user,
                address=form.cleaned_data.get('address'),
                phone_number=form.cleaned_data.get('phone_number'),
                account_number=form.cleaned_data.get('username')+form.cleaned_data.get('phone_number'),
            )
            login(request, user)
            return redirect('request_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'service_requests', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    raise Http404("File does not exist")