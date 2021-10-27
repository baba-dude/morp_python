#!/usr/bin/env python
import glob
import os
report_path = os.getcwd() + "/report/*patch_report*.json"
read_files = glob.glob(report_path)

final_report = os.getcwd() + "/role_linux_inspec/files/merged_file.json"
with open(final_report, "wb") as outfile:
    outfile.write('[{}]'.format(
        ','.join([open(f, "rb").read() for f in read_files])))
