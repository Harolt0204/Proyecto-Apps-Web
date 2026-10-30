# Thesis Management

Proyecto de Aplicaciones Web de Fernando Chantera, Harolt Farinango y Mateo Pilaquinga, Yachay Tech University.

Plataforma web para centralizar el proceso de tesis y titulación de pregrado, desde el registro del tema hasta la calificación de la defensa.

## Documentación

- [Propuesta principal](Proyecto_Apps_Web.pdf): define lo que se va a desarrollar.
- [Documento de punto de partida](documentation.md): análisis del proyecto heredado y decisiones técnicas. Sus pendientes deben contrastarse con la propuesta principal.
- [Presentación](Thesis%20Management%20%E2%80%93%20Project%20Proposal.pptx): diapositivas de la propuesta.
- [Guion de presentación](guion_presentacion.md): apoyo para la exposición del equipo.

## Tecnología prevista

Backend en FastAPI, con SQLAlchemy, Alembic y MySQL. Administradores, profesores y estudiantes tendrán acceso según su rol y su participación en cada tesis.

## Estado actual

Este repositorio contiene la documentación inicial y una API mínima en FastAPI.

### Ejecutar la API en Windows (PowerShell)

Se ha verificado con Python 3.12. Desde la carpeta del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Si el entorno `.venv` ya existe, omitir el primer comando. No es necesario activar el entorno para utilizar estos comandos.

- API: <http://127.0.0.1:8000/health>
- Documentación interactiva: <http://127.0.0.1:8000/docs>

`GET /health` devuelve HTTP 200 con `{"status":"ok"}`. Solo confirma que la API responde; todavía no comprueba MySQL ni las reglas del proceso de titulación. Para detener el servidor, presionar `Ctrl+C` en su terminal.

El código inicial está en `app/main.py`.

### Ejecutar las pruebas y la revisión de código

Instalar las dependencias de desarrollo (también incluyen las de la API):

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Ejecutar las comprobaciones desde la carpeta del proyecto:

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m pytest -v
```

Ruff revisa errores de código e importaciones. Pytest ejecuta `tests/test_health.py`, que comprueba que `GET /health` responde con HTTP 200, contenido JSON y `{"status":"ok"}`.

La prueba usa `TestClient` para enviar la petición directamente a la aplicación. No requiere iniciar Uvicorn ni tener MySQL instalado. Si una comprobación falla, el comando termina con un código de error; GitHub Actions utilizará ese resultado para marcar la ejecución como fallida.

### Integración continua con GitHub Actions

El archivo `.github/workflows/ci.yml` define el flujo **Thesis Management CI**. Se ejecuta al abrir o actualizar un pull request hacia `main` y al subir cambios a `main`.

El trabajo **Lint and API tests** descarga el repositorio en un entorno Ubuntu, prepara Python 3.12, instala `requirements-dev.txt`, revisa el código con Ruff y ejecuta Pytest. Si un paso falla, el trabajo falla y los pasos posteriores no se ejecutan.

Los resultados y los registros de cada paso se pueden consultar en la pestaña **Actions** del repositorio y en las comprobaciones del pull request. No requiere configurar contraseñas ni tokens manualmente.

Este flujo implementa CI: valida automáticamente los cambios. Todavía no despliega la API ni configura por sí solo la protección de `main`. Para impedir fusiones con errores, se debe exigir **Lint and API tests** en las reglas de la rama, si el repositorio lo permite.

El primer avance de desarrollo corresponde al Workshop 6: una API mínima, pruebas automatizadas y un flujo de integración continua con GitHub Actions.

## Despliegue de demostración

El repositorio incluye `render.yaml` para un servicio gratuito en Render. Consultar la [guía de despliegue](docs/workshop6/despliegue-render.md). Se requiere crear la cuenta, conectar GitHub y verificar la URL asignada. Estos archivos por sí solos no publican la API.

## Trabajo en equipo

La rama principal es `main`. Los cambios de desarrollo se realizarán en ramas separadas y se revisarán mediante pull requests. El laboratorio incorporará las comprobaciones automáticas antes de fusionar cambios.

Los entornos de Python y los archivos `.env` se excluyen mediante `.gitignore`. No se deben guardar contraseñas ni tokens en el repositorio.
