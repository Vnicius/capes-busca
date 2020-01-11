# -*- coding: utf-8 -*-
from copy import deepcopy
from urllib.parse import quote
import json

import requests

from src.searchresult import SearchResult
from src.searcherror import SearchError

SEARCH_URL = "https://catalogodeteses.capes.gov.br/catalogo-teses/rest/busca"
AGGREGATIONS_URL = SEARCH_URL + \
    "/agregacoes?termo={}&agregado={}&pagina={}&registrosPorPagina={}"


class Request:

    ''' Classe para realizar os requisições dos dados '''

    def search(self, search_query, full_aggregations=False):
        '''
            Realiza a requisição de busca

            Params:
                search_query (search_query.SearchQuery): Query de busca
                full_aggregations (bool): Flag para realizar a requisição da lista completa de agregações

            Returns:
                (searchresult.SearchResult): Resultado da busca
        '''

        response_json = {}

        try:
            response_json = requests.post(SEARCH_URL, data=search_query.json(),
                                          headers={'content-type': 'application/json'}).json()

            if full_aggregations:
                response_json['agregacoes'] = self.__get_full_aggregations(
                    search_query, response_json.get('agregacoes', []))

        except json.decoder.JSONDecodeError:
            raise SearchError("Error doing the search")
        except ConnectionError:
            raise SearchError("Connection error")

        return SearchResult(response_json)

    def __get_full_aggregations(self, search_query, initial_aggregations):

        aggregations = deepcopy(initial_aggregations)

        for aggregation in aggregations:
            aggregation_name = aggregation.get('campo', '') + '_raw'

            url = AGGREGATIONS_URL.format(
                quote(search_query.term), quote(aggregation_name), search_query.page, search_query.page_size)

            try:
                response = requests.post(url, data=search_query.json(), headers={
                    'content-type': 'application/json'}, timeout=5).json()

                if response.get('total', 0) > 0:
                    aggregation['agregados'] = response['agregados']

            except requests.exceptions.ReadTimeout:
                pass
            except json.decoder.JSONDecodeError:
                pass
            except ConnectionError:
                pass

        return aggregations
