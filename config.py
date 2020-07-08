#specific to extracting information from word documents
import os
import zipfile
#other tools useful in extracting the information from our document
import re
#to pretty print our xml:
import xml.dom.minidom

document = zipfile.ZipFile("C:\\Users\\srinidhi.emkay\\Documents\\PersonalGit\\DocxToConfigXML\\file.docx")

ZipFile.read(name, pwd=None)
document.namelist()