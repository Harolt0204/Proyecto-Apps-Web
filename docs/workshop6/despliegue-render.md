# Despliegue gratuito de la API en Render

## Configuración preparada

`render.yaml` define un servicio web de Python con plan `free`, conectado a `main`. `.python-version` selecciona Python 3.12, la misma serie utilizada en CI.

La instalación utiliza `python -m pip install -r requirements.txt`. El inicio utiliza `python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT`. Render proporciona `PORT`; no se utiliza `--reload` en el servidor público.

`healthCheckPath: /health` permite a Render comprobar que la API responde. `autoDeployTrigger: checksPass` solicita esperar las comprobaciones de CI antes de desplegar nuevos cambios. Para que funcione la integración de CI, se debe conectar la cuenta de GitHub; introducir únicamente la URL de un repositorio público no habilita esta integración.

## Crear el servicio

1. Registrarse e iniciar sesión en [Render](https://dashboard.render.com/).
2. Elegir **New > Blueprint** y conectar GitHub. Dar acceso al repositorio `Harolt0204/Proyecto-Apps-Web`.
3. Seleccionar ese repositorio y la rama `main`. Render leerá `render.yaml`.
4. Revisar que el único recurso sea `thesis-management-api`, de tipo Web Service y plan **Free**. No se necesita una base de datos para este endpoint.
5. Crear el Blueprint y esperar el resultado de la instalación y el inicio. Comprobar que el servicio muestra **Live**.
6. En la configuración del servicio verificar rama **main** y Auto-Deploy **After CI Checks Pass**. La creación inicial del servicio debe partir del commit de `main` con CI aprobado; esta opción controla los despliegues automáticos posteriores.
7. Copiar la URL real que asigne Render y consultar `/health`. Debe devolver HTTP 200 y `{"status":"ok"}`. Consultar también `/docs`.

La URL pública solo se podrá registrar como evidencia después de crear y verificar el servicio. Preparar estos archivos no publica la API.

## Evidencias del laboratorio

- Configuración del servicio: plan Free, rama main y despliegue después de CI.
- Instalación e inicio exitosos con el commit desplegado.
- Estado Live y URL pública real.
- Petición pública a `/health` con HTTP 200 y la respuesta JSON.

## CI, entrega y despliegue

- **CI:** GitHub Actions revisa el código y ejecuta la prueba.
- **Entrega continua:** los cambios validados quedan preparados para publicarse; una persona puede iniciar su despliegue.
- **Despliegue continuo:** una vez conectado y verificado el servicio, Render puede publicar los nuevos cambios de `main` automáticamente después de CI.

No se debe afirmar que hubo despliegue continuo basándose únicamente en un resultado verde de Actions. Hay que comprobar también la configuración y la publicación en Render.

## Limitaciones

El servicio gratuito se suspende tras 15 minutos sin tráfico y puede tardar alrededor de un minuto en volver a responder. Esta instancia es para la demostración del laboratorio; no representa el despliegue final de producción del proyecto.

La API todavía no usa MySQL ni almacena información de estudiantes o tesis. Para este despliegue mínimo no se requieren secretos de la aplicación.

## Referencias

- [Desplegar FastAPI](https://render.com/docs/deploy-fastapi)
- [Especificación de Blueprint](https://render.com/docs/blueprint-spec)
- [Versión de Python](https://render.com/docs/python-version)
- [Despliegues después de CI](https://render.com/docs/deploys)
- [Límites del plan gratuito](https://render.com/docs/free)
