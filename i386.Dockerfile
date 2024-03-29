# Build the Frontend
FROM i386/node:latest AS uibuilder

WORKDIR /uibuild

COPY ./frontend /uibuild

RUN yarn install
RUN npm audit fix || true
RUN npm run build


# Dockerfile for DJJoe Calendar App
FROM python:3.9

WORKDIR /server

COPY ./backend /server

# Copy React Files
COPY --from=uibuilder /backend /server

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

# Run Server on localhost:8383 so Nginx can Hit it without Direct Extern. Access
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--log-config", "log_conf.yml"]
