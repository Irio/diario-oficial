from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaJaborandiSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2917359"
    name = "ba_jaborandi"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/jaborandi/"]
