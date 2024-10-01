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


</details>

