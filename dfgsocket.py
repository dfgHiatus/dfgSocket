# Don't forget your packages!!
# Gaze tracking to be added in a future update
# from gaze_tracking import GazeTracking,
# Granted via 2019 Antoine Lamé's MIT License, https://github.com/antoinelame/GazeTracking
from imutils.video import VideoStream
from statistics import mean
import requests
import asyncio
import websockets
import socket
import numpy as np 
import datetime
import argparse
import imutils
import math
import dlib
import cv2

def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

# Load video input. Be sure the web camera you're using is the default device!
cap = cv2.VideoCapture(0) 

# AI Stuff, loading the face database
detector = dlib.get_frontal_face_detector() 
predictor = dlib.shape_predictor("gaze_tracking/trained_models/shape_predictor_68_face_landmarks.dat")

# Websocket runs on port 7000 by default
print("[Info] Websocket created")
socketString = ""

# The meat and potatoes
async def facetrack(websocket, path):
    async for message in websocket:
        # Wipe string buffer
        socketString = ""
        
        # Read in a webcamera frame
        _, frame = cap.read() 
        
		# Resize frame for performace++
        frame = imutils.resize(frame, width=400)

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray) 
        for face in faces: 
            # Use AI to get face landmarks
            landmarks = predictor(gray, face)
            
            # Append landmark points to string buffer 
            for n in range(0, 68): 
                x = landmarks.part(n).x 
                y = landmarks.part(n).y 
                # Parse to Float3 in Neos, maps to indexes 0-68
                socketString += ("[" + str(x/200) + ";0;" + str(y/200) + "],")
				# Superimpose on frame
                cv2.circle(frame, (x, y), 2, (255, 255, 0), -1) 
                    
		# Draw frame to screen, useful for debugging			
        cv2.imshow("Frame", frame) 

        # Send info to NeosVR. All info is send as float3's {[X;Y;Z]}, with a ',' as the delimiter.
        # Works well @ 30Hz, depending on server load/etc.
        # Reference face map for what each landmark correlates to
        await websocket.send(socketString)

# Pushes string to port 7000
asyncio.get_event_loop().run_until_complete(
    websockets.serve(facetrack, 'localhost', 7000))
asyncio.get_event_loop().run_forever()
