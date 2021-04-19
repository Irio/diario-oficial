from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class BaSantaRitadeCassiaSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "2928406"
    name = "ba_santa_rita_de_cassia"
    start_urls = [
        "http://ba.portaldatransparencia.com.br/prefeitura/santaritadecassia/"
    ]
