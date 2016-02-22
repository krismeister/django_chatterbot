=================
Django ChatterBot
=================

This is a Django project that makes it possible to create a simple chat bot web
app using
[Django](https://www.djangoproject.com),
[Django REST framework](http://www.django-rest-framework.org) and
[ChatterBot](https://github.com/gunthercox/ChatterBot).

Quick start
-----------

1. Add "django_chatterbot" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django_chatterbot',
    )

2. Include the django_chatterbot URLconf in your project urls.py like this::

    url(r'^chatterbot/', include('django_chatterbot.urls')),

3. Run `python manage.py migrate` to create the chatterbot models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. POST to http://127.0.0.1:8000/chatterbot/ to start a conversation.

Docker Quick start
------------------

1. If you have [`docker-compose`](https://docs.docker.com/compose/) installed:

    docker-compose up

2. Otherwise, build the docker image:

    docker build -t django_chatterbot .

3. Then run the container:

    docker run -it -p 8000:8000 django_chatterbot

4. Open the web app in a browser (assuming you have `docker-machine`):

    open http://$(docker-machine ip default):8000
