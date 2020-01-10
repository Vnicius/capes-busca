# -*- coding: utf-8 -*-


class Response:

    ''' 
        Classe para receber a reposta da requisição 
        e realizar o parser para os modelos
    '''

    def __init__(self, response_json):
        '''
            Construtor da classe Response

            Attr:
                response_json (dict): resposta da requisição
        '''
        self.response_json = response_json

        self.__parse_response()

    def __parse_response(self):
        '''
            Realiza o parse da resposta da requisição para os modelos
        '''
        return
