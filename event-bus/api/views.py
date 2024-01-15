from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response



class EventView(APIView):
    def post(self, request):
        try:
            event_data = json.loads(request.body)
            event_type = event_data.get('type')
            event_data = event_data.get('data', {})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        post_url = "http://127.0.0.1:8001/api/events/"
        comment_url = "http://127.0.0.1:8000/api/events/"
        query_url = "http://127.0.0.1:8003/api/events/"

        data = {
            "type": event_type,
            "data": event_data
        }
        
        headers = {'Content-Type': 'application/json'}
        requests.post(url=post_url, data=json.dumps(data),headers = headers)
        requests.post(url=comment_url, data=json.dumps(data),headers = headers)
        # requests.post(url=query_url, data=json.dumps(data),headers = headers)

        return Response(data)