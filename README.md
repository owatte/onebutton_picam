# Raspberry Pi One Button Picam PyLib

Python class to interact with a raspberry Pi with a picam and a pull button


## One button camera based on raspberry Pi and PiCam.

The OneButtonPiCam class provides a simple framework to interact with a PiCam,
just using a single button.

The OneButtonPiCam follows a very simple workflow, pressing button changes
the state. Each state is associated with a RGB led color value and optionnaly,
 an action.

* state 0 : READY = waiting for button key press
* state 1 : PROCESSING = doing action with picam (eg. taking picture or video)
* state 2 : POST-PROCESSING = doing post-processing treatments (optional)
* -> back to state 0

The OneButton PiCam does not do anything : it is intended to be used in new
python class created with inheritance mechanism and overwritting the
`do_processing()` and `do_post_processing()` methods.

## Todo

Replace the use of time.sleep() in the run() method by a time counter to improve button usability and reactivity.

## About OneButton PiCam 

### OneButton PiCam In Short

What we made:

#### Raspberry Pi
A Raspberry Pi with a PiCam and a single push button + a single RGB led to create a simple, powerful, affordable and hackable camera.

#### Python
Once assembled, just few lines of python code are needed to create a custom high-end camera, using the full resolution of the sensor (2592×1944), or another video mode provided by the PiCam.

#### Open Source

##### Free Software 

OneButton PiCam code parts is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

##### Open-Source Hardware

OneButton PiCam physical parts design is made publicly available so that anyone can study, modify, distribute, make, and sell the design or hardware based on that design. The hardware’s source, the design from which it is made, is available in the preferred format for making modifications to it.

#### Fork it or clone it !!!

You don't need to create your camera project from scratch : feel free to clone and hack an existing project. 

Or just make a verbatim copy of it. 

Pull requests are welcome.

## How-to make your own 

From the idea to the project, how Emnet makes it :

* Shopping list
* 3D printing parts
* Schematics and PCBs
* Python code 
* Instructions

### Models

Actually, there are 2 main models :

* the *OneButton PiCam basic* a simple button for a single function
* the *OneButton PiCam ultimate* : same as the basic one, with a rotary dip switch to select a functionnality.

Both model can be upgraded with additionnal PiCam lens and with motors, to create a full automated video acquisition system.

Actually, there are many functionnalities and many real-life use cases
* taking pictures
* recording videos
* making timelapse
* motion detection

### Power
The camera is powered by a USB wire plugged on the Raspberry's USB port. 

The camera can be 100% autonomous, using a dedicated clip on box containing a standard LiPo battery pack.

### External screen
The camera is intended to bo simplest as possible. Some people added an external screen for preview.

### Mods
The most popular and usable mods are probably :
* the GPS sensor
* the RTC clock

## Contributing

The *One Button PiCam* is a [EmNet](http://www.emnet.cc) Raspberry Pi project.

If you find this code useful here's how you can help:

* Send a Pull Request with your awesome enhancements and bug fixes
* Be a part of the community and help resolve Issues

## Team

### EmNet

* [Olivier Watté](https://github.com/owatte/)
* [Audrey Robinel](https://github.com/sarinkhan/)
