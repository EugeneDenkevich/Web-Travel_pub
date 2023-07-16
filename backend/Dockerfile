FROM python:3-alpine

# For viewing the application's code execution in a real time
ENV PYTHONDONTWRITEBYTECODE 1
# For not creating the .pyc files
ENV PYTHONUNBUFFERED 1

WORKDIR /backend_app

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./check_admin.py ./
COPY ./media/default ./media/default
COPY ./src ./
