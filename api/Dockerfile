FROM tiangolo/uwsgi-nginx:python3.8-alpine

ADD . /home/api/
WORKDIR /home/api/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python app.py