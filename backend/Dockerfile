FROM python:3.10


RUN mkdir /app
WORKDIR /app

# gdal for GeoDjango
RUN apt-get update && apt-get install -y \
    binutils \
    gdal-bin \
    libproj-dev \
    git \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]