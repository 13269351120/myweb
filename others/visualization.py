#!/usr/bin/python
#! -*- encoding: utf-8 -*-

#This script will find all the performance.txt and merge it and show it 
#By author sthsutenghui@didiglobal.com  2018.12.29

import os
import subprocess
import sys
import datetime
import time
import commands 
import re 


## Default Path 
task_path = "/nfs/project/web/localization/dailyjobs" 
template_path = "/nfs/project/sutenghui/html_template/"

table = ""
date = []
mean = []
median = []
rate = []

task_name = []
def gat_performance(task_path , filename):
    all_path = []
    task_names = [] 
    for parent,dirnames,filenames in os.walk(task_path):
        
        # path = os.path.join(parent , filenames)
        for m_file in filenames :
            if (m_file == filename ) : 
                absolute_path = os.path.join(parent, m_file)
                print "\033[1;32m[path] : \033[0m" + absolute_path 
                # :/nfs/project/web/localization/dailyjobs/20181228/gary/gary_SoftwareParkOne_iphone7p_20181210_iphone7p_populated_20181128_cuJEPG/performance.txt 
                info_arr = absolute_path.split('/') 
                task_names.append( info_arr[-2] ) 
                all_path.append(absolute_path)
            #else:
                #print "\033[1;31m[path] :\033[0m "+ os.path.join(parent, m_file)
    task_names = list(set(task_names))
    return (all_path,task_names)

def deal_with_each_task(all_path , task_name) : 
    table = "" 
    date = []
    mean = []
    median = []
    rate = []
    content = ""
    print "\033[1;41m[TASK_NAME]:" + task_name + "\033[0m"
    for each_path in all_path :
        if ( each_path.find(task_name) != -1) :
            f = open(each_path,'r')
            alllines = f.readlines()
 
            
            if(len(alllines) < 4) :
                print "\033[1;31m" + each_path + " is not finished ! \033[0m" 
            info_arr = each_path.split('/')
            date.append(info_arr[6]) 
            
            mean_error = filter(lambda ch: ch in '0123456789.' ,alllines[1])
            median_error = filter(lambda ch: ch in '0123456789.' ,alllines[2])
            rate_ = filter(lambda ch: ch in '0123456789.' ,alllines[3])

            mean.append(mean_error)
            median.append(median_error) 
            rate.append(rate_)
            content += read_performance_txt(each_path , task_name) 

    print "\033[1;32m[mean] :\033[0m" + str(mean) 
    print "\033[1;32m[median] :\033[0m" + str(median) 
    print "\033[1;32m[rate] : \033[0m" + str(rate) 
    print "\033[1;32m[date] : \033[0m" + str(date)
    
    return (content , mean , median , rate , date) 

## 
def read_performance_txt(performance_txt , task_name):
    content = ''
    path_info_arr = performance_txt.split('/')
    date = path_info_arr[6]

    if os.path.getsize(performance_txt) > 0:
        perf_file = open(performance_txt, 'r')
        content += '<tr>'
        content += '<td>' + date + '</td>'
        content += '<td>' + task_name + '</td>'
        while True:
            line = perf_file.readline()
            if line == '':
                break
            arr = line.split(':')
            if(len(arr) < 2) :
                content += '<td> NONE </td>' 
            else :
                content += '<td>' +line.split(':')[1]+ '</td>'
        content += '</tr>'
        perf_file.close()
    return content



if __name__ == "__main__":
    (all_path , task_names ) = gat_performance(task_path,"performance.txt")
    all_content = "" 
    
    table_3 = open(os.path.join(template_path , '3.html'),"r").read()
    
    all_table2 = "" 

    htmlfile = open(template_path + "/report.html","w") 
    for task_name in task_names : 
        (content , mean , median , rate , date) = deal_with_each_task(all_path , task_name) 
        all_content += content 
        table_2 = open(os.path.join(template_path , '2.html'),"r").read().replace("____ERRORTITLE____","error_"+task_name).replace("____RATETITLE____","rate_"+task_name).replace("____date____",str(date)).replace("____Mean____",str(mean)).replace("____Median____",str(median)).replace("____rate____",str(rate)).replace("____taskname____",str(task_name) )
        all_table2 += table_2 
    #print "\033[1;33mall_content : " + all_content + "\033[0m" 
    table_1 = open(os.path.join(template_path , '1.html'),"r").read().replace("____TABLE____",str(all_content))
    total = table_1 + all_table2 + table_3
    htmlfile.write(total)
    htmlfile.close()




         

