from django.shortcuts import render
from listings.models import PostJob
# from django.contrib import messages


# Create your views here.
def index(request):
    jobs = PostJob.objects.order_by('-post_date')
    # print(jobs)
    context = {
        'jobs': jobs
    }
    # messages.success(request, 'you message.')
    return render(request, 'home/index.html', context)
