FROM python:3.11.4-bullseye

# For viewing the application's code execution in a real time
ENV PYTHONDONTWRITEBYTECODE 1
# For not creating the .pyc files
ENV PYTHONUNBUFFERED 1

WORKDIR /backend_app

COPY ./requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools wheel
RUN pip3 install -r requirements.txt

COPY ./Makefile ./
COPY ./src ./

CMD ["make", "create_env_file"]