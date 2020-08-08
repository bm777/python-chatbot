from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests, os

from .models import Conversation
from .Query import Query

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


@csrf_exempt
def Post(request):
    if request.method == "POST":
        query = request.POST.get('msgbox') # msgbox
        response = Query().search(query)
        if response == None:
            return JsonResponse({'response': "<strong>Bot -> </strong>" + "None object found or I didn't understood your query, oups :(", 'query': "<strong>Me -> </strong>"+query})
        response = [str(elt)+"<br/>" for elt in response]
        print("query :: ", query)
        print('===========')
        #c = Conversation(query=query, response=response)

        return JsonResponse({'response': "<strong>Bot -> </strong>" + str(response), 'query': "<strong>Me -> </strong>"+query})
    else:
        return HttpResponse('Request must be POST.')
