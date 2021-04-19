from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaIbitiaraSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2913002"
    name = "ba_ibitiara"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/ibitiara/"]
