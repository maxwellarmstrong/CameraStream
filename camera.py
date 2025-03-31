import cv2
from ultralytics import YOLO  # Import YOLOv8

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)  # 0 = default camera
        if not self.video.isOpened():
            raise IOError("Cannot open webcam")

        # Load YOLOv8 model
        self.model = YOLO('yolov8n.pt')  # Use the nano model for speed

    def get_frame(self):
        success, frame = self.video.read()
        if not success:
            print("Failed to capture frame")
            return None

        # Run YOLOv8 on the captured frame
        results = self.model(frame)

        # Annotate the frame with bounding boxes and labels
        annotated_frame = results[0].plot()

        # Encode the annotated frame as JPEG
        ret, jpeg = cv2.imencode('.jpg', annotated_frame)

        return jpeg.tobytes()

    def release(self):
        self.video.release()

