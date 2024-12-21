# Используем базовый образ Ubuntu
FROM ubuntu:20.04

# Устанавливаем переменные среды для минимального взаимодействия с пользователем
ENV DEBIAN_FRONTEND=noninteractive

# Обновляем пакеты и устанавливаем Python и необходимые библиотеки
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-tk \
    x11-xserver-utils \
    xvfb \
    && apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY project/ /app/

# Печатаем структуру каталогов, чтобы проверить, что все файлы скопированы
RUN ls -R /app

# Создаем структуру для deb-пакета
RUN mkdir -p /build/calculator/DEBIAN \
    && mkdir -p /build/calculator/usr/local/bin \
    && cp /app/main.py /build/calculator/usr/local/bin/calculator \
    && chmod +x /build/calculator/usr/local/bin/calculator \
    && echo "Package: calculator\nVersion: 1.0.0\nSection: utils\nPriority: optional\nArchitecture: all\nEssential: no\nMaintainer: Евгений <your_email@example.com>\nDescription: A simple calculator with advanced functions written in Python.\n This package provides a Tkinter-based GUI calculator." > /build/calculator/DEBIAN/control


# Собираем deb-пакет
RUN dpkg-deb --build /build/calculator

# Копируем deb-пакет в доступное место
RUN mv /build/calculator.deb /app/calculator.deb

# Открываем порт для приложения
EXPOSE 5000

# Команда для запуска приложения
#CMD ["python3", "/app/main.py"]
CMD xvfb-run --server-args="-screen 0 1024x768x24" python3 /app/main.py
