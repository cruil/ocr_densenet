#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 18:42
# @Author : caius
# @Site : 
# @File : show_black.py
# @Software: PyCharm

import os
import sys
import json
sys.path.append('../ocr')
from utils import parse, py_op
args = parse.args

def cp_black_list(black_json, black_dir):
    word_index_dict = json.load(open(args.word_index_json))
    index_word_dict = { v:k for k,v in word_index_dict.items() }
    train_word_dict = json.load(open(args.image_label_json))
    train_word_dict = { k:''.join([index_word_dict[int(i)] for i in v.split()]) for k,v in train_word_dict.items() }

    py_op.mkdir(black_dir)
    black_list = json.load(open(black_json))['black_list']
    for i,name in enumerate(black_list):
        cmd = 'cp {:s} {:s}'.format(os.path.join(args.data_dir, 'train', name), black_dir)
        if train_word_dict[name] in ['Err:501', '#NAME?', '###']:
            continue
        print(name)
        print(train_word_dict[name])
        os.system(cmd)
        if i > 30:
            break

if __name__ == '__main__':
    black_dir = os.path.join(args.save_dir, 'black')
    cp_black_list(args.black_json, black_dir)
