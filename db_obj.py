#!/usr/bin/python



import sqlite3
import sys

class DB_Generic():
    '''generic class to add DB functionality'''
    def __init__(self, table_name):
        #par= name of the table to be used
        self.table_name = table_name
        
    def delete_entry(self):
        pass
    
    def get_data_generic(self):
        '''gets the data from the database
        generic so far, needs to be updated to include range'''        
        
        range = 1        
        (cursor, database) = link_db()
        
        if range == 1:
            cursor.execute("""SELECT * from %s""" % self.table_name)

        table_data = cursor.fetchall()
        raw_data = []
        for i in table_data:
            raw_data.append(list(i))
        
        self.table_data = raw_data
        
        database.close()

    def insert_data(self, values_list, insert_string):
        '''inserts data in the database'''
        
        (cursor, database) = link_db()

        cursor.execute(insert_string % self.table_name, values_list)

        database.commit()
        database.close()

#cur.executemany("insert into log (IP, EntryDate, Requestt, ErrorCode) values (:ip, :date, :request, :errorcode)", values) 


class Bac(DB_Generic):
    def __init_(self):
        self.bac_data = []
        DB_Generic.__init__(self, 'bac')
        
    def get_data(self):
        self.get_data_generic()
        return self.table_data
        
    def load_data(self):
        pass

    def add_data(self, values_list):
        insert_string = """INSERT INTO %s (projects, comments, temperature, cell, box, tubes, chromosome, sdate, clone, source, 
        location1, startpos, endpos, gene, genelink, dnaex, validation, pcr, refs, antibiotic) 
        VALUES (:projects, :comments, :temperature, :cell, :box, :tubes, :chromo, :date, :clone, :source, :location, :start,
        :end, :gene, :genelink, :dna, :validation, :pcr, :refs, :antibiotic)"""
        self.insert_data(values_list, insert_string)


##########################
def link_db():
    '''initializes the database file'''
    try:
        db = sqlite3.connect("samples.db")
    except sqlite3.Error, errmsg:
        print 'DB not available ' + str(errmsg)
        sys.exit()

    db_cursor = db.cursor()
    return db_cursor, db
