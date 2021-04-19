from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class SpDoisCorregosSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "3514106"
    name = "sp_dois_corregos"
    start_urls = ["http://sp.portaldatransparencia.com.br/prefeitura/doiscorregos/"]
