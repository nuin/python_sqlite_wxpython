#!/usr/bin/env python

import wx
import os
import sys
import db_obj
import wx.grid as gridlib

class bac_form(wx.App):
    '''main class for the GUI application '''
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)

class bac_grid(gridlib.Grid):
    def __init__(self, parent):
        '''grid class that shows all the bacs in a table'''
        
        #initialize the grid
        gridlib.Grid.__init__(self, parent, -1)
        
        #get the data
        bac_data = db_test.get_data()

        #creates the grid using the amount of data to set number
        #of rows and columns
        if not len(bac_data) == 0:
            self.CreateGrid(len(bac_data), len(bac_data[0]))
    
            #name each column
            self.SetColLabelValue(0, 'Bac ID')
            self.SetColLabelValue(1, 'Clone')
            self.SetColLabelValue(2, 'Date')
            self.SetColLabelValue(3, 'Source')
            self.SetColLabelValue(4, 'Gene')
            self.SetColLabelValue(5, 'Chromosome')
            self.SetColLabelValue(6, 'Start')
            self.SetColLabelValue(7, 'End')
            self.SetColLabelValue(8, 'Antibiotic')
            self.SetColLabelValue(9, 'Location')
            self.SetColLabelValue(10, 'Temper.')
            self.SetColLabelValue(11, '# of tubes')
            self.SetColLabelValue(12, 'Box #')
            self.SetColLabelValue(13, 'Cell #')
            self.SetColLabelValue(14, 'Dna extr')
            self.SetColLabelValue(15, 'FISH')
            self.SetColLabelValue(16, 'PCR')
            self.SetColLabelValue(17, 'Projects')
            self.SetColLabelValue(18, 'Comments')
            self.SetColLabelValue(19, 'Link')
            self.SetColLabelValue(20, 'References')
    
            #put the data in the grid, we're done
            for i, j in enumerate(bac_data):
                for m, n in enumerate(j):
                    self.SetCellValue(i, m, str(n))
        else:
            wx.MessageBox("There is nothing in the database.\nTry adding something first")

class view_bacs(wx.Frame):
    '''frame class tha contains the grid'''
    def __init__(self, parent, id, title, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.__do_layout()
        
    def __do_layout(self):
        '''creates the layout'''
        self.bac_list = bac_grid(self)

class bacs(wx.Frame):
    '''main application frame'''
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id,  'BACs', size = (600, 400), style = wx.DEFAULT_FRAME_STYLE)
        self.__do_layout()
        self.__do_binding()

    def __do_layout(self):
        '''creates the layout'''
        
        #use a gridbagsizer in order to make conf easier
        my_sizer = self.my_sizer = wx.GridBagSizer(20, 20)
        panel = wx.Panel(self, -1, style = wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        
        bac_date = self.bac_date = wx.DatePickerCtrl(panel, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
        
        #setup of window elements
        clone = self.clone = wx.TextCtrl(panel, -1, '', size = (100, -1))
        source = self.source = wx.TextCtrl(panel, -1, '', size = (100, -1))
        projects = self.projects = wx.TextCtrl(panel, -1, '', size = (100, -1))
        chromosome = self.chromo = wx.TextCtrl(panel, -1, '', size = (100, -1))
        start = self.start = wx.TextCtrl(panel, -1, '', size = (100, -1))
        end = self.end = wx.TextCtrl(panel, -1, '', size = (100, -1))
        gene = self.gene = wx.TextCtrl(panel, -1, '', size = (100, -1))
        dna = self.dna = wx.CheckBox(panel, -1, " DNA extraction")
        validation = self.validation = wx.CheckBox(panel, -1, " FISH")
        pcr = self.pcr = wx.CheckBox(panel, -1, " PCR")       
        
        #drop-down lists
        temper_list = ['-80', '-20']
        location_list = ['Richardson', 'Botterel']
        antibiotic_list = ['chloramphenicol', 'kanamycin']
        
        comments = self.comments = wx.TextCtrl(panel, -1, '', size = (250, 54), style=wx.TE_MULTILINE)
        temperature = self.temperature = wx.ComboBox(panel, -1, '', wx.DefaultPosition,  (100, -1), temper_list, wx.CB_DROPDOWN)
        location1 = self.location = wx.ComboBox(panel, -1, '', wx.DefaultPosition,  (100, -1), location_list, wx.CB_DROPDOWN)
        antibiotic = self.anti = wx.ComboBox(panel, -1, '', wx.DefaultPosition, (100, -1), antibiotic_list, wx.CB_DROPDOWN)
        box = self.box = wx.TextCtrl(panel, -1, '', size = (100, 18))
        tubes = self.tubes = wx.TextCtrl(panel, -1, '', size = (100, 18))
        
        add_button = self.add_button = wx.Button(panel, -1, "Add", size = (120, 30))
        cancel_button = self.cancel_button = wx.Button(panel, -1, "Cancel", size = (120, 30))
        grid_button = self.grid = wx.Button(panel, -1, 'Show BAC list', size = (120, 30))
        
        #postioning elements on the grid layout
        my_sizer.Add(wx.StaticText(panel, label = 'Date'), (0, 1))
        my_sizer.Add(bac_date, (0, 2))
        
        my_sizer.Add(wx.StaticText(panel, label = 'Clone'),  (1, 1))
        my_sizer.Add(clone, (1, 2))
       
        my_sizer.Add(wx.StaticText(panel, label = 'Source'), (1, 3))
        my_sizer.Add(source, (1, 4))

        my_sizer.Add(wx.StaticText(panel, label = 'Projects'), (2, 1))
        my_sizer.Add(projects, (2, 2))

        my_sizer.Add(wx.StaticText(panel, label = 'Chromosome'),  (2, 3))
        my_sizer.Add(chromosome, (2, 4))
 
        my_sizer.Add(wx.StaticText(panel, label = 'Start position'),  (3, 1))
        my_sizer.Add(start,  (3, 2))

        my_sizer.Add(wx.StaticText(panel, label = 'End position'),  (3, 3))
        my_sizer.Add(end, (3, 4))
        
        my_sizer.Add(wx.StaticText(panel, label = 'Gene'), (4, 1))
        my_sizer.Add(gene, (4, 2))
    
        my_sizer.Add(wx.StaticText(panel, label = 'Antibiotic'),  (4, 3))
        my_sizer.Add(antibiotic, (4, 4))
    
    
        my_sizer.Add(wx.StaticText(panel, label = 'Glycerol stock'), (5, 2))
        my_sizer.Add(wx.StaticText(panel, label = 'Location'), (6, 1))
        my_sizer.Add(location1, (6, 2))

        my_sizer.Add(wx.StaticText(panel, label = 'Temperature'), (6, 3))
        my_sizer.Add(temperature, (6, 4))

        my_sizer.Add(wx.StaticText(panel, -1, label = 'Number of tubes'), (7, 1))
        my_sizer.Add(tubes, (7, 2))
        
        my_sizer.Add(wx.StaticText(panel, -1, label = 'Box and Cell #'), (7, 3))
        my_sizer.Add(box, (7, 4))

        my_sizer.Add(wx.StaticText(panel, -1, label = 'Comments'), (8, 1))
        my_sizer.Add(comments, (8, 2), (2, 4))


        my_sizer.Add(dna, (10, 1))
        my_sizer.Add(validation, (10, 2))
        my_sizer.Add(pcr, (10, 3))
        
        my_sizer.Add(add_button, (11, 1))
        my_sizer.Add(cancel_button, (11, 2))     
        my_sizer.Add(grid_button, (12, 1))

        
        my_sizer.Add((11, 10), (9, 1))
        my_sizer.Add((11, 10), (1,5))
        box = wx.BoxSizer()
        box.Add(my_sizer, 0, wx.ALL, 10)
        
        panel.SetSizerAndFit(box)
        self.SetClientSize(panel.GetSize())

    def __do_binding(self):
        '''does the binding'''
        self.Bind(wx.EVT_BUTTON, self.add_values, self.add_button)
        self.Bind(wx.EVT_BUTTON, self.show_grid, self.grid)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, self.cancel_button)
    
    def load_data_box(self):
        '''deprecated'''
        for i in self.bac_data:
            yield i     
        
    def on_load_data(self, event):
        '''deprecated'''
        db_test.load_data()
        self.bac_data = db_test.get_data() 
        self.forward.Enable(True)
        self.a = self.load_data_box()
        b = self.a.next()
        
        print b

    def move_forward(self, event):
        '''deprecated'''
        b = self.a.next()
        print b

    def add_values(self, event):
        '''insert a value in the database'''
        not_exec = False
        values_list = {}
        
        values_list['projects'] = str(self.projects.GetValue())
        values_list['comments'] = str(self.comments.GetValue())
        try:
            values_list['temperature'] = int(self.temperature.GetValue())
        except:
            wx.MessageBox('Please select a temperature to continue')
            not_exec = True
             
        box_cell = self.box.GetValue().split(' ')
        try:        
            values_list['box'] = int(box_cell[0])
            values_list['cell'] = str(box_cell[1])
        except:
            wx.MessageBox('Enter box number and cell number separated by a space')
            not_exec = True

        values_list['tubes'] = int(self.tubes.GetValue())
        values_list['chromo'] = str(self.chromo.GetValue())
        values_list['antibiotic'] = str(self.anti.GetValue())
        values_list['date'] = str(self.bac_date.GetValue())
        values_list['clone'] = str(self.clone.GetValue())
        values_list['source'] = str(self.source.GetValue())   
        try:
            values_list['location'] = str(self.location.GetValue())
        except:
            wx.MessageBox('Please select a location')
            not_exec = True
        
        try:
            values_list['start'] = int(self.start.GetValue())
        except:
            values_list.append(0)
            
        try:
            values_list['end'] = int(self.end.GetValue())
        except:
            values_list.append(0)
        
        values_list['gene'] = str(self.gene.GetValue())
        values_list['genelink'] = ''
#        
        values_list['dna'] = self.dna.GetValue()
        values_list['validation'] = self.validation.GetValue()
        values_list['pcr'] = self.pcr.GetValue()
        values_list['refs'] = ''
        
        if not_exec == False:
            db_test.add_data(values_list)

    def on_cancel(self, event):
        self.clone.SetValue('')
        self.source.SetValue('')
        self.projects.SetValue('')
        self.chromo.SetValue('')
        self.start.SetValue('')
        self.end.SetValue('') 
        self.gene.SetValue('')
        self.dna.SetValue(False)
        self.validation.SetValue(False)
        self.pcr.SetValue(False)
 
        self.comments.SetValue('')
        self.temperature.SetValue('')
        self.location.SetValue('')
        self.anti.SetValue('')
        self.box.SetValue('')
        self.tubes.SetValue('')

    def show_grid(self, event):
        '''calls the grid frame to show contents'''
        my_bacs = view_bacs(self, -1, 'BAC list', size = (600, 400), style = wx.DEFAULT_FRAME_STYLE)
        my_bacs.Show()

if __name__ == '__main__':
    
    db_test = db_obj.Bac('bac')

    app = bac_form(redirect=False)
    frame = bacs(parent=None, id = -1)
    frame.CentreOnScreen()
    frame.Show()
    app.MainLoop()
    
    
    
    
#        metadata = MetaData(db)
#    #accessing the defined table
#    dbo = Table('bac', metadata, autoload = True )
#    #selecting all data from the database
#    s = dbo.select()
#
#    g = db_table('bac')
#    g.table_data = s.execute()
#    g.print_data()
    
        #load_button = self.load_button = wx.Button(panel, -1, "Load", size = (120, 30))
        #forward_button = self.forward = wx.Button(panel, -1, ">>" , size = (60, 30))
        #back_button = self.back = wx.Button(panel, -1, "<<", size = (60, 30))
        
                #self.Bind(wx.EVT_BUTTON, self.on_load_data, self.load_button)
        #self.Bind(wx.EVT_BUTTON, self.move_forward, self.forward)
        
        
                #back_button.Enable(False)
        #forward_button.Enable(False)
        
                #my_sizer.Add(load_button, (11, 3), (2, 1))
        #my_sizer.Add(forward_button, (11, 5), (2, 1), wx.ALIGN_LEFT)
        #my_sizer.Add(back_button, (11, 4), (1, 1), wx.ALIGN_RIGHT)