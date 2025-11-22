class Vechile:
    def start(self):
        print('Vechile started...')

    def stop(self):
        print('Vechile stoped...')

class Car(Vechile):
    def __init__(self,speed):
        self.speed=speed

    def speed_fn(self):
        print(f'Speed is {self.speed}')

scorpio=Car(100)

scorpio.start()
scorpio.speed_fn()
scorpio.stop()