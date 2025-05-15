FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy semua file
COPY . .

# Install dependency
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Menjalankan API dengan gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
