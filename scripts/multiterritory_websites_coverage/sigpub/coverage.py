import csv
import importlib
import logging
import pathlib
import re
import sys
from functools import lru_cache
from itertools import groupby
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from parsel import Selector

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

PROJECT_ROOT = pathlib.Path(__file__).absolute().parent.parent.parent.parent

scrapy_project_dir = PROJECT_ROOT / "data_collection"
sys.path.insert(0, str(scrapy_project_dir))
utils = importlib.import_module("gazette.utils")


def report():
    current_dir = pathlib.Path(__file__).absolute().parent
    websites = read_csv(current_dir / "covered_associations.csv")

    matchings = {"matched": [], "not_matched": []}

    for website in websites:
        raw_publishing_entities = extract_publishing_entities(
            url=f"{website['homepage']}/pesquisar"
        )
        website_matchings = try_matching_entities_to_territories(
            raw_publishing_entities, website
        )
        matchings["matched"].extend(website_matchings["matched"])
        matchings["not_matched"].extend(website_matchings["not_matched"])

    write_to_csv(current_dir / "matched_territories.csv", matchings["matched"])
    write_to_csv(current_dir / "not_matched_territories.csv", matchings["not_matched"])


def try_matching_entities_to_territories(raw_publishing_entities, website):
    state_territories = territories_by_state_code()[website["state_code"]]
    state_territories = map_territories_by_normalized_name(state_territories)

    matched_territories = []
    not_matched_territories = []

    for entity in raw_publishing_entities:
        territory_match = re.search(
            r"^\s*(prefeitura municipal|prefeitura|munic[íi]pio)(\s+d[aeo])?\s+(.+)",
            entity,
            re.IGNORECASE,
        )
        if not territory_match:
            continue

        territory_name = utils.normalize_place_name(territory_match.group(3))
        territory_name_variations = [
            territory_name,
            f"{territory_name} {utils.normalize_place_name(website['state'])}",
        ]

        for name in territory_name_variations:
            if name in state_territories:
                territory_id = state_territories[name]["id"]
                matched_territories.append(
                    {
                        "territory_id": territory_id,
                        "homepage": website["homepage"],
                        "state_code": website["state_code"],
                        "raw_publishing_entity": entity,
                        "matched_territory_name": name,
                    }
                )
                break
        else:
            not_matched_territories.append(
                {
                    "homepage": website["homepage"],
                    "state_code": website["state_code"],
                    "raw_publishing_entity": entity,
                }
            )

    return {"matched": matched_territories, "not_matched": not_matched_territories}


def extract_publishing_entities(url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    logging.info(f"Reaching {url} ...")
    try:
        response = Selector(urlopen(request).read().decode("utf8"))
    except HTTPError as exc:
        logging.error(f"Couldn't reach {url}. Maybe try again later.")
        raise exc

    names = response.xpath(
        "//select[@id='busca_avancada_entidadeUsuaria']/option/text()"
    ).getall()
    return names


@lru_cache()
def territories_by_state_code():
    return groupby_to_dict_of_lists(
        sort_and_group(utils.read_territories(), key=lambda t: t["state_code"])
    )


def map_territories_by_normalized_name(territories):
    return {utils.normalize_place_name(t["name"]): t for t in territories}


def read_csv(path):
    with path.open(encoding="utf-8") as f:
        yield from csv.DictReader(f)


def write_to_csv(path, lines):
    iterlines = iter(lines)
    try:
        first = next(iterlines)
    except StopIteration:
        logging.debug("Nothing to write.")
        return

    with path.open("w", encoding="utf-8") as f:
        columns = dict(first).keys()
        writer = csv.DictWriter(f, columns)
        writer.writeheader()
        writer.writerow(first)
        writer.writerows(iterlines)


def sort_and_group(iterable, key=None):
    return groupby(sorted(iterable, key=key), key=key)


def groupby_to_dict_of_lists(groupby_obj):
    dict_of_lists = {}
    for key, group in groupby_obj:
        dict_of_lists[key] = list(group)
    return dict_of_lists


if __name__ == "__main__":
    report()
