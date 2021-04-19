from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class RjComendadorLevyGasparianSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "3300951"
    name = "rj_comendador_levy_gasparian"
    start_urls = [
        "http://rj.portaldatransparencia.com.br/prefeitura/comendadorlevygasparian/"
    ]
