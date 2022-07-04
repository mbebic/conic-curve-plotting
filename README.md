# conic-curve-plotting
A proof-of-concept app demonstrating the following workflow 

1) user-input collection using heavily formatted forms
1) javascript-based form validation and transfer to a corresponding django form (held in a hidden div)
1) submittal to django database using javascript
1) protecting of django urls using authentication and authorization
1) implementation of back-end calculations and access to those from django views
1) access to back-end calculationns from javascript using ```fetch requests``` that exchange json objects
1) permission based access to back-end calculations and error handling in the calling javascript
1) plotting server-calculated curves using Plotly javascript library

# Usage
After cloning the repo run: 
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

The proof-of-concept ui works as follows.

1) Anyone can define new curves. 
1) Only the members of ```calcconic-subscribers``` can see the library of curves.
1) Only these same members can call the back-end calculations.
To demonstrate the permission-based access to back-end calculations, change the code in ```curveapp\views.py``` to allow anyone to access the library page.
Then, when a non-member attempts to plot, a 403 status is returned and reported in the console.
1) Usage of permission checking within html code is illustrated within the ```library.html``` template.

# Misc

To dumpdata when non-model-based permission are used, exclude the non-managed model from the dump using:
```
python manage.py dumpdata --exclude calcconic.calcrights --indent 2 > data.json
```

# ToDo
- [ ] Change the design to require login to add curves.
- [ ] Add a welcome page to land unregistered users
- [ ] Clean up the navigation menu
