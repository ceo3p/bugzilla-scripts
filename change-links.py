import csv

# ulazni fajl sa linkovima
# kolona 1 -> stari link
# kolona 2 -> novi link
csvFile = 'links.csv'

# tabela koja treba da se promeni
# longdesc
sqlFile = 'ulaz.sql'

# izlazni fajl posle promene
newFile = 'izlaz.sql'


links   = []
with open(csvFile) as file:
	content = csv.reader(file, delimiter=',')
	for row in content:
		links.append(row)

sqlContent = None
sqlReader  = open(sqlFile, "r")
sqlContent = sqlReader.read()
sqlReader.close()

if sqlContent is not None:
 for link in links:
  sqlContent = sqlContent.replace(link[0], link[1], 1)

file = open(newFile, 'w')
file.write(sqlContent)
file.close()
