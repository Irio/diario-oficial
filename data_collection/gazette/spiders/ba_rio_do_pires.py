from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaRiodoPiresSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2926905"
    name = "ba_rio_do_pires"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/riodopires/"]
