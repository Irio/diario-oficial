from gazette.spiders.base.portal_da_transparencia import PortalDaTransparenciaBaseSpider


class PrReboucasSpider(PortalDaTransparenciaBaseSpider):
    TERRITORY_ID = "4121505"
    name = "pr_reboucas"
    start_urls = ["http://pr.portaldatransparencia.com.br/prefeitura/reboucas/"]
