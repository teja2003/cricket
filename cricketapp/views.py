from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from pymongo import MongoClient
from datetime import datetime,timedelta
# Create your views here.
client=MongoClient()
db=client['cricket']

@api_view(['GET'])
def get_player_count(request):
    collection=db['players']
    cursor=collection.aggregate([{"$group":{"_id":"$country","count":{"$sum":1}}}])
    data=list(cursor)
    return JsonResponse(data,safe=False)


@api_view(['GET'])
def get_player_name(request):
     collection = db['players']
     cursor = collection.find({"is_keeper":True,"is_captain":True},{"_id":False})
     data=list(cursor)
     return JsonResponse(data,safe=False)

@api_view(['GET'])
def get_player_right(request):
     collection = db['players']
     cursor = collection.find({"batting_hand" : "Right_Hand"},{"_id":False})
     data=list(cursor)
     return JsonResponse(data,safe=False)
@api_view(['GET'])
def get_player_capcon(request):
     collection = db['players']
     cursor = collection.find({"is_captain" : True},{"_id":False})
     data=list(cursor)
     return JsonResponse(data,safe=False)

@api_view(["GET"])
def get_players_age(request):
    collection=db['players']
    dt= datetime.today()
    delta1 = timedelta(days=365*30)
    delta2 = timedelta(days=365*40) 
    max_date= dt-delta1
    min_date= dt-delta2
    cursor=collection.find({"dob":{"$gte":min_date,"$lte":max_date}},{"_id":0})
    data = list(cursor)
    return JsonResponse(data,safe = False)

@api_view(['GET'])
def get_emp_range(request):
    collection=db['players']
    from_date= datetime(1987,1,1,0,0)
    to_date = datetime(1987,12,31,0,0)
    cursor = collection.find({"dob":{"$gte":from_date,"$lt":to_date}},{"_id":0})
    data = list(cursor)
    return JsonResponse(data,safe = False)
@api_view(['POST'])
def get_emp_up(request):
    collection=db['players']
    cursor =collection.insert({"fav":"DHONI"})


@api_view(['GET'])
def get_emp_op(request):
    collection=db['players']
    cursor = collection.find({"fav":"DHONI"},{"_id":0})
    data = list(cursor)
    return JsonResponse(data,safe=False)
    
