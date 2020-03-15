FROM python:3.8

ADD . /Wartsila/charts_analyzier

WORKDIR /Wartsila/charts_analyzier

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin wait-for-it && pip install --no-cache-dir -r requirements.txt

CMD wait-for-it localhost:5432 -s -- python manage.py migrate && python manage.py runserver
