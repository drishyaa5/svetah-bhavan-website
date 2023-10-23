import xlsxwriter

data = [
    {
        'name': "Drishya",
        'phone': "91823912",
        'email': "dri@gmail.com",
        'address': "sukedhara",
        'country': "Nepal"
    },
    {
        'name': "Cal",
        'phone': "91823912",
        'email': "cal@gmail.com",
        'address': "sukedhara",
        'country': "Nepal"
    },
    {
        'name': "Deepali",
        'phone': "91823912",
        'email': "deepali@gmail.com",
        'address': "sukedhara",
        'country': "Nepal"
    },
    {
        'name': "Rajan",
        'phone': "91823912",
        'email': "raj@gmail.com",
        'address': "sukedhara",
        'country': "Nepal"
    },
    {
        'name': "Kopila",
        'phone': "91823912",
        'email': "kops@gmail.com",
        'address': "sukedhara",
        'country': "Nepal"
    }
    ]



workbook = xlsxwriter.Workbook("trial.xlsx")
worksheet = workbook.add_worksheet("firstSheet")

worksheet.write(0,0,"#")
worksheet.write(0,1,"Name")
worksheet.write(0,2,"Phone")
worksheet.write(0,3,"Email")
worksheet.write(0,4,"Address")
worksheet.write(0,5,"Country")


for index,entry in enumerate(data):
    worksheet.write(index+1,0,str(index+1))
    worksheet.write(index+1,1,entry["name"])
    worksheet.write(index+1,2,entry["phone"])
    worksheet.write(index+1,3,entry["email"])
    worksheet.write(index+1,4,entry["address"])
    worksheet.write(index+1,5,entry["country"])


workbook.close()

