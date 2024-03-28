FROM python:3.8
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade --index-url https://p-nexus-3.development.nl.eu.abnamro.com:8443/repository/python-group/simple -r /code/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY ./app /code/app
COPY ./employee_attrition_model /code/employee_attrition_model
CMD ["uvicorn", "app.main:app"]