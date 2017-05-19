#!/bin/bash
input="./all_ips.txt"

rm ./check_result/exist_in_MHL.txt
rm ./check_result/not_found_in_MHL.txt
rm ./check_result/exist_but_commented.txt
rm ./check_result/subnet_exist_in_MHL.txt
#rm ./check_result/subnet_not_found_in_MHL.txt
rm ./check_result/temp_file.txt

while IFS= read -r var
do
	grep -i "$var" ./mhl.txt >> ./check_result/exist_in_MHL.txt || echo $var >> ./check_result/not_found_in_MHL.txt
done < "$input"
	grep -i "#" ./check_result/exist_in_MHL.txt >> ./check_result/exist_but_commented.txt

echo "All IPs that exist in ACL and can be found in MHL have been recorded to exist_in_MHL.txt"
echo "All IPs can not be found in MHL have been recorded to not_found_in_MHL.txt"
echo "All IPs exist in ACL but have commented in MHL have been recorded to exist_but_commented.txt"


#input="./all_subnet.txt"

#while IFS= read -r var
#do
	#echo $var
#	grep -i "$var" ./mhl.txt >> ./check_result/subnet_exist_in_MHL.txt || echo $var >> ./check_result/temp_file.txt
#done < "$input"
