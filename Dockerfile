FROM python:3.9
RUN pip install prometheus_client
COPY metrics_app/metrics.py .
CMD ["python", "metrics.py"]
