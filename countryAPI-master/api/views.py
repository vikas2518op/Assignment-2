from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from bs4 import BeautifulSoup
from urllib.request import urlopen
from rest_framework import status
import requests
import json
# Create your views here.

class GetCountry(APIView):
    def get(self, request, cName):
        response_API = requests.get(f'https://restcountries.com/v3.1/name/{cName}')
        #print(response_API.status_code)
        data = response_API.text
        parse_json = json.loads(data)       
        status_code = status.HTTP_200_OK
        response = {
            'status code': status_code,
            'flag_link': parse_json[0]["flags"],
            'capital': parse_json[0]["capital"],

            'official_languages': parse_json[0]["languages"],
            'area_total': parse_json[0]["area"],
            'Population': parse_json[0]["population"],
            
        }
        return Response(response, status=status_code)
