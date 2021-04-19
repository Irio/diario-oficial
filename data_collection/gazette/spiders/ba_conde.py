from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaCondeSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2908606"
    name = "ba_conde"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/conde/"]
