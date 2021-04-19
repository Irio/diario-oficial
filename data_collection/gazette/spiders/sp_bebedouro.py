from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class SpBebedouroSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "3506102"
    name = "sp_bebedouro"
    start_urls = ["http://sp.portaldatransparencia.com.br/prefeitura/bebedouro/"]
