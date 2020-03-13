FROM python:3.8

ADD . /Wartsila/charts_analyzier

WORKDIR /Wartsila/charts_analyzier

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin && pip install --no-cache-dir -r requirements.txt

CMD sleep 5 && python manage.py runserver
