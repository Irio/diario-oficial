from datetime import date

from gazette.spiders.base.imprensa_oficial import ImprensaOficialSpider


class BaSapeacuSpider(ImprensaOficialSpider):

    name = "ba_sapeacu"
    allowed_domains = ["pmSAPEACUBA.imprensaoficial.org", "sapeacu.ba.gov.br"]
    start_date = date(2017, 1, 1)
    url_base = "http://sapeacu.ba.gov.br/{}"
    TERRITORY_ID = "2929602"
