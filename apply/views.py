from django.shortcuts import redirect
from django.contrib import messages
from .models import ApplicantForm


def apply(request):
    if request.method == "POST":
        job_title = request.POST.get("job_title", False)
        first = request.POST.get("first", False)
        last = request.POST.get("last", False)
        email = request.POST.get("email", False)
        mobile = request.POST.get("mobile", False)
        education = request.POST.get("education", False)
        experience = request.POST.get("experience", False)
        fileresume = request.FILES.get("fileresume", False)
        if not str(fileresume).lower().endswith(".pdf"):
            return redirect("index")
        # print(fileresume)
        # qwrqwerqwe@afasdf.com add email check here!
        if (
            first
            and email
            and mobile
            and education
            and experience
            and fileresume
            and job_title
        ):
            # print(request.POST)
            # print(request.FILES)
            ApplicantForm.objects.create(
                job=job_title,
                name=f"{first} {last}",
                email=email,
                mobile=mobile,
                education=education,
                exp=experience,
                resume=fileresume,
            )
            messages.success(request, f"Applied to post {job_title}, Successfully !")
            return redirect("index")
    return redirect("index")
