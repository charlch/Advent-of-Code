from collections import Counter

data="""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
from time import time
ti = time()

data="""CHBBKPHCPHPOKNSNCOVB

SP -> K
BB -> H
BH -> S
BS -> H
PN -> P
OB -> S
ON -> C
HK -> K
BN -> V
OH -> F
OF -> C
SN -> N
PF -> H
CF -> F
HN -> S
SK -> F
SS -> C
HH -> C
SO -> B
FS -> P
CB -> V
NK -> F
KK -> P
VN -> H
KF -> K
PS -> B
HP -> B
NP -> P
OO -> B
FB -> V
PO -> B
CN -> O
HC -> B
NN -> V
FV -> F
BK -> K
VC -> K
KV -> V
VF -> V
FO -> O
FK -> B
HS -> C
OV -> F
PK -> F
VV -> S
NH -> K
SH -> H
VB -> H
NF -> P
OK -> B
FH -> F
CO -> V
BC -> K
PP -> S
OP -> V
VO -> C
NC -> F
PB -> F
KO -> O
BF -> C
VS -> K
KN -> P
BP -> F
KS -> V
SB -> H
CH -> N
HF -> O
CV -> P
NB -> V
FF -> H
OS -> S
CS -> S
KC -> F
NS -> N
NV -> O
SV -> V
BO -> V
BV -> V
CC -> F
CK -> H
KP -> C
KH -> H
KB -> F
PH -> P
VP -> P
OC -> F
FP -> N
HV -> P
HB -> H
PC -> N
VK -> H
HO -> V
CP -> F
SF -> N
FC -> P
NO -> K
VH -> S
FN -> F
PV -> O
SC -> N"""

def get_counter_for_string(s):
    # ABC -> {AB:1, BC:1}
    c = Counter()
    for a,b in zip(s[:-1], s[1:]):
        c[a+b]+=1
    return c
    

polymer_template_str, bits = data.split("\n\n")
print(polymer_template_str)
pairs = {}
for line in bits.split("\n"):
    f,t = line.split(" -> ")
    pairs[f]=t

print(time()-ti, "seconds")
polymer_template = get_counter_for_string(polymer_template_str)
print(polymer_template)


for step in range(40):
    npt = Counter()
    for k in polymer_template:
        npt[k[0]+pairs[k]]+=polymer_template[k]
        npt[pairs[k]+k[1]]+=polymer_template[k]

    polymer_template = npt


c = Counter()
for k,v in polymer_template.items():
    c[k[0]]+=v/2
    c[k[1]]+=v/2

c[polymer_template_str[0]]+=0.5
c[polymer_template_str[-1]]+=0.5
print(max(c.values())-min(c.values()))
print(time()-ti, "seconds")

