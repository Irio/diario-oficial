from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaParamirimSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2923605"
    name = "ba_paramirim"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/paramirim/"]
