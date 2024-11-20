import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define las funciones para calcular el área y el volumen de las figuras geométricas
def area_rectangulo(a, b):
    x, y = sp.symbols('x y')
    f = 1
    area = sp.integrate(f, (x, 0, a), (y, 0, b))
    return area

def area_circulo(r):
    x, y = sp.symbols('x y')
    f = 1
    area = sp.integrate(f, (x, -r, r), (y, -sp.sqrt(r**2 - x**2), sp.sqrt(r**2 - x**2)))
    return area

def area_triangulo(base, altura):,m/ nbn  n   
    x, y = sp.symbols('x y')
    f = 1
    area = sp.integrate(f, (x, 0, base), (y, 0, altura * (1 - x / base)))
    return area

def area_elipse(a, b):
    x, y = sp.symbols('x y')
    f = 1
    area = sp.integrate(f, (x, -a, a), (y, -b * sp.sqrt(1 - x**2 / a**2), b * sp.sqrt(1 - x**2 / a**2)))
    return area

def volumen_cubo(a):
    x, y, z = sp.symbols('x y z')
    f = 1
    volumen = sp.integrate(f, (x, 0, a), (y, 0, a), (z, 0, a))
    return volumen

def volumen_esfera(r):
    x, y, z = sp.symbols('x y z')
    f = 1
    volumen = sp.integrate(f, (x, -r, r), (y, -sp.sqrt(r**2 - x**2), sp.sqrt(r**2 - x**2)), (z, -sp.sqrt(r**2 - x**2 - y**2), sp.sqrt(r**2 - x**2 - y**2)))
    return volumen

def volumen_cono(r, h):
    x, y, z = sp.symbols('x y z')
    f = 1
    volumen = sp.integrate(f, (x, -r, r), (y, -sp.sqrt(r**2 - x**2), sp.sqrt(r**2 - x**2)), (z, 0, h * (1 - sp.sqrt(x**2 + y**2) / r)))
    return volumen

def volumen_cilindro(r, h):
    x, y, z = sp.symbols('x y z')
    f = 1
    volumen = sp.integrate(f, (x, -r, r), (y, -sp.sqrt(r**2 - x**2), sp.sqrt(r**2 - x**2)), (z, 0, h))
    return volumen

# Define las funciones para graficar las superficies
def graficar_superficie_esfera(r):
    x, y, z = sp.symbols('x y z')
    f = sp.sqrt(r**2 - x**2 - y**2)
    func = sp.lambdify((x, y), f, modules="numpy")
    x_vals = np.linspace(-r, r, 100)
    y_vals = np.linspace(-r, r, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = func(X, Y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    plt.title("Esfera")

def graficar_superficie_cono(r, h):
    x, y, z = sp.symbols('x y z')
    f = h * (1 - sp.sqrt(x**2 + y**2) / r)
    func = sp.lambdify((x, y), f, modules="numpy")
    x_vals = np.linspace(-r, r, 100)
    y_vals = np.linspace(-r, r, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = func(X, Y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    plt.title("Cono")

def graficar_superficie_cilindro(r, h):
    x, y, z = sp.symbols('x y z')
    f = sp.sympify(h)
    func = sp.lambdify((x, y), f, modules="numpy")
    x_vals = np.linspace(-r, r, 100)
    y_vals = np.linspace(-r, r, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = np.full_like(X, h)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    plt.title("Cilindro")

# Calcula el área y volumen de las figuras geométricas
area_rect = area_rectangulo(2, 3)
area_circ = area_circulo(5)
area_trian = area_triangulo(4, 6)
area_elip = area_elipse(3, 2)

volumen_cub = volumen_cubo(4)
volumen_esf = volumen_esfera(3)
volumen_con = volumen_cono(2, 5)
volumen_cil = volumen_cilindro(4, 6)

# Grafica las superficies
graficar_superficie_esfera(3)
graficar_superficie_cono(2, 5)
graficar_superficie_cilindro(4, 6)

# Imprime los resultados
print("Área del rectángulo:", area_rect)
print("Área del círculo:", area_circ)
print("Área del triángulo:", area_trian)
print("Área de la elipse:", area_elip)

print("Volumen del cubo:", volumen_cub)
print("Volumen de la esfera:", volumen_esf)
print("Volumen del cono:", volumen_con)
print("Volumen del cilindro:", volumen_cil)

# Muestra las gráficas
plt.show()