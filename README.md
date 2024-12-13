# Club de Poesía - Tercera Pre-Entrega Agustin

Este proyecto es una página web desarrollada en Django que permite explorar y gestionar información sobre dos cursos de poesía inspirados en grandes autores como Shakespeare y Heine.

---


1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/MercedesAgustin/Tercera-pre-entrega-AgustinMaria.git
   cd Tercera-pre-entrega-AgustinMaria
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   python -m venv venv
    ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar las migraciones**:
   ```bash
   python manage.py migrate
   ```

5. **Cargar datos iniciales (si aplica)**:
     ```bash
   python manage.py loaddata nombre_archivo.json
   ```

6. **Ejecutar el servidor**:
   ```bash
   python manage.py runserver
   ```

7. **Abrir la página en el navegador**:
   Accede a `http://127.0.0.1:8000/` para comenzar.

---

## **Orden para probar las funcionalidades**

### 1. **Página de Inicio**
   - URL: [http://127.0.0.1:8000/app/inicio](http://127.0.0.1:8000/app/inicio)
   - Contenido: Introducción al club de poesía y enlaces a las secciones principales.

### 2. **Sección de Cursos**
   - URL: [http://127.0.0.1:8000/app/cursos](http://127.0.0.1:8000/app/cursos)
   - Descripción: Muestra los cursos disponibles: Shakespeare y Heine.

### 3. **Sección de Estudiantes**
   - URL: [http://127.0.0.1:8000/app/estudiantes](http://127.0.0.1:8000/app/estudiantes)
   - Descripción: Información sobre cómo unirse y qué actividades están disponibles para estudiantes.

### 4. **Sección de Profesores**
   - URL: [http://127.0.0.1:8000/app/profesores](http://127.0.0.1:8000/app/profesores)
   - Descripción: Información sobre los profesores encargados de los cursos.

### 5. **Contacto**
   - URL: [http://127.0.0.1:8000/app/contacto](http://127.0.0.1:8000/app/contacto)
   - Descripción: Formulario para contactar al club o solicitar más información.

---

## **Ubicación de las funcionalidades en el proyecto**

### **Plantillas HTML:**
- Todas las plantillas HTML están en `ClubDePoesia/app/templates/app/`.
  - `inicio.html`: Página de inicio.
  - `cursos.html`: Página de cursos.
  - `estudiantes.html`: Página de estudiantes.
  - `profesores.html`: Página de profesores.
  - `contacto.html`: Página de contacto.

### **Archivos estáticos:**
- Los archivos CSS, JavaScript e imágenes están en `ClubDePoesia/app/static/app/`.
  - CSS: `ClubDePoesia/app/static/app/css/`
  - JS: `ClubDePoesia/app/static/app/js/`
  - Imágenes: `ClubDePoesia/app/static/app/assets/img/`
    - Ejemplo: [1.jpeg](https://github.com/MercedesAgustin/Tercera-pre-entrega-AgustinMaria/blob/main/ClubDePoesia/app/static/app/assets/img/portfolio/fullsize/1.jpeg)

### **Rutas y vistas:**
- Las rutas están definidas en `ClubDePoesia/app/urls.py`.
- Las vistas están en `ClubDePoesia/app/views.py`.

---
