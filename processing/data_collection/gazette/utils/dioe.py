"""
This module has some utils function to retrieve data from DiOE web site
(https://dosp.com.br/), which contain gazettes from several cities and entities.

The site has a Modelandia state, so this (and it's cities and entities) was
used in tests docstrings.
"""

import requests
from lxml import html


def filter_by(data, value):
    """
    This function return data applying some filter.
    The data argument must be: estado, cod_cidades or entidade.
    The value is a valid internal code from DiOE.
    """
    valid_data = ("estado", "cod_cidades", "entidade")
    if data not in valid_data:
        raise RuntimeError(f"Data must be in {valid_data}")

    url = f"https://dosp.com.br/doant_filtra_ie.php?data={data}&val={value}"

    response = requests.get(url)

    parser = html.HTMLParser(encoding=response.encoding)
    data = html.fromstring(response.content, parser=parser)
    for d in data:
        id_data = d.attrib.get("value")
        yield {"id": id_data, "name": d.text}


def get_states():
    """
    Return all states from DiOE . Each state is a dict with id and name
    fields.
    >>> states = get_states()
    >>> {'id': '28', 'name': 'Modelândia (MO)'} in states
    True
    """
    return filter_by("estado", -1)


def get_cities(state):
    """
    Return all cities from state parameter. Each city is a dict with id and name
    fields.
    >>> cities = get_cities(28)
    >>> {'id': '5510', 'name': 'Modelândia Legislativo'} in cities
    True
    """
    return filter_by("cod_cidades", state)


def get_entities(city):
    """
    Return all entities from city argument. Each  is a dict with id and name
    fields.
    >>> cities = get_cities(28)
    >>> {'id': '5510', 'name': 'Modelândia Legislativo'} in cities
    True
    """
    return filter_by("entidade", city)


def get_all_entities():
    """
    This function return all entities from dosp.com.br
    """
    for state in get_states():
        id_state = state["id"]
        entity = {"id_state": id_state, "name_state": state["name"]}
        for city in get_cities(id_state):
            id_city = city["id"]
            entity["id_city"] = id_city
            entity["name_city"] = city["name"]

            for ent in get_entities(id_city):
                entity["id_entity"] = ent["id"]
                entity["name_entity"] = ent["name"]

            yield entity


if __name__ == "__main__":
    import doctest

    doctest.testmod()
