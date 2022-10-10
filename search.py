from xlrd import open_workbook

book = open_workbook('IT DEPT details.csv',on_demand=True)
prompt = '>'
print("Please enter a Zip Code.")
item = input(prompt)
sheet = book.sheet_by_index(0)
for cell in sheet.col(1): 
    print("Data: ",cell.row)
