FROM python:3.8


RUN mkdir /podrostoc
RUN pip3 install --no-cache-dir poetry

ADD pyproject.toml /podrostoc
RUN poetry config virtualenvs.create false
WORKDIR /podrostoc
RUN cd /podrostoc ; poetry install

ADD podrostoc /podrostoc/podrostoc
ADD tests /podrostoc/tests
ENV PYTHONPATH /podrostoc/:/podrostoc/tests:/podrostoc/podrostoc/