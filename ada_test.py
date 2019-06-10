#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import os
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--address')
parser.add_argument('--filename_to_write')
args = parser.parse_args()

y=args.address

x=os.listdir(args.address)
z=y.split('/')
if y[-1]=='/':
    parent_name=z[-2]
else:
    parent_name=z[-1]
parent_name


with open(args.address+'/'+ args.filename_to_write, "w+") as file_object:
	file_object.write('/* \n')
	#file_object.write('!/{}/ \n'.format(parent_name))
	#file_object.write('/{}/* \n'.format(parent_name))
	#file_object.write('!/{}/*.md \n'.format(parent_name))
	for i in x :
		if os.path.isdir(os.path.realpath(os.path.join(args.address,i))):
		    file_object.write('!/{} \n'.format(i))
		    file_object.write('/{}/* \n'.format(i))
		    file_object.write('!/{}/*.md \n'.format(i))


