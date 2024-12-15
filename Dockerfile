FROM python:3.12-bullseye
ENV PYTHONUNBUFFERED=1

# Loo koodikaust
RUN mkdir /code
WORKDIR /code

#Kopeeri requirements.txt ja requirements-dev.txt
COPY requirements.txt ./

# Paigalda põhja ja arenduse sõltuvused
RUN pip install --no-cache-dir -r requirements.txt

# Kopeeri kogu projektikood konteinerisse
COPY . /code/

# Ava pordid
EXPOSE 8000

# Käivita Django arenguserver
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
