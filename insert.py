import sys
import os
import sqlite3

ind = open(sys.argv[1]).readlines()

dinsert = {}
db = sqlite3.connect("samples.db")
cursor = db.cursor()

for i in range(1, len(ind)):
    temp = ind[i].rstrip().split('\t')
    dinsert['clone'] = temp[0]
    dinsert['chromosome'] = temp[1]
    if not temp[2] == 'no info': 
        dinsert['startpos'] = int(temp[2].split('-')[0])
        dinsert['endpos'] = int(temp[2].split('-')[1])
    else:
        dinsert['startpos'] = dinsert['endpos'] = 0
    dinsert['antibiotic'] = temp[3]
    dinsert['tubes'] = int(temp[4])
    dinsert['dnaex'] = temp[5]
    dinsert['gene'] = temp[6]
    dinsert['box'] = int(temp[7].split(';')[0])
    dinsert['cell'] = temp[7].split(';')[1].strip()
    dinsert['comments'] = temp[8]
    dinsert['projects'] = temp[9]
    dinsert['pcr'] = temp[10]
    dinsert['validation'] = temp[11]
    cursor.execute("INSERT INTO bac (projects, comments, cell, box, tubes, chromosome, clone, startpos, endpos, gene, dnaex, validation, pcr, antibiotic) VALUES (:projects, :comments, :cell, :box, :tubes, :chromosome, :clone, :startpos,:endpos, :gene, :dnaex, :validation, :pcr, :antibiotic)", dinsert)
    print dinsert
    db.commit()
db.close()
#    , , temperature, , ,, source, 
#        location1, , , , genelink, , , , refs, 


    
    
#    cur.execute("INSERT INTO %s (projects, comments, cell, box, tubes, chromosome, clone, startpos, endpos, gene, dnaex, validation, pcr, antibiotic) VALUES (:projects, :comments, :cell, :box, :tubes, :chromo, :clone, :start,:end, :gene, :dna, :validation, :pcr, :antibiotic)", dinsert)
