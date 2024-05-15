import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_process_image():
    # Prepare a sample image file
    with open("test_image.jpg", "rb") as image_file:
        files = {"image": ("test_image.jpg", image_file, "image/jpeg")}
        response = client.post("/process-image/", files=files)
    
    # Check if the response status code is 200
    assert response.status_code == 200
    
    # Check if the response contains the expected message
    assert response.json()["message"] == "Image processed successfully"
    
    # Check if the response contains the processed image path
    assert "processed_image_path" in response.json()
