import argparse
import csv
from os.path import abspath, dirname
from unicodedata import normalize
from urllib.parse import urlparse

from jinja2 import Environment, FileSystemLoader


def load_template(spider_data):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("spider_template.jinja")
    return template.render(
        spider_class_base=spider_data["spider_class_base"],
        spider_class_name=spider_data["spider_class_name"],
        spider_name=spider_data["spider_name"],
        allowed_domain=spider_data["allowed_domain"],
        start_year=spider_data["start_year"],
        start_month=spider_data["start_month"],
        start_day=spider_data["start_day"],
        base_url=spider_data["base_url"],
        territory_id=spider_data["territory_id"],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generate a spider structure from CSV.")
    parser.add_argument("file")
    args = parser.parse_args()
    project_root = dirname(dirname(dirname(abspath(__file__))))

    with open(args.file) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            normalized_city_name = (
                normalize("NFKD", row["city"]).encode("ASCII", "ignore").decode("utf8")
            )
            split_city_name = normalized_city_name.replace("-", " ").split()
            split_city_name = [word.title() for word in split_city_name]
            domain = urlparse(row["url"]).netloc
            spider_data = {
                "spider_class_base": row["base_class"],
                "spider_class_name": f"{row['state'].title()}{''.join(split_city_name)}",
                "spider_name": f"{row['state'].lower()}_{'_'.join(split_city_name).lower()}",
                "allowed_domain": domain,
                "start_year": row["start_year"],
                "start_month": row["start_month"],
                "start_day": row["start_day"],
                "base_url": row["url"],
                "territory_id": row["territory_id"],
            }
            spider_path = f"{project_root}/data_collection/gazette/spiders/"
            filepath = f"{spider_path}{row['state'].lower()}_{'_'.join(split_city_name).lower()}.py"
            with open(filepath, "w") as spiderfile:
                spiderfile.write(load_template(spider_data))
