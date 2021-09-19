from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Events
from .serializers import EventSerializer

class LatestEventsList(APIView):
    def get(self,request,format=None):
        events=Events.objects.all()[0:4]
        serializer=EventSerializer(events,many=True)
        return Response(serializer.data)

class EventDetail(APIView):
    def get_object(self,organizer_slug,event_slug):
        try:
            return Events.objects.filter(organizer__slug=organizer_slug).get(slug=event_slug)
        except Events.DoesNotExist:
            raise Http404
    def get(self,request,organizer_slug,event_slug,format=None):
        event=self.get_object(organizer_slug ,event_slug)
        serializer=EventSerializer(event)
        return Response(serializer.data)