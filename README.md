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


## License
Distributed under the MIT License. See `LICENSE.txt` for more information.

If you need a project or developer, please feel free to contact me:)