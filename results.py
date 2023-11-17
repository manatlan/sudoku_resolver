#!python3
"""
Script to display results from the file (RESULTS.TXT (generated by a github_action))
in a more human readable output (md)
"""

import json,statistics
from pprint import pp

all={}
for tests in open("RESULTS.TXT").read().splitlines():
    timestamp,results=json.loads(tests)
    for f in results.keys():
        for mode,result in results[f].items():
            result["timestamp"]=timestamp
            all.setdefault(f,{}).setdefault(mode,[]).append(result)

for file,tests in sorted(all.items()):
    print(file)
    for mode,tests in tests.items():
        times=[]
        for test in tests:
            times.append( test['seconds'] )
            # print(f"  - {mode:5s} : {test['seconds']} ({test['version']}) ({test['timestamp']})")
        seconds = statistics.median( times )
        print(f"  - {mode:5s} : {seconds:.03f} ({len(times)}x, {min(times):.03f}><{max(times):.03f})")
    print()