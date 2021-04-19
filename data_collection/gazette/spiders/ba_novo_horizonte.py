from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaNovoHorizonteSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2923035"
    name = "ba_novo_horizonte"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/novohorizonte/"]
