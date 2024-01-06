import board
import analogio
import time

flag = 1

# ADCピンの指定（例: GP26）
adc_pin = analogio.AnalogIn(board.GP26)

while True:
    time.sleep(10)
    if flag > 0:
        print("Start:")
        flag = 0
        for x in range(0, 10000):
            # アナログセンサからの値を取得
            sensor_value = adc_pin.value
        
            # 取得した値をターミナルに出力
            print(x," Analog Value:", sensor_value)
        
            # 適当な待機時間を設ける
            time.sleep(0.001)
        print("End:")



