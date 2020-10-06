# Diário Oficial

**Diário Oficial** is the Brazilian government gazette, one of the best places to know the latest actions of the public administration, with distinct publications in the federal, state and municipal levels.

Even with recurrent efforts of enforcing the [Freedom of Information legislation](http://www.acessoainformacao.gov.br/assuntos/conheca-seu-direito/principais-aspectos/principais-aspectos) across the country, official communication remains - in most of the territories - in PDFs.

The goal of this project is to upgrade **Diário Oficial** to the digital age, centralizing information currently only available through separate sources.

When this project was initially released, had two distinct goals: creating crawlers for governments gazettes and parsing bidding exemptions from them. Now going forward, it is limited to the first objective.

Table of Contents
=================
  * [Build and Run](#build-and-run)
     * [Run Gazette Crawler](#run-gazette-crawler)
  * [Tips and tricks](#tips-and-tricks)
  * [Troubleshooting](#troubleshooting)
     * ["Permission denied" error when files are downloaded](#permission-denied-error-when-files-are-downloaded)
  * [Contributing](#contributing)
  * [Acknowledgments](#acknowledgments)

## Build and Run

If you want to understand how Diário Oficial works, you'll want to get the source, build it, and run it locally.

The only prerequisites are [Docker](https://www.docker.com) and [Docker Compose](https://docs.docker.com/compose/overview/), which are the tools responsible for installing all the other dependencies.

After you cloned the repository, you may want to run the following from the source folder:

```console
$ make setup
$ docker-compose up
```

### Run Gazette Crawler

The gazettes spiders are written using Scrapy framework and must be executed with crawl command: `scrapy crawl <spider filename>`.
However, it's recommended to use the processing container for that: `docker-compose run --rm processing <command>`.
The following example is the command to run the gazette crawler for Florianópolis/SC:

```console
$ docker-compose run --rm processing bash -c "cd data_collection && scrapy crawl sc_florianopolis"
```

You can limit the gazettes you want to download passing `start_date` as argument with `YYYY-MM-DD` format. The
following command will download only gazettes which date is greater than 01/Sep/2020:

```console
$ docker-compose run --rm processing bash -c "cd data_collection && scrapy crawl sc_florianopolis -a start_date=2020-09-01"
```

## Tips and tricks

There is a make target allowing you run the scrapy shell inside the container used by the crawler:

```bash
make shell
```

There is another make target allowing you run access the PostgreSQL database:

```bash
make sql
```

You need the password to access the database. You can find it in the .env file.

You can also run the spider with some less key strokes. The following make target
allows you to run the spider. It calls the same command of the docker compose 
described in the documentation:

```bash
SPIDER=sc_florianopolis make run_spider
```

## Troubleshooting

### "Permission denied" error when files are downloaded

This problem most probably occurs due to a mismatch between your system's user id and the container's user id and there is a volume in place connecting both file systems (that's the default case here).

Run this command in your system's terminal to get your user's id:

```console
$ id -u
```

Copy the output, replace the value of the environment variable `LOCAL_USER_ID` in the generated `.env` file with the copied value and execute `docker-compose build`. With the image rebuilt you are ready to go.

To save yourself this effort in the future, you can replace the value of `LOCAL_USER_ID` in `.env.example` too and `.env` will already be generated with the correct value for it when `make setup` is executed.

## Contributing

If you are interested in fixing issues and contributing directly to the code base, please see the document [CONTRIBUTING.md](CONTRIBUTING.md).

## Acknowledgments

This project is maintained by Open Knowledge Foundation Brasil, thanks to the support of Digital Ocean and [hundreds of other names](https://serenata.ai/en/about/).
