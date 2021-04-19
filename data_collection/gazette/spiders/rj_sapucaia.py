from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class RjSapucaiaSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "3305406"
    name = "rj_sapucaia"
    start_urls = ["http://rj.portaldatransparencia.com.br/prefeitura/sapucaia/"]
