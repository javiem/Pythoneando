#!/usr/bin/python
#-*- coding: latin-1 -*-
import wx, os

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Una label de texto estático", pos=(20, 30))

        self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.button =wx.Button(self, label="Guardar", pos=(200, 325))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        self.lblname = wx.StaticText(self, label="Tu nombre :", pos=(20,60))
        self.editname = wx.TextCtrl(self, value="", pos=(120, 60), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        self.sampleList = ['Aburrido', 'Mola', 'Lo mejor', 'Alucinante']
        self.lblhear = wx.StaticText(self, label="Qué te parece el programa :", pos=(20, 90))
        self.edithear = wx.ComboBox(self, pos=(200, 90), size=(60, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)

        self.insure = wx.CheckBox(self, label="¿Quieres doble de queso en la pizza?", pos=(20,180))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        radioList = ['azul', 'rojo', 'amarillo', 'naranja', 'verde', 'lila', 'negro', 'gris']
        rb = wx.RadioBox(self, label="¿Cuál es tu color favorito?", pos=(20, 210), choices=radioList,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

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
        
class OtherPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        
        # Creamos un sizer para ocupar todo el tamaño
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.control,1, wx.EXPAND)
        self.SetSizer(self.sizer)
    

app = wx.App(False)
# Creamos el frame padre
frame = wx.Frame(None, title="Bloc de notas", size=(540,450))
# Creamos el bloc de notas
nb = wx.Notebook(frame)
# Añadimos los paneles con Addpage
nb.AddPage(ExamplePanel(nb), "Controles y eventos")
nb.AddPage(OtherPanel(nb), "Editor Simple")
frame.Show()
app.MainLoop()