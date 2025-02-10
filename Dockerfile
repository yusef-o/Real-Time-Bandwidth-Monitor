FROM python:3.12

ADD bandwidthMonitor.py . 

CMD ["python", "./bandwidthMonitor.py"]
