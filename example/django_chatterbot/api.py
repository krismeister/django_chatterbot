from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatterbot = ChatBot(
    'Example ChatterBot',
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
#        "chatterbot.adapters.logic.WeatherLogicAdapter"
    ],
    io_adapter="chatterbot.storage.JsonFileStorageAdapter"
)

# Training with Corpus file example:
# http://chatterbot.readthedocs.io/en/stable/training.html#training-with-corpus-data

# Specify Training File
chatterbot.set_trainer(ChatterBotCorpusTrainer)

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
