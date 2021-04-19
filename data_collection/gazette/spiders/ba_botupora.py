from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaBotuporaSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2904209"
    name = "ba_botupora"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/botupora/"]
