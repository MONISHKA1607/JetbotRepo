from jetbot import Robot, Camera
import cv2
import numpy as np
import time

# Initialize robot and camera
robot = Robot()
camera = Camera.instance(width=320, height=240)

print("Hand Guided JetBot Started")

# Capture initial reference frame
reference_frame = camera.value
reference_frame = cv2.cvtColor(reference_frame, cv2.COLOR_BGR2GRAY)
reference_frame = cv2.GaussianBlur(reference_frame, (7,7), 0)

try:

    for i in range(5000):

        # Capture frame
        frame = camera.value

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7,7), 0)

        # Difference between frames
        diff = cv2.absdiff(reference_frame, blur)

        # Calculate motion score
        change_score = np.sum(diff) / 255

        # Motion threshold
        CHANGE_THRESHOLD = 400

        change_detected = change_score > CHANGE_THRESHOLD

        h, w = diff.shape

        # Compare left and right side motion
        left_score = np.sum(diff[:, :w//2])
        right_score = np.sum(diff[:, w//2:])

        direction = "LEFT" if left_score > right_score else "RIGHT"

        print(f"Motion: {direction} | Score: {int(change_score)}")

        # Robot movement
        if change_detected:

            if direction == "LEFT":

                # Smooth left curve
                robot.set_motors(0.08, 0.18)

            else:

                # Smooth right curve
                robot.set_motors(0.18, 0.08)

        else:

            # Move forward slowly
            robot.set_motors(0.15, 0.15)

        # Slowly update reference frame
        if i % 20 == 0:
            reference_frame = blur

        time.sleep(0.05)

except KeyboardInterrupt:

    print("Stopped by user")

finally:

    robot.stop()
    print("Robot stopped safely")
