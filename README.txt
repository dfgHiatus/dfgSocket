dfgSocket v0.0.1
- Desktop mode only, at least so far
- Gaze tracking planned for future builds, granted via 2019 Antoine Lamé's MIT License,
https://github.com/antoinelame/GazeTracking

Included is the source code needed to get this thing running. You'll have to compile/run it yourself, but I've created this to make things as easy as possible for you.  Please let me know if anything gives you grief, I'm more than happy to help out.

Step 0) Have a web camera plugged in and make sure it's the default device.

Step 1) Install Python 3.8.6. If you already have python installed, you may need to upgrade/downgrade. Be sure to add python to PATH to run those batch files, since it uses pip directly.
- https://www.python.org/downloads/release/python-386/?hn

Step 2) Install needed packages by running INSTALL.bat. While these are the ones I explicitly use, there may some being used behind the scenes - let me know if I'm missing anything. 

Step 3) Now that this is done, we'll need to get a copy of CUDA 10.1, cudNN 7.6.4, and pyTorch. Get them from here:

- https://developer.nvidia.com/cuda-10.1-download-archive-base
- https://developer.nvidia.com/cudnn
- Also, run getTorch.bat at this time

Step 4) Final step - now we're actually going to download the AI thats runs this thing. Go here, and create a folder under gaze_tracking called trained_models. Paste it here!
- https://drive.google.com/file/d/1Duf9XZ7y_vVVDcBwcaN2nsU4uzMIdPCP/view?usp=sharing

Step 5) Now that this's taken care of, go to my public folder and get yourself a copy of "pointCloudAvatarDesktop". Run RUNME.bat, hop into NeosVR in screen mode and the avatar should automatically connect. If it doesn't press the reconnect button, you should see a point cloud of your face. Have fun!!

======================================================================================================================================================================

Changelog:

v0.0.1- Initial Commit

Desktop face tracking for NeosVR.

v0.0.2 - Alpha VR Commit

The moment we've all been waiting for. The way this implementation works is that it stitches together a picture of your upper face with your lower moving mouth. It's a weird solution, but beats having to retrain the AI.

To use this, 
1) Un-comment out lines 26, 53, 56, and 59.
2) Take a picture of your face, and crop it just so the bottom of the nose is visible. Name it "upper_face.jpg", and insert it into the same folder as dfgSocket.py.
3) Mount the camera to your HMD, shoulder, etc and have it face your mouth. Make sure it's in place!
4) Run and have fun. Camera calibration is iffy still, this is something I'm working on and will add
