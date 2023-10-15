import numpy as np

# Arreglo de una sola dimensión
a = np.array([1, 2, 3, 4, 5, 6])
print("Arreglo de una sola dimensión: ", a)

# Arreglo multidimencional
b = np.array([[1, 2, 3], [4, 5, 6]])
print("Arreglo multidimensional: ", b)

c = np.zeros([2, 2])
print("Arreglo con ceros: ", c)

d = np.ones([2, 2])
print("Arreglo de unos: ", d)

e = np.empty([3, 4])
print("Arreglo cuyo contenido es random: ", e)

print(np.eye(5))  # Regresa un arreglo de dos dimensiones que contiene unos en su
# Matriz Identidad

e = np.asarray([1, 2, 3, 4, 5, 6])  # Convert the input to an array
print("Arreglo unidimensional: ", e)

# La principal diferencia de array() y asarray() es que la primera copia el objet
# siguiente necesariamente no lo hace.


# Creando una secuencia de números.
f = np.arange(10, 20, 2)
print("Secuencia de numeros en un arreglo: ", f)

g = np.linspace(0, 99, 10)  # Arreglo de números consecutivos del 0 al 99 con espaci
print(g)

# forma de un arreglo
a = np.array([[1, 2], [2, 3], [5, 6]])
print(a.shape)  # Devuelve una tupla con el numero de filas y columnas
print(a.size)  # Devuelve el número total de elementos
print(a.ndim)  # Devuelve la cantidad de dimensiones del arreglo
print(a.dtype)  # Devuelve el tipo de datos de los elementos en el arreglo

# indexing
a = np.array([[1, 2], [3, 4]])
b = a[0][1]
print("a: ", a)
print("b: ", b)

# slicing
a = np.arange(10)
print(a)
print(
    a[2:8:2]
)  # Selecciona elementos desde el índice 2 hasta el índice 8 (exclusivo) con un paso de 2.
print(a[2:8])  # Selecciona elementos desde el índice 2 hasta el 8 (exclusivo)
print(a[2])  # Devuelve el indice 1
print(a[2:])  # Devuelve los elementos desde el indice 2 hasta el final del arreglo

# shape (dimensión de un arreglo)
a = np.arange(6)
b = a.reshape(
    2, 3
)  # Se está reorganizando en una matriz bidimensional con 2 filas y 3 columnas
print(a)
print(b)

# Multiplicación de dos arreglos de la misma dimension
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
c = a * b
print(c)

# Multiplicación de dos arreglos de diferentes dimensiones.
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([1, 2, 3])
print(a.shape)
print(b.shape)
np.array([b, b, b])  # utilizamos b para crear un arreglo de la misma dimension de a
# Para poder realizar cualquier operación de matrizes.
c = a + b
print("a: \n", a)
print("broadcasting:\n", c)


# Funciones de la libreria
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a.flat[:])  # Imprime todos los elementos en un orden unidimensional
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.transpose(a))  # Devuelve la matriz transpuesta

a = np.arange(6).reshape(2, 3)
b = np.insert(
    a, 2, [7, 8], axis=1
)  #  insertar los valores [7, 8] en la columna 2 de la matriz a. La especificación axis=1 indica que la inserción se debe realizar a lo largo del eje de las columnas.
c = np.insert(
    a, 2, [7, 8]
)  #  Aplana la matriz a y luego inserta [7, 8] en la posición 2 de ese arreglo plano.
print("a=", a)
print("b=", b)
print("c=", c)


a = np.arange(6).reshape(2, 3)
b = np.delete(
    a, 1, axis=1
)  # eliminar la columna 1 de la matriz a. La especificación axis=1 indica que la eliminación se debe realizar a lo largo del eje de las columnas
c = np.delete(a, 1)
print("a\n", a)
print("b\n", b)
print("c\n", c)


# Matix
import numpy.matlib

a = np.matlib.zeros((2, 2))
b = np.matlib.ones((2, 2))
print("a=", a)
print("b=", b)

c = np.matlib.eye(3)
print("c=", c)

# Transferir un arreglo a una matriz
a = np.array([[1, 2], [3, 4]])
d = np.mat(a)  # Convertir el arreglo en una matriz
print("d=", d)
print(type(d))

# Transferir una matrix a un array
a = np.mat([[1, 2, 3], [4, 5, 6]])
b = a.getA()  # Convierte la matrix como arreglo
print("matrix a=", a)
print(type(a))
print("array b=", b)
print(type(b))

a = np.matlib.rand(
    3, 3
)  # Crea una matriz de tipo matrix de 3 x 3 con numeros aleatorios
print("a=", a)
print(type(a))

# Operaciones con matrices
# Multiplicación
a = np.array([[1, 0], [0, 1]])
b = np.array([[1, 1], [2, 2]])
print(np.dot(a, b))
print(a @ b)
print(np.multiply(a, b))
print(a * b)


# Matriz inversa
a = np.matrix([[2, 0, 0], [0, 1, 0], [0, 0, 2]])
b = a.I
print("matrix a=", a)
print("matrix b=", b)


# Matriz determinante
a = np.matrix([[1, 2], [3, 4]])
b = np.linalg.det(a)
print("matrix a=", a)
print(" b=", b)

a = np.matrix([[1, 2], [3, 4]])
b = a.sum(axis=0)
c = a.sum(axis=1)
print("matrix a=", a)
print(" b=", b)
print(" c=", c)

d = a.max()
e = a.min()
print(" d=", d)
print(" e=", e)

r1 = np.random.rand(
    2, 2
)  # Genera una matriz de 2x2 de números aleatorios que siguen una distribución normal estándar (media 0 y desviación estándar 1)
r2 = np.random.randn(2, 2)
r3 = np.random.randint(
    0, 5
)  # Genera un único número entero aleatorio en el rango [0, 5) (excluyendo 5)
print(r1)
print(r2)
print(r3)

# Genera una matriz 2x2 donde los elementos son seleccionados aleatoriamente del conjunto [1, 2, 3, 4, 5]. Sin embargo, se especifican probabilidades para cada elemento en el argumento p. Las probabilidades indican la probabilidad de seleccionar cada elemento.
r4 = np.random.choice([1, 2, 3, 4, 5], (2, 2), p=[0.1, 0, 0.4, 0.5, 0])
print(r4)

a = np.array([1, 2, 3, 4, 5])
np.random.shuffle(a)  # Reorganiza aleatoriamente afectando al arreglo original
print("a=", "\n", a)
b = np.random.permutation(
    [1, 2, 3, 4, 5]
)  # Reorganiza aleatoriamente sin afectar al arreglo original
print("a=", "\n", a)
print("b=", "\n", b)

# Distribuciones
r1 = np.random.normal(
    0, 0.1, 5
)  # Genera una secuencia de 5 números aleatorios que siguen una distribución normal (gaussiana). Los argumentos son la media (0) y la desviación estándar (0.1) de la distribución normal.
r2 = np.random.uniform(
    0, 5, 2
)  # genera una secuencia de 2 números aleatorios que siguen una distribución uniforme en el rango [0, 5)
r3 = np.random.poisson(
    5, 2
)  # Genera una secuencia de 2 números aleatorios que siguen una distribución de Poisson. La distribución de Poisson se utiliza comúnmente para modelar eventos raros o aleatorios. Los argumentos son la tasa de ocurrencia (5) y el número de muestras (2).
print("r1=", "\n", r1)
print("r2=", "\n", r2)
print("r3=", "\n", r3)

# Funciones trigono metricas
a = np.array([0, 30, 45, 60, 90])
b = np.sin(a * np.pi / 180)
c = np.cos(a * np.pi / 180)
print("b=", b)
print("c=", c)

# redondeo
a = np.array([1.0, 1.5, 2.0, 2.55])
b = np.around(a)
c = np.around(a, decimals=1)
print("b=", b)
print("c=", c)

a = np.array([1.0, 1.5, 2.0, 2.55])
d = np.floor(a)
e = np.ceil(a)
print("d=", d)
print("e=", e)

a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])
c = np.add(a, b)
d = np.subtract(a, b)
e = np.multiply(a, b)
f = np.divide(a, b)
g = np.mod(a, b)
h = np.power(a, b)
print("c=", c)
print("d=", d)
print("e=", e)
print("f=", f)
print("g=", g)
print("h=", h)

a = np.array([[6, 7, 2], [0, 1, 5]])
b = np.amin(a, 0)
c = np.amax(a, 1)
d = np.median(a)
e = np.mean(a)
print("a=", a)
print("b=", b)
print("c=", c)
print("d=", d)
print("e=", e)

# Funcion sort
a = np.array([[3, 5, 1], [2, 8, 7]])
b = np.sort(a)
c = np.sort(a, axis=0)
print(b)
print(c)
