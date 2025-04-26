def co_rotation(R_mag, R_CO):
    if R_mag>R_CO:
        print("Effetto elica, accrescimento inibito!")
    else:
       print("La gravità è troppo alta, io accresco!") 
R_mag=input("Scegli un raggio magnetosferico (un: 10^6 cm):")
R_CO=input("Scegli un raggio di corotazione (un: 10^6 cm):")

co_rotation(R_mag,R_CO)
