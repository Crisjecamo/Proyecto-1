#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General
# 
# Hola Cristhoper, te felicito por el desarrollo de este primer proyecto. Se nota que tienes un muy buen dominó con estos componentes básicos de python.</div>

# Una empresa de comercio electrónico, Store 1, recientemente comenzó a recopilar datos sobre sus clientes. El objetivo final de Store 1 es comprender mejor el comportamiento de sus clientes y tomar decisiones basadas en datos para mejorar su experiencia online.
# 
# Como parte del equipo de análisis, tu primera tarea es evaluar la calidad de una muestra de datos recopilados y prepararla para futuros análisis.

# # Cuestionario
# 
# Store 1 tiene como objetivo garantizar la coherencia en la recopilación de datos. Como parte de esta iniciativa, se debe evaluar la calidad de los datos recopilados sobre los usuarios y las usuarias. Te han pedido que revises los datos recopilados y propongas cambios. A continuación verás datos sobre un usuario o una usuaria en particular; revisa los datos e identifica cualquier posible problema.

# In[ ]:


user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']


# **Opciones:**
# 
# 1. El tipo de datos para `user_id` debe cambiarse de una cadena a un número entero.
#     
# 2. La variable `user_name` contiene una cadena que tiene espacios innecesarios y un guion bajo entre el nombre y el apellido.
#     
# 3. El tipo de datos de `user_age` es incorrecto.
#     
# 4. La lista `fav_categories` contiene cadenas en mayúsculas. En su lugar, deberíamos convertir los valores de la lista a minúsculas.

# 1,2,3,4 debemos organizar nuevamente todos los datos para evitar errores futuros el: 
# 
# user_id: esta en una cadena debemos convertirlo a numero entero.
# 
# user_name: tiene espacio al inicio y final y un guion que es innecesario, ya que en una cadena no una variable que si necesita del guion para separar las palabras.
# 
# user_age: esta en float debemos colocarlo a int ya que es innecesario tenerlo en float.
# 
# fav_categoties: la pasaremos a lower "minuscula" solo para tener un mejor entendimiento y organizacion en el codigo pero no tiene nada de malo si igual quisieramos dejarlas como estan.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo Cristhoper. </div>

# Escribe en la celda Markdown a continuación el número de las opciones que has identificado como problemas. Si has identificado varios problemas, sepáralos con comas. Por ejemplo, si crees que los números 1 y 3 son correctos, escribe 1, 3.

# **Escribe tu respuesta y explica tu argumentación:**
# 

# # Ejercicio 1
# 
# Vamos a implementar los cambios que identificamos. Primero, necesitamos corregir los problemas de la variable `user_name`. Como vimos, tiene espacios innecesarios y un guion bajo como separador entre el nombre y el apellido; tu objetivo es eliminar los espacios y luego reemplazar el guion bajo con el espacio.

# In[3]:


user_name = ' mike_reed '
user_name = user_name.strip() # eliminar los espacios en la cadena original
user_name = user_name.replace("_", " ") # reemplazar el guion bajo con el espacio

print(user_name)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo usando los métodos ``strip()`` y ``replace()``. </div>

# # Ejercicio 2
# 
# Luego, debemos dividir el `user_name` (nombre de usuario o usuaria) actualizado en dos subcadenas para obtener una lista que contenga dos valores: la cadena para el nombre y la cadena para el apellido.

# In[4]:


user_name = 'mike reed'
name_split = user_name.split() # divide aquí el string user_name

print(name_split)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo usando el método ``split()``. </div>

# # Ejercicio 3
# 
# ¡Genial! Ahora debemos trabajar con la variable `user_age`. Como ya mencionamos, esta tiene un tipo de datos incorrecto. Arreglemos este problema transformando el tipo de datos y mostrando el resultado final.

# In[5]:


user_age = 32.0
user_age = int(user_age) # cambia el tipo de datos para la edad de un usuario o usuaria

print(user_age) 


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo transformando el tipo de dato de la variable. </div>

# # Ejercicio 4
# 
# Como sabemos, los datos no siempre son perfectos. Debemos considerar escenarios en los que el valor de `user_age` no se pueda convertir en un número entero. Para evitar que nuestro sistema se bloquee, debemos tomar medidas con anticipación.
# 
# Escribe un código que intente convertir la variable `user_age` en un número entero y asigna el valor transformado a `user_age_int`. Si el intento falla, mostramos un mensaje pidiendo al usuario o la usuaria que proporcione su edad como un valor numérico con el mensaje: `Please provide your age as a numerical value.` (Proporcione su edad como un valor numérico.)

# In[26]:


user_age = 'treinta y dos' # aquí está la variable que almacena la edad como un string.

# escribe un código que intente transformar user_age en un entero y si falla, imprime el mensaje especificado

try: # Podemos evitar los errores aplicando el operador de manejo de excepciones try-except.
    
    print(int(user_age)) # Si los valores son correctos se imprimira la edad en numeros enteros.
except:
    print('Please provide your age as a numerical value') # Si no son correctos los datos suministrado, entonces imprimira el siguiente mensaje de error.
    


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo, perfecto el uso de la sentencia ``try`` - ``except``.
# </div>

# # Ejercicio 5
# 
# Finalmente, considera que todas las categorías favoritas se almacenan en mayúsculas. Para llenar una nueva lista llamada `fav_categories_low` con las mismas categorías, pero en minúsculas, itera los valores en la lista `fav_categories`, modifícalos y agrega los nuevos valores a la lista `fav_categories_low`. Como siempre, muestra el resultado final.

# In[24]:


fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []

# escribe tu código aquí
for fav_lower in fav_categories: # Se crea un bucle for para recorrer cada cadena
    fav_categories_low.append(fav_lower.lower()) # Se incorporan los daros a la lista de fav_categories_low con la funcion "append" y luego se convirtio cada cadena contenida en fav_categories a minuscula con "lower".

# no elimines la siguiente declaración print
print(fav_categories_low)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo Cristhoper, usas los métodos ``lower()`` y ``append()`` de manera correcta para solucionar el ejercicio.  
# 
# </div>

# # Ejercicio 6
# 
# Hemos obtenido información adicional sobre los hábitos de gasto de nuestros usuarios y usuarias, incluido el importe gastado en cada una de sus categorías favoritas. La gerencia está interesada en las siguientes métricas:
# 
# - Importe total gastado por el usuario o la usuaria.
# - Importe mínimo gastado.
# - Importe máximo gastado.
# 
# Vamos a calcular estos valores y mostrarlos en la pantalla:

# In[28]:


fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]

total_amount = sum(spendings_per_category) # escribe tu código aquí. Se realizo la suma de todos los gastos del cliente con la funcion "sum()".
max_amount = max(spendings_per_category) # escribe tu código aquí. Se utilizo la funcion "max()" para extraer el importe maximo gastado que realizo el cliente.
min_amount = min(spendings_per_category) # escribe tu código aquí. Se utilizo la funcion "min()" para extraer el importe minimo gastado que realizo el cliente.

# no elimines la siguiente declaración print
print(total_amount)
print(max_amount)
print(min_amount)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo realizando los cálculos correspondientes.  </div>

# # Ejercicio 7
# 
# La empresa quiere ofrecer descuentos a sus clientes leales. Los clientes y las clientas que realizan compras por un importe total mayor a $1500 se consideran leales y recibirán un descuento.
# 
# Nuestro objetivo es crear un bucle `while` que compruebe el importe total gastado y se detenga al alcanzarlo. Para simular nuevas compras, la variable `new_purchase` genera un número entre 30 y 80 en cada iteración del bucle. Esto representa el importe de dinero gastado en una nueva compra y es lo que hay que sumar al total.
# 
# Una vez que se alcance el importe objetivo y se termine el bucle `while`, se mostrará la cantidad final.

# In[42]:


from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent < target_amount: # escribe tu código aquí, Se crea el blucle white para comprar si total_amount_spent es menor que target_amoun, si es true se sigue ejecutando el bucle hasta conseguir un false. 
	new_purchase = randint(30, 80) # generamos un número aleatorio de 30 a 80, Aca se simula las posibles nuevas compras del cliente para llegar a la cantidad necesaria '1500' y asi generar un false y que el bucle se detenga.
	total_amount_spent += new_purchase # escribe tu código aquí, con este codigo simplemente estamos poniendo en funcionamiento la variable new_purchase que contiene lalibreria 'randing', para que la misma sume los valores que tiene establecidos hasta llegar al objetivo y lograr el false para que el bucle se detenga. 

print(total_amount_spent)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo con el desarrollo del ejercicio usando el bucle ``while``.  </div>

# # Ejercicio 8
# 
# Ahora tenemos toda la información sobre un cliente o una clienta de la forma que queremos que sea. La gerencia de una empresa nos pidió proponer una forma de resumir toda la información sobre un usuario o una usuaria. Tu objetivo es crear una cadena formateada que utilice información de las variables `user_id`, `user_name` y `user_age`.
# 
# Esta es la cadena final que queremos crear: `User 32415 is mike who is 32 years old.` (El usuario 32415 es Mike, quien tiene 32 años).

# In[47]:


user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

user_info = f'User {user_id} is {user_name[0]} who is {user_age} years old.' # escribe tu código aquí se utilizo la 'fstring' para lograr la fucion de las variales con los textos colocados en caso de que variables cambien su valor el contenido de la variable user_info tambien lo hara.

# no elimines la siguiente declaración print
print(user_info)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo aplicando el formato de texto.  </div>

# Como sabes, las empresas recopilan y almacenan datos de una forma particular. Store 1 desea almacenar toda la información sobre sus clientes y clientas en una tabla.
# 
# | user_id | user_name | user_age | purchase_category | spending_per_category |
# | --- | --- | --- | --- | --- |
# | '32415' | 'mike', 'reed' | 32 | 'electronics', 'sport', 'books' | 894, 213, 173 |
# | '31980' | 'kate', 'morgan' | 24 | 'clothes', 'shoes' | 439, 390 |
# 
# En términos técnicos, una tabla es simplemente una lista anidada que contiene una sublista para cada usuario o usuaria.
# 
# Store 1 ha creado una tabla de este tipo para sus usuarios y usuarias. Se almacena en la variable `users`. Cada sublista contiene el ID del usuario o la usuaria, nombre y apellido, edad, categorías favoritas y el importe gastado en cada categoría.

# # Ejercicio 9
# 
# Para calcular los ingresos de la empresa, sigue estos pasos.
# 
# 1. Utiliza `for` para iterar sobre la lista `users`.
# 2. Extrae la lista de gastos de cada usuario o usuaria y suma los valores.
# 3. Actualiza el valor de los ingresos con el total de cada usuario o usuaria.
# 
# Así obtendrás los ingresos totales de la empresa que mostrarás en la pantalla al final.

# In[415]:


users = [ 
	  # este es el inicio de la primera sublista
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]], # este es el final de la primera sublista

    # este es el inicio de la segunda sublista
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'shoes'], [439, 390]] 
] # este es el final de la segunda sublista


revenue = 0

for user in users:
	spendings_list = sum(user[4])  # extrae la lista de gastos de cada usuario o usuaria y suma los valores
	total_spendings = spendings_list  # suma los gastos de todas las categorías para obtener el total de un usuario o una usuaria en particular
	revenue += total_spendings # actualiza los ingresos
# no elimines la siguiente declaración print
print('Ganancias totales =', revenue)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo con el desarrollo del ejercicio usando el bucle ``for``.  </div>

# # Ejercicio 10
# 
# Recorre la lista de usuarios y usuarias que te hemos proporcionado y muestra los nombres de la clientela menor de 30 años.

# In[412]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

# escribe tu código aquí
for user in users: #blucle for para recorrer la lista
    if user[2] <= 30: #las condiciones que deben tener los clientes para que nos de los datos solicitados.
        print('Nombre y Apellido =', ' '.join(user[1])) #se agrego texto para un mejor entendimiento y se convirtio la lista a cadena 'join()'.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo construyendo el bucle con la condición.  </div>

# # Ejercicio 11
# 
# Juntemos las tareas 9 y 10 e imprimamos los nombres de los usuarios y las usuarias que tengan menos de 30 años y un gasto total superior a 1000 dólares.

# In[410]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]


for user in users: #se implementa el bucle for para recorrer la lista.
    if sum(user[4]) > 1000 and user[2] < 30: #se implementan las condiciones que deben tener los clientes para los nuevos datos solicitados.
        print('Nombre y Apellido =', ' '.join(user[1])) #se agrego texto para un mejor entendimiento y se convirtio la lista a cadena 'join()'
    # escribe tu código aquí
    


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto. Buen trabajo construyendo el bucle con la condición y el operador lógico.  </div>

# # Ejercicio 12
# 
# Ahora vamos a mostrar el nombre y la edad de todos los usuarios y todas las usuarias que han comprado ropa. Imprime el nombre y la edad en la misma declaración print.

# In[406]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]
  

#escribe tu código aquí
for user in users:
    if 'clothes' in user[3]: # se utilizo el operador 'in' de esta forma ya que haciendolo de la forma "if user[3] == 'clothes'." no arrojaba ningun resultado ya que es una lista de varias listas. y el operador == no funciona correctamente en este caso se debe buscar 'clothes' 'in' la lista 'user[3]' que en este caso vendria siendo la columna 'purchase_category'. 
        print('Nombre y Apellido =', ' '.join(user[1]), '|Edad =', user[2], 'Años.') # se imprimio solo el nombre y apellido del cliente que compro ropa 'user[1]' y su edad 'user[2]', ademas se le colaron textos para mayor entendimiento. y se utilizo la funcion join() para convertir la lista de nombre y apellido en una cadena.      


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Excelente. Buen uso de la sentencia ``ìn`` para solucionar el ejercicio.  </div>

# #### Escribe aquí cualquier comentario o reflexión final

# en uno que otro ejercicio me quede un poco trabado pero simplemente buscaba las teorias las repasaba y lograba solucionarlos. el unico ejercicio fue el numero 12 que despues de 1 hora mas o menos y luego no encontrar respuesta en la teoria. tome la desicion de buscarla en Google. y me di cuenta que lo estaba realizando mal ya que dicha tabla del ejercicio es una lista que contiene 5 listas mas. Por lo que no se realizaba la comparacion como lo vimos en la teoria que es "if user == 'clothes'." en este caso como se trata de listas dentro de una lista lo correcto es buscar el parametro o cadena que queremos encontrar dentro de dicha lista y la formula correcta aprendi que para estos casos es la siguiente. "if 'clothes' in user[3]" y fue asi como logres resolverlo. Espero sus comentarios y posibles modificaciones al proyecto. Saludos

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Hola, Cristhoper, te entiendo. Este ejercicio 12 puede llegar a ser un poco retador; sin embargo, enfrentarse a este tipo de retos genera grandes avances en la curva de aprendizaje.  </div>
