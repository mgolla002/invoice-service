FROM python:3.12-slim
ARG BUILD_NUMBER=dev
ENV APP_VERSION=$BUILD_NUMBER
WORKDIR /app
COPY wheels ./wheels
RUN pip install --no-cache-dir --no-index --find-links=wheels invoice-service gunicorn
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "invoice.main:app"]