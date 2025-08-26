# docker build -t test_dynaconf:latest .

FROM python:3.10.11

# Set a working directory inside the container
WORKDIR /app

# install packages
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Copy app
COPY *.py .
COPY *.yaml .

# Define the command to run your application when the container starts
CMD ["python", "main.py"]
