from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaWanderleySpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2933455"
    name = "ba_wanderley"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/wanderley/"]
