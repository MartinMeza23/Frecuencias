import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
import thinkplot

señalUno = SinSignal(freq=380, amp=0.5, offset=0)
señalDos = SinSignal (freq=900, amp=0.8, offset=0)

mezcla = señalUno + señalDos

waveMezcla = mezcla.make_wave(duration=1, start=0, framerate= 44100)
waveMezcla.plot()
#pip3 install pandas
decorate(xlabel="Tiempo (s)")
thinkplot.show()

espectro = waveMezcla.make_spectrum()
espectro.plot()
decorate(xlabel="Frecuencia (Hz)")
thinkplot.show()




