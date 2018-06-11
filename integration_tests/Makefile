IMAGE_NAME=alpacadb/test:v0.0.1
CONTAINER_NAME=integtest

DOCKER_CMD=tail -f /dev/null
DOCKER_OPTS=--net host

build:
	docker build -t $(IMAGE_NAME) .

pull:
	docker pull $(IMAGE_NAME)

rm:
	docker rm -f $(CONTAINER_NAME) || echo

run:
	docker run $(DOCKER_OPTS) \
		-d --name $(CONTAINER_NAME) $(IMAGE_NAME) $(DOCKER_CMD)

bash:
	docker exec -i -t $(CONTAINER_NAME) bash


################################################################################
# Tests
################################################################################

reset_marketstore:
	$(MAKE) -C marketstore rm run
	echo Waiting initialization of marketstore
	sleep 5


testohlcv: reset_marketstore
	docker exec -i -t $(CONTAINER_NAME) bash -c \
		"pytest -v -v -v test_ohlcv.py"
