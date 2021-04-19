from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaSantaMariadaVitoriaSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2928109"
    name = "ba_santa_maria_da_vitoria"
    start_urls = [
        "http://ba.portaldatransparencia.com.br/prefeitura/santamariadavitoria/"
    ]
