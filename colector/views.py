from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from colector.models import Station, Error, OnlineStations, NewConfig
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from colector.serializers import ErrorSerializer, OnlineStationsSerializer, NewConfigSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from colector.tasks import sendn as sn







@csrf_exempt
def error_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        errors = Error.objects.all()
        serializer = ErrorSerializer(errors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ErrorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            st = str(serializer.initial_data['station'])
            msg = str(serializer.initial_data['msg'])
            print(st, msg)
            sn(st)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    """
    @api_view(['GET', 'POST'])
    @csrf_exempt
    def online_list(request):
    
        if request.method == 'GET':
            online = OnlineStations.objects.all()
            serializer = OnlineStationsSerializer(online, many=True)
            return JsonResponse(serializer.data, safe=False)
    
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = OnlineStationsSerializer(data=data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
    
    """


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def online_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        online = OnlineStations.objects.get(pk=pk)
    except Error.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OnlineStationsSerializer(online)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OnlineStationsSerializer(online, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        online.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def new_config(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        new = NewConfig.objects.get(pk=pk)
    except Error.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NewConfigSerializer(new)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NewConfigSerializer(new, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        new.delete()
        return HttpResponse(status=204)


def about(request):
    return HttpResponse("Developed under Qarantine COVID 19 2020")


def index(request):
    context_dict = {}
    stations_list = Station.objects.all()

    last_error_list = []
    for i in stations_list:
        try:
            last_error_list.append(Error.objects.filter(station=i).latest('time'))
        except:
            last_error_list.append('No Errors')
    print(last_error_list.reverse())
    context_dict['Stations'] = stations_list
    context_dict['Errors'] = last_error_list

    return render(request, 'colector/index.html', context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    print(category_name_slug)
    try:
        category = Station.objects.get(slug=category_name_slug)
        pages = Error.objects.filter(station=category)

        context_dict['pages'] = pages
        context_dict['category'] = category

    except Station.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'colector/category.html', context_dict)


#notify_someone(repeat=10, repeat_until=None)
