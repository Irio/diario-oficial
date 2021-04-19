from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaVarzeadaRocaSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2933059"
    name = "ba_varzea_da_roca"
    start_urls = ["http://ba.portaldatransparencia.com.br/prefeitura/varzeadaroca/"]
