FROM python:3.7-alpine
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt
CMD ["python", "run.py"]