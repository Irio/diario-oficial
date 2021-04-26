from dateparser import parse

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PrCampoMouraoSpider(BaseGazetteSpider):
    TERRITORY_ID = "4104303"
    name = "pr_campo_mourao"
    start_urls = ["https://campomourao.atende.net/?pg=diariooficial&pagina=1"]

    def parse(self, response):
        url_base = response.url[0:56]
        page = int(response.url[56:])

        list = response.xpath("//div[@class='nova_listagem ']/div[@class='linha']")

        if not list:
            return

        for row in list:
            date = row.xpath("//div[@class='info']/div[@class='data']/text()").get()
            date = parse(date, languages=["pt"]).date()

            edition_type = row.xpath(
                "//div[@class='info']/div[@class='tipo']/text()"
            ).get()
            edition_number = row.xpath(
                "//div[@class='info']/div[@class='titulo']/text()"
            ).get()
            edition_number = edition_number.split(" ")[1]

            code = row.xpath("//button[@data-acao='download']/@data-codigo").get()
            id = row.xpath("//button[@data-acao='download']/@data-id").get()

            is_extra = True if edition_type == "Extraordinária" else False

            url = f"https://campomourao.atende.net/atende.php?rot=54002&aca=737&processo=download&codigo={code}&hash={id}"

            yield Gazette(
                date=date,
                edition_number=edition_number,
                file_urls=[url],
                is_extra_edition=is_extra,
                power="executive_legislative",
            )

        yield response.follow(url_base + str(page + 1))
