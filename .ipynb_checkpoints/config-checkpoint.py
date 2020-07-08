from docx import Document 

document = Document("C:\\Users\\srinidhi.emkay\\Documents\\PersonalGit\\DocxToConfigXML\\file.docx")

tables = document.tables
for row in tables[2].rows:
   print("#######")
   print(row[0].text)
   print("#######")