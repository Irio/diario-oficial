import re
from datetime import date, datetime

from dateparser import parse
from dateutil.rrule import MONTHLY, rrule
from scrapy import FormRequest

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class ScFlorianopolisSpider(BaseGazetteSpider):
    name = "sc_florianopolis"
    TERRITORY_ID = "4205407"

    start_date = date(2009, 6, 1)

    def start_requests(self):
        end_date = date.today()

        periods_of_interest = [
            (date.year, date.month)
            for date in rrule(freq=MONTHLY, dtstart=self.start_date, until=end_date)
        ]
        for year, month in periods_of_interest:
            data = dict(ano=str(year), mes=str(month), passo="1", enviar="")
            yield FormRequest(
                "http://www.pmf.sc.gov.br/governo/index.php?pagina=govdiariooficial",
                formdata=data,
            )

    def parse(self, response):
        for link in response.css("ul.listagem li a"):
            url = self.get_pdf_url(response, link)
            if not url:
                continue

            gazette_date = self.get_date(link)

            gazette_edition_number = link.css("::attr(title)").re_first(r"Edição (\d+)")

            yield Gazette(
                date=gazette_date,
                edition_number=gazette_edition_number,
                file_urls=(url,),
                is_extra_edition=self.is_extra(link),
                territory_id=self.TERRITORY_ID,
                power="executive_legislature",
                scraped_at=datetime.utcnow(),
            )

    @staticmethod
    def get_pdf_url(response, link):
        relative_url = link.css("::attr(href)").extract_first()
        if not relative_url.lower().endswith(".pdf"):
            return None

        return response.urljoin(relative_url)

    @staticmethod
    def get_date(link):
        text = " ".join(link.css("::text").extract())
        pattern = r"\d{1,2}\s+de\s+\w+\s+de\s+\d{4}"
        match = re.search(pattern, text)
        if not match:
            return None

        return parse(match.group(), languages=("pt",)).date()

    @staticmethod
    def is_extra(link):
        text = " ".join(link.css("::text").extract())
        return "extra" in text.lower()
