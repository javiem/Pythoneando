#!/usr/bin/python
#-*- coding: latin-1 -*-
import wx

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Cremos algunos sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)    # Cremos un sizer vertical padre
        grid = wx.GridBagSizer(hgap=5, vgap=5)  # Una red cuadriculada de 5 * 5
        hSizer = wx.BoxSizer(wx.HORIZONTAL)     # Y un sizer horizontal hijo 

        self.quote = wx.StaticText(self, label="Una label de texto estático: ")
        
        # Añadimos el texto estático en la posición 0,0
        grid.Add(self.quote, pos=(0,0))

        self.logger = wx.TextCtrl(self, size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.button =wx.Button(self, label="Guardar")
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        self.lblname = wx.StaticText(self, label="Tu nombre :")
        
        # El texto del nombre estático en 1,0
        grid.Add(self.lblname, pos=(1,0))
        self.editname = wx.TextCtrl(self, value="", size=(140,-1))
        
        # Ya vemos de qué va la cosa...
        grid.Add(self.editname, pos=(1,1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        self.sampleList = ['Aburrido', 'Mola', 'Lo mejor', 'Alucinante']
        self.lblhear = wx.StaticText(self, label="Qué te parece el programa: ")
        grid.Add(self.lblhear, pos=(3,0))
        self.edithear = wx.ComboBox(self, size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        grid.Add(self.edithear, pos=(3,1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)

        # Podemos añadir un espacio en blanco en una posición
        grid.Add((10, 40), pos=(2,0))

        self.insure = wx.CheckBox(self, label="¿Quieres doble de queso en la pizza?")
        grid.Add(self.insure, pos=(4,0), span=(1,2), flag=wx.BOTTOM, border=5)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        radioList = ['azul', 'rojo', 'amarillo', 'naranja', 'verde', 'lila', 'negro', 'gris']
        rb = wx.RadioBox(self, label="¿Cuál es tu color favorito?", pos=(20, 210), choices=radioList,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        grid.Add(rb, pos=(5,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

        hSizer.Add(grid, 0, wx.ALL, 5)  # Añadimos la grid y el loguer al sizer horizontal
        hSizer.Add(self.logger)
        mainSizer.Add(hSizer, 0, wx.ALL, 5) # Y el sizer horizontal al vertical
        mainSizer.Add(self.button, 0, wx.CENTER)    # Por último nos falta añadir el botón
        self.SetSizerAndFit(mainSizer)  # Y establecer el tamaño automático del size padre
        
    
    def EvtRadioBox(self, event):
        self.logger.AppendText('Evento de radio box: %d\n' % event.GetInt())
    def EvtComboBox(self, event):
        self.logger.AppendText('Evento de combo box: %s\n' % event.GetString())
    def OnClick(self,event):
        self.logger.AppendText("Clic en el objeto con Id %d\n" % event.GetId())
    def EvtText(self, event):
        self.logger.AppendText('Evento de texto: %s\n' % event.GetString())
    def EvtChar(self, event):
        self.logger.AppendText('Evento de carácter: %d\n' % event.GetKeyCode())
        event.Skip()
    def EvtCheckBox(self, event):
        self.logger.AppendText('Evento de check box: %d\n' % event.Checked())    
    
app = wx.App(False)
frame = wx.Frame(None, title="Controles y eventos", size=(550,420))
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()