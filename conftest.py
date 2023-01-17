import pytest
from apply.models import ApplicantForm
from apply.models import Review


@pytest.fixture()
def applicant_db(db):
    applicant = ApplicantForm.objects.create(job="Engineer", name="salah")
    return applicant


@pytest.fixture
def new_applicant_factory(db):
    # apply model fields
    def create_new_applicant(
        # job: str,
        job: str,
        name: str,
        email: str,
        mobile: str,
        education: str,
        exp: str,
        resume: str = None,
    ) -> ApplicantForm:
        applicant: object = ApplicantForm.objects.create(
            job=job,
            name=name,
            email=email,
            mobile=mobile,
            education=education,
            exp=exp,
            resume=resume,
        )
        return applicant

    return create_new_applicant


@pytest.fixture
def applicant_1(db, new_applicant_factory):
    return new_applicant_factory(
        "engineer", "Salah", "test@test,com", "00-001-00011", "BS", "2"
    )


@pytest.fixture
def new_applicant_review_factory(db):
    def create_new_applicant_review(
        name: str, reviewd: bool = False, ratings: str = "0", remarks: str = None
    ) -> Review:
        applicant_review = Review.objects.create(
            name=name, reviewd=reviewd, ratings=ratings, remarks=remarks
        )
        return applicant_review

    return create_new_applicant_review


@pytest.fixture
# applicant_1 foreign key
def applicant_1_review(db, new_applicant_review_factory, applicant_1):
    # "'Salah'": "Review.name" must be a "ApplicantForm" instance., That's why only applicant_1
    return new_applicant_review_factory(applicant_1, True, "8", "Pending..")
