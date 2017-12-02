import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet('first')
workbook.add_worksheet()
workbook.add_worksheet('third')

bold = workbook.add_format()
bold.set_bold()

worksheet.write('A1', 'hello')
worksheet.write('B1', 'world', bold)
worksheet.write('C1', 'yes', bold)

worksheet.write('A2', 3)
worksheet.write('B2', 5)
worksheet.write('C2', '=SUM(A2+B2)')

worksheet.set_column('A:A', 20)
worksheet.set_column('C:C', 20)

worksheet.insert_image('A5', 'C:\Users\Administrator\Pictures\weight.PNG')

chart = workbook.add_chart({'type': 'pie'})
chart.add_series({
                  'categories':'=first!$A$1:$C$1', 
                  'values':'=first!$A$2:$C$2', 
                  'points':[
                            {'fill':{'color':'#5ABAFE'}}, 
                            {'fill':{'color':'#FE110E'}}, 
                            {'fill':{'color':'#BA55D3'}}, 
                    ], 
                  })
chart.set_title({'name':'my chart test'})
worksheet.insert_chart('C5', chart)


workbook.close()
