from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class ApTartarugalzinhoSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "1600709"
    name = "ap_tartarugalzinho"
    start_urls = ["http://ap.portaldatransparencia.com.br/prefeitura/tartarugalzinho/"]
