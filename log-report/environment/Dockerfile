FROM python:3.11-slim
WORKDIR /app
# Installing pytest and the CTRF plugin
RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5
COPY access.log /app/access.log
COPY instruction.md /app/instruction.md