from django.shortcuts import render
from realtors.models import Realtor

# Create your views here.
def index(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'realtors' : realtors,
    }
    return render(request, 'pages/sell.html', context)
