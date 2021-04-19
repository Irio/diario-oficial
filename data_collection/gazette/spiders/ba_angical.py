from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaAngicalSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2901403"
    name = "ba_angical"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/angical/"]
