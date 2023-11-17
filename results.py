#!python3
import json
from pprint import pp

all={}
for tests in open("RESULTS.TXT").read().splitlines():
    timestamp,results=json.loads(tests)
    for f in results.keys():
        for mode,result in results[f].items():
            result["timestamp"]=timestamp
            all.setdefault(f,{}).setdefault(mode,[]).append(result)


for file,tests in all.items():
    print(file)
    for mode,tests in tests.items():
        for test in tests:
            print(f"  - {mode:5s} : {test['seconds']} ({test['version']}) ({test['timestamp']})")
