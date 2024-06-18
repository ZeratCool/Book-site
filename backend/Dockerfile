FROM python:3.11-alpine

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash backend && chmod 777 /opt /run

WORKDIR /backend
COPY --chown=backend:backend . .

ADD requirements.txt /backend/

ADD .env.docker /backend/.env

RUN  mkdir /backend/media && chown -R backend:backend /backend && chmod 755 /backend

RUN apk add --update --no-cache -- virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev && \
    pip install --no-cache-dir -r requirements.txt

USER backend

CMD python manage.py migrate \
    && python
