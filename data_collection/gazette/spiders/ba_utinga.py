from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaUtingaSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2932804"
    name = "ba_utinga"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/utinga/"]
