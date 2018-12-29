#!/usr/bin/python
#! -*- encoding: utf-8 -*-

#This script will run all daily jobs, control by crontab
#Example:
#    $ python run_daily_jobs.py
#Author:    liweiwesley@didichuxing.com

import os
import subprocess
import sys
import datetime
import time

ROOT_PATH = "/nfs/project/web/localization/dailyjobs"
CONFIG_FILE = ROOT_PATH + '/tools/job.config' # job config files
today_dir=str(datetime.date.today().strftime('%Y%m%d'))
    
JobValidationSetDict = {}

# ======================================================
# load daily running jobs 
# =======================================================
def load_job_config():
    dicFile = open(CONFIG_FILE, 'r')
    while True:
        line = dicFile.readline()
        if line == '':
            break
        kv = line.split(' ')
        key = kv[0]
        value = kv[1]
        JobValidationSetDict[key] = value
    dicFile.close()

# ======================================================
# Desc: run scrips
# Args:
#       file:   the running scripts
#       log:   the output localization file log
# Return:
# =======================================================
def run_script(file, log):
    res_path = log.replace(".log","")
    if not os.path.exists(res_path):
        os.mkdir(res_path)
    log = os.path.join(res_path, os.path.basename(log))
    #os.chdir(path)
    cmd = "sh " + file + " > " + log + "&"
    print cmd
    status = os.system(cmd)
    time.sleep(1)
 
# ======================================================
# Desc: check job finished or not
# Args:
#       file:   check job done?
# Return: success?
# =======================================================
def is_job_end(file):
    res=os.popen('tail ' + file + ' | grep Done | wc -l ').read()
    return int(res)

# ======================================================
# Desc: get all success localization results
# Args: 
#       file:   retrieve all success results
#       distance_dir:   cal distance file path
#       validation_file: related validation set
# =======================================================
def get_success_result(file, distance_dir, validation_file):
    #print os.path.dirname(file)
    os.chdir(os.path.dirname(file))
    res = file.replace(".log", "_result.txt")
    if os.path.exists(res):
        os.popen('rm ' + res)
    cmd = 'cat ' + file + ' | grep ___PerfTestSuccess___ >' + res
    os.popen(cmd)
    cmd = 'sh ' + distance_dir + '/distance.sh ' + validation_file.strip('\n') + ' ' + res + ' > performance.txt'
    print cmd
    os.popen(cmd)

def open_performance_txt(performance_txt, file):
    content = ''
    if os.path.getsize(performance_txt) > 0:
        perf_file = open(performance_txt, 'r')
        content += '<tr>'
        content += '<td>' +os.path.basename(file).replace(".log","")+ '</td>'
        while True:
            line = perf_file.readline()
            if line == '':
                break
            content += '<td>' +line.split(':')[1]+ '</td>'
        content += '</tr>'
        perf_file.close()
    return content
    
def open_performance_txt_with_date(performance_txt, file):
    content = ''
    if os.path.getsize(performance_txt) > 0:
        perf_file = open(performance_txt, 'r')
        date = file.split('/')[-4]  
        content += '<tr>'
        content += '<td>' +date+'</td>'
        content += '<td>' +os.path.basename(file).replace(".log","")+ '</td>'
        while True:
            line = perf_file.readline()
            if line == '':
                break
            content += '<td>' +line.split(':')[1]+ '</td>'
        content += '</tr>'
        perf_file.close()
    return content

# ======================================================
# Desc: integrate all performance.txt into html
# =======================================================
def integrate():
    #load integration html template
    integration_ = open('/home/luban/sutenghui/myweb/others/integration.template',"r").read()
    content = ''
    for parent,dirnames,filenames in os.walk(ROOT_PATH):
        for filename in filenames:
            file=os.path.join(parent, filename)
            if filename == 'performance.txt':
                  
                



# ======================================================
# Desc: retreive all finished jobs
# =======================================================
def parse_jobs():
    #check the job done or not
    if not os.path.exists(os.path.join(ROOT_PATH, today_dir)):
        print "daily job of "+today_dir+" not start yet!"
        os._exit(0)
        
    print "start parse daily job in "+os.path.join(ROOT_PATH, today_dir)
    #load table html template
    table_ = open(os.path.join(ROOT_PATH, 'tools/table.template'),"r").read()
    
    content = ''
    #walk dir recursively, and run each script bg
    for parent,dirnames,filenames in os.walk(os.path.join(ROOT_PATH, today_dir)):
        for dirname in  dirnames:
            tmp=os.path.join(parent, dirname)
            
        for filename in filenames:
            file=os.path.join(parent, filename)
            performance_txt=os.path.join(parent, 'performance.txt')
            if "log" in file:
                if is_job_end(file) > 0 and not os.path.exists(performance_txt):
                    print "\n\n\n#================================================"
                    print "#job finished, start parsing..."
                    print "#FileName: " + file
                    print "#================================================"
                    distance_dir = os.path.join(ROOT_PATH, "tools")
                    job_name = os.path.basename(file).replace(".log","")
                    get_success_result(file, distance_dir, JobValidationSetDict[job_name])
                    content += open_performance_txt(performance_txt, file);
                    print "#######################Finished#####################"
                elif is_job_end(file) > 0 and os.path.exists(performance_txt):
                    # create html table
                    content += open_performance_txt(performance_txt, file);
                    print "\n\n\n#================================================"
                    print "#job parse finished or parsing by other process"
                    print "#FileName: " + file
                    print "#================================================" 
                else:
                    print "\n\n\n#================================================"
                    print "#job still running...."
                    print "#FileName: " + file
                    print "#================================================" 
    
    
    htmlfile = open(ROOT_PATH + "/"+ today_dir+"/report.html","w")
    htmlfile.write(table_.replace("____TABLE____", content))
    htmlfile.close()

# ======================================================
# Desc: start run today jobs
# =======================================================
def run_jobs():
    os.mkdir(os.path.join(ROOT_PATH, today_dir))
    print "Run daily job in "+os.path.join(ROOT_PATH, today_dir)
    
    #walk dir recursively, and run each script bg
    for parent,dirnames,filenames in os.walk(os.path.join(ROOT_PATH, "scripts")):
        for dirname in  dirnames:
            parent=parent.replace("scripts", today_dir)
            tmp=os.path.join(parent, dirname)
            if not os.path.exists(tmp):
                os.mkdir(tmp)
            
        for filename in filenames:
            file=os.path.join(parent, filename)
            print "\n\n\n#================================================"
            print "# start job fileName: " + file
            print "#================================================" 
            run_script(file,file.replace("scripts", today_dir).replace("sh","log"))


# Let's go
if __name__ == "__main__":
    load_job_config()
    #check the job done or not
    if os.path.exists(os.path.join(ROOT_PATH, today_dir)):
        print "daily job of "+today_dir+" finished"
        parse_jobs()
    else:
        run_jobs()




