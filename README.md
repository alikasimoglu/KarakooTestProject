# django-marketing-management-project

This is a back-end aimed marketing management test project with minimal front-end functions. The aim of the project is a small web-based application for XYZ service company, which would facilitate the marketing and contribute to efficient communication between staff and customers.

## Before You Begin

1. You should generate SecretKey here <https://djecrety.ir/>
2. If you want to use pasword reset system, you should have a gmail account and in the account security settings; 
   1. Activate two-factor authentication
   2. Create App password
   
   _**Not:** It's not necessary. When debug mode is on, console is used as mail manager._
3. In your IDE install project environment requirements we need.

```bash
$ git@github.com:alikasimoglu/KarakooTestProject.git
```
Now you can access the application at <http://127.0.0.1:8000/> and the admin site
at <http://127.0.0.1:8000/controlme>.

## Stack and version numbers used:

| Name           | Version |
|----------------|---------|
| Django         | 4.0.6   |
| Python         | 3.10    |


## Folder structure
```
.
├── accounts                # accounts app (extends from django user system)
│   ├── forms               # application forms are here
│   ├── models              # models for the application are here
│   ├── templates           
│   │   ├── accounts        # templates for the application are here
│   ├── views               # views of the application are here
├── config                  # main project files needed for configuration
├── mainsite                # The main app of the project is here. (For general-purpose models, like index page)
│   ├── forms               # application forms are here
│   ├── models              # models for the application are here
│   ├── templates           
│   │   ├── mainsite        # templates for the application are here
│   ├── views               # views of the application are here
├── templates               # base templates are here
├── .env-example            # environments file
├── .gitignore              # determines files excluded from github
├── LICENSE.txt             # license file
├── manage.py
├── README.md               # this file
└── requirement.txt         # project environment requirements
```

## Screenshots
Dashboard
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-1.jpg" width="100%"/>

Login
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-2.jpg" width="100%"/>

Password Reset: _with confirmation email_
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-4.jpg" width="100%"/>

Employee Signup: _registration via unique email_
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-3.jpg" width="100%"/>

Employee Profile Detail: 
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-10.jpg" width="100%"/>

Employee Company List Page: _all employees can only see their own companies_
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-5.jpg" width="100%"/>

Add a Company
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-9.jpg" width="100%"/>

It is possible to delete the company before the company approves.
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-7.jpg" width="100%"/>

Edit Company: _if checkbox "Is Accepted" will be selected, an email with registration link will be send to company.
email sending is automated via django signals._
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-8.jpg" width="100%"/>

Example Email In Consol
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-14.jpg" width="100%"/>

After sending an email, "Is Email Sent" in the company status will change to green.
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-13.jpg" width="100%"/>

The customer registration system will make the necessary changes through signals.
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-15.jpg" width="100%"/>

All statuses turn green after the company is registered.
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-6.jpg" width="100%"/>

Customer Profile Details
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-11.jpg" width="100%"/>

Customer Profile Update
<img height="100%" src="https://alikasimoglu.com/static/mmp/mmp-12.jpg" width="100%"/>

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.

If you need a project or developer, please feel free to contact me:)