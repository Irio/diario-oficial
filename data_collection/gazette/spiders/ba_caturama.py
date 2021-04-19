from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaCaturamaSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2907558"
    name = "ba_caturama"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/caturama/"]
