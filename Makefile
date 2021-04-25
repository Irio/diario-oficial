ISORT_ARGS := --combine-star --combine-as --order-by-type --thirdparty scrapy --multi-line 3 --trailing-comma --force-grid-wrap 0 --use-parentheses --line-width 88

SRC_DIRS := ./data_collection

IMAGE_NAMESPACE ?= serenata
IMAGE_NAME ?= querido-diario
IMAGE_TAG ?= latest
POD_NAME ?= run-querido-diario-data-extraction

check:
	python3 -m isort --check --diff $(ISORT_ARGS) $(SRC_DIRS)
	python3 -m black --check $(SRC_DIRS)
	flake8 $(SRC_DIRS)

format:
	python3 -m isort --apply $(ISORT_ARGS) $(SRC_DIRS)
	python3 -m black $(SRC_DIRS)

run_spider:
	cd $(SRC_DIRS) && scrapy crawl $(SPIDER)

sql:
	cd $(SRC_DIRS) && sqlite3 querido-diario.db

clean:
	find ./$(SRC_DIRS)/data/* -type d -exec rm -rv {} \;

shell:
	cd $(SRC_DIRS) && scrapy shell

run_spider_since:
	cd $(SRC_DIRS) && scrapy crawl -a start_date=$(START_DATE) $(SPIDER)

shell_build:
	podman build --tag $(IMAGE_NAMESPACE)/$(IMAGE_NAME):$(IMAGE_TAG) -f ./Dockerfile-shell

shell_run: shell_build
	cp --no-clobber contrib/sample.env .env
	podman run --rm -ti \
	    --volume $(PWD)/data_collection:/mnt/code/data_collection:ro \
		--pod $(POD_NAME) \
		--env-file .env \
		--user=$(UID):$(UID) $(IMAGE_NAMESPACE)/$(IMAGE_NAME):$(IMAGE_TAG)
