# This script can be used for replacing part of text inside database table
import csv
# Input File
# column 1 -> Old text
# column 2 -> New text
csvFile = 'input.csv'
# Old SQL File
oldFile = 'old.sql'
# New SQL File
newFile = 'new.sql'
# list from csv file
old_new_text = []
# SQL file content
sqlContent = None

with open(csvFile) as file:
  content = csv.reader(file, delimiter=',')
    for row in content:
      links.append(row)

reader = open(oldFile, "r")
sqlContent = reader.read()
reader.close()

if sqlContent is not None:
 for text in old_new_text:
  sqlContent = sqlContent.replace(old_new_text[0], old_new_text[1], 1)

writer = open(newFile, 'w')
writer.write(sqlContent)
writer.close()
