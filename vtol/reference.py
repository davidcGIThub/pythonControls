import numpy as np
import vtolParam as P
import math
from signalGenerator import signalGenerator

def reference_z(time):

    reference = P.z0

    if (False):
        reference = P.z0

    if(True):
        ref = signalGenerator(amplitude=P.amplitude_z, frequency=P.frequency_z, y_offset=P.offset_z)
        reference = ref.square(time)[0]

    return reference

def reference_h(time):

    reference = P.h0

    if (True):
        reference = P.h0

    if(False):
        ref = signalGenerator(amplitude=P.amplitude_h, frequency=P.frequency_h, y_offset=P.offset_h)
        reference = ref.square(time)[0]

    return reference
