# Используем официальный образ Python 3.10
FROM python:3.10

# Обновляем систему и устанавливаем необходимые зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        g++ \
        libatlas-base-dev \
        python3-dev \
        && \
    rm -rf /var/lib/apt/lists/*

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем requirements.txt отдельно для кэширования слоя
COPY requirements.txt .

# Устанавливаем pip и зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Если ты качаешь файлы при старте — раскомментируй:
# RUN python download_files.py

# Команда запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
