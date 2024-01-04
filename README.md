1. Install django
> pip install django

2. Start a project 
> django-admin startproject mysite .
> python -m django startproject mysite .

3. Run server
> python manage.py runserver 

4. Git
> git config --global user.name "Tan Do"
> git config --global user.email tan@ix.com

5. Start a app
5.1 run cmd
> python manage.py startapp home
5.2 declare in Project's settings.py
5.3 routing
- Project's urls.py
- App's urls.py
5.4 views

GitHub:
> https://github.com/letdoitnow/mysite2309

> git clone https://github.com/letdoitnow/mysite2309
> git pull

6. Database
> python manage.py migrate

7. Admin
> python manage.py createsuperuser

8. Model
> python manage.py makemigrations
> python manage.py migrate
