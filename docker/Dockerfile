FROM python:3.12.0a7-alpine3.17
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD app.py .
CMD ["python", "app.py"]
