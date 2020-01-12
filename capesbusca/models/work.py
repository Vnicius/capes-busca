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

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        return str(vars(self))

    @staticmethod
    def parse(dictionary):
        '''
            Reliza o parser de dados em dict para o objeto

            Params:
                dictionary (dict): dicionário com os dados

            Returns:
                Work
        '''

        id = dictionary.get('id', '')
        instituicao = dictionary.get('instituicao', '')
        nome_programa = dictionary.get('nomePrograma', '')
        municipio_programa = dictionary.get(
            'municipioPrograma', '')
        titulo = dictionary.get('titulo', '')
        autor = dictionary.get('autor', '')
        data_defesa = dictionary.get('dataDefesa', '')
        volumes = dictionary.get('volumes', 0)
        paginas = dictionary.get('paginas', 0)
        biblioteca = dictionary.get('biblioteca', '')
        grau_academico = dictionary.get('grauAcademico', '')
        link = dictionary.get('link', '')

        return Work(
            id=id,
            instituicao=instituicao,
            nome_programa=nome_programa,
            municipio_programa=municipio_programa,
            titulo=titulo,
            autor=autor,
            data_defesa=data_defesa,
            volumes=volumes,
            paginas=paginas,
            biblioteca=biblioteca,
            grau_academico=grau_academico,
            link=link,
        )
