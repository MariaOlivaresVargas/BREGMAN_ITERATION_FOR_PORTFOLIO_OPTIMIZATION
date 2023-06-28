# BREGMAN_ITERATION_FOR_PORTFOLIO_OPTIMIZATION
Se implementó el algoritmo de Bregman modificado a un modelo l1 regularizado de Markowitz expuesto en el artículo “Modified bregman iteration for portfolio optimization” (Corsaro &amp; Simon, 2017). Se implementan gráficas con el número de entradas activas, el número de iteraciones y el tiempo de ejecución para cada uno de los portafolios.
------------------------------------------------------------------------------------------------------------------------------------------------------



---------------------------------------------------------------------------
main(READ ME)
---------------------------------------------------------------------------
Abrir main.py
*main.py exporta las funciones de funciones.py, fun_axu.py y los métodos de optimizacion.py.

*El programa utiliza numpy y csv. Además de que exporta funciones del archivo
funciones.py, fun_axu.py y optimizacion.py


** Fue ejecutado en Spyder (Python 3.8) y en Google Colaboraty (Colab).

La interfaz no es interactiva con el usuario
---------------------------------------------------------------------------
1) Ejecute el programa (main.py). 

2) El algoritmo se implementará. 

*El algoritmo tiene cargado un ejemplo. Imprime el portafolio 1 y 2.Esto puede ajustarse en
 en el for de la linea 35. Para activar todos los portafolios, se pone (0,40).

**No se recomienda al usuario cambia parámetros de toleracia y regularización.


*Si desea modificar paramétros: 

  optimizacion.py
 FISTA:  
	L-linea 116
	eta- linea 117
	t- linea 118
	lamda- linea 119
	toletacia- linea 121

BREGMAN:
	tolerancia- linea 155

   main.py 
  	tau inicial- se puede comentar de la línea 35-38 e incluir una nueva variable tau0=c, donde c es el valor deseado. 

---------------------------------------------------------------------------
En consola se mostrará un letrero: Portafolio k+1, donde k=0,1,2...


Además se mostrará la multiplicación Aw, donde A:=[w 1]^T donde w son los pesos de los 
activos. Aw=[p 1], por lo que se deberá mostrar un vector con una constante y un 1 o aproximado.


**Si desea desactivar las impresiones: 

 -main.py : Desactivar lineas: 63-67


Se muestran 3 gráficas relacionadas al número de iteraciones, al tiempo promedio y al número de entradas activas. 
