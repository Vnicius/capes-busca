# -*- coding: utf-8 -*-


class Work:

    ''' Modelo dos trabalhos de tese e dissertação '''

    def __init__(self,
                 id='',
                 instituicao='',
                 nome_programa='',
                 municipio_programa='',
                 titulo='',
                 autor='',
                 data_defesa='',
                 volumes=0,
                 paginas=0,
                 biblioteca='',
                 grau_academico='',
                 link=''
                 ):
        '''
            Construtor da classe Work

            Attr:
                id (str): id do trabalho
                instituicao (str): instituição atribuída ao trabalho
                nome_programa (str): nome do programa atribuído ao trabalho
                municipio_programa (str): município do programa
                titulo (str): título do trabalho
                autor (str): autor do trabalho
                data_defesa (str): data da defesa do trabalho
                volumes (int): volumes do trabalho
                paginas (int): quantidade de páginas
                biblioteca (str): biblioteca que possuí o trabalho
                grau_academico (str): grau acadêmico do trabalho
                link (str): link de acesso do trabalho
        '''

        self.id = id
        self.instituicao = instituicao
        self.nome_programa = nome_programa
        self.municipio_programa = municipio_programa
        self.titulo = titulo
        self.autor = autor
        self.data_defesa = data_defesa
        self.volumes = volumes
        self.paginas = paginas
        self.biblioteca = biblioteca
        self.grau_academico = grau_academico
        self.link = link
