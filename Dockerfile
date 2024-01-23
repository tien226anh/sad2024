FROM python:3.12.0

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=anh_proj1.settings

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "sh", "-c", "python manage.py migrate && python manage.py runserver" ]