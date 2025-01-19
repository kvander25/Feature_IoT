import os
import time

# Пороговые значения
MOISTURE_THRESHOLD = 40  # Влажность почвы меньше 40% 
TEMP_THRESHOLD = 30  # Температура больше 30°C требует включения вентилятора

soil_moisture_file = 'soil_moisture.txt'
pump_state_file = 'pump_state.txt'
temperature_file = 'temperature.txt'
fan_state_file = 'fan_state.txt'
light_file = 'light.txt'

#Чтение данных из файла
def read_sensor_data(file_path): 
    try:
        with open(file_path, 'r') as file:
            return float(file.read().strip())
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    
# Запись состояния устройства (например, насоса или вентилятора) в файл
def write_device_state(file_path, state):
    with open(file_path, 'w') as file:
        file.write(str(state))

# Контроль за поливом
def control_pump(soil_moisture):
    if soil_moisture < MOISTURE_THRESHOLD:
        write_device_state(pump_state_file, 1)  # Включить насос
        print("Включен насос для полива.")
    else:
        write_device_state(pump_state_file, 0)  # Выключить насос
        print("Насос выключен.")
        
# Контроль за вентилятором
def control_fan(temperature):
    if temperature > TEMP_THRESHOLD:
        write_device_state(fan_state_file, 1)  # Включить вентилятор
        print("Включен вентилятор.")
    else:
        write_device_state(fan_state_file, 0)  # Выключить вентилятор
        print("Вентилятор выключен.")

while True:
    
    # Считывание данных с датчиков
    soil_moisture = read_sensor_data(soil_moisture_file)
    temperature = read_sensor_data(temperature_file)
    light = read_sensor_data(light_file)
        
    if soil_moisture is not None:
       control_pump(soil_moisture)

    if temperature is not None:
       control_fan(temperature)

    # Логика для света
    if light is not None and light < LIGHT_THRESHOLD:
        print("Не хватает света. Подумать о включении освещения.")
        
    time.sleep(5)  # Пауза перед следующим циклом