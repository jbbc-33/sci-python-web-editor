FROM python:3.10-bullseye

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libatlas-base-dev \
    gfortran \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir numpy pandas matplotlib scipy pillow

ENV MPLBACKEND=Agg

WORKDIR /app
COPY run.py /app/run.py

CMD ["python", "run.py"]