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


#    def get_some_data(self):
#        conn = sqlite3.connect('samples.db')
#        c = conn.cursor()
#        c.execute('select * from bac')
#        a = []
##        bac_date = wx.DatePickerCtrl(panel, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
##        clone = wx.TextCtrl(panel, -1, '', size=(100, 18))
##        source = wx.TextCtrl(panel, -1, '', size=(100, 18))
##        location = wx.TextCtrl(panel, -1, '', size=(100, 18))
##        start = wx.TextCtrl(panel, -1, '', size=(100, 18))
##        end = wx.TextCtrl(panel, -1, '', size=(100, 18))
##        gene = wx.TextCtrl(panel, -1, '', size=(100, 18))
##        dna = wx.CheckBox(panel, -1, " DNA extraction")
##        validation = wx.CheckBox(panel, -1, " FISH")
##        pcr = wx.CheckBox(panel, -1, " PCR")    
##        
#        
#        for i in c:
#            print i
#            a.append(i[1].encode())
#
#        
#        print a[0]
#        
##        metadata = MetaData(bind = db, reflect = True)
##        dbo = Table('bac', metadata, autoload = True)
##        s = dbo.select()
##        g.table_data = s.execute()
##        my_data = g.table_data.fetchall()
##        print g.table_data.fetchall()
###        for i in range(len(my_data)):
###            for j in range(len(my_data[i])):
###                print my_data[i][j]
