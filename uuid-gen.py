import sys
import uuid

if len(sys.argv) > 1:
    count = int(sys.argv[1])
    for i in range(0, count):
        print(uuid.uuid4())
else:
    print(uuid.uuid4())
