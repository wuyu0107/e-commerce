1; Example how you implemented above step-by-step
First of all, I created a directory and enabled the virtual environment. Then created a Django project. After creating, on the settings.py file of the Django project, I added the PWS deployment URL to the ALLOWED_HOSTS field. Then I ran a command to create a new application with the name main. In settings.py file inside the project directory, I added 'main' to the INSTALLED_APPS so that the application is registered to the project. Next step is build a html file, added a section to put my name and class. Then I modified the models.py file so that it has a model with name Products, and its attributes, name, price, subject, description. After modifying the file, I ran the command to create model migrations. Next is to connect views with templates. Open the views.py file in main application file, then add the import lines 'from django.shortcuts import render.' The render function is used to render HTML views using the data.
Then create a urls.py file in main directory to manage the URL routing related to the application. Add an URL route in the project's urls.py to connect it to the main view. 

2; Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.

3; Git is used to track changes in source code during development. It also enables multiple developers to work together on non-linear development. 

4; I think Django is used as the starting point because it's very easy to learn and allow us to quickly implement any web in code. 

5; Djangdo model is called an ORM (Object Relational Mapper) as Django web framework includes a default ORM that interacts with data from various relational databses. Django model is a SQL database; used for creating, deleting, updating, or any other actions that relates to databases. The ORM enables users to interact with databses using high-level object-oriented APIs rather than writing SQL queries directly. 
