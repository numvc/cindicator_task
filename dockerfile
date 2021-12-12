FROM python:3.8-slim-buster
ADD solution.py /
RUN pip install pandas
RUN pip install bta-lib
RUN pip install binance-connector
ENTRYPOINT [ "python", "./solution.py"]