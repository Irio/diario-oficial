from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaVarzeadoPocoSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2933109"
    name = "ba_varzea_do_poco"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/varzeadopoco/"]
