import serial
from tkinter import filedialog
name = input('Enter your Steam username (what people see in-game, this is case-sensitive!): ')
port = input('Enter the port number of the Arduino: COM')
ser = serial.Serial(f'COM{port}', 115200, timeout=1)
file_path = filedialog.askopenfilename()
deaths = 0
kills = 0
if __name__ == '__main__':
    while True:
        with open(f'{file_path}', 'r+', encoding='UTF-8') as f:
            for line in f:
                if f'{name} killed' in line:
                    kills += 1
                    print(f"Current Kills: {kills}")
                    print(line)
                    ser.write(str.encode(f'vent {kills}'))
                    f.seek(0)
                    f.truncate()
                    break
                elif f'killed {name}' in line:
                    deaths += 1
                    print(f"Current Deaths: {deaths}")
                    print(line)
                    ser.write(str.encode(f'pump {100 - (kills / 20)}, {deaths}'))
                    kills = 0
                    f.seek(0)
                    f.truncate()
                    break
                    time.sleep(0.001)
