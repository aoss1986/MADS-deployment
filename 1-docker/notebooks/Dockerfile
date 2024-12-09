FROM python:3.12-slim

COPY ~/*.toml /src/
COPY /data /src/
COPY /img /src/
COPY /ingest.ipynb /src/

WORKDIR /src

EXPOSE 9000

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=9000", "--no-browser", "--allow-root"]