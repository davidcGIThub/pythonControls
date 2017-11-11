import numpy as np
import bobParam as P
import math
from signalGenerator import signalGenerator

def reference(time):

    reference = P.z0

    if (False):
        reference = P.z0

    if(True):
        ref = signalGenerator(amplitude=P.amplitude, frequency=P.frequency, y_offset=P.offset)
        reference = ref.square(time)[0]

    return reference
