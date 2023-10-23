# Use the official Python 3.8 image as the base
FROM python:3.8

# Install libffi-dev to fix compilation issues
# RUN apt-get update && \
#     apt-get install -y libffi-dev

# Set a working directory for your application
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and activate a virtual environment
RUN python -m venv venv
RUN . venv/bin/activate

# Install your project's dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy your project files into the container
COPY . .

# Define the command to run your application
# CMD ["gunicorn", "cf.wsgi:application", "--bind", "0.0.0.0:8011"]
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]


# # pull official base image
# FROM python:3.8-alpine

# # set work directory
# WORKDIR /usr/src/app

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # RUN apk add libffi-dev gcc

# # install dependencies
# RUN pip install --upgrade pip
# # RUN pip install --upgrade setuptools
# # RUN pip install --upgrade cffi
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt


# # copy entrypoint.sh
# COPY ./entrypoint.sh .
# RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
# RUN chmod +x /usr/src/app/entrypoint.sh

# # copy project
# COPY . .

# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]