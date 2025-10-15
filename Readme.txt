Project : Smart Assistance For Visually Impaired(B21PD03)


Libraries required:

Library               Command Prompt command
1. Open CV(CV2)       pip install opencv-python
2. Pyttsx3            pip install pyttsx3
3. Playsound          pip install playsound
4. Numpy              pip install numpy
5. OS
6. Time


Data set requirements:

1. COCO names
2. YOLOv3 config and weights file

These files can be downloaded directly from COCO website or from the link given in PPT and Report


After downloading all the required files, open the Live Assistance file. Once you run this file in the python environment, the process gets 
started and the detected object name will be seen in the TERMINAL of the python environment. Along with the name of the detected object a video 
file starts running with the object surrounded by a bounding box.


               
In Raspberry Pi it is a bit complicated to install OpenCV.
* First open terminal and start line by line enter below commands. After completion of below commands opencv will be installed successfully.
   * $ sudo apt-get install build-essential cmake pkg-config
   * $ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
   * $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
   * $ sudo apt-get install libxvidcore-dev libx264-dev
   * $ sudo apt-get install libfontconfig1-dev libcairo2-dev
   * $ sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev
   * $ sudo apt-get install libgtk2.0-dev libgtk-3-dev
   * $ sudo apt-get install libatlas-base-dev gfortran
   * $ sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103
   * $ sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
   * $ sudo apt-get install python3-dev
   * $ wget https://bootstrap.pypa.io/get-pip.py
   * $ sudo python get-pip.py
   * $ sudo python3 get-pip.py
   * $ sudo rm -rf ~/.cache/pip
   * $ sudo pip install virtualenv virtualenvwrapper


   * Now we have to install camera
   * $ pip install "picamera[array]"
      *    * Now time comes to install open cv library
   * $ pip install opencv-contrib-python==4.1.0.25










For E-voice connect Raspberry pi to any of Speaker or an earpiece through bluetooth then along with the video output and terminal output
playsound library generates electronic voice simultaneously.


NOTE: Make sure all the YOLO files are in the same folder.