build:
	cp ~/.ssh/id_rsa* ./
	docker build . -t solomonxie/gitissues-docker:latest
	rm -f ./id_rsa*

run:
	docker rm -f gitissues |true
	sh envgen.sh
	docker run -dt --name gitissues --restart always \
		--env-file=/tmp/env.txt -v ${PWD}:/Gitissues \
		solomonxie/gitissues-docker:latest
	rm /tmp/env.txt

into:
	docker exec -it gitissues /bin/sh
