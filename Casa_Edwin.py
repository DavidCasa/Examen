from tkinter import *
import tkinter
import math
root = Tk()
text_Input =StringVar()
text_InputA =StringVar()
text_InputB =StringVar()
text_InputC =StringVar()
root.geometry("160x100")
var1 = ''
var2 = ''
operador = ''
root.title('Examen Bimestre 1')

def btnClick(num,tecla,dos):
    global operador
    global val
    global val1
    if num == 1:
        if tecla == dos:
            operador = int(tecla)**2
            text_InputB.set(str(operador))
            operator = ''
        elif tecla != dos:
            operator = int(tecla)*int(dos)
            text_InputB.set(str(operador))

        
    elif num == 2:
        
        operador = str((int(tecla)*int(dos)))
        text_InputB.set(operador)


    elif num ==3:
        
        
        print('')
##################
def btnAreaC(valor):
    global operador
    operador = int(valor)**2
    text_InputB.set(str(operador))

def btnPerTri(valor1,val2,val3):
    global operador
    operador = int(valor1)+int(val2)+int(val3)
    text_InputA.set(str(operador))
    print()

def btnArTr(base,altura):
    global operador
    operador = (int(base)*int(altura))/2
    text_InputB.set(str(operador))
    print()
######################

def btnArP(lado,apotema):
    global operador
    operador = (int(lado)*int(apotema)*5)/2
    text_InputB.set(str(operador))



    
def btnPoli(valor):
    global operador
    operador = int(valor)*5
    text_InputB.set(str(operador))
    
def btnPerC(valor):
    global operador
    operador = int(valor)*4
    text_InputB.set(str(operador))
    
def btnclear():
    text_Input.set('')
    text_InputA.set('')
    text_InputB.set('')
    text_InputC.set('')
    
def mostrarVen():
    root.deiconify()
    
def mostrarVenAn():
    root.deiconify()
    text_Input.set('')
    text_InputA.set('')
    text_InputB.set('')
    text_InputC.set('')
    


def ventFunci():
    vent = Toplevel(root)
    vent.geometry("200x200")
    vent.title("Calculadora de perimetros")
    labe1 = Label(vent,text='Seleccione una opcion a calcular').grid(row=0, column = 0)
    btnAn = Button(vent, text='Una figura de 3 lados',command=lambda:venOp(1),width = 20).grid(row=10, column = 0)
    btnAn = Button(vent, text='Una figura de 4 lados',command=lambda:venOp(2),width = 20).grid(row=11, column = 0)
    btnAn = Button(vent, text='Una figura de 5 lados',command=lambda:venOp(3),width = 20).grid(row=12, column = 0)
    
    root.iconify()


def venOp(num):
        calcu = Toplevel(root)
        calcu.geometry("200x200")
        calcu.title("OPCIONES DE CALCULO")
        labe1 = Label(calcu,text='Seleccione una opcion a calcular').grid(row=0, column = 0)
        if num == 1:
            btnAn = Button(calcu, text='PERIMETRO',command=lambda:venCal(3),width = 20).grid(row=10, column = 0)
            btnAn = Button(calcu, text='AREA',command=lambda:venCal(4),width = 20).grid(row=11, column = 0)
        elif num == 2:
            btnAn = Button(calcu, text='PERIMETRO',command=lambda:venCal(1),width = 20).grid(row=10, column = 0)
            btnAn = Button(calcu, text='AREA',command=lambda:venCal(2),width = 20).grid(row=11, column = 0)
        elif num == 3:
            btnAn = Button(calcu, text='PERIMETRO',command=lambda:venCal(5),width = 20).grid(row=10, column = 0)
            btnAn = Button(calcu, text='AREA',command=lambda:venCal(6),width = 20).grid(row=11, column = 0)
    

def venCal(numero):
    venCal = Toplevel(root)
    venCal.geometry("640x480")
    ####################################area########
    if numero ==2:

        venCal.title("Calculo de una figura de 4 lados")
        btnAn = Button(venCal, text='Regresar Al menu principal',command=lambda:mostrarVenAn(),width = 20).grid(row=10, column = 0)
        labe1 = Label(venCal,text='Bienvenidos, calculo del area..!!').grid(row=10, column = 11)
        labe1 = Label(venCal,text='LARGO ').grid(row=15, column = 10)
        labe1 = Label(venCal,text='ANCHO').grid(row=25, column = 10)
        btnTot = Button(venCal, text='TOTAL',command=lambda:btnClick(1,text_Input.get(),text_InputA.get()),width = 20).grid(row=30, column = 10)
        btnBorr = Button(venCal, text='BORRAR',command=lambda:btnclear(),width = 20).grid(row=31, column = 10)

        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_Input, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=15,column=11)
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputB, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=30,column=11)
        
        txt_DisplayD = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputA, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=25,column=11)
        
        root.iconify()

    if numero ==1:
        venCal.title("Calculo de una figura de 4 lados")
        btnAn = Button(venCal, text='Regresar Al menu principal',command=lambda:mostrarVenAn(),width = 20).grid(row=10, column = 0)
        labe1 = Label(venCal,text='Bienvenidos, calculo del perimetro..!!').grid(row=10, column = 11)
        labe1 = Label(venCal,text='LADO ').grid(row=15, column = 10)
        btnTot = Button(venCal, text='TOTAL',command=lambda:btnPerC(text_Input.get()),width = 20).grid(row=30, column = 10)
        btnBorr = Button(venCal, text='BORRAR',command=lambda:btnclear(),width = 20).grid(row=31, column = 10)

        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_Input, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=15,column=11)
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputB, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=30,column=11)

        
        root.iconify()

    

    ###############################triangulo##################################
    elif numero ==3:
        venCal.title("Calculo de una figura de 3 lados")
        btnAn = Button(venCal, text='Regresar Al menu principal',command=lambda:mostrarVenAn(),width = 20).grid(row=10, column = 10)
        root.iconify()
        labe1 = Label(venCal,text='Bienvenidos, calculo del perimetro..!!').grid(row=10, column = 11)
        labe1 = Label(venCal,text='LADO1 ').grid(row=15, column = 10)
        labe1 = Label(venCal,text='LADO2').grid(row=25, column = 10)
        labe1 = Label(venCal,text='LADO3').grid(row=30, column = 10)
        btnTot = Button(venCal, text='TOTAL',command=lambda:btnPerTri(text_Input.get(),text_InputB.get(),text_InputC.get()),width = 20).grid(row=31, column = 10)
        btnBorr = Button(venCal, text='BORRAR',command=lambda:btnclear(),width = 20).grid(row=32, column = 10)
        
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_Input, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=15,column=11)
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputB, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=25,column=11)
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputC, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=30,column=11)
        
        txt_DisplayD = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputA, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=31,column=11)

    elif numero ==4:
        venCal.title("Calculo de una figura de 3 lados")
        btnAn = Button(venCal, text='Regresar Al menu principal',command=lambda:mostrarVenAn(),width = 20).grid(row=10, column = 10)
        root.iconify()
        labe1 = Label(venCal,text='Bienvenidos, calculo del area..!!').grid(row=10, column = 11)
        labe1 = Label(venCal,text='BASE ').grid(row=15, column = 10)
        labe1 = Label(venCal,text='ALTURA').grid(row=25, column = 10)
        btnTot = Button(venCal, text='TOTAL',command=lambda:btnArTr(text_Input.get(),text_InputA.get()),width = 20).grid(row=30, column = 10)
        btnBorr = Button(venCal, text='BORRAR',command=lambda:btnclear(),width = 20).grid(row=31, column = 10)
        
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_Input, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=15,column=11)
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputB, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=30,column=11)
        
        txt_DisplayD = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputA, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=25,column=11)

    ################################################################################

        #########################################pentagono########################
    elif numero == 5:
        venCal.title("Calculo de una figura de 5 lados")
        btnAn = Button(venCal, text='Regresar Al menu principal',command=lambda:mostrarVenAn(),width = 20).grid(row=10, column = 10)
        root.iconify()
        labe1 = Label(venCal,text='Bienvenidos, calculo del perimetro..!!').grid(row=10, column = 11)
        labe1 = Label(venCal,text='LONGITUD DE UN LADO').grid(row=15, column = 10)
        btnTot = Button(venCal, text='TOTAL',command=lambda:btnPoli(text_Input.get()),width = 20).grid(row=30, column = 10)
        btnBorr = Button(venCal, text='BORRAR',command=lambda:btnclear(),width = 20).grid(row=31, column = 10)
        
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_Input, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=15,column=11)
        
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputB, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=30,column=11)
    elif numero ==6:
        venCal.title("Calculo de una figura de 5 lados")
        btnAn = Button(venCal, text='Regresar Al menu principal',command=lambda:mostrarVenAn(),width = 20).grid(row=10, column = 10)
        root.iconify()
        labe1 = Label(venCal,text='Bienvenidos, calculo del perimetro..!!').grid(row=10, column = 11)
        labe1 = Label(venCal,text='LADO').grid(row=15, column = 10)
        labe1 = Label(venCal,text='APOTEMA').grid(row=20, column = 10)
        btnTot = Button(venCal, text='TOTAL',command=lambda:btnArP(text_Input.get(),text_Input.get()),width = 20).grid(row=30, column = 10)
        btnBorr = Button(venCal, text='BORRAR',command=lambda:btnclear(),width = 20).grid(row=31, column = 10)
        
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_Input, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=15,column=11)
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputC, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=20,column=11)
        txt_Display = Entry(venCal, font=('arial',14,'bold'), textvariable=text_InputB, bd=5, insertwidth=4, width=10, justify=RIGHT).grid(row=30,column=11)
        
######################################################################################
        
def ventanaCal():
    ventana_cal = Toplevel(root)
    ventana_cal.geometry("640x480")
    ventana_cal.title("Calculadora de perimetros")

    btnAn = Button(ventana_cal, text='Regresar Al menu principal',command=lambda:mostrarVen(),width = 20).grid(row=10, column = 10)
    labe1 = Label(root,text='Bienvenidos a Este programa').grid(row=0, column = 0)
    txt_Display = Entry(ventana_cal, font=('arial',14,'bold'), textvariable=text_Input, bd=15, insertwidth=4,
                    state = DISABLED, width=10, justify=RIGHT).grid(row=15,column=20)
    root.iconify()


def venAni():
    ventana_ani = Toplevel(root)
    ventana_ani.geometry("640x480")
    ventana_ani.title("Animacion de Objetos")
    btnAn = Button(ventana_ani, text='Regresar Al menu principal',command=lambda:mostrarVenAn(),width = 20).grid(row=10, column = 10)
    btn 

    root.iconify()



labe1 = Label(root,text='Bienvenidos a Este programa').grid(row=0, column = 0)
labe1 = Label(root,text='Elija lo que desea realizar').grid(row=1, column = 0)
btnCal = Button(root, text='Calculo',command=lambda:ventFunci(), width = 20).grid(row=2, column = 0)
btnAn = Button(root, text='Animacion',command=lambda:venAni(),width = 20).grid(row=3, column = 0)


root.mainloop()

#triangulo cuadrado pentagono
