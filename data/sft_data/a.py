#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import re

f_write = open('dev.json', "w")
items = []
with open('dev-fact.json') as f_read:
    lines = f_read.readlines()
    for line in lines:
        data = json.loads(line)
        # if len(data['history']) > 0:
        #     instruction, output = data['history'][0][0], data['history'][0][1]
        # else:
        #     instruction, output = data['prompt'], data['response']
        # items.append({"instruction": instruction, "output": output, 'input': ''})
        items.append({
            "instruction": data['prompt'], "output": data['response'],
            "history": data['history'], "input": "",
        })

f_write.write(json.dumps(items, ensure_ascii=False))
f_write.close()
