# docker build -t test_dynaconf:latest .


FROM python:3.10.11 AS builder

WORKDIR /app

COPY . /app

# Install dependencies and build application
RUN python -m pip install -r requirements.txt
RUN python -m pip install pyinstaller
RUN pyinstaller --onefile --name app.exe main.py

# ---

FROM frolvlad/alpine-glibc:latest

# Set a working directory inside the container
WORKDIR /app

# install packages
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt

# Copy app
# COPY *.py .
# COPY *.yaml .

COPY --from=builder /app/settings.yaml .
COPY --from=builder /app/dist/app.exe .
RUN chmod +x app.exe

# Define the command to run your application when the container starts
# CMD ["python", "main.py"]
CMD ["./app.exe"]
