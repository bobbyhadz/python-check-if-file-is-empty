# Check if a file is empty in Python

import os

# ✅ with relative path

if os.stat('example.txt').st_size == 0:
    print('The file is empty')
else:
    print('The file is not empty')

# ---------------------------------------------

# ✅ with absolute path

if os.stat(
  '/home/borislav/Desktop/bobbyhadz_python/example.txt'
).st_size == 0:
    print('The file is empty')
else:
    print('The file is not empty')