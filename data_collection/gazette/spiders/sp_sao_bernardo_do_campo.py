import re
from datetime import date, datetime

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpSaoBernardoDoCampoSpider(BaseGazetteSpider):
    TERRITORY_ID = "3548708"
    name = "sp_sao_bernardo_do_campo"
    allowed_domains = ["saobernardo.sp.gov.br"]
    start_date = date(2002, 5, 3)
    end_date = date.today()

    def start_requests(self):
        base_url = "https://www.saobernardo.sp.gov.br/web/sbc/todas-as-edicoes"
        yield scrapy.Request(base_url)

    def parse(self, response):
        base_files_url = "https://www.saobernardo.sp.gov.br"
        years = response.xpath(
            "/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/section/div/div/div/a/text()"
        ).re(r" *(.+)")
        hrefs = response.xpath(
            "/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/section/div/div/div/a/@href"
        ).re(r"#(\w+)")
        ids = dict(zip(years, hrefs))
        duplicated = [" NM 1915"]

        for y in range(self.start_date.year, self.end_date.year + 1):
            y = str(y)
            anchors = response.xpath(
                "/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/section/div/div/div/ul[@id=$a_id]/li/a",
                a_id=ids[y],
            )
            for gazette in anchors:
                text = gazette.xpath("text()").get()
                # Duplicated gazettes can be ignored
                if text in duplicated:
                    continue

                gazette_edition = self.extract_edition(text, y)
                if gazette_edition is not None:
                    gazette_edition_number = self.extract_edition_number(
                        gazette_edition
                    )
                else:
                    gazette_edition_number = None
                    self.logger.error(
                        "Couldn't extract edition for gazette: '%s' / year: %s", text, y
                    )
                    continue

                gazette_date = self.extract_date(text, y)
                if gazette_date is None:
                    if gazette_edition_number is not None:
                        gazette_date = self.estimate_date(gazette_edition_number)
                    else:
                        self.logger.error(
                            "Couldn't extract either edition number or date for gazette: '%s' / year: %s",
                            text,
                            y,
                        )
                        continue

                if gazette_date >= self.start_date and gazette_date <= self.end_date:
                    gazette_link = base_files_url + gazette.xpath("@href").get()
                    # TODO Extract info about extra edition
                    yield scrapy.Request(
                        gazette_link,
                        cb_kwargs={
                            "gazette_date": gazette_date,
                            "file_urls": [gazette_link],
                            "edition_number": gazette_edition_number,
                        },
                        callback=self.parse_gazette,
                    )

    def parse_gazette(self, response, gazette_date, file_urls, edition_number):
        gazette = Gazette(
            date=gazette_date,
            file_urls=file_urls,
            power="executive",
            is_extra_edition=False,
            edition_number=edition_number,
        )
        yield gazette

    def extract_edition(self, text, year):
        """Return edition number + extra edition info from the text, according to each year's naming rules."""
        # Regular expressions to extract edition number for each year
        # Each entry can contain up to 2 regexes concatenated with '|'
        re_edition = {
            "2002": r"^NM 2002 (.+) \d\d_\d\d_2002$",
            "2003": r"^NM (.+) \d\d_\d\d_2003$",
            "2004": r"^NM 2004 (.+)\.pdf$|^NM (.+) \d\d_\d\d_2004$",
            "2005": r"^NM 2005 (.+)\.pdf$|^NM (.+) \d\d_\d\d_2005$",
            "2006": r"^NM 2006 (.+)\.pdf$",
            "2007": r"^NM 2007 (.+)\.pdf$",
            "2008": r"^NM 2008 (.+)\.pdf$",
            "2009": r"^NM 2009 (.+)\.pdf$",
            "2010": r"^NM 2010 (.+)\.pdf$",
            "2011": r"^NM 2011 (.+)\.pdf$",
            "2012": r"^NM 2012 (.+)\d\d_\d\d_2012$",
            "2013": r"^NM (.+)_\d\d_\d\d_13$",
            "2014": r"^NM 2014 (.+)$|^\d\d_\d\d_2014_NM_(.+)$",
            "2015": r"^\d\d_\d\d_2015_NM_(.+)$",
            "2016": r"^\d\d_\d\d_(?:16|2016)[_ ]NM[_ ](.+)$",
            "2017": r"^NM (.+) de \d\d[./]\d\d[./]2017.*$",
            "2018": r"^NM (.+) de \d\d\.\d\d\.2018.*$",
            "2019": r"^NM (.+) de \d\d\.\d\d\.2019.*$",
            "2020": r"^NM (.+) de \d\d\.\d\d\.2020.*$",
            "2021": r"^NM (.+) de \d\d\.\d\d\.2021.*$",
            "next": r"^NM (.+) de \d\d\.\d\d\.\d\d\d\d.*$",
        }
        # Editions that can't be extracted using regular expressions (because of absent/wrong info)
        known_edition = {
            "NM 1186 22_-5_2003": "1186",
            "NM 1183 03_042003": "1183",
            "NM 1 a 4 Especial 16_12_2003": "1215 1 a 4 Especial",
            "NM 5 a 8 Especial 17_12_2003": "1215 5 a 8 Especial",
            "NM 2004 1252": "1252",
            "NM 1270 02_01_2002": "1270",
            "NM 1298 11 a 20 08_07_2005.pdf": "1298 11 a 20 ",
            "NM 2012 1701 1 a 9 21_12_2013": "1701 1 a 9",
            "NM 2012 1702 8 a 36.pdf": "1702 8 a 36",
            "NM 2012 1654 37 a 43 27_01_0212": "1654 37 a 43",
            "NM 2012 1698_30_11_12_otz": "1698",
            "NM 2012 1698 Edição Especial_LOA_30_11_2012": "1698 Edição Especial_LOA",
            "NM 1748_08_11_13_Edição especial PPA": "1748 Edição especial PPA",
            "27_02_2015_NM_1817": "1817",
            "NM 1915": "1915",
            "NM LOA 2016_Parte I": "1859 LOA 2016_Parte I",
            "NM LOA 2016_Parte II": "1859 LOA 2016_Parte II",
            "NM LOA 2016_Parte III": "1859 LOA 2016_Parte III",
            "31 12 2016 NM 1915 otz.pdf": "1915",
        }

        text = text.strip()
        if text in known_edition:
            return known_edition[text]

        if year not in re_edition:
            year = "next"
        found = re.findall(re_edition[year], text)
        if len(found) == 0:
            return None
        # Return the first non empty value, or None otherwise
        result = found[0]
        if type(result) is tuple:
            if result[0] != "":
                return result[0]
            elif result[1] != "":
                return result[1]
        elif result != "":
            return result
        return None

    def extract_edition_number(self, edition):
        result = re.findall(r"^ *(\d+)", edition)
        if len(result) == 0:
            return None
        return result[0]

    def extract_date(self, text, year):
        # Regular expressions to extract date for each year
        re_date = {
            "2002": r"^NM 2002 .* (\d\d_\d\d_2002)$",
            "2003": r"^NM .* (\d\d_\d\d_2003)$",
            "2004": r"^NM .* (\d\d_\d\d_2004)$",
            "2005": r"^NM .* (\d\d_\d\d_2005)$",
            "2006": r"^$",
            "2007": r"^$",
            "2008": r"^$",
            "2009": r"^$",
            "2010": r"^$",
            "2011": r"^$",
            "2012": r"^NM 2012 .* (\d\d_\d\d_2012)$",
            "2013": r"^NM .*_(\d\d_\d\d_)13$",
            "2014": r"^(\d\d_\d\d_2014)_NM_.*$",
            "2015": r"^(\d\d_\d\d_2015)_NM_.*$",
            "2016": r"^(\d\d_\d\d_)2?0?16[_ ]NM.*$",
            "2017": r"^NM .* de (\d\d\.\d\d\.2017) .*$",
            "2018": r"^NM .* de (\d\d\.\d\d\.2018) .*$",
            "2019": r"^NM .* de (\d\d\.\d\d\.2019) .*$",
            "2020": r"^NM .* de (\d\d\.\d\d\.2020) .*$",
            "2021": r"^NM .* de (\d\d\.\d\d\.2021) .*$",
        }
        # Dates that can't be extracted using regular expressions (because of wrong info)
        # Format: dd/mm/yyyy
        known_date = {
            "NM 1215 12_11_2003": "12/12/2003",
            "NM 1166 13_12_2003": "03/01/2003",
            "NM 1167 11_12_2003": "10/01/2003",
            "NM 1181 21_04_2003": "17/04/2003",
            "NM 1186 22_-5_2003": "22/05/2003",
            "NM 1183 03_042003": "02/05/2003",
            "NM 1270 02_01_2002": "28/12/2004",
            "NM 1298 11 a 20 08_07_2005.pdf": "08/07/2005",
            "NM 2012 1654 37 a 43 27_01_0212": "27/01/2012",
            "NM 2012 1698 Edição Especial_LOA_30_11_2012": "30/11/2012",
            "NM 2012 1698_30_11_12_otz": "30/11/2012",
            "NM 2012 1701 1 a 9 21_12_2013": "21/12/2012",
            "NM 1748_08_11_13_Edição especial PPA": "08/11/2013",
            "27_02_2015_NM_1817": "27/02/2015",
            "NM 1917 de 06/01/2017 - Conteúdo Integral": "06/01/2017",
            "NM 1916 de 04/01/2017 - Conteúdo Integral": "04/01/2017",
        }

        text = text.strip()
        if text in known_date:
            return datetime.strptime(known_date[text], "%d/%m/%Y").date()

        found = re.findall(re_date[year], text)
        if len(found) == 0:
            return None
        result = found[0]
        if result == "":
            return None
        if year in ("2013", "2016"):
            result = result + year
        result = result.replace(".", "_")
        return datetime.strptime(result, "%d_%m_%Y").date()

    def estimate_date(self, edition):
        # Some verified dates on which the estimation will be based
        # Format: dd/mm/yyyy
        # Edition 1431 is unavailable
        known_date = {
            "1131": "03/05/2002",
            "1181": "17/04/2003",
            "1231": "02/04/2004",
            "1281": "11/03/2005",
            "1331": "24/02/2006",
            "1381": "09/02/2007",
            "1432": "01/02/2008",
            "1481": "02/01/2009",
            "1531": "29/10/2009",
            "1581": "01/10/2010",
            "1631": "19/08/2011",
            "1681": "03/08/2012",
            "1731": "12/07/2013",
            "1781": "16/06/2014",
            "1831": "03/06/2015",
            "1881": "13/05/2016",
            "1931": "12/04/2017",
            "1981": "23/02/2018",
            "2031": "07/12/2018",
            "2081": "13/09/2019",
            "2131": "10/04/2020",
            "2181": "19/11/2020",
        }

        # Find the two editions in "known_date" that are closest to "edition"
        # "edition" can be smaller or greater than any edition in "known_date"
        edition = int(edition)
        ed_list = list(known_date)
        list.sort(ed_list)
        low_ed = ed_list[0]
        high_ed = ed_list[len(ed_list) - 1]
        del ed_list[0]
        del ed_list[len(ed_list) - 1]
        for e in ed_list:
            if int(e) < edition:
                low_ed = e
            else:
                high_ed = e
                break

        # Calculate estimated date from dates of "low_ed" and "high_ed"
        # "rate" is around 7 days per edition
        low_ts = datetime.strptime(known_date[low_ed], "%d/%m/%Y").timestamp()
        high_ts = datetime.strptime(known_date[high_ed], "%d/%m/%Y").timestamp()
        low_ed = int(low_ed)
        high_ed = int(high_ed)
        rate = (high_ts - low_ts) / (high_ed - low_ed)
        estimated_ts = rate * (edition - low_ed) + low_ts
        return date.fromtimestamp(estimated_ts)
