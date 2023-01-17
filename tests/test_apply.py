"""
https://pytest-django.readthedocs.io/en/latest/configuring_django.html
"""


def test_new_applicant_job(applicant_1):
    print('ApplicantForm:', applicant_1.job)
    assert applicant_1.job == "engineer"


def test_new_applicant_name(applicant_1):
    print('ApplicantForm:', applicant_1.name)
    assert applicant_1.name == "Salah"


# foreign key, name = models.ForeignKey(ApplicantForm, on_delete=models.CASCADE, null=False)
def test_new_applicant_review_reviewd(applicant_1_review):
    print('Review:', applicant_1_review.reviewd)
    assert applicant_1_review.reviewd


# That's why applicant_1_review.name.name
def test_new_applicant_review_name(applicant_1_review):
    print('Review:', applicant_1_review.name.name)
    assert applicant_1_review.name.name == "Salah"
