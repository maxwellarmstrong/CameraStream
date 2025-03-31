import cv2

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)  # 0 = default camera
        if not self.video.isOpened():
            raise IOError("Cannot open webcam")

    def get_frame(self):
        success, frame = self.video.read()
        if not success:
            print("Failed to capture frame")
            return None
        ret, jpeg = cv2.imencode('.jpg', frame)
        print("Frame captured")
        return jpeg.tobytes()

    def release(self):
        self.video.release()


