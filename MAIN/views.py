from django.shortcuts import render, redirect
from .forms import LandRequestForm
from .models import LandRequest
from django.db.models import Q


def home(request):
    return render(request, 'index.html')

def create_land_request(request):
    if request.method == "POST":
        form = LandRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('land_request_list')  # Change 'work' to 'land_request_list'
    else:
        form = LandRequestForm()

    return render(request, 'create.html', {'form': form})



def land_request_list(request):
    land_requests = LandRequest.objects.all()  # removed .order_by('-created_at')
    return render(request, 'list1.html', {'land_requests': land_requests})

def search_land_requests(request):
    query = request.GET.get('q', '')
    land_requests = LandRequest.objects.filter(
        Q(client_name__icontains=query) |
        Q(mobile_number__icontains=query) |
        Q(user_area__icontains=query) |
        Q(user_district__icontains=query) |
        Q(user_state__icontains=query) |
        Q(user_country__icontains=query) |
        Q(land_area__icontains=query) |
        Q(land_district__icontains=query) |
        Q(land_state__icontains=query) |
        Q(land_country__icontains=query) |
        Q(land_required_sqft__icontains=query) |
        Q(additional_details__icontains=query)
    )
    return render(request, 'request.html', {'land_requests': land_requests})