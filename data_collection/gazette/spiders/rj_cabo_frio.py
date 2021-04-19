from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class RjCaboFrioSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "3300704"
    name = "rj_cabo_frio"
    start_urls = ["http://rj.portaldatransparencia.com.br/prefeitura/cabofrio/"]
