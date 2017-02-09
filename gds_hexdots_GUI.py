## Code written by Elliot Cheng, ANFF-Q, The University of Queensland
## for generating dot array gds-II files for mask printing
## version 1.0

from gdsCAD import *
import numpy as np
import math

# GUI interface
import tkinter
window = tkinter.Tk()
window.title('GDS-II Dot Array Generator')
#window.configure(background='firebrick')
window.geometry('350x500')
#window.wm_iconbitmap('anfficon.ico')

disc = tkinter.Label(window,text='Dot Array Mask Generator\nAn ANFF-Q Software', font=('Helvetica',12))
disc.pack()

#create widgets for entering parameters
lblradius = tkinter.Label(window, text='Diameter (um):')
rad_entry= tkinter.Entry(window)

lbllcc = tkinter.Label(window, text='Lattice spacing (um):')
lcc_entry = tkinter.Entry(window)

lblwidth= tkinter.Label(window, text='Mask Widths (um):')
writearea_entry = tkinter.Entry(window)

lblradius.pack()
rad_entry.pack()
lbllcc.pack()
lcc_entry.pack()
lblwidth.pack()
writearea_entry.pack()

filename = 'init'

def onclick():
    global dd,pcc,writearea,filename
    
#print("Welcome to use ANFFQ's dot array GDS-II generator\nThis program will generate a hexagonally packed dot array\nProgram developed by Elliot Cheng, University of Queensland, 2016")
#print("Author email: h.cheng6@uq.edu.au\n\nPlease Enter The Following:\n")
# radius for the dots
#dd  = float(input("radius of the dots in um? "))
# center to center pitch of the dots
#pcc = float(input("center to center distance of the dots in um? "))

# Layout widths of the overall pattern
#writearea = float(input("widths of the write area in um? "))

    dd=float(rad_entry.get())/2
    pcc=float(lcc_entry.get())
    writearea = float(writearea_entry.get())    
    filename = "Area"+str(int(writearea/1000))+"mm"+"_circ"+"_Dia"+str(int(2*dd))+"um"+"_Lcc"+str(int(pcc))+ "um"+".gds"
#Calculate the hexagonal translations for the placements
    hextrans_y = pcc*math.sqrt(3)/2
    hextrans_x = pcc/2

#Calculate the number of rol & cols required
    rn = math.ceil(writearea/pcc)
    cn = math.ceil(writearea/hextrans_y)/2

    corn1 = [-(writearea/2), -(writearea/2)]
    corn2 = [writearea/2,writearea/2]

    dot = core.Cell('unit_dots_cell')
    dot.add(shapes.Disk((0,0),dd))
    dot.add(shapes.Disk((hextrans_x,hextrans_y),dd))
#dot.show()

    limit = core.Cell('Bounding_box')
    limit.add(shapes.Box(corn1, corn2, 0.2, layer = 99))

    dotarray = core.CellArray(dot, rn,cn,(2*hextrans_x,2*hextrans_y), origin = (-writearea/2,-writearea/2))
    cell2 = core.Cell('dotarray')
    cell2.add(dotarray)

# Add the copied cell to a Layout and save
    layout = core.Layout('LIBRARY')
    layout.add(cell2)
    layout.save(filename)
    #print("file: "+filename+" has been prepared")
    lblb = tkinter.Label(window,text=filename+'\nhas been prepared')
    lblb.pack()
    
    return
    

but=tkinter.Button(window, text='Generate',command=onclick)
but.pack()
lab_dis = tkinter.Label(window, text='Program developed by Elliot Cheng\nh.cheng6@uq.edu.au',font=('Arial',8))
lab_dis.pack()
window.mainloop()