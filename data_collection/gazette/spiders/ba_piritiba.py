from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaPiritibaSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2924801"
    name = "ba_piritiba"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/piritiba/"]
