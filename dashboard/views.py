from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from apply.models import ApplicantForm, Review

@login_required(login_url='/dashboard/signin/') #or settings.LOGIN_URL='/dashboard/signin/'
def dashboard(request):
    if request.method == 'POST':
        applicant_id = request.POST.get('applicant_id',0)
        applicant_name_id =request.POST.get('applicant_name_id',0)
        name = request.POST.get('name',0)
        ratings = request.POST.get('ratings',0)
        reviewd = request.POST.get('reviewd',0)
        remarks = request.POST.get('remarks',0)
        print(request.POST)
        if applicant_id and name and reviewd:
            applicant = Review.objects.filter(id=applicant_id, name=applicant_name_id)
            if not applicant:
                return redirect('dashboard')
            print(applicant)
            applicant.update(name=applicant_name_id,ratings=ratings,reviewd=reviewd,remarks=remarks)
            messages.success(request, f'Reviewd {name}, Successfully !')
            return redirect('dashboard')

    applicants = Review.objects.all()
    context = {
        'applicants':applicants
    }
    return render(request,'dashboard/dashboard.html',context)