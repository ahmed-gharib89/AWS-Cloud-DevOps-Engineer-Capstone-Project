FROM python:3.8.8-slim-buster

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY requirements.txt /app/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Copy source code to working directory
COPY ./urlshort/ /app/urlshort

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "urlshort/app.py" ]
