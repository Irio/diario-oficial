from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class PeIpubiSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2607307"
    name = "pe_ipubi"
    start_urls = ["http://pe.portaldatransparencia.com.br/prefeitura/ipubi/"]
