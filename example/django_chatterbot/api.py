from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot


chatterbot = ChatBot(
    'Example ChatterBot',
    io_adapter="chatterbot.adapters.io.JsonAdapter"
)

# Train based on the english corpus
chatterbot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
chatterbot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
chatterbot.train("chatterbot.corpus.english.conversations")

# Custom training
chatterbot.train([
    "Hi",
    "Hello",
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])


class ChatterBotView(View):

    def get(self, request, *args, **kwargs):
        data = {
            'detail': 'You should make a POST request to this endpoint.'
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)

    def post(self, request, *args, **kwargs):
        input_statement = request.POST.get('text')

        response_data = {
            'text': chatterbot.get_response(input_statement)
        }

        return JsonResponse(response_data)
