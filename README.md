Website: http://min-kim-ecommerce.pbp.cs.ui.ac.id

# Week 1

1; My application is about sharing notes of many subjects in all grades by selling them online. First of all, I created a directory and enabled the virtual environment. Then created a Django project. After creating, on the settings.py file of the Django project, I added the PWS deployment URL to the ALLOWED_HOSTS field. Then I ran a command to create a new application with the name main. In settings.py file inside the project directory, I added 'main' to the INSTALLED_APPS so that the application is registered to the project. Next step is build a html file, added a section to put my name and class. Then I modified the models.py file so that it has a model with name Products, and its attributes, name, price, subject, description. After modifying the file, I ran the command to create model migrations. Next is to connect views with templates. Open the views.py file in main application file, then add the import lines 'from django.shortcuts import render.' The render function is used to render HTML views using the data.
Then create a urls.py file in main directory to manage the URL routing related to the application. Add an URL route in the project's urls.py to connect it to the main view. 

2; 


<img width="256" alt="Screenshot 2024-09-11 at 12 51 18 AM" src="https://github.com/user-attachments/assets/3ca7f5ff-bf49-434e-9cdb-bd0af15d9a7c">

The urls.py, maps the URL request to appropriate view function. It acts like a router, directing the request based on the URL pattern. The views.py(View Layer) processes the request. It handles the data, and prepare the data to be rendered. The models.py is interacted with the view. Models.py represents the data structure and handles database queries. Once the view has necessary data, it renders the html template. It presents the data to the client using Django's tmeplating engine using the html file.

3; Git is used to track changes in source code during development. It also enables multiple developers to work together on non-linear development. 

4; I think Django is used as the starting point because it's very easy to learn and allow us to quickly implement any web in code. 

5; Djangdo model is called an ORM (Object Relational Mapper) as Django web framework includes a default ORM that interacts with data from various relational databses. Django model is a SQL database; used for creating, deleting, updating, or any other actions that relates to databases. The ORM enables users to interact with databses using high-level object-oriented APIs rather than writing SQL queries directly. 


# Week 2

Data delivery is important in implementing a platform because it ensures an efficient and secure transfer of data between the service and the users. Fast data delivery allows companies to monitor and optimize their operations in real-time. If something goes wrong, they can take immediate actions to correct it. It also supports both the platform's functionality and user experience.
***
I personally think JSON is better because JSON gives easier view on the code. JSON is more popular because it is more compact and easier to read and write. It can be easily loaded in JavaScript, and it allows a simple documentation and is more flexible. Additionally, because of its simpler structure, JSON has a smaller file size and allows faster data transmission.
***
Functional usage of is_valid is to check if the submitted form data meets all the validation criteria defined for each field in the form. If the form data is invalid, it displays an error message. It is required because it ensures that data stored are in valid form. This is important because if there is invalid data in the database, it can lead to vulnerabilities in the database.
***
CSFR_token is needed when creating a form in Django because it provides protection against Cross-Site Request Forgery (CSRF) attaks. It is a type of attack in which malicious user tricks another user's browser into making unwanted requests to web application where user is authenticated.

When user submits a form, Django will check the token to ensure the request is coming from the correct source. Without it, a third-party website could create and send request to the application. Django also uses the token to make sure that the user submitting the form is the same user who loaded the page. 
***
In this assignment, the main thing was to implement a form input data and display the entries on HTML.

I created a new file to create the structure of the form that can receive new data entry for notes. Then, I edited the views.py in the main directory. I imported the required imports and the model being used in the application. I wrote a new function so that it produces a form that can be added to data entry for notes automatically when data is submitted from the form. Then in the show_main function, Product.objects.all() is added to retrieve all objects in Product objects stored in the database. 

Next is to return data in xml and json format. In the views.py file in main directory, I imported the HttpResponse and Serializer. Then created a new function that receives parameter request, with the name show_xml and show_json. A variable with name data is created inside the functions to store the result of the query of all data in entry. Then add a return function as an HttpResponse that contains a serialised data result and content_type, one in xml and another in JSON. Finally, in the urls.py file, import the function I created just now, then add URL path to urlpatterns variable to access the functions. 

To return data based on an ID in XML and JSON format, first thing to do is initialize a new model field in the application model named id. Run makemigrations and migrate to save changes in model. Similar to returning data in xml and json format, create a two functions with name show_xml_by_id and show_json_by_id. These functions take in parameter request and id. Inside these functions create a variable that stores the result of data with the specific ID that exists in the entry. Then add a return function as an HttpResponse that contains the serialised data result as JSON and XML (separate for each function) and content_type with value 'application/xml' for XML and 'application/json' for JSON. After this step, I opened the urls.py file and imported the functions created, and added URL path to urlpatterns in urls.py file to finish the assignment. 
***
XML
<img width="1392" alt="Screenshot 2024-09-16 at 11 41 20 PM" src="https://github.com/user-attachments/assets/a6f4c2d3-ebdc-4b11-8487-dc1a0fb4013e">

JSON
<img width="1392" alt="Screenshot 2024-09-16 at 11 41 33 PM" src="https://github.com/user-attachments/assets/7ff18fff-d7c4-4a98-9808-b2cef5f8400b">

JSON by ID
<img width="1392" alt="Screenshot 2024-09-16 at 11 41 57 PM" src="https://github.com/user-attachments/assets/d4fadfb6-a5e5-43e4-bb72-16b5e130d84e">

XML by ID
<img width="1392" alt="Screenshot 2024-09-16 at 11 42 03 PM" src="https://github.com/user-attachments/assets/99576f95-26d4-4ad3-b4e4-c827b38df01a">
