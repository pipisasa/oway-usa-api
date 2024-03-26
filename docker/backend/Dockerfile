FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
ADD ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN pip install psycopg2-binary
ADD ./docker /app/docker
ADD ./ /app
EXPOSE 8000