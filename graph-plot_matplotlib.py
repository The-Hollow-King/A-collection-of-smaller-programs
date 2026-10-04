import matplotlib.pyplot as pt
import numpy as np

Year = np.array([1900,1925,1950,1975,2000,2025])
Valuation = np.array([50000, 75000, 90000, 95000, 175000, 225000])
IO = np.array([1,2,1,0,2,1])

pt.plot(Year, Valuation, IO)

pt.show()