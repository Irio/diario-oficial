import importlib
import pathlib
import sys
from functools import lru_cache
from itertools import groupby

import pkg_resources
from jinja2 import Environment, FileSystemLoader
from scrapy.utils.spider import iter_spider_classes

PROJECT_ROOT = pathlib.Path(__file__).absolute().parent.parent.parent
SCRAPY_PROJECT_DIR = PROJECT_ROOT / "data_collection"
sys.path.insert(0, str(SCRAPY_PROJECT_DIR))
utils = importlib.import_module("gazette.utils")


def update():
    territories = list(utils.read_territories())
    for territory in territories:
        territory_population = int(territory["population_ibge_2020"])
        territory.update(
            {
                "population_ibge_2020": territory_population,
                "normalized_name": utils.normalize_place_name(territory["name"]),
                "spiders": spiders_by_territory().get(territory["id"], []),
                "is_capital_bool": bool(int(territory["is_capital"])),
                "is_population_above_100k": territory_population > 100000,
            }
        )

    territories_by_state = groupby_to_dict_of_lists(
        sort_and_group(
            territories, key=lambda t: utils.latin_to_ascii_characters(t["state"])
        )
    )

    coverage_file = PROJECT_ROOT / "COVERAGE.md"
    with coverage_file.open("w") as covfile:
        covfile.write(load_template(territories, territories_by_state))


def get_spiders_metadata():
    spiders_dir_path = pkg_resources.resource_filename("gazette", "spiders")
    spider_files = pathlib.Path(spiders_dir_path).glob("*.py")

    for spider_file in spider_files:
        spider_module = importlib.import_module(f"gazette.spiders.{spider_file.stem}")
        spiders = iter_spider_classes(spider_module)
        for spider in spiders:
            spider_territories = [spider.TERRITORY_ID] + getattr(
                spider, "TERRITORIES_COVERAGE", []
            )
            yield {
                "territories": spider_territories,
                "name": spider.name,
                "path": str(spider_file.relative_to(PROJECT_ROOT)),
            }


@lru_cache()
def spiders_by_territory():
    territories = {}
    for spider in get_spiders_metadata():
        for territory_id in spider["territories"]:
            territories.setdefault(territory_id, []).append(spider)

    return territories


def load_template(territories, territories_by_state):
    update_coverage_dir = pathlib.Path(__file__).absolute().parent
    env = Environment(loader=FileSystemLoader(str(update_coverage_dir)))
    template = env.get_template("coverage_template.jinja")
    return template.render(
        territories=territories, territories_by_state=territories_by_state
    )


def sort_and_group(iterable, key=None):
    return groupby(sorted(iterable, key=key), key=key)


def groupby_to_dict_of_lists(groupby_obj):
    dict_of_lists = {}
    for key, group in groupby_obj:
        dict_of_lists[key] = list(group)
    return dict_of_lists


if __name__ == "__main__":
    update()
