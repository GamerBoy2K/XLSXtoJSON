import requests
import pandas
import os
#url = input("Enter the URL")
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRPmiXyhDRj_7CdfUmEHHjvi2YcYvw7-Mo2F_0Fb7EsMCVkRtznznsDqq9Sail-9FpC-zB7su4Do_AM/pub?output=xlsx'
r = requests.get(url, allow_redirects=True)  # to get content after redirection
open('temp.xlsx', 'wb').write(r.content)


xls = pandas.ExcelFile('temp.xlsx')
for sheet_name in xls.sheet_names:
	shenamejson=sheet_name+".json"
	excel_data_df = pandas.read_excel('temp.xlsx', sheet_name)
	json_str = excel_data_df.to_json(shenamejson,orient='records')
# shename='Snacks'
# shenamejson="Snacks"+".json"
# excel_data_df = pandas.read_excel('temp.xlsx', shename)
# json_str = excel_data_df.to_json(shenamejson,orient='records')
#print('Excel Sheet to JSON:\n', json_str)
xls.close()
os.remove("temp.xlsx")