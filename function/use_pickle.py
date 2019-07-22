#!/user/bin/env python3
# -*- coding: utf-8 -*-

import pickle

d = dict(name='zyx',age=20,score=90)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)
