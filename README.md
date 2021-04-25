# Diário Oficial

**Diário Oficial** is the Brazilian government gazette, one of the best places to know the latest actions of the public administration, with distinct publications in the federal, state and municipal levels.

Even with recurrent efforts of enforcing the [Freedom of Information legislation](http://www.acessoainformacao.gov.br/assuntos/conheca-seu-direito/principais-aspectos/principais-aspectos) across the country, official communication remains - in most of the territories - in PDFs.

The goal of this project is to upgrade **Diário Oficial** to the digital age, centralizing information currently only available through separate sources.

When this project was initially released, had two distinct goals: creating crawlers for government gazettes and parsing bidding exemptions from them. Now going forward, it is limited to the first objective.

Table of Contents
=================
  * [Development environment](#development-environment)
    * [Run Gazette Crawler](#run-gazette-crawler)
    * [Generate multiple spiders from template](#generate-multiple-spiders-from-template)
  * [Contributing](#contributing)
  * [Acknowledgments](#acknowledgments)

## Development environment

The best way to understand how **Querido Diário** works is to get the source
and run it locally. All crawlers are developed using [Scrapy](https://scrapy.org)
framework. They provide a [tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
so you can learn to use it.

If you are on a Windows computer, before you run the steps below you will need Microsoft Visual Build Tools (download [here](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/)). When you start the installation you need to select 'C++ build tools' on the Workload tab and also 'Windows 10 SDK' and 'MSVC v142 - VS 2019 C++ x64/x86 build tools' on the Individual Components tab.

If you are in a Linux-like environment, the following commands will create a new
[virtual environment](https://docs.python.org/3/library/venv.html) - that will keep
everything isolated from your system - activate it and install all libraries needed
to start running and developing new spiders.

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r data_collection/requirements.txt
$ pre-commit install
```

On a Windows computer, you can use the code above. You just need to substitute ```source .venv/bin/activate ``` for ```.venv/Scripts/activate.bat```. The rest is the same as in Linux.

### Run inside a container

You can run inside a container using [podman](https://podman.io/getting-started/).
Before get inside this container you need start environment as explainedZ
[setup instructions](https://github.com/okfn-brasil/querido-diario-data-processing#setup).

After that, get inside de container:
```console
$ make shell_run
```

Now you can follow below instructions for populate data

### Run Gazette Crawler

After configuring your environment, you will be able to execute and develop new spiders.
The Scrapy project is in the `data_collection` directory, so you must enter it to execute the
spiders and the `scrapy` command:

```console
$ cd data_collection
```

Following we list some helpful commands.

Get the list of all available spiders:

```console
$ scrapy list
```

Execute spider with name `spider_name`:

```console
$ scrapy crawl spider_name
```

You can limit the gazettes you want to download by passing `start_date` as an argument with the `YYYY-MM-DD` format. The
following command will download only gazettes whose date is greater than 01/Sep/2020:

```console
$ scrapy crawl sc_florianopolis -a start_date=2020-09-01
```

### Generate multiple spiders from template

You may end up in a situation where you have different cities using the same spider base,
such as `FecamGazetteSpider`. To avoid creating the spider files manually, you can use a script
for cases where we have a few spiders that are not complex and from the same spider base.

The spider template lives in the `scripts/` folder. Here an example of a generated spider:

```
from datetime import date
from gazette.spiders.base import ImprensaOficialSpider


class BaGentioDoOuroSpider(ImprensaOficialSpider):

    name = "ba_gentio_do_ouro"
    allowed_domains = ["pmGENTIODOOUROBA.imprensaoficial.org"]
    start_date = date(2017, 2, 1)
    url_base = "http://pmGENTIODOOUROBA.imprensaoficial.org"
    TERRITORY_ID = "2911303"
```

To run the script, you only need a CSV file following the structure below:

```
url,city,state,territory_id,start_day,start_month,start_year,base_class
http://pmXIQUEXIQUEBA.imprensaoficial.org,Xique-Xique,BA,2933604,1,1,2017,ImprensaOficialSpider
http://pmWENCESLAUGUIMARAESBA.imprensaoficial.org,Wenceslau Guimarães,BA,2933505,1,1,2017,ImprensaOficialSpider
http://pmVERACRUZBA.imprensaoficial.org,Vera Cruz,BA,2933208,1,4,2017,ImprensaOficialSpider
```

Once you have the CSV file, run the command:

```
cd scripts/

python generate_spiders.py new-spiders.csv
```

That's it. The new spiders will be in the directory `data_collection/gazette/spiders/`.

## Troubleshooting

### `Python.h` missing

While running `pip install` command, you can get an error like this one below:

```
module.c:1:10: fatal error: Python.h: No such file or directory
     #include <Python.h>
              ^~~~~~~~~~
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
```

Please try to install `python3-dev`. E.g. via `apt install python3-dev`, if you
are using a Debian-like distro, or use your distro manager package. Make sure that
you use the correct version (e.g. `python3.6-dev` or `python3.7-dev`). You can
check your version via `python3 --version`.

## Contributing

If you are interested in fixing issues and contributing directly to the code base, please see the document [CONTRIBUTING.md](CONTRIBUTING.md).

## Acknowledgments

This project is maintained by Open Knowledge Foundation Brasil, thanks to the support of Digital Ocean and [hundreds of other names](https://serenata.ai/en/about/).
