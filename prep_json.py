#!/usr/bin/env python
import sys
import glob
import os
import json

file_before_processing = sys.argv[1]
new_file_before_processing = '/tmp/test/'+file_before_processing
read_files = glob.glob(new_file_before_processing)
modidy_file_before_processing =  '/tmp/test/new_'+file_before_processing

read_files = glob.glob(new_file_before_processing)

with open(modidy_file_before_processing, "wb") as outfile:
    outfile.write('[{}]'.format(
        ','.join([open(f, "rb").read() for f in read_files])))

fp = open(modidy_file_before_processing, 'r')
json_file=fp.read()
fp.close()
json_list=json.loads(json_file)
for each_json in json_list:
  if 'profiles' in each_json.keys():
    if 'patches' == each_json['profiles'][0]['controls'][0]['id']:
      if len(each_json['profiles'][0]['controls'][0]['results']) > 0:
        for each_item in each_json['profiles'][0]['controls'][0]['results']:
          each_item['message']=each_item['message'].replace('\n','').replace('"','').replace('(compared using ==)','').replace(' ','').replace('expected:', 'Available Version: ').replace('got:',' and Installed Version: ')
          each_item['code_desc']=each_item['code_desc'].split()[2]
print "Json Processing Completed"


fp = open(new_file_before_processing,'w')
fp.write(json.dumps(json_list,sort_keys=True,indent=4, separators=(',', ': ')))
fp.close()
print "new_merged_file.json is created"

os.remove(modidy_file_before_processing)
