import ipaddress
file_mhl = open('./mhl.txt')
try:
    mhl = file_mhl.read()
finally:
    file_mhl.close()

with open('./check_result/temp_file.txt') as file_object:
    for line in file_object:

        line = line[:-1]
        for temp in ipaddress.ip_network(line).hosts():
            if str(temp) in mhl:
                print("Find this:" + str(temp) + " from " + str(line))
                break

