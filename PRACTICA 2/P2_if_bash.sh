
#!/bin/bash

echo -n "Por favor ingresa un número: "
read n
 
rem=$(( $n % 2 )) #nos dira si es par o no
 
if [ $rem -eq 0 ]
then
  echo "$n es un numero par"
fi

