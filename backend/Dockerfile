FROM python:3.10-bullseye

# Dependencias del sistema para numpy, pandas, matplotlib
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libatlas-base-dev \
    gfortran \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python
RUN pip install --no-cache-dir numpy pandas matplotlib pillow flask

# Matplotlib sin interfaz gráfica
ENV MPLBACKEND=Agg

WORKDIR /app

# Copiar todo el backend
COPY . /app

# Exponer puerto
EXPOSE 5000

# Ejecutar el servidor
CMD ["python", "server.py"]
