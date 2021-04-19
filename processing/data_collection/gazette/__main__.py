import argparse
import re

from collections import defaultdict
from pathlib import Path
from re import sub
from textwrap import dedent


def list_spiders(path="spiders", states=None):
    """
    Lists all the spiders available and breaks their names
    in state and city.

    Returns a dictionary containing the state's initials
    and a list of its cities.
    """
    root = Path(__file__).parent
    spiders = root / "spiders"
    pattern = r"^([a-z]{2})_([a-z_]+)\.py$"

    states = set(state.upper() for state in states) if states else None

    results = defaultdict(list)

    for f in spiders.glob("*.py"):
        name = f.name
        matches = re.findall(pattern, name)

        if matches:
            state, city = matches[0]
            state = state.upper()

            if not states or state in states:
                city = city.replace("_", " ").title()
                results[state].append(city)
    return results


def print_spiders_list(spider_list):
    """
    Given a dictionary as returned by `lists_spiders`,
    prints them in a user-friendly format.

    Currently, it will order the keys alphabetically
    and print each city on a separate line, also
    alphabetically. At the end of each key, it
    prints a separator.
    """
    for state in sorted(spider_list.keys()):
        print(f"Cidades de {state}")
        for city in sorted(spider_list[state]):
            print(f"\t{city}")
        print("*-" * 20, "*", sep="")


def main(subcommand, states=None):
    if subcommand == "list":
        results = list_spiders(states=states)
        print_spiders_list(results)


if __name__ == "__main__":
    usage = dedent(
        """
    Gazette's CLI exposes the currently available spiders. You can list
    all the spiders with:

        $ python gazette list

    It is also posible to limit the search by one state:

        $ python gazette list --state=sp

    You can also limit the search to multiple states:

        $ python gazette list --state=sp,pr,rj
    """
    )
    parser = argparse.ArgumentParser(usage=usage)
    subparsers = parser.add_subparsers()

    list_group = subparsers.add_parser("list", help="Lists all the available spiders")
    subparsers = list_group.add_subparsers()
    state_list = list_group.add_argument(
        "--state",
        type=lambda s: [item for item in s.split(",")],
        help="A comma separated list of the state's initials to be looked up",
    )

    args = parser.parse_args()

    if "state" in args:
        main("list", states=args.state)
