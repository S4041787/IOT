from sense_hat import SenseHat
import time
from moodAnimator import MoodAnimator


class TiltEmotions:
    def __init__(self):
        self.animator = MoodAnimator()
        self.sense = self.animator.sense

        self.current_state = None
        self.paused = False

        self.last_roll = 0
        self.last_time = time.time()

    def play_emotion(self, index):
        frames = self.animator.emojis[index]

        for frame in frames:
            self.sense.set_pixels(frame)
            time.sleep(0.4)

    def detect_orientation(self):
        o = self.sense.get_orientation()
        pitch = o["pitch"]
        roll = o["roll"]
        yaw = o["yaw"]

        if 45 < roll < 135:
            return 0  # happy
        elif 225 < roll < 315:
            return 1  # sad
        elif 45 < pitch < 135:
            return 2  # angry
        elif 225 < pitch < 315:
            return 3  # surprise
        else:
            return 4  # expressionless

    def detect_flip(self, roll):
        now = time.time()

        if abs(roll - self.last_roll) > 60 and (now - self.last_time) < 0.5:
            self.last_roll = roll
            self.last_time = now
            return True

        self.last_roll = roll
        self.last_time = now
        return False
    
    def detect_flip(self, roll):
    now = time.time()

    if abs(roll - self.last_roll) > 120 and (now - self.last_time) < 0.2:
        self.last_roll = roll
        self.last_time = now
        return True

    self.last_roll = roll
    self.last_time = now
    return False

    def play_flip(self):
        for _ in range(3):
            self.sense.clear([255, 0, 0])
            time.sleep(0.2)
            self.sense.clear([0, 0, 255])
            time.sleep(0.2)

    def handle_input(self):
        for event in self.sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    self.paused = not self.paused

    def run(self):
        while True:
            self.handle_input()

            if self.paused:
                continue

            o = self.sense.get_orientation()
            roll = o["roll"]

            # flip (MoodEmo6)
            if self.detect_flip(roll):
                self.play_flip()
                continue

            state = self.detect_orientation()

            # flicker 
            if state != self.current_state:
                self.current_state = state
                self.play_emotion(state)

            time.sleep(0.2)


if __name__ == "__main__":
    app = TiltEmotions()
    app.run()