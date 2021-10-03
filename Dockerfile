# Dockerfile for DJJoe Calendar App
FROM python:3.9

WORKDIR /server

COPY ./backend /server/app

RUN pip install --no-cache-dir --upgrade -r /server/app/requirements.txt

# Run Server on localhost:8383 so Nginx can Hit it without Direct Extern. Access
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8383", "--log-config", "app/log_conf.yml"]
