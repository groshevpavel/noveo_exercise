FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

# install requirements
COPY Pipfile.lock Pipfile ./
RUN pip install -U pip pipenv && pipenv install --system --deploy --ignore-pipfile --dev

# Add project files
COPY . .

RUN chmod +x ./entrypoint.sh

# Create directory for logs and coverage report
RUN mkdir -p /usr/src/app/logs \
    && mkdir -p /usr/src/app/tests/coverage \
    && chmod -R 777 /usr/src/app/logs \
    && chmod -R 777 /usr/src/app/tests/coverage

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]