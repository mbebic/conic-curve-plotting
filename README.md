# Conic Curve Plotting Application

## Overview
As someone with an engineering background, I was inclined to make an application that had functionality in a math classroom.
I wanted to demonstrate the knowledge of using the numpy library extensively and implement it in the converting from standard to general canonical form for ellipses and circles.
Furthermore, I wanted to allow a user to see all the entries they have made and select which conics they would like to view and refresh the plot without refreshing the page entirely. 

To summarize, the app demonstrates the following workflow:

1) User-input collection using heavily formatted forms
1) Javascript-based form validation and transfer to a corresponding django form (held in a hidden div)
1) Submittal to django database using Javascript
1) Protecting of django urls using authentication and authorization
1) Implementation of back-end calculations and access to those from django views
1) Access to back-end calculations from Javascript using ```fetch requests``` that exchange json objects
1) Permission based access to back-end calculations and error handling in the calling Javascript
1) Plotting server-calculated curves using Plotly Javascript library
1) The creation of a login page but not a register page.
This was to simulate a class environment where a professor would assign students with their own accounts with different levels of access than the professor themselves or a TA would be privy to.
This was to further simulate the idea that students not registered within the class are not able to access the plotting application unless they are a student of the class.

## Distinctiveness and Complexity
Adhering to the CS50 guidelines, my project must obey the following guidelines:
```Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those.```
My project meets this requirement for the following reasons:

1) My project is based on an original idea, and creates a unique and interactive web platform for young students to engage in linear algebra concepts.
1) The project has no similarity to any of the other projects assigned during this course.
1) The project has three user types: admin, userpaid, and userfree, all with various levels of access. 
1) The application uses Plotly functionality to show all conics that are chosen to be plotted
1) The use of Bootstrap tables with click/unclick functionality to add/remove plots on the page without reloading the page entirely
1) The use of a backend XMLHttpRequest to retrieve x and y points to plot the user-selected conic(s)

```Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.```
My application was built with Django, with one model on the backend and uses two Javascript scripts to make XMLHttpRequests and other dynamic updates on the front-end of the application.
All information is saved in SQLite by default.

```Your web application must be mobile-responsive.```
With the use of Bootstrap and CSS, the styling of all pages and features of this web application is mobile-responsive.

## Models 
There is one model for the Conic Curve Plotter database:
conicselection - this model gets populated upon submittal from user inputted values.
Once the user submits their values for the standard form of their conic, the values are converted to general form in ```coniccurve.js```.
The general values then populate the form based on the conicselection model.
This form then gets saved and the values are stored in the model.

## Routes
 
### Welcome '/'
Page that welcomes the user to the app, and provides the options to do one of the following: Define your curve, view the curve library, login, or register.

### Define '/define'
The page that allows the user to select from a dropdown which curve they want to input - either a circle or ellipse - and then allows the input of the center of the conic, radius, and rotation (ellipse only).

### Library '/library'
Page that allows the user to see all their conic inputs in their standard form values, select which ones they would like to plot and refresh the Plotly-supported plot to view their selected conics.
They are also able to set their grid size.

### Login '/login'
Users can log into the website using their valid username and password.

### Logout '/logout'
If user clicks logout, it will logout the user and redirect them to the index, or Define Your Curve, page.

### Error '/error'
A page that pops up whenever an error occurs. For example, if a user tries to access the curve library, but does not have the authorization permission to do so.

## Files and Directories
Summary of files:
- `calcconic` App that contains all calculations for conic points to be plotted and redirection from XMLHttpRequest
	- `__init__.py` Created by Django
	- `admin.py` Created by Django
	- `apps.py` Created by Django
	- `models.py` Holds the permission can_calc_conics
	- `plotting.py` Handles the conversion of the general conic form and creates points to plot
	- `tests.py` Created by Django
	-`urls.py` defines XMLHttpRequest url path
	- `views.py` contains view of XMLHttpRequest
- `curveapp` - main app directory
	- `static/curveapp` contains all static content (CSS files, Javascript files, etc.)
		- `bootstrap.min.css` is the standard CSS script for bootstrap functionality.
		- `bootstrap.min.js` is the standard JS script for bootstrap functionality.
		- `circle.jpg` is the image used in the upper left corner of the web application as an `emoji` of sorts.
		- `coniccurve.js` sees what conic was selected (circle or ellipse), validates the form, removes and adds validation css, populates the django form and submits it
		- `Navbar-Right-Links.css` is the standard CSS script for navbar functionality in Bootstrap
		- `plotconics.js` makes the XMLHttpRequest, plots the selected conics, sets up the grid and relayouts it if user inputs grid limits
		- `styles.css` is the standard CSS script. Only an asteriskField is set to display:none, no other functionality.
	- `templates/curveapp` contains all the html templates for the application
		- `error.html` template for error page
		- `index.html` template for define your curve page
		- `layout.html` template for layout of page
		- `library.html` template for library page
		- `login.html` template for login page
		- `welcome.html` template for welcome page
	- `__init__.py` Created by Django
	- `admin.py` Registers models to the Django admin interface
	- `apps.py` Created by Django
	- `forms.py` defines models as forms to be used in application ('conicForm')
	- `models.py` defines models used to add and update Django database
	- `tests.py` created by Django
	- `urls.py` defines all the web applications url paths
	- `views.py` contains all the views of the html pages within the web application
- `curveproj` main project directory
	- `__init__.py` Created by Django
	- `asgi.py` Created by Django
	- `settings.py` Created by Django, specify which apps exist in this file
	- `urls.py` contains all project urls
	- `wsgi.py` Created by Django
- `db.sqlite3` database
- `manage.py` created by Django
- `data.json` JSON file that contains all users and their various authorizations, as well as the conic curves already saved in the library
- `requirements.conda` Packages needed for successful application run
- `requirements.txt` Text version of packages need for successful application run
- `.gitignore` Defines files to be ignored by Git
- `README.md` Markdown file with explanation of project

## Running the application, login procedure and levels of access explained
1) Clone the repo to your computer system and redirect your command prompt to the project folder by using the `cd foldername` command.
2) Create the environment for the application to run by inputting the following command:
``` shell
conda create --name ENVNAME --file requirements.conda (or requirements.txt)
```
3) After cloning the repo run the following: 
``` shell
python manage.py loaddata data.json
```

This will build the database with three users and configured permissions to showcase the functionality.

| username | password |
|----------|----------|
| ```useradmin``` | ```test1234``` |
| ```userpaid``` | ```paid1234``` |
| ```userfree``` | ```free1234``` |

The permission to access the back-end calculations is called ```calcconic.can-calc-conics```. 
This permission is defined within the ```calcconic``` app and not attached to any model.
It is assigned to the group called ```calcconic-subscribers```.
It is then applied to ```userpaid``` by having their membership in ```calcconic-subscribers```.

The levels of access are as follows:

- Anyone can define new curves. 
- Only the members of ```calcconic-subscribers``` can see the library of curves.
- Only these same members can call the back-end calculations.
To demonstrate the permission-based access to back-end calculations, you can change the code in ```curveapp\views.py``` to allow anyone to access the library page by removing the ```@user_passes_test(is_calcconic_sub, login_url="error")``` line.
Then, when a non-member attempts to plot, a 403 status is returned and reported in the console.
- Usage of permission checking within html code is illustrated within the ```library.html``` template, starting at line 10.

4) Run the following in your command prompt:
``` shell
python manage.py runserver
```

5) Visit the website in your browser. Use any of the following usernames and passwords above and enjoy!
