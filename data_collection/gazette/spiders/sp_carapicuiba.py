import datetime
import re

from scrapy.http import FormRequest

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpCarapicuiba(BaseGazetteSpider):
    TERRITORY_ID = "3510609"
    name = "sp_carapicuiba"
    allowed_domains = ["carapicuiba.sp.gov.br"]

    base_url = "http://www.carapicuiba.sp.gov.br/index.php/ajax/atosOficiais"
    custom_settings = {"MEDIA_ALLOW_REDIRECTS": True}

    start_date = datetime.date(2018, 2, 21)
    end_date = datetime.datetime.today().date()

    def start_requests(self):
        params = {"page": "1", "categoria": "21-DiarioOficial"}

        yield FormRequest(
            self.base_url,
            formdata=params,
            cb_kwargs={"params": params},
        )

    def parse(self, response, params):
        gazettes = response.css("#lista-servicios img + a")
        for a in gazettes:
            gazette = self.get_gazette(a)
            if gazette and self.start_date <= gazette["date"] <= self.end_date:
                yield response.follow(
                    a, callback=self.parse_gazette, cb_kwargs={"gazette": gazette}
                )
            else:
                return

        if gazettes:
            new_params = params.copy()
            new_params["page"] = str(int(params["page"]) + 1)
            yield FormRequest(
                self.base_url,
                formdata=new_params,
                cb_kwargs={"params": new_params},
            )

    def get_gazette(self, a):
        if "COMUNICADO DIÁRIO OFICIAL" in a.get():
            return None

        pattern = r"[^\d]*(\d+)[^\d]*(\d+) De (\w+) De (\d+)"
        edition, day, month_name, year = a.re(pattern)
        month = [
            "",
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ].index(month_name)

        return Gazette(
            edition_number=edition,
            date=datetime.date(int(year), month, int(day)),
            is_extra_edition=("Extra" in a.get()),
        )

    def parse_gazette(self, response, gazette):
        file_url = response.css("hr + div + div a").attrib["href"]

        if "drive.google.com" in file_url:
            pattern_id = r"([^/]+(?=/view)|(?<=id=)[^&]+)"
            doc_id = re.search(pattern_id, file_url).group()
            file_url = "https://drive.google.com/uc?id=" + doc_id
        else:
            file_url = response.urljoin(file_url)

        gazette["file_urls"] = [file_url]
        gazette["power"] = "executive"

        yield gazette
