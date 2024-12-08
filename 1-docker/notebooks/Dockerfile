FROM apache/beam_python3.12_sdk:2.32.0

COPY /home/andres/so3_mads/deployment/MADS-deployment/*.toml /src/
COPY /home/andres/so3_mads/deployment/MADS-deployment/1-docker/notebooks/data /src/
COPY notebooks/1.ingest.ipynb /src/

WORKDIR /src

EXPOSE 9000

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=9000", "--no-browser", "--allow-root"]