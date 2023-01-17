# job-portal
Jobs portal Django, Easily post jobs and review the applications.

![D-version](https://img.shields.io/badge/Django-4.0.2-blue)
![P-version](https://img.shields.io/badge/Python-3.10-green)
![B-version](https://img.shields.io/badge/Bootstrap-5.0-purple)


## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/4yub1k/job-portal.git
   ```
2. Install requirements.txt
   ```sh
     pip install -r requirements.txt
   ```
3. Add SECRET_KEY (settings.py)\
   To generate key : [YouTube](https://youtube.com/shorts/kcmVnL2rQDI?feature=share)
   ```
   SECRET_KEY = '=========USE YOUR SECRET KEY=============' # from settings.py
   ```
4. Configure
   ```
   Configure Database(MySQL)
   Make migrations
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run
   ```
   python manage.py runserver
   ```
6. Run Tests:
   ```
   python -rP
   ```
   
   ```python
   ======================================================================= PASSES ======================================================================== 
   _______________________________________________________________ test_new_applicant_job ________________________________________________________________ 
   ---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------- 
   ApplicantForm: engineer
   _______________________________________________________________ test_new_applicant_name _______________________________________________________________ 
   ---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------- 
   ApplicantForm: Salah
   __________________________________________________________ test_new_applicant_review_reviewd __________________________________________________________ 
   ---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------- 
   Review: True
   ___________________________________________________________ test_new_applicant_review_name ____________________________________________________________ 
   ---------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------- 
   Review: Salah
   ============================================================ 4 passed in 0.96s ============================================================ 
   ```


**Add Job:**



https://user-images.githubusercontent.com/45902447/159235303-f5fbe2c0-5b7c-46b2-957d-84ae9eb617f9.mp4

**Apply:**


https://user-images.githubusercontent.com/45902447/159236848-f3f754c0-73d7-4022-bb9c-05b218ed935a.mp4


**Review:**



https://user-images.githubusercontent.com/45902447/159238264-c5fed053-3f36-4d86-855e-72c331cb4eeb.mp4

