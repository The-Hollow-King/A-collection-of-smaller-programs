import numpy as np
ar = np.array([[['A','B','C'], ['D','E','F'], ['G','H','I']],
               [['J','K','L'], ['M','N','O'], ['P','Q','R']],
               [['S','T','U'], ['V','W','X'], ['Y','Z','&']]])
word = ar[2,0,1] + ar[1,1,2] + ar[1,2,2] + ar[2,0,2]
print(word)
