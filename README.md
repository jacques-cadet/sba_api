## SBA Submission of Forgiveness Request for SBA decisioning and Lookup/Validate disbursed Loans Django Rest Api


Create virtual environment.

In bash terminal type;
* `cd src`
* `pip install -r requirements.txt`
* `cd sba`
* `./manage.py migrate`
* `./manage.py createsuperuser`

Follow prompts
* `./manage.py runserver`

Then navigate to:
* `hostname/api`

Sign in at top right with username and password,

Then navigate to any of the following;

* `hostname/api/ppp_loan_forgiveness_requests`
* `hostname/api/ppp_loan_validations`
* `hostname/api/ppp_loan_documents`