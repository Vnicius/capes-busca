# Capes Busca

Biblioteca para realizar busca de termos no catálogo de teses e dissertações da Capes (https://catalogodeteses.capes.gov.br/catalogo-teses)

## Instalação

```
    $ pip install capesbusca
```

## Requisitos

- Python 3

```sh
    $ pip install -r requirements.txt
```

## Exemplo

- Buscando o termo 'ia' nos anos 2018 e 2019

```python
    # example.py

    from capesbusca import search, SearchQuery
    from capesbusca.filters import Ano

    search_query = SearchQuery.Builder("ia").set_page(
        1).set_page_size(40).add_filters(Ano(2018), Ano(2019)).build()

    result = search(search_query)

    for work in result.works:
        print(work.titulo)
```

```
    $ python example.py
    PyRDMIA: um pacote intervalar para aritmética RDM
    Avaliação e Sintonia de Controladores PID nos Domínios do Tempo e Frequên ia
    Pedagogia da Circularidade Afrocênica: Candomblé Congo-Angola, Filosofia Bantu e Ensino de Arte Transdisciplinar
    ...
```

## Filtros

- Ano
- Área de Avaliação
- Área de Concentração
- Área de Conhecimento
- Autor
- Banca
- Biblioteca
- Grau Acadêmico
- Instituição
- Orientador
- Programa

## Modelos dos dados

- Trabalho (Work)

  - id
  - instituição
  - nome do programa
  - município do programa
  - título
  - autor
  - data da defesa
  - volumes
  - páginas
  - biblioteca
  - grau acadêmico
  - link

- Agregação (Aggregation)

  - campo
  - total
  - agragados

- Agregado (Aggregate)

  - valor
  - total

## Sobre o uso

O uso das informações da referida base de dados e de seus registros está sujeito às leis de direito autorais vigentes (Lei nº 9.610, de 19.02.98). Saiba mais [aqui](https://sdi.capes.gov.br/banco-de-teses/02_bt_sobre.html).
