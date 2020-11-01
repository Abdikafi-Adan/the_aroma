# The Aroma 

### [The aroma--------live website](https://thearoama.herokuapp.com/)

It’s a website that is for those that are looking for For the best perfumes brands and want to know more about perfumes 
They are buying the aroma it’s perfumes are your best wingmen and best friends Because we give you the confidence and the mood boosting,perfumes suited for every situation from nights out to a seductive date night or hope you make the best  first impression possible.

# UX

## Project Goals

**Target Audience**
* People who like high quality brands 
* People who love  perfume of all kinds in one place of easy purchase
* People what party 
* people that are looking for new scent to try
* People what are looking for Romantic date perfume 
* People what are looking for socail gathering perfume

**User Goals**
* User finds the good perfumes from high quality brands 
* The find the perfume that suits my situation
* Purchase perfume esay in a safe and secure way 

**Business Goals**
* To make a profit from high quality brand perfume
* To increase the reach of our products by shipping worldwide
* To provide users with the best brands and product collection in the world
## Features

This website is build using Django (a high-level Python Web framework) and Stripe (a payment processing platform) to build an ecommerce website,with many app,models and view build to be fully responsive. 
### Existing Features

### Viewing and Navigation
* As an user , I want to view a list of all  products so that I can select one or more to purchase
* As an user I want to view a individual brand to choose from
* As an user I want to view a individual perfume for more  details so I can make better choose
* As an user, I want to view the total of my cart at any time to see how much I'm going to spend
### navbar
All pages contain a navigation bar to allow for easy access. 
It contains links to the main pages for the site to allow for easy access. 
The contents of the menu changes depending on if a user is logged in or not.
The navigation bar for logged in users features a 'Logout' link where the 'Register' and 'Login' links usually are. 
At top underneath the navbar  there's a calling card that encourages users to buy over $100 to get free shipping worldwide.

### Home app  
The home page is the landing page that contains a bootstrap carousel, 
it features a large images that are responsive and have  a short text that showcaes the benefits of perfume and how it affects you and your surrounding. Below it we have a call to action button in all the images to begin shopping and takes them to the products page.

### Product app 
The Product Page displays  all  product in the database and in shop to get overview of all the collection and the user is able see the product name,
the product image,the product category,the product price and the product rating as a overall view.the user clicks on a product to see more they are redirected to the product info page where the user can see additional infromation such as the product description, the product sku and in the product info page the user has the functions to add product to the cart and selected quantity with a quantity box that allow the user to add any number of the selected product to the cart.

A product can be added to the cart by clicking the button at the bottom of the page "Add to Cart". If the item is successfully added to the cart, the grand total price in the navbar will increaseand a toast message sucess will show the current contents of the cart. 

If the user is admin, there are also 2 buttons displayed in the cards: Edit and Delete. Clicking Edit button redirects admin to the Edit Product page. 
Clicking the Delete button deletes the product.

The page reloads and the toast message will inform about the successful deletion. 
These actions can be done only by superuser, attempts to access them by other users will end up redirected to the homepage with toast error messages displayed.

### cart app 
The shopping cart page has a heading at the top to make the user aware they are on the correct page.
The shopping cart features the product info of the products that are currently in the shopping cart. It has the product name,
the product image,the product category,the product price and the product rating It also shows the price, quantity and sub total of the product.

the same as in the product info page the user can adjust quantity selector to either update the quantity of the product or remove the product completely from there shopping cart.
the free delivery threshold , if the total price is below the free delivery threshold, a small message will appear letting the user know how much money is required for free shipping. At the bottom of the page, if the user selects the checkout button, they will be taken to the checkout page. If they select the other button, they will be directed to the shop page to continue adding more products.

### Checkout app

The Checkout cart page has a heading at the top to make the user aware they are on the correct page.
The checkout page has 3 seperate forms for the user to fill out to the complete the order. The first form is the detals form where the user will enter in there full name and e-mail address. The second form is the delivery form where the user will fill out delivery address.the checkout page contains summary order    that includes  the product image, name, quantity, subtotal and grand total.

If a user already has a profile with the shipping information saved, the form will be filled with the users information and if a required field is not fill the user will be receive a toast message.Once the form is filled and  submitted the payment is successfully proceeded, the Checkout sucesss page is loaded and a confirmation email is sent to the user's email. Also, a toast message appears to ensure the user that the order was processed successfully.A webhook is used to make sure that the order is processed even in the cases when the payment process is interrupted.

### Profile app

Once registered or signed in, the user can update your mobile number and delivery address.
They can also view their order history (Order Number, Date, Items and Order Total)

### superuser Product managment

The product managment feature is available only for superusers. Admin page allows an owner of the website to add new paintings by filling out a form on the Product Management page. If the form is valid, the painting is added to the database and the user is redirected to the newly created paintings details page. The defensive design is implemented to restrict other than admin users to manually enter the url to get access to the page. User will be redirected to the home page with the toast error messages appeared.


### Django-allauth

Django allauth has all the standard features including...

Sign up - requires username, email, password twice and an email will be sent with a verification link
Login - requires either username or email and password with a toast message confirming successfully signed in
Logout - Once completed logout, a toast message confirming successfully logged out
Forgot password - requires email and email will be sent to link to update password



### Features Left to Implement

* A Contact app where user can make requests for new brands and products
* To be able to signup/login through social media acounts like facebook and google for better UX and more signups.


# Technologies

###  Languages, Frameworks, Libraries and other tools used for this project:

* [Gitpod](https://www.gitpod.io/): Used as IDE to write, run, and debug the code used for the web-app.
* [Github](https://github.com/): Used for version control of the code by using Git functions in the control panel.
* [Heroku](https://heroku.com/): Used as deployment platform
* [SQlite3](https://www.sqlite.org/index.html): SQL database engine
* [PostgreSQL](https://www.postgresql.org/): Object-relational database system
* [Django]( https://www.djangoproject.com/): Web framework
* [AWS S3 Bucket](https://aws.amazon.com/s3/): Used to store static and media files in production

---
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): Used as a fundamental basis for building the web-app. Where possible semantic HTML is used to give the user a better understanding.
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS): Used for styling of elements within the website. 
* [JavaScript](https://www.javascript.com/): Provides dynamic interactivity, as it is a full-fledged versatile programming language.
* [Bootstrap](https://getbootstrap.com/): To customise the html and make it responsive to different devices.
* [JQuery](https://www.jquery.com/jquery-3.4.1): Simplifies many complicated tasks from JavaScript, such as AJAX calls and DOM manipulation. 

----
* [Python]( https://www.python.org/): Python3 is used as programming language
* [Allauth](https://fontawesome.com/?from=io): Addressing authentication, registration and account management
* [Stripe](https://stripe.com/docs/payments/checkout): To enable the user to make payments and check credit cards
* [Crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): To easily build the forms and make them user-friendly.
* [Pillow 4.3.0](https://pillow.readthedocs.io/en/stable/handbook/overview.html): Adds image processing capabilities to your Python interpreter. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/): A modern and designer-friendly templating language for Python. It is fast, widely used and secure with the optional sandboxed template execution environment.
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): The Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS services, such as S3.
* [Gunicorn](https://docs.gunicorn.org/en/stable/): A Python WSGI HTTP Server to enable deployment to Heroku
* [Psycopg2]( https://pypi.org/project/psycopg2/): needed to enable the PostgreSQL database to function with Django

## Testing

Validation, manual unit, cross browser/cross device, accessibility, travis, coverage, jasmine, this app has a dash of everything test related.
## Validation Testing
- [CSS Validator](https://jigsaw.w3.org/css-validator/) Note, any error associated with root: color variables were ignored. 
- [HTML Validator](https://validator.w3.org/)  - validation of HTML with Django is pretty useless as all {{}} bracketed values raise errors. I ran only a few files through the validator and instead relied heavily upon pycharm's IDE to identify mismatched tags and closing Django directives.
- [JavaScript Validator](http://beautifytools.com/javascript-validator.php) Note any errors for let, variables set in other .js files, and constants were ignored. I also used a more [ES6 friendly checker](https://www.piliapp.com/syntax-check/es6/) and there were no errors.

### Responsive and Functional Testing

I used Google Chrome's Development tools to constantly test each change that I made to my project and to ensure that it appeared in the desired way on different screen sizes. I also tested my app on different screen sizes (mobile, tablet and desktop) to ensure it appeared in the desired way on different devices.

I created my own account and some fake user accounts to test the functionality and validation worked as expected.
The spreadsheet also documents any responsive features and confirms that they work and appear as intended on different screen sizes. In addition to my own testing, I also asked family members, friends to test my app and provide any feedback.


#### If you would like to test the payment functionality of this project, please use the following payment details:
* Card number: 4242 4242 4242 4242 
* CVC: any 3 digit number
* Exparation Date: any future date
* Address: any address details

#### To test the site as a superuser, you can use the following credentials to login:
* Username: testuser
* Password: test12345

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.


## Deployment

## Setting up Heroku
I went to [Heroku](https://www.heroku.com/) to set up an my app  'thearoama'

### Heroku Postgres
- On Gitpod console install dj-database-url: ` pip3 install dj-database-url`. This package allows connection to a database URL.
- Then install psycopg2  `pip3 install psycopg2` which allows connection to the postgres database.
- Create a requirements.txt file  ```pip3 freeze > requirements.txt```
**import dj_database_url** at top of settings.py file and change default sqlite3 database to be default dj_database_url
```DATABASES = { 'default' :dj_database_url.parse(os.environ.get('DATABASE_URL')) }```
Add DATABASE_URL config vars code to env.py 
Make migrations to migrate all files to new database.
```
python3 manage.py makemigrations
python3 manage.py migrate

```
Create new superuser via ```python3 manage.py createsuperuser``` and add username, email and password.
This will be production database for deploying on Heroku
Ensure Heroku has all Config Vars required = SECRET_KEY, STRIPE_SECRET, STRIPE_PUBLISHABLE, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
add DISABLE_COLLECTSTATIC and set to 1 this will disable staticfiles from being added to Heroku meaning can use AWS bucket.
To allow deployment via github automatic/manual select Deploy> GitHub> connect to repo = 'ecommerce' in Heroku menu. For automatic deployment select button 'enable automatic deploys'.
Otherwise use manual deployment to 'deploy branch'.
## Committing files to GitHub
When I make changes to each file I push them from GitHub from GitPod and below are the steps I do to do this. This is essential as to not losing any of the work I have done.
1.	On my GitPod project scroll down and click on the command prompt at the bottom.
2. Check status by typing in ‘git status’.
3.	Type ‘git add’ to add the files for staging.
4.	Type ‘git commit -m "Add all files" to commit the files.
5.	Type ‘git push’ to push the files to GitHub.


## Credits

### Content
- Find most on the description text att  [Gertrude.co](https://gertrude.co/) .I strongly recommend you visit the website it is a great website great information.

### Media
found all my image in google,I have all the image urls in my fixtures for more information.

### Acknowledgements

the code are inspired by the Boutique Ado mini project from Code Institute gerat project. 

> NOTE: This project was created for educational purposes only as 'The Aroma' is a fictional business and is only used to learn and understanding Django application.
