import base64
import cv2
def image_to_base64(frame):
    ret, buffer = cv2.imencode('.jpg', frame)
    if not ret:
        raise IOError("Failed to convert frame to JPEG")

    # Convert to base64 encoding and return the result
    base64_image = base64.b64encode(buffer).decode('utf-8')
    return f'data:image/jpeg;base64,{base64_image}'