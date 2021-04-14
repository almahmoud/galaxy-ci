import json
import sys
args = sys.argv
with open(args[1], 'r') as f:
    old = json.load(f)
with open(args[2], 'r') as f:
    new = json.load(f)
def make_dict(l):
    out = {}
    for i in l:
        outl = out.get(i.get('id'), [])
        outl.append(i)
        out[i.get('id')] = outl
    return out
oldids = make_dict(old['tests'])
newids = make_dict(new['tests'])
nowremoved = {}
for i in oldids.keys():
    if i not in newids.keys():
        nowremoved[i] = newids[i]
print("Writing summary to: {}.summary".format(args[3]))
with open("{}.summary".format(args[3]), 'w') as f:
    f.write("{} Total removed tests. Full list Below:\n\n".format(str(len(nowremoved.keys()))))
    f.write("\n".join(list(nowremoved.keys())))


print("Writing json test details to: {}.json".format(args[3]))
with open("{}.json".format(args[3]), 'w') as f:
    json.dump(nowremoved, f)
