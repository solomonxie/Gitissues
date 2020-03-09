build:
	docker build --no-cache -t solomonxie/gitissues-docker:latest .

run:
	docker run -dt --always solomonxie/gitissues-docker:latest
