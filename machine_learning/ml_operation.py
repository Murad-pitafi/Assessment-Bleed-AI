from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
import cv2
import mediapipe as mp
import tempfile
import os

def process_image(image: UploadFile = File(...)):
    try:
        # Save the uploaded image to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_image:
            tmp_image.write(image.file.read())
            tmp_image_path = tmp_image.name
        
        # Read the image using OpenCV
        img = cv2.imread(tmp_image_path)
        
        # Initialize MediaPipe face detection
        mp_face_detection = mp.solutions.face_detection
        mp_drawing = mp.solutions.drawing_utils
        with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
            # Convert the image to RGB
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Process the image and detect faces
            results = face_detection.process(img_rgb)
            
            # Draw facial landmarks on the image
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(img, detection)
            
            # Save the processed image with facial landmarks
            processed_image_path = "processed_image.jpg"
            cv2.imwrite(processed_image_path, img)
            
            # Return the processed image path
            return JSONResponse(status_code=200, content={"message": "Image processed successfully", "processed_image_path": processed_image_path})
    
    finally:
        # Remove the temporary image file
        os.unlink(tmp_image_path)
