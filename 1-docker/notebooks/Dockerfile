FROM python:3.12-slim

COPY /home/andres/so3_mads/deployment/MADS-deployment/*.toml /src/
COPY /home/andres/so3_mads/deployment/MADS-deployment/1-docker/notebooks/data /src/
COPY /home/andres/so3_mads/deployment/MADS-deployment/1-docker/notebooks/img /src/
COPY /home/andres/so3_mads/deployment/MADS-deployment/1-docker/notebooks/ingest.ipynb /src/

WORKDIR /src

EXPOSE 9000

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=9000", "--no-browser", "--allow-root"]