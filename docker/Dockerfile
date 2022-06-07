FROM python:3.8

RUN mkdir /podrostoc
ADD requirements.txt /podrostoc
ADD test_requirements.txt /podrostoc
RUN pip3 install -r /podrostoc/requirements.txt -r /podrostoc/test_requirements.txt
ADD src /podrostoc/src
ADD tests /podrostoc/tests
