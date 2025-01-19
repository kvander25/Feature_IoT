import os
import time

# Пороговые значения
MOISTURE_THRESHOLD = 40  # Влажность почвы меньше 40% 

soil_moisture_file = 'soil_moisture.txt'
pump_state_file = 'pump_state.txt'

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

while True:
        # Считывание данных с датчиков
    soil_moisture = read_sensor_data(soil_moisture_file)
        
    if soil_moisture is not None:
       control_pump(soil_moisture)
        
        
    time.sleep(5)  # Пауза перед следующим циклом