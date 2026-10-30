# Workshop 6: fallo intencional de revisión de código

Fecha: 30 de octubre de 2026.

## Cambio y resultado

Se añadió temporalmente `import os` en `app/main.py` sin utilizar el módulo. El cambio se guardó en el commit [c0afd4e](https://github.com/Harolt0204/Proyecto-Apps-Web/commit/c0afd4eb3366e0377e0e504b7079750607f2245c) de la rama `codex/api-health`.

Ruff detectó `F401: os imported but unused` y terminó con código de salida 1, tanto localmente como en GitHub Actions.

La [ejecución fallida](https://github.com/Harolt0204/Proyecto-Apps-Web/actions/runs/41060169957) muestra el fallo en **Lint with Ruff**. El paso **Test API with pytest** se omitió porque el paso anterior había fallado. No se fusionó el pull request.

El [registro del paso fallido](evidence/01-lint-failure.log) se descargó de GitHub Actions; conserva las marcas de tiempo UTC del servicio.

## Corrección

Se eliminó la importación innecesaria. No se desactivó ninguna regla de Ruff ni se cambió el comportamiento de `/health`. Tras la corrección, Ruff terminó sin errores y la prueba de la API pasó localmente.

La [ejecución corregida en GitHub Actions](https://github.com/Harolt0204/Proyecto-Apps-Web/actions/runs/41060441119) terminó aprobada, con Ruff y Pytest exitosos.

## Qué demuestra

La revisión estática puede detectar problemas aunque el endpoint siga respondiendo. Actions marca el trabajo como fallido y detiene sus pasos posteriores. Esto no configura por sí solo la protección de `main`: impedir una fusión con comprobaciones fallidas requiere reglas de la rama.

## Captura para el informe

Abrir la ejecución fallida, seleccionar **Lint and API tests** y desplegar **Lint with Ruff**. Capturar el mensaje `F401`, el código de salida 1 y el estado fallido. La captura debe ser legible, numerada y acompañada de una explicación. El archivo de registro complementa la captura y no la sustituye.
