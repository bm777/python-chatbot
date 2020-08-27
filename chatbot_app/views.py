from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests, os, re

from tensorflow import Session
import tensorflow_core
from .models import Conversation
from .Query import Query
from chatbot_app.chatbot.botpredictor import BotPredictor
from chatbot_app.settings import PROJECT_ROOT

# Create your views here.

#
# @csrf_exempt
# def Bot(request):
#     if request.method == "POST":
#         query = request.POST.get('msgbox')
#         response = Query().search(query)
#         return JsonResponse({'response': response, "query": query})



#Display recent 3 python questions which are not answered
firstQuestion = "Hi, How may i help you?"



def Home(request):
    return render(request, "app/home.html", {'home': 'active', 'chat': 'chat'})

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

@csrf_exempt
def Post(request):
    if request.method == "POST":
        query = request.POST.get('msgbox') # msgbox
        corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
        knbs_dir = os.path.join(PROJECT_ROOT, 'Data', 'KnowledgeBase')
        res_dir  = os.path.join(PROJECT_ROOT, 'Data', 'Result')

        with Session() as sess:
            predictor = BotPredictor(sess, corpus_dir=corp_dir, knbase_dir=knbs_dir, result_dir=res_dir, result_file='basic')
            session_id = predictor.session_data.add_session()
            tmp = predictor.predict(session_id, query)
            response = tmp
            print("====",type(response))
            #response = Query().search(query)
            if response == None:
                return JsonResponse({'response': "<strong>Bot -> </strong>" + "None object found or I didn't understood your query, oups :(", 'query': "<strong>Me -> </strong>"+query})
            #response = [str(elt)+"<br/>" for elt in response]
            print("query :: ", query)
            print('===========')
            #c = Conversation(query=query, response=response)

            return JsonResponse({'response': "<strong>Bot -> </strong>" + response, 'query': "<strong>Me -> </strong>"+query})
    else:
        return HttpResponse('Request must be POST.')
