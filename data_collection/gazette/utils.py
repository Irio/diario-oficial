import csv
import re
from unicodedata import normalize

import pkg_resources


def read_territories():
    territories_file = pkg_resources.resource_filename(
        "gazette", "resources/territories.csv"
    )

    with open(territories_file, encoding="utf-8") as f:
        yield from csv.DictReader(f)


def normalize_place_name(name):
    """Gets rid of most common irregularities in names of places.

    Puts everything in lowercase and tries to encode latin to ascii characters:
    >>> normalize_place_name("Conceição")
    "conceicao"

    Removes prepositions "da(s)", "de(s)", "do(s)" and "d[`´-]" (apostrophes may vary
    in character used):
    >>> normalize_place_name("Pedra do Indaiá")
    "pedra indaia"
    >>> normalize_place_name("Riacho das Almas")
    "riacho almas"
    >>> normalize_place_name("Barra D` Alcântara")
    "barra alcantara"

    Translates hyphen to whitespace:
    >>> normalize_place_name("Xangri-lá")
    "xangri la"

    Removes variations of apostrophes (`, ´ and '):
    >>> normalize_place_name("Sant'Ana do Livramento")
    "santana do livramento"

    Removes excess of whitespace:
    >>> normalize_place_name(" Coronel   Sapucaia")
    "coronel sapucaia"
    """

    normalized = name.lower()
    normalized = normalized.replace("-", " ")
    normalized = re.sub(" d[`´']", " ", normalized)
    normalized = re.sub("[`´']", "", normalized)
    normalized = re.sub(" d[aeo]s? ", " ", normalized)
    normalized = latin_to_ascii_characters(normalized)
    normalized = " ".join(map(str.strip, normalized.split()))
    return normalized


def latin_to_ascii_characters(text):
    return normalize("NFKD", text).encode("ASCII", "ignore").decode("utf8")
