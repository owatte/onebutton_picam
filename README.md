# onebutton-picam

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

## Contributing

The *One Button PiCam* is a [EmNet](http://www.emnet.cc) Raspberry Pi project.

If you find this code useful here's how you can help:

* Send a Pull Request with your awesome enhancements and bug fixes
* Be a part of the community and help resolve Issues

## Team

### EmNet

* [Olivier Watté](https://github.com/owatte/)
* [Audrey Robinel](https://github.com/sarinkhan/)
