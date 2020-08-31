from __future__ import absolute_import as _absolute_import
from __future__ import division as _division

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests, os, re

from tensorflow import Session
#import tensorflow_core
from .models import Conversation
from .Query import Query
from chatbot_app.ner import nl
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
            stop_words_search = ['phone', 'iphone', 'samsung', 'telephone', 'xiaomi', 'tecno', 'processor', 'memory', 'camera', 'storage']
            stop_words_meeting = ['meeting', 'appointment', 'rendez-vous', 'rendez vous']

            # =========== generate token of sentences =========================
            tmp = nl(query)

            # =========== test if word in words exist in tmp search ===========
            for w in tmp:

                if w in stop_words_search:
                    response = Query().search(query)
                    response = ['<br/><button class="btn btn-outline-primary>{}</button>'.format(elt) for elt in response]
                    print('=============')
                    return JsonResponse({'response': "<strong>Bot -> </strong>About {}, We have :{} <br />wich one are interested in?".format(w, response) , 'query': "<strong>Me -> </strong>"+query})

            # ============ test if word in words exist in tmp search for meeting======
            for w in tmp:
                if w in stop_words_meeting:
                    #response = Query().search(query)
                    response = ['<br/><button class="btn btn-primary>{}</button>'.format(elt) for elt in ["Monday: 8:00AM - 6:30PM", "Tuesday: 8:00AM - 6:30PM", "Wednesday: 8:00AM - 6:30PM", "Thursday: 8:00AM - 6:30PM", "Friday: 8:00AM - 6:30PM", "Saturady: 9:00AM - 2:30PM"]]
                    print('=============')
                    return JsonResponse({'response': "<strong>Bot -> </strong>About {}, We are opened :{} <br />wich day are interested in?".format(w, response) , 'query': "<strong>Me -> </strong>"+query})
            response = predictor.predict(session_id, query)

            if response == None:
                return JsonResponse({'response': "<strong>Bot -> </strong>" + "I didn't understood your query, oups :(", 'query': "<strong>Me -> </strong>"+query})



            return JsonResponse({'response': "<strong>Bot -> </strong>" + response, 'query': "<strong>Me -> </strong>"+query})
    else:
        return HttpResponse('Request must be POST.')
