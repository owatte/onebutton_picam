#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#       onebutton_picam.py
#
#       Copyright 2016 Olivier Watte - EmNet.cc
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

"""One button camera based on raspberry Pi and PiCam.

The OneButtonPiCam class provides a simple framework to interact with a PiCam,
just using a single button.

The OneButtonPiCam follows a very simple workflow, pressing button changes
the state. Each state is associated with a RGB led color value and optionnaly,
 an action.

* state 0 : READY = waiting for button key press
* state 1 : PROCESSING = doing action with picam (eg. taking picture or video)
* state 2 : POST-PROCESSING = doing post-processing treatments (optional)
* -> back to state 0

The OneButtonPiCam does not do anything : it is intended to be used in new
python class created with inheritance mechanism and overwritting the
do_processing() and do_post_processing() methods.

Todo:
    replace the use of time.sleep() in the run() method by a time counter to
    improve button usability and reactivity.

"""
from __future__ import unicode_literals

import ConfigParser
import os
import RPi.GPIO as GPIO
import time
import gettext

gettext.bindtextdomain('onebutton_picam', 'locale')
gettext.textdomain('onebutton_picam')
_ = gettext.gettext

__all__ = ['OneButtonPiCam', 'run']

BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'onebutton_picam')


class OneButtonPiCam(object):
    """This class manages triggered PiCam actions when the button is pushed.

    Attributes:
        config_file (str): Configuration .ini file

    Properties:
        button_state (boolean): Raspberry Pi button's GPIO value

    """
    def __init__(self, config_file=os.path.join(BASE_DIR,
                                                'onebutton_picam.ini')):
        """Sets up the Raspberry Pi GPIOs and sets the working directory.

        Args:
            config_file (str): Configuration .ini file path.

        """
        # cfg ini file
        self.config_file = config_file
        try:
            cfg = open(self.config_file, 'r')
        except (IOError, OSError), e:
            raise e

        self._config = ConfigParser.ConfigParser()
        self._config.read(self.config_file)
        cfg.close()

        # work tree
        self.root_dir = self._config.get('directories', 'root_dir')

        try:
            os.chdir(self.root_dir)
        except (IOError, OSError), e:
            raise e

        # raspi GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # push button
        self._button_gpio = self._config.getint('button', 'gpio')
        self._button_pud_up = self._config.getboolean('button', 'pud_up')
        GPIO.setup(self._button_gpio, GPIO.IN, self._button_pud)

        # led colours : green, red and orange (
        # note: because of the used RGB we use blue for orange
        states = ['READY', 'PROCESSING', 'POST-PROCESSING']
        # [TODO] penser au cas ERROR. KEY_PB
        # no usb key found or no enough space left on device ...
        # When we have the new (r,g,b) led we could use a blue in that case ?
        self.states = {}
        for state in states:
            self.states[state] = self._config.getint('states', state.lower())
            GPIO.setup(self.states[state], GPIO.OUT)
            GPIO.output(self.states[state], True)

        self._show_state_on_led('READY')

    @property
    def _button_pud(self):
        """set the `pull_up_down value` (used for GPIO setup).

        """
        if self._button_pud_up:
            return GPIO.PUD_UP
        else:
            return GPIO.PUD_DOWN

    @property
    def _button_is_pressed(self):
        """set the `button_is_pressed` attr depending on push up/down type.

        """
        if self._button_pud_up:
            return False
        else:
            return True

    @property
    def _button_state(self):
        """Read the button state on the GPIO.

        """
        return GPIO.input(self._button_gpio)

    def do_processing(self):
        print 'BEGIN do_processing'
        time.sleep(5)
        print 'END do_processing'
        return True

    def do_post_processing(self):

        print 'BEGIN do_post-processing'
        time.sleep(5)
        print 'END do_post-processing'
        return True

    def run(self):
        state = 'READY'

        while True:
            if self._button_state == self._button_is_pressed:
                if state == 'READY':
                    state = 'PROCESSING'
                    self._show_state_on_led(state)
                    self.do_processing()
                elif state == 'PROCESSING':
                    state = 'POST-PROCESSING'
                    self._show_state_on_led(state)
                    self.do_post_processing()
                    state = 'READY'
                    self._show_state_on_led(state)
                else:
                    print "Atann' !!! fo ou kalmé'w timal !!!'"
            else:
                if state == 'PROCESSING':
                    self.do_processing()

    def _set_led_off(self):
        """set led(s) off

        For the old and/or cultivated reader : do you know dBase ? :-D

        """

        for led in self.states.iteritems():
            GPIO.output(led[1], True)

    def _show_state_on_led(self, state):
        #
        try:
            for state_ in self.states:
                if state_ == state:
                    GPIO.output(self.states[state_], False)
                else:
                    GPIO.output(self.states[state_], True)
        except KeyError:
            print "unattended state value %s" % state
            exit(1)


def run():
    action = OneButtonPiCam().run()

if __name__ == '__main__':
    run()
