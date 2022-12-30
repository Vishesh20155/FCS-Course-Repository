import subprocess
# x = "foobar.iiitd.edu.in"
# subprocess.call("host '%s' >> pvt_ip.txt" % x, shell=True)

import csv
 
with open('Subdomains.csv', mode ='r')as file:
    csvFile = csv.reader(file)

    csvFileList = []
    for lines in csvFile:
        csvFileList.append(lines)

    # print(len(csvFileList))
public_ip_map = {}
for lines in csvFileList:
    if lines[0]=="Hostname" or lines[0]=='ns1.iiitd.edu.in.' or lines[0]=='ns2.iiitd.edu.in.' or lines[0]=='ns2.iiitd.edu.in' or lines[0]=='ns1.iiitd.edu.in' or lines[0]=='cellatlassearch.iiitd.edu.in' or lines[0]=='ecell.iiitd.edu.in':
        continue

    else:
        x = lines[0]
        subprocess.call("host '%s' >> pvt_ip.txt" % x, shell=True)
        public_ip_map[x]=lines[1]

with open('SubdomainMappings.csv', 'w', newline='') as file1:
    writer = csv.writer(file1)
    writer.writerow(["Subdomain", "Private IP", "Public IP"])

txtFileList = []
with open('pvt_ip.txt', 'r') as file2:
    txtFile = file2.readlines()

    for l in txtFile:
        txtFileList.append(l)

with open('SubdomainMappings.csv', 'w', newline='') as file1:
    writer = csv.writer(file1)
    writer.writerow(["Subdomain", "Private IP", "Public IP"])
    
    for l in txtFileList:
        l1 = []
        l1 = l.split(' ')
        print(l1[0]+':['+l1[-1][:-1]+']')
        if l1[0] in public_ip_map.keys():
            writer.writerow([l1[0], l1[-1][:-1], public_ip_map[l1[0]]])


