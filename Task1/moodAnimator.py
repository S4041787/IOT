from sense_hat import SenseHat
import time

class MoodAnimator:
    def __init__(self):
        self.sense = SenseHat()
        self.index = 0
        self.paused = False
        self.last_input_time = time.time()
        self.sleeping = False

        Y = [255, 255, 0]
        R = [255, 0, 0]
        B = [0, 0, 255]
        W = [255, 255, 255]
        O = [0, 0, 0]

        happy1 = [
            O,O,Y,Y,Y,Y,O,O,
            O,Y,Y,Y,Y,Y,Y,O,
            Y,Y,O,Y,Y,O,Y,Y,
            Y,O,Y,O,O,Y,O,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            O,Y,Y,O,O,Y,Y,O,
            O,O,Y,Y,Y,Y,O,O
        ]

        happy2 = [
            O,O,Y,Y,Y,Y,O,O,
            O,Y,Y,Y,Y,Y,Y,O,
            Y,Y,O,Y,Y,O,Y,Y,
            Y,O,Y,O,O,Y,O,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            O,Y,O,O,O,O,Y,O,
            O,O,Y,Y,Y,Y,O,O
        ]

        happy3 = [
            O,O,Y,Y,Y,Y,O,O,
            O,Y,Y,Y,Y,Y,Y,O,
            Y,Y,O,Y,Y,O,Y,Y,
            Y,O,Y,O,O,Y,O,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            Y,O,Y,Y,Y,Y,O,Y,
            O,Y,O,O,O,O,Y,O,
            O,O,Y,Y,Y,Y,O,O
        ]

        sad1 = [
            O,O,B,B,B,B,O,O,
            O,B,B,B,B,B,B,O,
            B,B,O,B,B,O,B,B,
            B,B,B,B,B,B,B,B,
            B,B,B,B,B,B,B,B,
            B,B,B,O,O,B,B,B,
            O,B,B,B,B,B,B,O,
            O,O,B,B,B,B,O,O
        ]

        sad2 = [
            O,O,B,B,B,B,O,O,
            O,B,B,B,B,B,B,O,
            B,B,O,B,B,O,B,B,
            B,B,B,B,B,B,B,B,
            B,B,B,B,B,B,B,B,
            B,B,O,O,O,O,B,B,
            O,B,B,B,B,B,B,O,
            O,O,B,B,B,B,O,O
        ]

        sad3 = [
            O,O,B,B,B,B,O,O,
            O,B,B,B,B,B,B,O,
            B,B,O,B,B,O,B,B,
            B,B,B,B,B,B,B,B,
            B,B,B,B,B,B,B,B,
            B,B,O,O,O,O,B,B,
            O,B,O,B,B,O,B,O,
            O,O,B,B,B,B,O,O
        ]

        angry1 = [
            O,O,R,R,R,R,O,O,
            O,R,R,R,R,R,R,O,
            R,R,O,R,R,O,R,R,
            R,R,R,R,R,R,R,R,
            R,R,R,R,R,R,R,R,
            R,R,R,O,O,R,R,R,
            O,R,R,R,R,R,R,O,
            O,O,R,R,R,R,O,O
        ]

        angry2 = [
            O,O,R,R,R,R,O,O,
            O,R,R,R,R,R,R,O,
            R,R,O,R,R,O,R,R,
            R,R,R,R,R,R,R,R,
            R,R,R,O,O,R,R,R,
            R,R,O,R,R,O,R,R,
            O,R,R,O,O,R,R,O,
            O,O,R,R,R,R,O,O
        ]

        angry3 = [
            O,O,R,R,R,R,O,O,
            O,R,R,R,R,R,R,O,
            R,R,O,R,R,O,R,R,
            R,R,R,R,R,R,R,R,
            R,R,O,O,O,O,R,R,
            R,R,O,R,R,O,R,R,
            O,R,O,O,O,O,R,O,
            O,O,R,R,R,R,O,O
        ]

        surprise1 = [
            O,O,Y,Y,Y,Y,O,O,
            O,Y,Y,Y,Y,Y,Y,O,
            Y,Y,O,Y,Y,O,Y,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            Y,Y,Y,O,O,Y,Y,Y,
            Y,Y,O,Y,Y,O,Y,Y,
            O,Y,Y,O,O,Y,Y,O,
            O,O,Y,Y,Y,Y,O,O
        ]

        surprise2 = [
            O,O,Y,Y,Y,Y,O,O,
            O,Y,Y,Y,Y,Y,Y,O,
            Y,Y,O,Y,Y,O,Y,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            Y,Y,O,O,O,O,Y,Y,
            Y,Y,O,O,O,O,Y,Y,
            O,Y,Y,Y,Y,Y,Y,O,
            O,O,Y,Y,Y,Y,O,O
        ]

        surprise3 = [
            O,O,Y,Y,Y,Y,O,O,
            O,Y,Y,Y,Y,Y,Y,O,
            Y,Y,O,Y,Y,O,Y,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            Y,Y,Y,O,O,Y,Y,Y,
            Y,Y,Y,O,O,Y,Y,Y,
            O,Y,Y,O,O,Y,Y,O,
            O,O,Y,Y,Y,Y,O,O
        ]

        expressionless1 = [
            O,O,W,W,W,W,O,O,
            O,W,W,W,W,W,W,O,
            W,O,O,W,W,O,O,W,
            W,W,W,W,W,W,W,W,
            W,W,W,W,W,W,W,W,
            W,W,W,O,O,W,W,W,
            O,W,W,W,W,W,W,O,
            O,O,W,W,W,W,O,O
        ]

        expressionless2 = [
            O,O,W,W,W,W,O,O,
            O,W,W,W,W,W,W,O,
            W,O,O,W,W,O,O,W,
            W,W,W,W,W,W,W,W,
            W,W,W,W,W,W,W,W,
            W,W,O,O,O,O,W,W,
            O,W,W,W,W,W,W,O,
            O,O,W,W,W,W,O,O
        ]

        expressionless3 = [
            O,O,W,W,W,W,O,O,
            O,W,W,W,W,W,W,O,
            W,O,O,W,W,O,O,W,
            W,W,W,W,W,W,W,W,
            W,W,W,W,W,W,W,W,
            W,O,O,O,O,O,O,W,
            O,W,W,W,W,W,W,O,
            O,O,W,W,W,W,O,O
        ]

        self.emojis = [
            [happy1, happy2, happy3],
            [sad1, sad2, sad3],
            [angry1, angry2, angry3],
            [surprise1, surprise2, surprise3],
            [expressionless1, expressionless2, expressionless3]
        ]

    def show_animation(self):
        if self.paused:
            return

        frames = self.emojis[self.index]

        for frame in frames:
            self.sense.set_pixels(frame)
            time.sleep(0.4)

    def show_sleep_face(self):
        dim = [10, 10, 10]
        off = [0, 0, 0]

        face = [
            dim,dim,dim,dim,dim,dim,dim,dim,
            off,off,off,off,off,off,off,off,
            dim,dim,dim,dim,dim,dim,dim,dim,
            off,off,off,off,off,off,off,off,
            dim,dim,dim,dim,dim,dim,dim,dim,
            off,off,off,off,off,off,off,off,
            dim,dim,dim,dim,dim,dim,dim,dim,
            off,off,off,off,off,off,off,off
        ]

        self.sense.set_pixels(face)

    def handle_input(self):
        now = time.time()

        for event in self.sense.stick.get_events():
            if event.action == "pressed":

                self.sleeping = False

                if now - self.last_input_time < 3:
                    return

                self.last_input_time = now

                if event.direction == "right":
                    self.index = (self.index + 1) % len(self.emojis)

                elif event.direction == "left":
                    self.index = (self.index - 1) % len(self.emojis)

                elif event.direction == "middle":
                    self.paused = not self.paused

    def run(self):
        while True:
            self.handle_input()

            if time.time() - self.last_input_time > 15:
                self.sleeping = True

            if self.sleeping:
                self.show_sleep_face()
                time.sleep(0.5)
            else:
                self.show_animation()


if __name__ == "__main__":
    app = MoodAnimator()
    app.run()