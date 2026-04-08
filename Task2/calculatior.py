from sense_hat import SenseHat
import math

class Calculator:
    def __init__(self):
        self.sense = SenseHat()
        self.x = 16

    def display(self):
        print("Current x:", self.x)
        self.sense.show_message(str(self.x), scroll_speed=0.05)

    def increase(self):
        self.x += 1

    def decrease(self):
        self.x -= 1

    def square(self):
        self.x = self.x ** 2

    def sqrt(self):
        if self.x >= 0:
            self.x = int(math.sqrt(self.x))
        else:
            self.sense.show_message("Err", scroll_speed=0.05)

    def reset(self):
        self.x = 16

    def handle_input(self):
        for event in self.sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    self.increase()
                elif event.direction == "down":
                    self.decrease()
                elif event.direction == "left":
                    self.square()
                elif event.direction == "right":
                    self.sqrt()
                elif event.direction == "middle":
                    self.reset()

    def run(self):
        while True:
            self.handle_input()
            self.display()


if __name__ == "__main__":
    app = Calculator()
    app.run()