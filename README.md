Website: http://min-kim-ecommerce.pbp.cs.ui.ac.id

<details>
<summary>Assignment 2</summary>

1; My application is about sharing notes of many subjects in all grades by selling them online. First of all, I created a directory and enabled the virtual environment. Then created a Django project. After creating, on the settings.py file of the Django project, I added the PWS deployment URL to the ALLOWED_HOSTS field. Then I ran a command to create a new application with the name main. In settings.py file inside the project directory, I added 'main' to the INSTALLED_APPS so that the application is registered to the project. Next step is build a html file, added a section to put my name and class. Then I modified the models.py file so that it has a model with name Products, and its attributes, name, price, subject, description. After modifying the file, I ran the command to create model migrations. Next is to connect views with templates. Open the views.py file in main application file, then add the import lines 'from django.shortcuts import render.' The render function is used to render HTML views using the data.
Then create a urls.py file in main directory to manage the URL routing related to the application. Add an URL route in the project's urls.py to connect it to the main view. 

2; 


<img width="256" alt="Screenshot 2024-09-11 at 12 51 18 AM" src="https://github.com/user-attachments/assets/3ca7f5ff-bf49-434e-9cdb-bd0af15d9a7c">

The urls.py, maps the URL request to appropriate view function. It acts like a router, directing the request based on the URL pattern. The views.py(View Layer) processes the request. It handles the data, and prepare the data to be rendered. The models.py is interacted with the view. Models.py represents the data structure and handles database queries. Once the view has necessary data, it renders the html template. It presents the data to the client using Django's tmeplating engine using the html file.

3; Git is used to track changes in source code during development. It also enables multiple developers to work together on non-linear development. 

4; I think Django is used as the starting point because it's very easy to learn and allow us to quickly implement any web in code. 

5; Djangdo model is called an ORM (Object Relational Mapper) as Django web framework includes a default ORM that interacts with data from various relational databses. Django model is a SQL database; used for creating, deleting, updating, or any other actions that relates to databases. The ORM enables users to interact with databses using high-level object-oriented APIs rather than writing SQL queries directly. 
</details>

<details>
<summary>Assignment 3</summary>

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
</details>

<details>
<summary>Assignment 4</summary>
  
#### What is the difference between HttpResponseRedirect() and redirect()?
For HttpResponseRedirect, the first argument can only be a url, however for redirect, it retuns a HttpResponseRedirect that can accept model, view, or url as it's 'to' argument. 

#### Explain how the MoodEntry model is linked with User!
MoodEntry model is linked with the User model using the foreign key. This creates a one-to-many relationship where each mood entry belongs to single user, but each user can have many entries. 
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
This line of code connects MoodEntry to a User. ```ForeignKey(User)``` creates a relationship between the models. ```on_delete=models.CASCADE``` ensures that if an user is deleted, all their associated MoodEntry objects are also deleted. 

#### What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.
Authentication verifies the identity of a user or a service to ensure they're who they claim to be. It involves checking credentials, such as usernames, biometric information, and passwords. Authorization determines the access rights to a user or a system. It determines what an authenticated user is allowed to do. 

Authentication is implemented by initiating Django's ```form = AuthenticationForm(data=request.POST)```. The system validates credentials and if the form is valid (user's credentials are correct), ```get_user()``` method will retrieve the User object for the authenticated user. Authorization is implemented by the decorator ```@login_required(login_url='/login')```. It will allow the only authenticated users to access the view. If the user is not authenticated, the user will be redirected to the login page.

#### How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.
Django remembers logged_in users using sessions and cookies. When a user logs in, Django creates a session and assigns a session ID which is stored in the browser cookie. When user makes a request, session ID cookie is sent back to the server, allowing Django to identify the user without the need to log in again. 

Other uses of cookies include remembering user preferences, tracking user as he/she navigate the website, and to enable the use of e-commerce facilities. 

Not all cookies are safe. Cookies can be stolen or copied from the user, which could either reveal information in the cookies or allow the attacker to edit the contents of the cookies and impersonate the user. 

#### Explain how did you implement the checklist step-by-step
1. #### Implement registration forms
   First thing to do is importing UserCreationForm which simplifies creating registration forms in the web app. Add ```register``` function to views.py to generate the registration form and create a user account when the form data is submitted.
```def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
  Then, I created a new HTML file named ```register.html``` and add the URL to urlpatterns to access the imported function. 
```
{% extends 'base.html' %} {% block meta %}
<title>Register</title>
{% endblock meta %} {% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Register" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
```
urlpatterns = [
     ...
     path('register/', register, name='register'),
 ]
```

2. #### Implement login function
  Import authenticate, login and AuthenticationForm, HttpResponseRedirect, reverse, and datetime in views.py. Then add a ```login_user``` function to authenticate users trying to log in. In the login_user, a cookie, named last_login is set to track when the user is last logged in. Modify the show_main function and add the snippet ```'last_login': request.COOKIES['last_login']```. 
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
```
...
context = {
        'name' : request.user.username,
        'class': 'KKI',
        'notes_entries' : notes_entries,
        'last_login' : request.COOKIES['last_login'],
    }
...
```
  Create a new HTML file named ```login.html``` and fill it with the following code:
```{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
  Then import the function in urls.py, and add the URL path to ```urlpatterns` to access the function. 
```urlpatterns = [
   ...
   path('login/', login_user, name='login'),
]
```

3. #### Implement Logout Function
  First, import logout in views.py and add a logout_user function to implement the logout mechanism. ```response.delete_cookie('last_login')``` deletes the last_login cookie when user logs out. 
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
  Open main.html file and add this code after the hyperlink tag for "Add New Note Entry." Then in urls.py, import the logout_user function and add the URL path to urlpatterns.
```<a href="{% url 'main:logout' %}">
    <button>Logout</button>
</a>
<h5>Last login session: {{ last_login }}</h5>
```
```urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
]
```

4. #### Restrict Access to Main Page
   In views.py, import login_required import and add the code snippet above the show_main function, so that the main page can be accessed only by the authenticated users.
```
@login_required(login_url='/login')
```

5. #### Connect Product model to User model
In models.py, import the model User. Then add in Product model:
```class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```
This will connect the models through a relationship so that each Product has associatiation with the user. Then reopen views.py and modify the code in create_note_entry function:
```
def create_note_entry(request):
    form = NotesEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        note_entry = form.save(commit=False)
        note_entry.user = request.user
        note_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_note_entry.html", context)
```
Then change the value of note_entries in show_main function so that it displays Product objects associated with the logged-in user.
```
def show_main(request):
    notes_entries = Product.objects.filter(user=request.user)
...
```

</details>

<details>
<summary>Assignment 5</summary>

####  If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!
Priority in CSS selection goes in the order: inline styles, IDs, classes/pseudo-classes/attribute selectors, then elements and pseudo-elements. The priority matters when an element has more than one CSS rules that apply to the element. The selector with the highest priority will override the rules that are below its' priority level. Inline style has the highest priority because it is directly written on the element. 

#### Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!
Responsive web design is essential firstly because it minimizes the amount of data and code that needs to be loaded, by loading only the necessary resources needed. It also lowers the maintenance since only one website will be used, as that website will adapt and customize its layout accordingly to the device. Additionally, it makes the website user-friendly and may also increase the website's ranking in the search engine as responsive web design can increase website dwell time. Applications that have implemented responsive design include social media platforms (Facebook, Instagram, LinkedIn), email clients(Gmail), video streaming website (Netflix, Youtube), and many more. Applications that have not implemented responsive designs are more of older software applications, and specialized tools like CAD software and video editing softwares. 

#### Explain the differences between margin, border, and padding, and how to implement these three things!
Margin is the space outside of element's border, while padding is a space inside the element's border. Border wraps around the padding and content of the element.
Margin controls the outside space of an element, padding controls the inside spce of the element and border forms a line around the element. Below are implementations of margin, border, and padding.

1. Margin
```p {
  margin-top: 100px;
  margin-bottom: 100px;
  margin-right: 100px;
  margin-left: 100px;
  }
```
```
p {
  margin: 100px 100px 100px 100px;
}
```

2. Border (multiple styles of borders)
```
p.dotted {border-style: dotted;}
p.dashed {border-style: dashed;}
p.solid {border-style: solid;}
p.double {border-style: double;}
p.groove {border-style: groove;}
p.ridge {border-style: ridge;}
p.inset {border-style: inset;}
p.outset {border-style: outset;}
p.none {border-style: none;}
p.hidden {border-style: hidden;}
p.mix {border-style: dotted dashed solid double;}
```

3. Padding
```
div {
  padding-top: 50px;
  padding-right: 30px;
  padding-bottom: 50px;
  padding-left: 80px;
}
```
```
div {
  padding: 50px 30px 50px 80px;
}
```

#### Explain the concepts of flex box and grid layout along with their uses!
Flexbox allows developers to create a flexible grid layout, by allocating and aligning space among items. Flexbox is used one-dimensional layout. It is used arrange rows or columns with equal spacing and create flexible navigation bars. On the other hand, grid layout is used for two-dimensional layout with rows and columns. Grid enables developers to develop complex and responsive strategies that are easy to maintain and manage. Grid can be used to create navigation menus with different levels and design a card-based layout with precise control over item placement. 

#### Explain how you implemented the checklist above step-by-step
1. #### Implement "Edit Entry" feature
To add an 'edit entry' feature, create a new function ```edit_entry``` that takes parameters request and id in ```views.py```. Then fill the following function with this code.
```
def edit_entry(request, id):
    note = Product.objects.get(pk = id)

    form = NotesEntryForm(request.POST or None, instance = note)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_entry.html", context)
```
Then import the ```edit_entry``` function in ```urls.py```. Next, create a new html page named ```edit_entry.html``` to ```main/templates``` to make a page just for editing the entry. 
```
{% extends 'base.html' %}
{% load static %}
{% block content %}
{% include 'navbar.html' %}

<h1>Edit Entry</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <button type="submit" class="mt-4 bg-teal-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
                    Edit Note Entry
                </button>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Add a URL path to ```urlpatterns``` to access the function
```
...
path('edit-entry/<uuid:id>', edit_entry, name='edit_entry'),
...
```
In ```main.html```, add the code snippet so that the main page will display the edit button on each data.
```
<tr>
    ...
    <td>
        <a href="{% url 'main:edit_entry' note_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
</tr>
```

2. #### Implement "Delete Entry" feature
To implement a 'delete entry' feature, create a new function named ```delete_entry``` that takes in parameters request and id. Then fill the function with this code:
```
def delete_entry(request, id):
    note = Product.objects.get(pk = id)
    note.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
Import the function created in ```urls.py``` and add a URL path to ```urlspattern``` to access the function.
```
path('delete/<uuid:id>', delete_entry, name='delete_entry'),
```
Make changes in ```main.html``` to display the delete button for each product. Place the code below the code for 'edit' button.
```
<td>
        <a href="{% url 'main:delete_entry' note_entry.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
```

3. #### Implement a navigation bar
Create a new HTML file named ```navbar.html``` inside the ```templates/``` folder in the root directory. Then fill it out with the code to get the desired result. My file looks like this:
```
<nav style="background-color: rgb(35, 144, 144);", class="shadow-lg fixed top-0 left-0 z-40 w-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <h1 class="text-2xl font-bold font-serif text-center text-white">Study Together with Notes</h1>
        </div>
        <div class="hidden md:flex items-center">
          {% if user.is_authenticated %}
            <span class="font-mono text-white mr-4">{{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Register
            </a>
          {% endif %}
        </div>
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button">
            <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
    <!-- Mobile menu -->
    <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
      <div class="pt-2 pb-3 space-y-1 mx-auto">
        {% if user.is_authenticated %}
          <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
    </div>
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
    
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>
```
Don't forget to link the navbar to ```main.html```, ```create_note_entry.html```, and ```edit_entry.html``` by using the include tag after ```{% block content %}```
```
{% include 'navbar.html' %}
```

4. #### Configuring Static File and Styling Website
Modify ```settings.py``` so that MIDDLEWARE includes WhiteNoise middleware and configure the STATIC variables so that it looks like this:
```
...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
...
```
```
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static'
```

To add styles to the application, first create a new directory ```/static/css``` in the root directory. Then create a ```global.css``` and link  ```global.css``` and Tailwind script to ```base.html```.
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    {% block meta %}
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>{% block title %}Study Together With Notes{% endblock title %}</title>
    {% endblock meta %}
  </head>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  <body>
    {% block content %} 
    {% endblock content %}
  </body>
</html>
```
After this, modify and css rules to the HTML files in the application file so that it gives the desired website view. 

<details>
<summary>Styled HTML files</summary>
1. card_entry.html
  
```
<div class="relative break-inside-avoid">
   
    <!-- Note Entry Card -->
    <div style="background-color: rgb(174, 217, 217);", class="relative top-5 shadow-md mb-6 border-2 border-teal-600 transform rotate-0 hover:rotate-1 transition-transform duration-300">
  
      <!-- Card Header -->
      <div style="background-color: rgb(174, 217, 217);color: rgb(45, 45, 45);", class="p-4 border-b-2 border-teal-600">
        <div class="flex items-center justify-center mb-4">
          <i style="color:rgb(43, 30, 30)", class="fa fa-circle"></i>
        </div>
        <h3 class="font-bold text-center text-lg mb-2">{{ note_entry.subject }}</h3>
      </div>
  
      <!-- Card Body -->
      <div style="background-color: rgb(231, 244, 244);", class="p-4">
        <p class="font-semibold text-lg mb-2"></p>
        <p class="text-gray-600">{{ note_entry.description }}</p>

  
        <!-- Edit and Delete Icons (Aligned Flexbox) -->
        <div class="flex justify-end space-x-1 mt-4">
          <a href="{% url 'main:edit_entry' note_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
              <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
            </svg>
          </a>
          <a href="{% url 'main:delete_entry' note_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
          </a>
        </div>
      </div>
    </div>
  </div>
```

2. card_info.html
```
<div style="background-color:rgb(76, 157, 157); border-color: rgb(45, 117, 117);", class="rounded-xl overflow-hidden border-2">
    <div class="p-4 animate-shine">
      <h5 class="text-lg font-semibold underline font-serif text-white">User Information</h5>
      <p class="text-white">Name: {{ name }}</p>
      <p class="text-white">Class: {{ class }}</p>
    </div>
</div>
```

3. create_note_entry.html
```
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Create Entry</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="flex flex-col min-h-screen bg-gray-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Create Note Entry</h1>
  
    <div class="bg-white shadow-md rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
            Create Note Entry
          </button>
        </div>
      </form>
    </div>
  </div>
</div>

{% endblock %}
```

4. edit_entry.html
```
{% extends 'base.html' %}
{% load static %}
{% block content %}
{% include 'navbar.html' %}

<h1>Edit Entry</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <button type="submit" class="mt-4 bg-teal-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
                    Edit Note Entry
                </button>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

5. login.html
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8">
    <div>
      <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
        Login to your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST" action="">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        <div>
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm" placeholder="Username">
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm" placeholder="Password">
        </div>
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Sign in
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-red-400 hover:text-red-600">
          Register Now
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```

6. main.html
```
{% extends 'base.html' %}
{% load static %}
{% block meta %}

<title>Study Together with Notes</title>
{% endblock meta %}
{% block content %}
{% include 'navbar.html' %}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-100 flex flex-col">
  <div class="p-2 mb-6 relative">
    <div class="relative grid grid-cols-1 z-30 md:grid-cols-2 gap-8">
      {% include "card_info.html" with title='Name' value=name %}
    </div>
    <p class="mt-6 border-b-2 border-gray-400"></p>
    <p class="mt-2 border-b-2 border-gray-400"></p>
  <div class="flex justify-end mt-6 mb-6">
        <a href="{% url 'main:create_note_entry' %}" style="background-color: rgb(136, 195, 193);", class="text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105"> 
          <i class="fa fa-plus mr-2"></i> Add New Note Entry
        </a>
    </div>
    
    {% if not notes_entries %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/no-data.png' %}" alt="No Data Entered" class="w-32 h-32 mb-4"/>
        <p class="text-center text-gray-600 mt-4">There is no note entries in this page</p>
    </div>
    {% else %}
    <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
        {% for note_entry in notes_entries %}
            {% include 'card_entry.html' with note_entry=note_entry %}
        {% endfor %}
    </div>
    </div>
    <p class="mt-6 border-b-2 border-gray-400"></p>
    <p class="mt-2 border-b-2 border-gray-400"></p>
    <div class="mt-5 px-3 mb-4">
      <h1 class="text-gray-600 text-left">Last Login: {{last_login}}</h1>
    </div>
    {% endif %}

</div>
{% endblock content %}
```

7. register.html
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-blue-400 hover:text-blue-500">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
</details>
</details>

