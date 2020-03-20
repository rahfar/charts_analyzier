FROM python:3.8

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin wait-for-it 

ADD ./requirements.txt /Wartsila/charts_analyzier/

WORKDIR /Wartsila/charts_analyzier

RUN pip install --no-cache-dir -r requirements.txt

ADD . /Wartsila/charts_analyzier

ENTRYPOINT wait-for-it db:5432 -s -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000
