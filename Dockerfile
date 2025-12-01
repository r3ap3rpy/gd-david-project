FROM python:3.12-slim
WORKDIR app 
COPY ./flask_app/app.py .
COPY ./flask_app/requirements.txt .
RUN pip install -r requirements.txt
CMD ["python","app.py"]
