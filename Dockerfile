FROM python:3.11
LABEL name="WisemenPokedex" \
    version="0.1.0" \
    summary="Pokedex API for Wisemen"\
    description="Pokedex API built using django for Wisemen"

RUN apt-get -y update && apt-get -y upgrade && apt-get -y clean && apt-get -y autoclean && apt-get -y autoremove
RUN mkdir -p wisemen
COPY . /wisemen

WORKDIR /wisemen
RUN set -ex \
    # Install poetry
    && pip3 install -U pip poetry \
    && poetry install --no-interaction --no-ansi \
    && poetry install
RUN
CMD ["poetry", "run", "python", "manage.py", "runserver"]
EXPOSE 8000