ctags -f - -R | grep -e "\.cpp" | awk '{print $1","$2}' | sed 's/\/\^//' > functions_list.txt
cat ./functions_list.txt > functions_list0.csv
#python3 ~/codes/scripts/xml2csv.py xml/.
#python3 ~/codes/scripts/funcList2diagram.py doxygen_output_combined.csv
#cat doxygen_output_combined.csv | grep -e "function" > functions.csv 
python3 ~/codes/scripts/list_callee4.py functions_list0.csv .
