# pcompProj
1. sudo apt-get install omniorb  	#Corba python package 
2. After cloning project 'cd ../' in console and run 'virtualenv --system-site-packages .'.
3. Run 'source bin/activate'
4. Run 'pip install --upgrade pip'
5. Run 'pip install django'
6. Run 'pip install --upgrade pep8'
7. Run 'pip install pep257'
8. Run 'pip install Sphinx'
9. Run 'pip install djangorestframework'
10. Run 'pip install markdown'       # Markdown support for the browsable API.
11. Run 'pip install django-filter'  # Filtering support
12. Run 'pip install django-rest-swagger' #An API documentation generator for Swagger UI and Django REST Framework
13. Run 'pip install raven --upgrade' # Logging with Sentry
14. Run 'pip install django-redis' #Caching services
15. Run 'pip install marshmallow'


----OMNINAMES----
run omniNames.sh located in base dir


----ISSUES---
1.order.json contains at the body a list of items where one of them is different than the other. For example item1 has
no attribute parentItemId while item2 does. So now we have to delete the extra parentItemId when serializing.
This value defaults to empty

2. No account is present in this order, so we have no way to know its description







