import re

#file_name = input("Please input the file name that you gonna search for IPs (include extension):")
file_object = open('./acl_pa5050.txt')
try:
    all_the_text = file_object.read()
finally:
    file_object.close()

#print(all_the_text)    # just for testing
#print(type(all_the_text))

fp_ips = open('./all_ips.txt','w')
fp_subnet = open('./all_subnet.txt','w')

pattern_ip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
all_ip = list(set(pattern_ip.findall(all_the_text)))    # Find all IPs and delete the repetitive ones, convert to list again
#print(all_ip)
for i in range (0, len(all_ip)):
    #print(all_ip[i] + '\n')
    fp_ips.write(all_ip[i] + "|\n")
print("All IPs in ACL have been extracted to all_ips.txt")
print("Number of lines:"+ str(len(all_ip)))

pattern_network = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}-\d{1,2}') # The format in ACL is like 172.18.28.100-31
all_subnet = list(set(pattern_network.findall(all_the_text)))
#print(all_subnet)
for i in range (0, len(all_subnet)):
    #print(all_subnet[i] + '\n')
    all_subnet[i] = str(all_subnet[i]).replace("-","/")	#In ACL the netmask start with dash, but in MHL, start with slash. So I followed the MHL file. 
    fp_subnet.write(all_subnet[i] + "\n")
print("All subnets in ACL have been extracted to all_subnet.txt")
print("Number of lines:"+ str(len(all_subnet)))
