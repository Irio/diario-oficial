Spider writing guidelines
=========================

Before start working on a spider, read carefully the following guidelines that will make the project more consistent and your PR more probable to be accepted.

Reading code of existing spiders will also help you to understand how to develop.

Spider class
------------

- All spiders must inherit from `BaseGazetteSpider`
- Class name must follow the pattern `<State><CityName>Spider` (for example `SpSaoPauloSpider` or `MtFelizNatalSpider`)
- Spider `name` must follow the pattern `<state>_<city_name>` (for example `sp_sao_paulo` or `mt_feliz_natal`)
- Add `TERRITORY_ID` attribute with the code found in `territories.csv` file
- Add `start_date` attribute containing the date of the first gazette available

Example initial spider:
```
from datetime import date
from gazette.spiders.base import BaseGazetteSpider

class SpJundiaiSpider(BaseGazetteSpider):
    TERRITORY_ID = "3525904"
    name = "sp_jundiai"
    allowed_domains = ["jundiai.sp.gov.br"]
    start_urls = ["https://imprensaoficial.jundiai.sp.gov.br/"]
    start_date = date(2000, 1, 1)

    def parse(self, response):
        # Here we have all parsing logic
```

Field definitions
-----------------

These are the information that we need to extract for each gazette:

- **date (datetime.date)**: publication date
- **edition_number (string)**: edition number of gazette
- **is_extra_edition (boolean)**: some gazettes are extra editions. You can identify them when they have words like *Extra*, *Extraordinário*, *Suplemento*, etc. If unable to identify, return as `False`
- **territory_id (string)**: value of `TERRITORY_ID` spider attribute
- **power (string)**: if the gazette refers to Executive power, Legislative or both (`executive`, `legislative`, `executive_legislative`)
- **scraped_at (datetime.datetime)**: fixed to `datetime.datetime.utcnow()`
- **file_urls (URL list)**: list of URLs to download the gazettes (usually we will have just one value here)

Date filtering
--------------

We want all spiders to be able to retrieve **ALL** available gazettes. But we also want to be able to restrict the amount of data we retrieve. To achieve that we have `start_date` attribute that will help filtering.

By default this attribute must have the date of the first gazette available in the site (hard-coded). But we can change that between executions passing the desired date as argument. The following command should return only gazettes after 01/Sep/2020:

`scrapy crawl my_spider -a start_date=2020-09-01`

When developing a spider, try to make **as few requests as possible**. Some pages allows you to filter the results passing date information, so use `start_date` information in your favour.

Before submitting a PR
----------------------

**RUN THE SPIDER IN YOUR DEVELOPMENT ENVIRONMENT AND WAIT UNTIL IT FINISHES ITS EXECUTION!**

Before submitting a new PR for your spider, make sure that it is running properly:

- Check if the downloaded files are valid;
- Check if you are getting all expected gazettes;
- Check if when you specify a `start_date` you are not collecting more gazettes than expected;
- Check if you run the spider twice, the results are the same;
- Check for ERRORS in spider stats
- ...

