IMAGE_NAME=binrop/marketstore:latest
CONTAINER_NAME=marketstore

# DATA_DIR ?= $(MAKEFILE_PATH)/data
DOCKER_CMD=marketstore -config /tmp/mkts_config.yaml
DOCKER_OPTS=--net host

build:
	docker build -t $(IMAGE_NAME) .

pull:
	docker pull $(IMAGE_NAME)

rm:
	docker rm -f $(CONTAINER_NAME) || echo

run:
	docker run $(DOCKER_OPTS) \
		-v $(CURDIR)/mkts_config.yaml:/tmp/mkts_config.yaml \
		-v $(CURDIR):/marketstore \
		-d --name $(CONTAINER_NAME) $(IMAGE_NAME) $(DOCKER_CMD)

bash:
	docker exec -i -t $(CONTAINER_NAME) bash

ls:
	docker exec -i -t $(CONTAINER_NAME) ls -lR /project/data/mktsdb


################################################################################
# DB
################################################################################

loaddb:
	docker run $(DOCKER_OPTS) -it \
		$(IMAGE_NAME) \
		/project/dockerfiles/marketstore/loaddb.sh \
		https://s3.amazonaws.com/dev.alpaca.markets/gobroker/mktsdb.tar.gz

resetdb:
	docker exec -i -t $(CONTAINER_NAME) /marketstore/resetdb.sh



################################################################################
# Import ticks
################################################################################
# e.g. TEST_NUM=1
import_csv:
	docker exec -i -t $(CONTAINER_NAME) bash -c "/project/tick/$(TEST_NUM)/load_csv.sh"
