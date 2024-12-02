build:
	docker build -t mads-ingest -f ingest/ingest.Dockerfile .
	docker build -t mads-preprocess -f preprocess/preprocess.Dockerfile .
	docker build -t mads-model -f model/serve.Dockerfile .

run:
	docker run \
		-v ./data:/app/data \
		-v ./logs:/app/logs mads-ingest
	docker run \
		-v ./data:/app/data \
		-v ./logs:/app/logs mads-preprocess
	docker run \
		-v ./data:/app/data \
		-v ./logs:/app/logs \
		-p 8000:8000 \
		mads-model

clean:
	rm -rf data/*

