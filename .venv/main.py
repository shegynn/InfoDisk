import os
import psutil

# Получаем информацию о диске
disk_usage = psutil.disk_usage("/")  # "/" - корневой раздел
total_bytes = disk_usage.total
used_bytes = disk_usage.used
free_bytes = disk_usage.free

free_procent = round(free_bytes * 100 / total_bytes, 0)

print(f"Общая емкость: {total_bytes} байт")
print(f"Использовано: {used_bytes} байт")
print(f"Свободно: {free_bytes} байт")
print(f"Использовано {free_procent} %")

print("Test Git")

print("Test Git 2")