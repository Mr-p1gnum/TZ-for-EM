FROM python:3.12-alpine

WORKDIR /app

COPY server.py .

EXPOSE 8080

RUN addgroup -S backendgroup && adduser -S backenduser -G backendgroup &&\
chown -R backenduser:backendgroup /app

USER backenduser

CMD ["python", "server.py"]