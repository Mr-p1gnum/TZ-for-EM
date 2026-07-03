FROM python:3.12-alpine

WORKDIR /app

COPY app.py .

EXPOSE 8080

RUN addgroup -S backendgroup && adduser -S backenduser -G backendgroup &&\
chown -R backenduser:backendgroup /app

USER backenduser

CMD ["python", "app.py"]