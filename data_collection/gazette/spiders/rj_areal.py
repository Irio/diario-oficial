from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class RjArealSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "3300225"
    name = "rj_areal"
    start_urls = ["http://rj.portaldatransparencia.com.br/prefeitura/areal/"]
