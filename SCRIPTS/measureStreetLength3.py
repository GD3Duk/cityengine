'''
Created on Apr 13, 2010 modified 2014

@author: andi modified by Elliot Hartley

USAGE
start script
select a street segment
update
-> segment data
'''

from scripting import *
from math import *
from java.awt import *
from java.awt.event import  *

# get a CityEngine instance
ce = CE()

 



def calc():
    if len(ce.getObjectsFrom(ce.selection)) < 1 or not ce.isGraphSegment(ce.selection()[0]):
        return ("No Segment Selected", "","","","","")
    
    segment = ce.selection()[0]
    
    nodes = ce.getObjectsFrom(segment)
    v0 = ce.getVertices(nodes[0])
    v1 = ce.getVertices(nodes[1])
    
    xdist = v1[0]-v0[0]
    zdist = v1[2]-v0[2]
    
    xangle = -atan(zdist/xdist)/3.14*180
    
    dist = sqrt(pow(v1[0]-v0[0],2)+pow(v1[1]-v0[1],2)++pow(v1[2]-v0[2],2))
    
    name = ce.getName(segment)
    oid = ce.getOID(segment)
    aposition = ce.getPosition(segment)
      
    return (name, oid, dist, xdist, zdist, xangle, aposition)




class Listener(WindowAdapter):
    def windowClosing(self, e):
        e.getSource().dispose()


def update(event):
    (name, oid, dist, xdist, zdist, xangle, aposition) = calc()
    event.getSource().tfield0.setText(name)
    event.getSource().tfield1.setText(str(oid))
    event.getSource().tfield2.setText(str(dist))
    event.getSource().tfield3.setText(str(xdist))
    event.getSource().tfield4.setText(str(zdist))
    event.getSource().tfield5.setText(str(xangle))
    event.getSource().tfield6.setText(str(aposition))

def cancel(event):
    event.getSource().dialog.dispose()


    
class DiaButton(Button):
    dialog = None
    tfield = None

def dialog():
    frame = Frame("MeasureFrame")
    dia = Dialog(frame, "www.GeoPlanIT.co.uk --> Measure Segment", False)
    dia.setSize(550,500)
    
    ceversion = ce.getVersion()
    l = Listener()
    dia.addWindowListener(l)

    dia.add(Label("Select Street Segment and hit Update"))
    dia.add(Label(""))
    
    dia.add(Label("CityEngine Version :"))
    dia.add(Label(ceversion))

    dia.add(Label("Name"))
    tfield0 = TextField("", 30)
    dia.add(tfield0)

    dia.add(Label("OID"))
    tfield1 = TextField("", 30)
    dia.add(tfield1)
    
    dia.add(Label("Length"))
    tfield2 = TextField("", 30)
    dia.add(tfield2)
           
    dia.add(Label("LengthX"))
    tfield3 = TextField("", 30)
    dia.add(tfield3)
    
    dia.add(Label("LengthZ"))
    tfield4 = TextField("", 30)
    dia.add(tfield4)

    dia.add(Label("xAngle"))
    tfield5 = TextField("", 30)
    dia.add(tfield5)

    dia.add(Label("Centroid Position"))
    tfield6 = TextField("", 30)
    dia.add(tfield6)

    
    b1 = DiaButton("Update & Measure", actionPerformed=update)
    b1.tfield0 = tfield0
    b1.tfield1 = tfield1
    b1.tfield2 = tfield2
    b1.tfield3 = tfield3
    b1.tfield4 = tfield4
    b1.tfield5 = tfield5
    b1.tfield6 = tfield6
    dia.add(b1)
    
    b2 = DiaButton("Cancel", actionPerformed=cancel)
    dia.add(b2)
    b2.dialog = dia
    

    
    layout = GridLayout(10,2)
    dia.setLayout(layout)
    dia.pack()
    dia.show()
    dia.setAlwaysOnTop(True)
    



if __name__ == '__main__':
    dialog()
         
        
    pass