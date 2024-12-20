# Используем базовый образ Ubuntu
FROM ubuntu:20.04

# Устанавливаем переменные среды для минимального взаимодействия с пользователем
ENV DEBIAN_FRONTEND=noninteractive

# Обновляем пакеты и устанавливаем Python и необходимые библиотеки
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-tk \
    && apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости из requirements.txt
#RUN pip3 install --no-cache-dir -r requirements.txt

# Открываем порт для приложения
EXPOSE 5000

# Команда для запуска приложения
CMD ["python3", "main.py"]
