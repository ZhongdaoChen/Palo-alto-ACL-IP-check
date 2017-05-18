# Palo-alto-ACL-IP-check
Compare the IP addresses in ACL with Master Host Listing file to find outdated rules

These scripts are used to check the ACL. Put the firewall rules files(acl_pa5050.txt) to the directory. 

Run the extract_IPs_from_ACL.py to extract all IPs and network addresses. By running this script, two files will be created: all-ips.txt and all_subnet.txt

Command: python ./extract_IPs_from_ACL.py

Run the compare_acl_withMHL script to compare the IPs that exist in ACL with the MHL file. The result will be saved in the check_result folder. There are three types of IPs: exsist in MHL, exsist but commented in MHL and can not be found in MHL. 

Command: bash -f ./compare_acl_withMHL

Run the compare_subnet_withMHL.py to see which subnets can be found in MHL file.(This may take a long time because it will traverse the whole network range and python 3.5 is required)

Peter Chen
