import os
library = "название_библиотеки"
try:
    __import__(library)
except ImportError:
    os.system("pip install " + library)
