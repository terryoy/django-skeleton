# django-skeleton
A skeleton for me to develop and deploy django application. (There are so f**king many times for me to start a prototype project with django!)

It setups the skeleton of a server app for prototyping. With the power of django, it's easy to extend to any type of server application just by adding your django app plugins.


## How to use?

### 1. Download the package and unpack

```bash

$ wget https://github.com/terryoy/django-skeleton/archive/master.zip -O django-skeleton.zip
$ unzip django-skeleton.zip
$ mv django-skeleton-master <your_app_name>

```

### 2. Installing Django

```

$ cd <your_app_name>/app
$ mkvirtualenv <your_app_name>
$ pip install -r requirements.txt

# (note) for installing Pillow, you need to install the image libraries first
$ sudo apt-get install libjpeg8 libjpeg8-dev libfreetype6 libfreetype6-dev zlib1g-dev

# initialize sqlite3 database (using sqlite3 is only for prototypes, not for production)
$ python manage.py syncdb

```

### 3. Start Web Server

There are two ways of running the server, one is for local development, another is for hosting on server(with gunicorn and nginx)

Local Development:

```bash

# test dev server 
$ python manage runserver

```

Simple hosting with nginx and gunicorn:

```bash

# Update any settings you want at "app/local_settings.py", "start_server.sh", "../nginx/django-skeleton.conf",
# (Separating "app/settings.py" and "app/local_settings.py" is for the separation of local development and public preview.)
$ sudo cp ../nginx/django-skeleton.conf /etc/nginx/site-enabled/<your_app_name>.conf
$ sudo service nginx reload

# execute the start server script
$ ./start_server.sh

```

## What to do next?

1. Install your third party dependencies
2. Start to write you own app with the powerful django framework


## About

Project Page: https://github.com/terryoy/django-skeleton
