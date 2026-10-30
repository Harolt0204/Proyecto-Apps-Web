# Workshop 6: fallo intencional de la prueba de API

Fecha: 30 de octubre de 2026.

## Cambio y resultado

Se cambió temporalmente la respuesta de `GET /health` de `{"status":"ok"}` a `{"status":"error"}`, sin modificar la prueba. El cambio se guardó en el commit [4c3671a](https://github.com/Harolt0204/Proyecto-Apps-Web/commit/4c3671a345ac46f45dec3b7cc92d18beff4db70f) de la rama `codex/api-health`.

Ruff terminó sin errores porque el código seguía cumpliendo sus reglas. Pytest detectó el comportamiento incorrecto en la comparación `assert response.json() == {"status": "ok"}` y terminó con código de salida 1. La respuesta seguía siendo HTTP 200 y JSON, pero su contenido incumplía el contrato esperado.

La [ejecución fallida](https://github.com/Harolt0204/Proyecto-Apps-Web/actions/runs/41061161773) muestra **Lint with Ruff** aprobado y **Test API with pytest** fallido. No se fusionó el pull request.

El [registro del paso fallido](evidence/02-test-failure.log) se descargó de GitHub Actions; conserva las marcas de tiempo UTC del servicio.

## Corrección

Se restauró `{"status":"ok"}` en la API. La prueba permaneció sin cambios: no se debilitó la comprobación ni se aceptó la respuesta incorrecta. Tras la corrección, Ruff terminó sin errores y la prueba de la API pasó localmente.

La [ejecución corregida en GitHub Actions](https://github.com/Harolt0204/Proyecto-Apps-Web/actions/runs/41061390999) terminó aprobada. Después se [fusionó el pull request #1](https://github.com/Harolt0204/Proyecto-Apps-Web/pull/1) y el [pipeline de main](https://github.com/Harolt0204/Proyecto-Apps-Web/actions/runs/41063038695) también pasó.

## Qué demuestra

La revisión estática y las pruebas verifican aspectos diferentes. Una respuesta puede cumplir las reglas de código y aun así ser incorrecta para sus consumidores. Esta prueba detecta ese cambio de comportamiento antes de fusionarlo con `main`.

## Capturas para el informe

Abrir la ejecución fallida, seleccionar **Lint and API tests** y desplegar **Test API with pytest**. Capturar el `AssertionError` con los valores esperado y recibido, junto con Ruff aprobado y Pytest fallido. Después capturar la ejecución aprobada de la corrección. Numerar y explicar cada captura; el registro complementa las capturas y no las sustituye.
