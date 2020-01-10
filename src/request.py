# -*- coding: utf-8 -*-
import json
import requests
from src.response import Response

SEARCH_URL = "https://catalogodeteses.capes.gov.br/catalogo-teses/rest/busca"


class Request:

    ''' Classe para realizar os requisições dos dados '''

    def search(self, search_query):
        '''
            Realiza a requisição de busca

            Params:
                search_query (search_query.SearchQuery): Query de busca

            Returns:
                (response.Response): Resposta da busca
        '''

        response_json = {}

        try:
            response_json = requests.post(SEARCH_URL, data=search_query.json(),
                                          headers={'content-type': 'application/json'}).json()
        except ConnectionError:
            pass

        return Response(response_json)
