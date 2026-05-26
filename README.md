# LABORATORIO 2 Oscar Rivera Solis

## Descripción

Proyecto de automatización web desarrollado con Python y Playwright.

El proyecto automatiza diferentes funcionalidades del sitio:
https://storedemo.testdino.com/

---

## Tecnologías utilizadas

- Python
- Playwright

---

## Estructura del proyecto

```text
SOFT-311-Lab2-OscarRivera/
│
├── pages/
│   ├──  __init__.py
│   ├──  faq_page.py
│   ├──  login_page.py
│   ├──  products_page.py
│   ├──  register_page.py
│   ├──  review_page.py
│
├── tests/
│   ├── test_faq.py
│   ├── test_login.py
│   ├── test_register.py
│   ├── test_review.py
│   ├── test_view_mode.py
│
├── screenshots/
│   ├── faq.png
│   ├── listviewsuccess.png
│   ├── loginsuccess.png
│   ├── registersuccess.png
│   ├── reviewsuccess.png
│
├── README.md
└── pyproject.toml
```

---

# Casos de Prueba Automatizados

---

## test_register - Validacion de Creacion de cuentas

### Objetivo
Verificar que un usuario pueda crear una cuenta exitosamente en el sistema.

### Pasos
1. Ingresar al link de signup.
2. Completar el formulario con datos válidos.
3. Presionar el botón de crear cuenta.

### Resultado Esperado
El sistema debe mostrar el mensaje:

```text
Account created successfully! Please login to continue.
```

---

## test_login - Validación de inicio de sesión

### Objetivo
Validar que un usuario registrado pueda iniciar sesión correctamente.

### Pasos
1. Ingresar al link de login.
2. Completar el formulario con datos válidos.
3. Presionar el botón de Sign in.

### Resultado Esperado
El sistema debe mostrar el mensaje:

```text
Logged in successfully
```

---

## test_faq - Expansión de FAQ

### Objetivo
Validar que las preguntas frecuentes se expandan al hacer clic.

### Pasos
1. Ingresar al link principal del sitio web.
2. Dirigirse a la parte inferior de dicha pagina.
3. Presionar el titulo de una pregunta frecuente.

### Resultado Esperado
La pregunta frecuente debe expandirse y mostrar su contenido.

---

## test_view_mode - Validación de cambio de vista de productos

### Objetivo
Validar que el listado de productos cambió de vista cuadriculada a vista lista.

### Pasos
1. Ingresar al link de products.
2. Presionar el boton de Switch a listado.
3. Verificar el listado mostrado en pantalla.

### Resultado Esperado
El sistema debe cambiar correctamente la vista

---

## test_review - Publicación de Review

### Objetivo
Verificar que un usuario pueda publicar una review correctamente.

### Pasos
1. Ingresar al link de products.
2. Presionar un producto del listado.
3. Presionar la seccion de review. 
4. Presionar el boton de Write a review.
5. Rellenar el formulario con datos validos.
6. Presionar el boton de Submit.

### Resultado Esperado
La review debe mostrarse con el título:

```text
Titulo de Pruebas
```

---


## Assertions implementados

### Validacion de Creacion de cuentas: Verifica que el sistema muestre el mensaje correcto después de crear una cuenta. 
```python
assert page.get_by_role("status").text_content() == "Account created successfully! Please login to continue."
```

### Validación de inicio de sesión: Comprueba que el usuario inició sesión correctamente.
```python
assert page.get_by_role("status").text_content() == "Logged in successfully"
```

### Validación de expansión de Faq : Verifica que una pregunta frecuente se expanda al hacer clic. 
```python
assert faq.faq_is_expanded(), "FAQ did not expand correctly"
```

### Validación de cambio de vista de productos: Confirma que el listado de productos cambió de vista cuadriculada a vista lista.
```python
assert "all-products-view-switcher-list" in page.content()
```

### Validación de publicación de review: Verifica que la review creada se publique correctamente.
```python
assert page.locator("[data-testid='review-title']").text_content() == "Titulo de Pruebas"
```

---

## Ejecutar pruebas (Modificar luego del slash por el test que desee ejecutar)

### Para Mac

```bash
.venv/bin/python tests/login_test.py
```

### Para Windows

```bash
.venv\Scripts\python tests\login_test.py
```

---

## Repositorio GitHub

Repositorio oficial del proyecto:

https://github.com/Test-Isaak/SOFT-311-Lab2-OscarRivera