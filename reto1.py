
#RF1
print('Bienvenido al sistema de ubicación para zonas públicas WIFI')

#RF2
nombre_usuario=51705
contraseña=50715

ingreso_usuario=int(input("Ingrese su usuario: "))

if ingreso_usuario != nombre_usuario:
    print('Error')
else:
    ingreso_contraseña=int(input("Ingrese su contraseña: "))

    if ingreso_contraseña != contraseña:
        print('Error')
    else:
#RF3 y #RF4
        primer_termino=705
        segundo_termino=(5*1-7+1+1)+(7%5-1-1)+(7**1/7-1)
        suma=primer_termino + segundo_termino

        print(primer_termino, "+" ,segundo_termino)
        captcha = int(input('Respuesta:  '))

        if captcha != suma:
            print('Error')
        else:
            print("Sesión iniciada")







