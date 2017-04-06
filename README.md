
# Django ChatterBot

## Docker Quick start

1. Install [`docker-compose`](https://docs.docker.com/compose/):
2. Build the project
    docker-compose build
3. Set the admin password
    docker-compose run web python manage.py createsuperuser
4. Run the project
    docker-compose up
5. Visit http://localhost:8000/ to chat, visit http://localhost:8000/admin/ to edit the responses.

## Out of the box Training Data

The following modules are loaded out of the box:

1. english.greetings
2. english.ai

Additional training data can be found from [Chatterbot Corpus](https://github.com/gunthercox/chatterbot-corpus)
