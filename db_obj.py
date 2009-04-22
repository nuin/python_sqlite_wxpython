#!/usr/bin/python

import sqlite3
import sys

class DB_Generic():
    '''generic class to add DB functionality'''
    def __init__(self, table_name, db_path = ''):
        #par= name of the table to be used
        self.table_name = table_name
        if len(db_path) > 0:
            self.db_path = db_path
            print db_path
    
    def get_data_generic(self, range = 1, bac_to_get = 0):
        '''gets the data from the database
        generic so far, needs to be updated to include range'''        
        

        if sys.platform == 'darwin':
            (cursor, database) = link_db(self.db_path)
        else:
            (cursor, database) = link_db()
        
        if range == 1:
            cursor.execute("""SELECT * FROM %s""" % self.table_name)
        elif range == 2:
            cursor.execute("""SELECT * FROM %s where idbac = %d""" % (self.table_name, bac_to_get))

        table_data = cursor.fetchall()
        raw_data = []
        for i in table_data:
            raw_data.append(list(i))
        
        self.table_data = raw_data
        database.close()

    def insert_data(self, values_list, insert_string):
        '''inserts data in the database'''
        
        if sys.platform == 'darwin':
            (cursor, database) = link_db(self.db_path)
        else:
            (cursor, database) = link_db()

        cursor.execute(insert_string % self.table_name, values_list)

        database.commit()
        database.close()

    def update_data(self, update_string):
        '''edits and updates fields'''
        
        if sys.platform == 'darwin':
            (cursor, database) = link_db(self.db_path)
        else:
            (cursor, database) = link_db()
        cursor.execute(update_string)
        
        database.commit()
        database.close()

    def delete_data(self, delete_string):
        '''deletes one field'''
       
        if sys.platform == 'darwin':
            (cursor, database) = link_db(self.db_path)
        else:
            (cursor, database) = link_db()
        cursor.execute(delete_string)
        
        database.commit()
        database.close()

class Bac(DB_Generic):
    def __init_(self):
        self.bac_data = []
        if sys.platform == 'darwin':
            DB_Generic.__init__(self, bac, db_path)
        else:
            DB_Generic.__init__(self, 'bac')
        
    def get_data(self, range = 1, bac_to_get = 0):
        self.get_data_generic(range, bac_to_get)
        return self.table_data
        
    def load_data(self):
        pass

    def add_data(self, values_list):
        insert_string = """INSERT INTO %s (projects, comments, temperature, cell, box, tubes, chromosome, sdate, clone, source, 
        location1, startpos, endpos, gene, genelink, dnaex, validation, pcr, refs, antibiotic) 
        VALUES (:projects, :comments, :temperature, :cell, :box, :tubes, :chromosome, :sdate, :clone, :source, :location1, :startpos,
        :endpo, :gene, :genelink, :dnaex, :validation, :pcr, :refs, :antibiotic)"""
        self.insert_data(values_list, insert_string)

    def edit_data(self, values_list):    
        update = ','.join(['%s=\"%s\"' % (y, values_list[y]) for y in values_list])
        edit_string = 'UPDATE bac set ' + update + ' where idbac=' + values_list['idbac']
        self.update_data(edit_string)

    def delete_entry(self, idbac):
        delete_string = "DELETE from bac WHERE idbac = %s" % idbac
        self.delete_data(delete_string)


##########################
def link_db(db_path =''):
    '''initializes the database file'''
    try:
        if not sys.platform == 'darwin':
            db = sqlite3.connect("samples.db")
        else:
            print db_path
            db = sqlite3.connect(str(db_path))
    except sqlite3.Error, errmsg:
        print 'DB not available ' + str(errmsg)
        sys.exit()

    db_cursor = db.cursor()
    return db_cursor, db


#"legacy code"
#        cursor.execute('UPDATE %s set %s where %s=%s' % self.table_name, insert, values_list, "idbac", )
    
#        cursor.execute("UPDATE bac SET  projects = ?, comments = ?, temperature = ?, cell = ?, box = ?, tubes = ?, chromosome = ?, sdate = ?, clone = ?, source = ?, location1 = ?, startpos = ?, endpos = ?, gene = ?, genelink = ?, dnaex = ?, validation = ?, pcr = ?, refs = ?, antibiotic = ? WHERE idbac = ?",                        
#        (values_list['projects'], values_list['comments'], values_list['temperature'], values_list['cell'], values_list['box'], values_list['tubes'], 
#         values_list['chromo'], values_list['date'], values_list['clone'], values_list['source'], values_list['location'], values_list['start'], values_list['end'],
#         values_list['gene'], values_list['genelink'], values_list['dna'], values_list['validation'], values_list['pcr'], 
#         values_list['refs'], values_list['antibiotic'], values_list['idbac']))
    
