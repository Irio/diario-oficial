from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class RsPintoBandeiraSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "4314548"
    name = "rs_pinto_bandeira"
    start_urls = ["http://rs.portaldatransparencia.com.br/prefeitura/pintobandeira/"]
