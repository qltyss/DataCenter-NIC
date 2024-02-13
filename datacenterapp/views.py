import cv2
from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render
# from .tcp import tcp_handler
# from .videostream import global_video_stream
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators import gzip
import time
from .amr import amr_command
# from .amr_test import amr_test
import json
from .arm_tcp import arm
from .constants import *
from .load_models import fire_model, cabinet_model
# from .facial_recognition import *
from .image_base64 import image_to_base64
import requests
import numpy as np
# import pyrealsense2 as rs

import os
from .depth_cam import camera_stream

# cabinet_model, fire_model= load()
# Constants
PATH_TO_JOIN = 'datacenterapp/static/mydetect'
def save_image(frame):
    global image_counter
    current_time_str = time.strftime("%Y%m%d_%H%M%S")
    image_name = f"{image_counter}_{current_time_str}.png"
    image_path = os.path.join(PATH_TO_JOIN, image_name)
    cv2.imwrite(image_path, frame)
    image_counter += 1
    return os.path.join(PATH_TO_JOIN, image_name)

@csrf_exempt
def start_scanning(request):
    global response, notification_value
    if request.method == 'POST':
        # Parse the JSON data from the request body
        body = json.loads(request.body)
        value = body.get('dataItem')  
        
        notification_value = 'AMR is moving to A20 area'
        # amr_test(value)
        notification_value = 'AMR is in A20 area'
        # time.sleep(1)
        if value == "scan":
            notification_value = 'Scanning process has begun'
            response = arm('unlock')
            notification_value = 'An issue has been detected'
            # amr_command("LM9")
            # print(value)  # This will print the list to the console
            
            # response = arm('unlock')
            # print(response) # now it's 0

        
        return JsonResponse({'message': "message"})

@csrf_exempt
def start_swapping(request):
    
    global response, notification_value
    if request.method == 'POST':
        # Parse the JSON data from the request body
        body = json.loads(request.body)
        value = body.get('dataItem')  
        if value == "swap":
            notification_value = 'Swapping process has begun'
            response = arm('value')
            notification_value = 'Swapping process is finished'
            # print(value)  
            # amr_new = arm(value) # Value should be swap always
            # print(amr_new) # now it's 1
            # if amr_new == "swapped":
            #     amr_command("LM10")
            #     response = "swapped"
        elif value == "cancel":
            notification_value = 'Swapping process was canceled'
            response = arm('value')
            # print("cancellllllllllllllllllllllll")
            notification_value = 'AMR is moving to A50 area'
            # amr_command("LM10")
            notification_value = 'AMR is in A50 area'
            # response = 'swapped'
            
        return JsonResponse({'message': "message"})
    
@csrf_exempt
def faical_recog(request):
    
    global response
    if request.method == 'POST':
        # Parse the JSON data from the request body
        body = json.loads(request.body)
        value = body.get('dataItem')  

        response = '5' # should be "facial"
        
        return JsonResponse({'message': "message"})  
@csrf_exempt
def faical_recog_cancel(request):
    
    global response
    if request.method == 'POST':
       
        response = '6' # should be "facial"
        
        return JsonResponse({'message': "message"})    
@csrf_exempt
@gzip.gzip_page
def video_feed_depth(request):
    
    def generate_frames():
       
        while True:
                  
            frame = camera_stream.read_depth()
            
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    response = StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
    return response

@csrf_exempt
@gzip.gzip_page
def video_feed_html(request):
    
    global response
   
    def generate_frames():
        global detected_objects, start_timer, condition_met, fire_alert, black_white, image_name, fire_image_saved, fire_detection_start
        global notification_value
        # List of names to be recognized
        frame_counter = 0  # Initialize a frame counter
        # names_to_recognize = ['Sarah']
        

        # Sending a POST request
        # init_response = requests.post(init_url, json={'names': names_to_recognize})
        # print(init_response.text)
        
        while True:
            frame_counter += 1  # Increment the frame counter
            red_counter = 0
            green_counter = 0 
            fire_alert = ''
            black_white = {}
            # frame = camera_stream.read_color()
            frame = camera_stream.read_color()
            # if response == "unlocked": # To be changed to "unlocked" 
            if response == "0": # To be changed to "unlocked" 
                if cabinet_model !=  None:
                    results = cabinet_model(frame, conf = 0.50) # Detect Red and Green Lights
                    for r in results:
                        boxes = r.boxes
                        for box in boxes:
                            confidence = box.conf.item()
                            class_id = r.names[box.cls[0].item()]

                            if class_id == "red":
                                red_counter = red_counter + 1
                            if class_id == "green":
                                green_counter = green_counter + 1
                            
                            label = f"{class_id} {confidence:.2f}"
                            xA, yA, xB, yB = map(int, box.xyxy[0])
                            if class_id == "red":
                                color = (0, 0, 255)  # Red color
                            else:
                                color = (0, 255, 0)  # Green color
                            cv2.rectangle(frame, (xA, yA), (xB, yB), color, 2)
                else:
                    pass
            if green_counter == 2:
                if not condition_met:
                                # Start the timer when condition is met for the first time
                    start_timer = time.time()
                    condition_met = True
                elif time.time() - start_timer >= 2:
                    qr_reading()
                                # Reset the timer and condition
                    condition_met = False
                    start_timer = None
            else:
                # Reset the timer and condition if they no longer hold
                condition_met = False
                start_timer = None
            if red_counter > 0 or green_counter > 0:
                detected_objects = {"red": red_counter, "green": green_counter}
            elif red_counter == 0 and green_counter == 0:
                detected_objects = {"red": 0, "green": 0}
            
            if response == "1": # To be changed to "swapped" 
            # if response == "swapped": # To be changed to "swapped" 
                if fire_model is not None:
                    results = fire_model(frame, conf = 0.50, classes = [1]) # Detect Red and Green Lights
                    fire_currently_detected = False  # Flag to check if fire is currently detected
                    for r in results:
                        boxes = r.boxes
                        for box in boxes:
                            confidence = box.conf.item()
                            class_id = r.names[box.cls[0].item()]
                            if class_id == "fire":
                                fire_currently_detected = True
                                if fire_detection_start is None:
                                    fire_detection_start = time.time()  # Record the start time of fire detection

                                elapsed_time = time.time() - fire_detection_start
                                fire_alert = "fire"
                                # if elapsed_time >= 1.0 and not fire_image_saved:  # Check if fire has been detected for at least 1 second
                                    
                                image_name = save_image(frame)  # Save image
                                fire_image_saved = True
                            label = f"{class_id} {confidence:.2f}"
                            xA, yA, xB, yB = map(int, box.xyxy[0])
                            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
                            cv2.putText(frame, label, (xA, yA - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) 
                else:
                    pass          
            # if frame_counter % 15 == 0:
            if response == "5": # To be changed to "facial"
                    
                    # # Face Recognition
                    image_data = image_to_base64(frame)
                    
                    recog_response = requests.post(recog_url, json={'image': image_data})
                    recog_response = recog_response.json()['name']
                    print(recog_response)
                    if recog_response in black_list:
                        black_white = {'black': recog_response}

                    elif recog_response in white_list:
                        black_white = {'white': recog_response}
                    print(black_white)

                    # threading.Thread(target=handle_api_call, args=(image_data, recog_url)).start()
                    # black_white = {"black": "Sarah"}
                    # black_white = recognize_face(frame)
                    
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    response = StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
    return response

def qr_reading():
    print("qr reading")

def Red_Green(request):
    
    global detected_objects
    print(detected_objects)
    return JsonResponse({'objects': detected_objects})

def fire(request):
     
    global fire_alert, black_white, image_name
    print(fire_alert)
    print(black_white)
    return JsonResponse({'fire': fire_alert, 'face' : black_white, 'path' : image_name})


# def armController(request):
#     if request.method == 'POST' and request.is_ajax():
#         action = request.POST.get('action')
        
#         if action == 'runScriptAmr':
#             # Perform the action you want here
#             print("Received runScriptAmr signal")
            
#             # You can return a JsonResponse if needed
#             return JsonResponse({'message': 'Action successful'}, status=200)

#     # Handle other cases or return an error
#     return JsonResponse({'error': 'Invalid request'}, status=400)

def armController(request):
    if request.method == 'POST':
        data = request.POST.get('command')
        # print(data)
        if data == "runScriptArm":
            print(data)
        elif data == "StopScriptArm":
            print(data)
        elif data == "emergencyStopArm":
            print(data)
        elif data == "enableRobotArm":
            print(data)
        elif data == "disableRobotArm":
            print(data)

        # You can perform additional actions with the received data here
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
def amrController(request):
    if request.method == 'POST':
        data = request.POST.get('command')
        # print(data)
        if data == "runScriptAmr":
            print(data)
        elif data == "stopScriptAmr":
            print(data)
        elif data == "emergencyStopAmr":
            print(data)

        # You can perform additional actions with the received data here
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



def index(request):
    return render(request, 'index.html') 
