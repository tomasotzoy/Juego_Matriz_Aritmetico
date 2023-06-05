# Juego_Matriz_Aritmetico

# Juego de Matriz      
# Integrantes: Tomás Alexander Otzoy Siquiná y Julio Carlos Cos García
#carnets: 202307032 y 20230803

from tkinter import * #esta es la biblioteca para el modo grafico
import random

def clic1():
    
    global numero1_3

    numero1_3 = random.randint(1,11)
    btn_1 = Button(ventana,text= numero1_3 ,bg="white",font=("Arial Bold",15),fg="red")
    btn_1.grid(column=3,row=18)

    global numero2_3
    numero2_3 = random.randint(1,11)
    btn_2 = Button(ventana, text=numero2_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_2.grid(column=4,row=18)

    global numero4_3
    numero4_3 = random.randint(1,11)
    btn_4 = Button(ventana, text=numero4_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_4.grid(column=3,row=19)

    global numero5_3
    numero5_3 = random.randint(1,11)
    btn_5 = Button(ventana, text=numero5_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_5.grid(column=4,row=19)

def clic2():
    global numero1_3
    numero1_3 = random.randint(1,11)
    btn_1 = Button(ventana,text= numero1_3 ,bg="white",font=("Arial Bold",15),fg="blue")
    btn_1.grid(column=3,row=18)

    global numero2_3
    numero2_3 = random.randint(1,11)
    btn_2 = Button(ventana, text=numero2_3,bg="white",font=("Arial Bold",15),fg="red")
    btn_2.grid(column=4,row=18)

    global numero3_3
    numero3_3 = random.randint(1,11)
    btn_3 = Button(ventana, text=numero3_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_3.grid(column=5,row=18)

    global numero4_3
    numero4_3 = random.randint(1,11)
    btn_4 = Button(ventana, text=numero4_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_4.grid(column=3,row=19)


    global numero5_3
    numero5_3 = random.randint(1,11)
    btn_5 = Button(ventana, text=numero5_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_5.grid(column=4,row=19)

    global numero6_3
    numero6_3 = random.randint(1,11)
    btn_6 = Button(ventana, text=numero6_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_6.grid(column=5,row=19)

def clic3():
    global numero2_3
    numero2_3 = random.randint(1,11)
    btn_2 = Button(ventana, text=numero2_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_2.grid(column=4,row=18)

    global numero3_3
    numero3_3 = random.randint(1,11)
    btn_3 = Button(ventana, text=numero3_3,bg="white",font=("Arial Bold",15),fg="red")
    btn_3.grid(column=5,row=18)



    global numero5_3
    numero5_3 = random.randint(1,11)
    btn_5 = Button(ventana, text=numero5_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_5.grid(column=4,row=19)

    global numero6_3
    numero6_3 = random.randint(1,11)
    btn_6 = Button(ventana, text=numero6_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_6.grid(column=5,row=19)
    
def clic4():
    global numero1_3
    numero1_3 = random.randint(1,11)
    btn_1 = Button(ventana,text= numero1_3 ,bg="white",font=("Arial Bold",15),fg="blue")
    btn_1.grid(column=3,row=18)

    global numero2_3
    numero2_3 = random.randint(1,11)
    btn_2 = Button(ventana, text=numero2_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_2.grid(column=4,row=18)

    global numero4_3
    numero4_3 = random.randint(1,11)
    btn_4 = Button(ventana, text=numero4_3,bg="white",font=("Arial Bold",15),fg="red")
    btn_4.grid(column=3,row=19)

    global numero5_3
    numero5_3 = random.randint(1,11)
    btn_5 = Button(ventana, text=numero5_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_5.grid(column=4,row=19)

    global numero7_3
    numero7_3 = random.randint(1,11)
    btn_7 = Button(ventana, text=numero7_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_7.grid(column=3,row=20)

    global numero8_3
    numero8_3 = random.randint(1,11)
    btn_8 = Button(ventana, text=numero8_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_8.grid(column=4,row=20)

def clic5():
    global numero1_3
    numero1_3 = random.randint(1,11)
    btn_1 = Button(ventana,text= numero1_3 ,bg="white",font=("Arial Bold",15),fg="blue")
    btn_1.grid(column=3,row=18)

    global numero2_3
    numero2_3 = random.randint(1,11)
    btn_2 = Button(ventana, text=numero2_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_2.grid(column=4,row=18)

    global numero3_3
    numero3_3 = random.randint(1,11)
    btn_3 = Button(ventana, text=numero3_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_3.grid(column=5,row=18)


    global numero4_3
    numero4_3 = random.randint(1,11)
    btn_4 = Button(ventana, text=numero4_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_4.grid(column=3,row=19)


    global numero5_3
    numero5_3 = random.randint(1,11)
    btn_5 = Button(ventana, text=numero5_3,bg="white",font=("Arial Bold",15),fg="red")
    btn_5.grid(column=4,row=19)

    global numero6_3
    numero6_3 = random.randint(1,11)
    btn_6 = Button(ventana, text=numero6_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_6.grid(column=5,row=19)

    global numero7_3
    numero7_3 = random.randint(1,11)
    btn_7 = Button(ventana, text=numero7_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_7.grid(column=3,row=20)

    global numero8_3
    numero8_3 = random.randint(1,11)
    btn_8 = Button(ventana, text=numero8_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_8.grid(column=4,row=20)

    global numero9_3
    numero9_3 = random.randint(1,11)
    btn_9 = Button(ventana, text=numero9_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_9.grid(column=5,row=20)

def clic6():
    global numero2_3
    numero2_3 = random.randint(1,11)
    btn_2 = Button(ventana, text=numero2_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_2.grid(column=4,row=18)

    global numero3_3
    numero3_3 = random.randint(1,11)
    btn_3 = Button(ventana, text=numero3_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_3.grid(column=5,row=18)

    global numero5_3
    numero5_3 = random.randint(1,11)
    btn_5 = Button(ventana, text=numero5_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_5.grid(column=4,row=19)

    global numero6_3
    numero6_3 = random.randint(1,11)
    btn_6 = Button(ventana, text=numero6_3,bg="white",font=("Arial Bold",15),fg="red")
    btn_6.grid(column=5,row=19)

    global numero8_3
    numero8_3 = random.randint(1,11)
    btn_8 = Button(ventana, text=numero8_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_8.grid(column=4,row=20)

    global numero9_3
    numero9_3 = random.randint(1,11)
    btn_9 = Button(ventana, text=numero9_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_9.grid(column=5,row=20)

def clic7():
    global numero4_3
    numero4_3 = random.randint(1,11)
    btn_4 = Button(ventana, text=numero4_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_4.grid(column=3,row=19)


    global numero5_3
    numero5_3 = random.randint(1,11)
    btn_5 = Button(ventana, text=numero5_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_5.grid(column=4,row=19)

    global numero7_3
    numero7_3 = random.randint(1,11)
    btn_7 = Button(ventana, text=numero7_3,bg="white",font=("Arial Bold",15),fg="red")
    btn_7.grid(column=3,row=20)

    global numero8_3
    numero8_3 = random.randint(1,11)
    btn_8 = Button(ventana, text=numero8_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_8.grid(column=4,row=20)

def clic8():
    global numero4_3
    numero4_3 = random.randint(1,11)
    btn_4 = Button(ventana, text=numero4_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_4.grid(column=3,row=19)


    global numero5_3
    numero5_3 = random.randint(1,11)
    btn_5 = Button(ventana, text=numero5_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_5.grid(column=4,row=19)

    global numero6_3
    numero6_3 = random.randint(1,11)
    btn_6 = Button(ventana, text=numero6_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_6.grid(column=5,row=19)

    global numero7_3
    numero7_3 = random.randint(1,11)
    btn_7 = Button(ventana, text=numero7_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_7.grid(column=3,row=20)

    global numero8_3
    numero8_3 = random.randint(1,11)
    btn_8 = Button(ventana, text=numero8_3,bg="white",font=("Arial Bold",15),fg="red")
    btn_8.grid(column=4,row=20)

    global numero9_3
    numero9_3 = random.randint(1,11)
    btn_9 = Button(ventana, text=numero9_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_9.grid(column=5,row=20)

def clic9():
    global numero5_3
    numero5_3 = random.randint(1,11)
    btn_5 = Button(ventana, text=numero5_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_5.grid(column=4,row=19)

    global numero6_3
    numero6_3 = random.randint(1,11)
    btn_6 = Button(ventana, text=numero6_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_6.grid(column=5,row=19)

    global numero8_3
    numero8_3 = random.randint(1,11)
    btn_8 = Button(ventana, text=numero8_3,bg="white",font=("Arial Bold",15),fg="blue")
    btn_8.grid(column=4,row=20)

    global numero9_3
    numero9_3 = random.randint(1,11)
    btn_9 = Button(ventana, text=numero9_3,bg="white",font=("Arial Bold",15),fg="red")
    btn_9.grid(column=5,row=20)

def total_boton1():
    global total_btn1
    global respuesta_falsa1
    global respuesta_falsa2
    global respuesta_falsa3
  
    total_btn1 = (numero2_3+numero4_3+numero5_3)*numero1_3
   
    respuesta_falsa1= total_btn1 + 5
    respuesta_falsa2 = total_btn1 + 3
    respuesta_falsa3 = total_btn1 + 2
    print(respuesta_falsa1)
    print(respuesta_falsa2)
    print(respuesta_falsa3)
    print(total_btn1)

    mensaje= respuesta_falsa1
    label_ver1.configure(text=mensaje)
    mensaje= respuesta_falsa2
    label_ver2.configure(text=mensaje)
    mensaje= respuesta_falsa3
    label_ver3.configure(text=mensaje)
    mensaje= total_btn1
    label_ver4.configure(text=mensaje)

def total_boton2():

    global respuesta_falsa1
    global respuesta_falsa2
    global respuesta_falsa3

    global total_btn2
    total_btn2 = (numero1_3+numero3_3+numero4_3+numero5_3+numero6_3)*numero2_3
   
    respuesta_falsa1= total_btn2 + 5
    respuesta_falsa2 = total_btn2 + 3
    respuesta_falsa3 = total_btn2 + 2
    print(respuesta_falsa1)
    print(respuesta_falsa2)
    print(respuesta_falsa3)
    print(total_btn2)

    mensaje= respuesta_falsa1
    label_ver1.configure(text=mensaje)
    mensaje= respuesta_falsa2
    label_ver2.configure(text=mensaje)
    mensaje= respuesta_falsa3
    label_ver3.configure(text=mensaje)
    mensaje= total_btn2
    label_ver4.configure(text=mensaje)

def total_boton3():

    global respuesta_falsa1
    global respuesta_falsa2
    global respuesta_falsa3

    global total_btn3
    total_btn3 = (numero2_3+numero5_3+numero6_3)*numero3_3
   
    respuesta_falsa1= total_btn3 + 5
    respuesta_falsa2 = total_btn3 + 3
    respuesta_falsa3 = total_btn3 + 2
    print(respuesta_falsa1)
    print(respuesta_falsa2)
    print(respuesta_falsa3)
    print(total_btn3)

    mensaje= respuesta_falsa1
    label_ver1.configure(text=mensaje)
    mensaje= respuesta_falsa2
    label_ver2.configure(text=mensaje)
    mensaje= respuesta_falsa3
    label_ver3.configure(text=mensaje)
    mensaje= total_btn3
    label_ver4.configure(text=mensaje)

def total_boton4():
    global respuesta_falsa1
    global respuesta_falsa2
    global  respuesta_falsa3
    global total_btn4

    total_btn4 = (numero1_3+numero2_3+numero5_3+numero7_3+numero8_3)*numero4_3
   
   

    respuesta_falsa1= total_btn4 + 5
    respuesta_falsa2 = total_btn4 + 3
    respuesta_falsa3 = total_btn4 + 2
    print(respuesta_falsa1)
    print(respuesta_falsa2)
    print(respuesta_falsa3)
    print(total_btn4)

   

    mensaje= respuesta_falsa1
    label_ver1.configure(text=mensaje)
    mensaje= respuesta_falsa2
    label_ver2.configure(text=mensaje)
    mensaje= respuesta_falsa3
    label_ver3.configure(text=mensaje)
    mensaje= total_btn4
    label_ver4.configure(text=mensaje)

def total_boton5():
    global total_btn5
    global respuesta_falsa1
    global respuesta_falsa2
    global  respuesta_falsa3
    global total_btn5

    total_btn5 = (numero1_3+numero2_3+numero3_3+numero4_3+numero6_3+numero7_3+numero8_3+numero9_3)*numero5_3
   
   

    respuesta_falsa1= total_btn5 + 5
    respuesta_falsa2 = total_btn5 + 3
    respuesta_falsa3 = total_btn5 + 2
    print(respuesta_falsa1)
    print(respuesta_falsa2)
    print(respuesta_falsa3)
    print(total_btn5)

   

    mensaje= respuesta_falsa1
    label_ver1.configure(text=mensaje)
    mensaje= respuesta_falsa2
    label_ver2.configure(text=mensaje)
    mensaje= respuesta_falsa3
    label_ver3.configure(text=mensaje)
    mensaje= total_btn5
    label_ver4.configure(text=mensaje)

def total_boton6():
    global respuesta_falsa1
    global respuesta_falsa2
    global  respuesta_falsa3
    global total_btn6

    total_btn6 = (numero2_3+numero3_3+numero5_3+numero8_3+numero9_3)*numero6_3
   
   

    respuesta_falsa1= total_btn6 + 5
    respuesta_falsa2 = total_btn6 + 3
    respuesta_falsa3 = total_btn6+ 2
    print(respuesta_falsa1)
    print(respuesta_falsa2)
    print(respuesta_falsa3)
    print(total_btn6)

   

    mensaje= respuesta_falsa1
    label_ver1.configure(text=mensaje)
    mensaje= respuesta_falsa2
    label_ver2.configure(text=mensaje)
    mensaje= respuesta_falsa3
    label_ver3.configure(text=mensaje)
    mensaje= total_btn6
    label_ver4.configure(text=mensaje)

def total_boton7():
    global respuesta_falsa1
    global respuesta_falsa2
    global  respuesta_falsa3
    global total_btn7

    total_btn7 = (numero4_3+numero5_3+numero8_3)*numero7_3
   
   

    respuesta_falsa1= total_btn7 + 5
    respuesta_falsa2 = total_btn7 + 3
    respuesta_falsa3 = total_btn7+ 2
    print(respuesta_falsa1)
    print(respuesta_falsa2)
    print(respuesta_falsa3)
    print(total_btn7)

   

    mensaje= respuesta_falsa1
    label_ver1.configure(text=mensaje)
    mensaje= respuesta_falsa2
    label_ver2.configure(text=mensaje)
    mensaje= respuesta_falsa3
    label_ver3.configure(text=mensaje)
    mensaje= total_btn7
    label_ver4.configure(text=mensaje)

def total_boton8():
    global respuesta_falsa1
    global respuesta_falsa2
    global  respuesta_falsa3
    global total_btn8

    total_btn8 = (numero7_3+numero4_3+numero5_3+numero6_3+numero9_3)*numero8_3
   
   

    respuesta_falsa1= total_btn8 + 5
    respuesta_falsa2 = total_btn8 + 3
    respuesta_falsa3 = total_btn8+ 2
    print(respuesta_falsa1)
    print(respuesta_falsa2)
    print(respuesta_falsa3)
    print(total_btn8)

   

    mensaje= respuesta_falsa1
    label_ver1.configure(text=mensaje)
    mensaje= respuesta_falsa2
    label_ver2.configure(text=mensaje)
    mensaje= respuesta_falsa3
    label_ver3.configure(text=mensaje)
    mensaje= total_btn8
    label_ver4.configure(text=mensaje)

def total_boton9():
    global respuesta_falsa1
    global respuesta_falsa2
    global  respuesta_falsa3
    global total_btn9

    total_btn9 = (numero8_3+numero5_3+numero6_3)*numero9_3
   
    respuesta_falsa1= total_btn9 + 5
    respuesta_falsa2 = total_btn9 + 3
    respuesta_falsa3 = total_btn9+ 2
    print(respuesta_falsa1)
    print(respuesta_falsa2)
    print(respuesta_falsa3)
    print(total_btn9)

    mensaje= respuesta_falsa1
    label_ver1.configure(text=mensaje)
    mensaje= respuesta_falsa2
    label_ver2.configure(text=mensaje)
    mensaje= respuesta_falsa3
    label_ver3.configure(text=mensaje)
    mensaje= total_btn9
    label_ver4.configure(text=mensaje)


# Verificar mis respuestas
def verificar1_3x3():
    global puntos1 
    mensaje= text_verificar.get()
    label_verificar3x3.configure(text=mensaje)
    if (int(mensaje) == total_btn1):
        puntos1 = 3
        matriz3_1_j2()   
    else:
        puntos1 = 0
        matriz3_1_j2()
       
    print("Puneto es de:",puntos1)

def matriz3_1_j2():
    btn_1= Button(ventana, text="X",bg="grey",font=("Arial Bold",15))
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic2)
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic3)
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic4)
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic5)
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic6)
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic7)
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic8)
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic9)
    btn_9.grid(column=5,row=20) 



def verificar2_3x3():
    global puntos1 
    mensaje= text_verificar.get()
    label_verificar3x3.configure(text=mensaje)
    if (int(mensaje) == total_btn2):
        puntos1 = 3
        matriz3_2_j2()
    else:
        puntos1 = 0
        matriz3_2_j2()
      
    print("Puneto es de:",puntos1)



    btn_1= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15))
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text="X",bg="grey",font=("Arial Bold",15),command=clic2)
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic3)
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic4)
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic5)
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic6)
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic7)
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic8)
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic9)
    btn_9.grid(column=5,row=20) 

def matriz3_2_j2():
    btn_1= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic1)
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text="X",bg="grey",font=("Arial Bold",15))
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic3)
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic4)
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text="",bg="grey",font=("Arial Bold",15))
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic6)
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic7)
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic8)
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic9)
    btn_9.grid(column=5,row=20)



def verificar3_3x3():
    global puntos1 
    mensaje= text_verificar.get()
    label_verificar3x3.configure(text=mensaje)
    if (int(mensaje) == total_btn3):
        puntos1 = 3
        matriz3_2_j2()
    else:
        puntos1 = 0
        matriz3_2_j2()
        
    print("Puneto es de:",puntos1)

def matriz3_3_j2():
    btn_1= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic1)
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic2)
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text="X",bg="grey",font=("Arial Bold",15))
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic4)
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic5)
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic6)
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic7)
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic8)
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic9)
    btn_9.grid(column=5,row=20)



def verificar4_3x3():
    global puntos1 
    mensaje= text_verificar.get()
    label_verificar3x3.configure(text=mensaje)
    if (int(mensaje) == total_btn4):
        puntos1 = 3
        matriz3_2_j2()
    else:
        puntos1 = 0
        matriz3_2_j2()
   
    print("Puneto es de:",puntos1)

def matriz3_4_j2():
    btn_1= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic1)
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic2)
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic3)
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text="X",bg="grey",font=("Arial Bold",15))
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic5)
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic6)
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic7)
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic8)
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic9)
    btn_9.grid(column=5,row=20)



def verifica5_3x3():
    global puntos1 
    mensaje= text_verificar.get()
    label_verificar3x3.configure(text=mensaje)
    if (int(mensaje) == total_btn5):
        puntos1 = 3
        matriz3_5_j2()
    else:
        puntos1 = 0
        matriz3_5_j2()
      
    print("Puneto es de:",puntos1)
    
def matriz3_5_j2():
    btn_1= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic1)
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic2)
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic3)
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic4)
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text="X",bg="grey",font=("Arial Bold",15))
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic6)
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic7)
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic8)
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic9)
    btn_9.grid(column=5,row=20)



def verifica6_3x3():
    global puntos1 
    mensaje= text_verificar.get()
    label_verificar3x3.configure(text=mensaje)
    if (int(mensaje) == total_btn6):
        puntos1 = 3
        matriz3_6_3x3()
    else:
        puntos1 = 0
        matriz3_6_3x3()
 
    print("Puneto es de:",puntos1)

def matriz3_6_3x3():
    btn_1= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic1)
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic2)
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic3)
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic4)
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic5)
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text="X",bg="grey",font=("Arial Bold",15))
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic7)
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic8)
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic9)
    btn_9.grid(column=5,row=20)



def verifica7_3x3():
    global puntos1 
    mensaje= text_verificar.get()
    label_verificar3x3.configure(text=mensaje)
    if (int(mensaje) == total_btn7):
        puntos1 = 3
        matriz3_7_3x3()
    else:
        puntos1 = 0
        matriz3_7_3x3()
      
    print("Puneto es de:",puntos1)

def matriz3_7_3x3():
    btn_1= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic1)
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic2)
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic3)
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic4)
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic5)
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic6)
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text="X",bg="grey",font=("Arial Bold",15))
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic8)
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic9)
    btn_9.grid(column=5,row=20)



def verifica8_3x3():
    global puntos1 
    mensaje= text_verificar.get()
    label_verificar3x3.configure(text=mensaje)
    if (int(mensaje) == total_btn8):
        puntos1 = 3
        matriz3_8_3x3()
    else:
        puntos1 = 0
        matriz3_8_3x3()

    print("Puneto es de:",puntos1)

def matriz3_8_3x3():
    btn_1= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic1)
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic2)
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15))
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic4)
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic5)
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic6)
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic7)
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text="X",bg="grey",font=("Arial Bold",15))
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic9)
    btn_9.grid(column=5,row=20)



def verifica9_3x3():
    global puntos1 
    mensaje= text_verificar.get()
    label_verificar3x3.configure(text=mensaje)
    if (int(mensaje) == total_btn9):
        puntos1 = 3
        matriz3_9_3x3()
    else:
        puntos1 = 0
        matriz3_9_3x3()

    print("Puneto es de:",puntos1)

def matriz3_9_3x3():
    btn_1= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic1)
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic2)
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15))
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic4)
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic5)
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic6)
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic7)
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic8)
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text="X",bg="grey",font=("Arial Bold",15))
    btn_9.grid(column=5,row=20)

# cuerpo de la matrix original
def martriz_3x3():
    # matriz 3x3
    mensaje= "El jugador 1 es: "+ text1.get()
    label_j1_confir.configure(text=mensaje)

    mensaje= "El jugador 2 es: "+ text2.get() 
    label_j2_confir.configure(text=mensaje)


    btn_1= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic1)
    btn_1.grid(column=3,row=18)

    btn_2= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic2)
    btn_2.grid(column=4,row=18)

    btn_3= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic3)
    btn_3.grid(column=5,row=18)

    btn_4= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic4)
    btn_4.grid(column=3,row=19)

    btn_5= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command= clic5)
    btn_5.grid(column=4,row=19)

    btn_6= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic6)
    btn_6.grid(column=5,row=19)

    btn_7= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic7)
    btn_7.grid(column=3,row=20)

    btn_8= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic8)
    btn_8.grid(column=4,row=20)

    btn_9= Button(ventana, text=" ",bg="grey",font=("Arial Bold",15),command=clic9)
    btn_9.grid(column=5,row=20)



#creo una variable donde meto a meter la funcino del mofo grafico
ventana = Tk()
# esta linea es para el taaño de la ventana 
ventana.geometry("900x900")
ventana.title("Juego de Matriz ")
ventana.configure(background="grey")

#esta linea es para poner un titulo y cambiarle el estilo

label_titulo = Label(ventana, text="Juego de Matriz",bg="grey",font=("Arial Bold",30)) 
label_j1 = Label(ventana, text="Ingrese el nombre del primer jugador 1:",bg="grey",font=("Arial Bold",15))
label_j1_confir = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))

label_j2 =Label(ventana, text="Ingrese el nombre del primer jugador 2:",bg="grey",font=("Arial Bold",15))
label_j2_confir = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))

label_op_de_amtriz = Label(ventana, text="lista de las matrices accesibles:",bg="grey",font=("Arial Bold",10))
#boton1
label_ver11 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_ver12 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_ver14 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_ver15 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_verificar1_3x3 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
#boton5
label_boton5r = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_ver1 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_ver2 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_ver3 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_ver4 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_verificar3x3 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_punteoj1 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
label_punteoj2 = Label(ventana, text=" ",bg="grey",font=("Arial Bold",10))
#esta linea es para pocisionar la linea de texto en la ventana
label_titulo.grid(column=0,row=0)
label_j1.grid(column=0,row=1)
label_j2.grid(column=0,row=3)
label_boton5r.grid(column=8,row=20)
label_ver1.grid(column=8,row=19)
label_ver2.grid(column=8,row=20)
label_ver3.grid(column=8,row=21)
label_ver4.grid(column=8,row=22)
label_verificar3x3.grid(column=8,row=27)
label_punteoj1.grid(column=7,row=20)
#label_punteoj2.grid(column=7,row=21)

label_j1_confir.grid(column=0,row=18)
label_j2_confir.grid(column=0,row=19)

# crear una caja para escribirSSSS
text1 = Entry(ventana,width=20)
text1.grid(column=0,row=2)

text2 = Entry(ventana,width=20)
text2.grid(column=0,row=4)

text_verificar= Entry(ventana, width=20 )
text_verificar.grid(column=8,row=25)
#aqui va la accion del boton    
btn_3x3=Button(ventana,text="Matriz 3x3",bg="white",fg="black", command=martriz_3x3 )
btn_3x3.grid(column=0,row=8)
btn_4x4=Button(ventana,text="Matriz 4x4",bg="white",fg="black" )
btn_4x4.grid(column=0,row=9)
btn_5x5=Button(ventana,text="Matriz 5x5",bg="white",fg="black")
btn_5x5.grid(column=0,row=10)


btn_ver_respuesta_3x3=Button(ventana, text = "ver respuestas boton 1" ,bg="white",fg="black", command=total_boton1)
btn_ver_respuesta_3x3.grid(column=7,row=14)
btn_ver_respuesta_3x3=Button(ventana, text = "ver respuestas boton 2" ,bg="white",fg="black", command=total_boton2)
btn_ver_respuesta_3x3.grid(column=7,row=15)
btn_ver_respuesta_3x3=Button(ventana, text = "ver respuestas boton 3" ,bg="white",fg="black", command=total_boton3)
btn_ver_respuesta_3x3.grid(column=7,row=16)
btn_ver_respuesta_3x3=Button(ventana, text = "ver respuestas boton 4" ,bg="white",fg="black", command=total_boton4)
btn_ver_respuesta_3x3.grid(column=7,row=17)
btn_ver_respuesta_3x3=Button(ventana, text = "ver respuestas boton 5" ,bg="white",fg="black", command=total_boton5)
btn_ver_respuesta_3x3.grid(column=7,row=18)
btn_ver_respuesta_3x3=Button(ventana, text = "ver respuestas boton 6" ,bg="white",fg="black", command=total_boton6)
btn_ver_respuesta_3x3.grid(column=7,row=19)
btn_ver_respuesta_3x3=Button(ventana, text = "ver respuestas boton 7" ,bg="white",fg="black", command=total_boton7)
btn_ver_respuesta_3x3.grid(column=7,row=20)
btn_ver_respuesta_3x3=Button(ventana, text = "ver respuestas boton 8" ,bg="white",fg="black", command=total_boton8)
btn_ver_respuesta_3x3.grid(column=7,row=21)
btn_ver_respuesta_3x3=Button(ventana, text = "ver respuestas boton 9" ,bg="white",fg="black", command=total_boton9)
btn_ver_respuesta_3x3.grid(column=7,row=22)


btn_siguiente1=Button(ventana, text = "Comprobar respuesta boton 1" ,bg="white",fg="black", command=verificar1_3x3)
btn_siguiente1.grid(column=8,row=27)
btn_siguiente2=Button(ventana, text = "Comprobar respuesta boton 2" ,bg="white",fg="black", command=verificar2_3x3)
btn_siguiente2.grid(column=8,row=28)
btn_siguiente3=Button(ventana, text = "Comprobar respuesta boton 3" ,bg="white",fg="black", command=verificar3_3x3)
btn_siguiente3.grid(column=8,row=29)
btn_siguiente4=Button(ventana, text = "Comprobar respuesta boton 4" ,bg="white",fg="black", command=verificar4_3x3)
btn_siguiente4.grid(column=8,row=30)
btn_siguiente5 =Button(ventana, text = "Comprobar respuesta boton 5" ,bg="white",fg="black", command=verifica5_3x3)
btn_siguiente5.grid(column=8,row=31)
btn_siguiente6 =Button(ventana, text = "Comprobar respuesta boton 6" ,bg="white",fg="black", command=verifica6_3x3)
btn_siguiente6.grid(column=9,row=27)
btn_siguiente7 =Button(ventana, text = "Comprobar respuesta boton 7" ,bg="white",fg="black", command=verifica7_3x3)
btn_siguiente7.grid(column=9,row=28)
btn_siguiente8 =Button(ventana, text = "Comprobar respuesta boton 8" ,bg="white",fg="black", command=verifica8_3x3)
btn_siguiente8.grid(column=9,row=29)
btn_siguiente9 =Button(ventana, text = "Comprobar respuesta boton 9" ,bg="white",fg="black", command=verifica9_3x3)
btn_siguiente9.grid(column=9,row=30)

#aquie es para que la venta se vea
ventana.mainloop()
