import datetime as dt
from urllib.parse import urljoin

from dateutil.relativedelta import relativedelta
from scrapy.http import Request

from gazette.items import Gazette
from gazette.spiders.base.instar import BaseInstarSpider


class SpTaubateSpider(BaseInstarSpider):
    TERRITORY_ID = "3554102"
    name = "sp_taubate"
    allowed_domains = ["camarataubate.sp.gov.br"]
    start_url = "https://www.taubate.sp.gov.br/anexos/publicacoes/"
    start_date = None

    def __init__(self, start_date=None, end_date=None, *args, **kwargs):
        self.start_date = dt.date(2013, 6, 1)
        self.end_date = dt.date.today()

    def start_requests(self):
        base_url = "https://www.taubate.sp.gov.br/anexos/publicacoes/"

        target_date = self.start_date

        while target_date <= self.end_date:
            urlEnd = self.getUrlEnd(target_date)
            target_url = urljoin(base_url, urlEnd)
            yield Request(
                target_url,
                callback=self.parse,
                meta={"urlEnd": urlEnd, "date": target_date},
            )
            target_date = target_date + relativedelta(months=+1)

    def getUrlEnd(self, target_date):
        year = target_date.year
        monthInString = [
            "Janeiro",
            "Fevereiro",
            "Marco",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]
        monthNumber = ""
        separator = ""
        monthText = ""

        if year >= 2013 and year <= 2017:
            monthNumber = str(target_date.month).zfill(2)
            separator = ".%20"
            monthText = monthInString[target_date.month - 1]

        if year > 2017 and year < 2020:
            monthNumber = str(target_date.month).zfill(2)
            separator = "."
            monthText = monthInString[target_date.month - 1]

        if year >= 2020:
            monthNumber = str(target_date.month).zfill(2)
            separator = "-"
            monthText = (monthInString[target_date.month - 1]).upper()

        return str(year) + "/" + monthNumber + separator + monthText

    def parse(self, response):
        year = response.xpath("/html/body/div/h2/text()").get()
        urlEnd = response.meta["urlEnd"]
        gazette_date = response.meta["date"]

        if int(year) <= 2020:
            links = response.xpath('//*[@id="ul1"]/li[*]/a')
            links = links.xpath("@href").getall()

        for index, file_url in enumerate(links):
            full_url = self.start_url + "/" + urlEnd + "/" + file_url

            yield Gazette(
                date=gazette_date,
                file_urls=[full_url],
            )
