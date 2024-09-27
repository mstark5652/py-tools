# pipe logs from kubectl to pretty print json logs
# add alias - `alias formatlogs="python3 <path_to_this_file>"`
# kubectl logs <pod_name> | formatlogs

import json
import sys

try:
    for line in sys.stdin:
        try:
            print(json.dumps(json.loads(line), indent=2))
        except:
            print(line)
except KeyboardInterrupt:
    sys.exit(0)
