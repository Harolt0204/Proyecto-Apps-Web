# Guion de presentación — Thesis Management (Project Proposal)

**Duración estimada:** 12–14 minutos (≈ 1 minuto por diapositiva) + preguntas.

| Expositor | Diapositivas | Bloque | Tiempo aprox. |
| :-- | :-: | :-- | :-: |
| Fernando | 1–4 | Introducción y problema | 4 min |
| Mateo | 5–9 | Objetivos, justificación y fundamentos técnicos | 4–5 min |
| Harolt | 10–14 | Trabajo relacionado, metodología, plan y cierre | 4–5 min |

> Las diapositivas están en inglés y la exposición en español. Los términos técnicos (REST, JWT, RBAC, Scrum, sprint, migrations) se dicen tal cual.

---

## Fernando — Introducción y problema

### Diapositiva 1 · Portada
Buenos días. Somos Fernando Chantera, Harolt Farinango y Mateo Pilaquinga, y les presentamos nuestra propuesta de proyecto para Aplicaciones Web: **Thesis Management**, una plataforma web basada en roles para gestionar de principio a fin el proceso de tesis y titulación de pregrado.

Antes de empezar, un poco de contexto: este proyecto no parte de cero. Continúa el trabajo de un compañero que, en la materia de Bases de Datos, diseñó la base de datos de este sistema. Nuestra propuesta es tomar esa base de datos como punto de partida, corregirla y construir sobre ella una aplicación web completa y en producción.

### Diapositiva 2 · El proceso de titulación
Empecemos por entender el problema. Graduarse implica nueve pasos que dependen unos de otros y en los que participan muchas personas: el registro y la aprobación del tema, la asignación de tutor y cotutor, Titulación I y II, la revisión por un comité de tres profesores, el control de similitud o plagio, la certificación de requisitos administrativos, la programación de la defensa, la defensa con las notas del tribunal y, por último, la nota final y la graduación.

Lo importante son los pasos 4, 5 y 6: funcionan como un filtro. Sin el comité completo, el análisis de plagio aprobado y todos los requisitos certificados, no se puede programar la defensa. Además, requisitos como las prácticas preprofesionales, la vinculación con la sociedad y el inglés los exige el Reglamento de Régimen Académico del CES, así que la universidad también tiene que poder **demostrar** que se verificaron.

### Diapositiva 3 · Herramientas desconectadas
Hoy ese proceso se maneja con herramientas que no se comunican entre sí: un sistema aparte para emitir oficios, otra herramienta para reservar las aulas, módulos dispersos para validar solvencias y hojas de cálculo locales para coordinar calendarios y tribunales.

¿Qué provoca esto? El personal tiene que consolidar la información a mano. Eso genera retrasos y registros inconsistentes, y no deja rastro de quién aprobó qué ni cuándo. Basta con que se pase por alto un solo paso, por ejemplo una solvencia, para que la graduación de un estudiante se retrase un periodo académico completo.

### Diapositiva 4 · La base de datos heredada
Y aquí está la segunda parte del problema. Revisamos todo lo que dejó el proyecto anterior: documentos, diagramas, el modelo de Power Architect y el código. Encontramos **cuatro versiones distintas del mismo esquema** que no coinciden entre sí.

En la versión que realmente se ejecuta, las reglas clave no se cumplen: el sistema acepta dos tutores principales, más de tres revisores o una nota de 15 sobre 10. Tampoco hay usuarios, autenticación ni separación de roles, y faltan el historial de cambios, la gestión de aulas y la validación de requisitos antes de la defensa.

Por eso decimos que la base heredada es un buen cimiento, pero todavía no es un producto. El problema es doble: la institución necesita un sistema centralizado, y ese sistema necesita una base de datos que haga cumplir las reglas.

*Transición:* Con esto claro, Mateo les va a presentar qué nos proponemos lograr.

---

## Mateo — Objetivos, justificación y fundamentos

### Diapositiva 5 · Objetivo general
Gracias, Fernando. Nuestro objetivo general es **diseñar, desarrollar y desplegar una aplicación web segura y basada en roles que centralice el proceso de tesis y titulación**, desde el registro del tema hasta la nota final de la defensa, sobre la base de datos heredada ya corregida.

Quiero destacar cuatro palabras: *segura*, *basada en roles*, *centralizada* y *desplegada*. La meta no es otro prototipo, sino un producto que se use de verdad.

### Diapositiva 6 · Objetivos específicos
Ese objetivo lo dividimos en seis objetivos específicos.

Los tres primeros tratan de que el sistema sea **correcto**:
1. Un esquema que haga cumplir las reglas: que la propia base de datos garantice un solo tutor, máximo tres revisores y notas válidas, y que todos los cambios se apliquen mediante migraciones versionadas.
2. Una API REST segura, con autenticación y autorización por roles, donde los permisos de tutor y revisor se obtengan de cada tesis.
3. Un flujo automatizado: una tesis solo avanza si cumple los prerrequisitos, y las defensas se programan sin choques de aula ni de tribunal.

Los otros tres tratan de **trazabilidad, uso y puesta en producción**:

4. Un historial de auditoría que registre quién hizo cada cambio de estado y cuándo.
5. Interfaces específicas para cada rol y reportes de carga de tutores, notas por escuela y disponibilidad de aulas.
6. Pruebas automatizadas y funcionales, y el despliegue en producción.

### Diapositiva 7 · Justificación
¿Por qué vale la pena construirlo? Por tres razones.

Es **relevante**: los errores en este proceso cuestan defensas aplazadas y trámites repetidos, y el reglamento exige evidencia de que cada requisito se verificó.

Es **útil**: habrá una única fuente de verdad. El estudiante ve qué le falta, el profesor solo actúa sobre las tesis en las que participa y el personal programa las defensas sin choques. Las reglas las hace cumplir el sistema y no dependen de la disciplina de las personas.

Y es **formativo**: recorremos todo el ciclo de vida de una aplicación web con un cliente real, aprovechando el trabajo del curso anterior en lugar de desecharlo.

### Diapositiva 8 · Fundamentos técnicos
El sistema se apoya en seis conceptos:
- **Integridad relacional:** claves, restricciones CHECK y triggers en MySQL 8, para que las reglas vivan en la base de datos.
- **Migraciones:** con SQLAlchemy y Alembic, el esquema evoluciona en pasos versionados y reversibles, en lugar de borrarlo y recrearlo.
- **REST con FastAPI:** recursos sobre HTTP y JSON, con validación tipada y documentación OpenAPI generada automáticamente.
- **JWT y RBAC:** tokens firmados para la autenticación y control de acceso basado en roles, tomando como guía el OWASP API Security Top 10.
- **Single-page application:** un cliente web desacoplado de la API, que se puede desarrollar y desplegar por separado.
- **Historial de auditoría:** registros inmutables que se escriben en la misma transacción que el cambio, para que nunca se desincronicen.

### Diapositiva 9 · Modelo de permisos
Este punto es una de las correcciones más importantes que hicimos al diseño original. Ahí se trataba a "tutor" y "revisor" como roles de usuario, pero en la realidad un mismo profesor puede ser tutor de una tesis y revisor de otra.

Por eso proponemos solo **tres roles globales**: administrador, profesor y estudiante. Los permisos de tutor, revisor o presidente del tribunal **se obtienen de las asignaciones de cada tesis**. En la tabla se ve: el profesor A es tutor de la tesis 1 y revisor de la tesis 2, y no tiene ningún papel en la tesis 3.

Si un usuario no está asignado a una tesis, no puede verla ni modificarla. Con eso evitamos el riesgo número uno del OWASP API Security Top 10, la autorización rota a nivel de objeto.

*Transición:* Ahora Harolt les cuenta cómo nos comparamos con lo que ya existe y cómo vamos a trabajar.

---

## Harolt — Trabajo relacionado, metodología y cierre

### Diapositiva 10 · Trabajo relacionado
Gracias, Mateo. Revisamos sistemas publicados de gestión de tesis. Entre ellos están un sistema basado en un motor de workflow de 2012, un sistema chino para la selección de temas, un LMS iraní para tesis de maestría y un sistema ecuatoriano de la Universidad Técnica de Cotopaxi, desarrollado con Scrum. También revisamos ThesisIT, que programa defensas de forma automática, un diseño indonesio de monitoreo de proyectos finales y la plataforma de código abierto de la Universidad Técnica de Múnich, que es la más completa.

En la tabla comparamos siete características. Una aclaración importante: un guion significa que **la fuente no lo reporta**, no que ese sistema no pueda hacerlo. Solo comparamos lo que cada publicación describe.

### Diapositiva 11 · La brecha
De esa comparación salen tres cosas que **ningún sistema revisado reporta**:
1. La validación de los requisitos que exige la normativa ecuatoriana antes de la defensa: prácticas, vinculación e inglés.
2. El registro de los análisis de similitud como parte del expediente de la tesis.
3. Un historial auditable de cada cambio de estado.

Ahí está nuestro aporte: estas reglas las hace cumplir la base de datos, los permisos se obtienen de cada tesis y la plataforma se construye sobre un esquema que ya fue diseñado para la institución.

### Diapositiva 12 · Metodología
Vamos a trabajar con **Scrum en sprints de dos semanas**. Scrum ya ha funcionado bien en proyectos estudiantiles y es la misma metodología que usó el antecedente ecuatoriano más cercano. Cada sprint pasa por el backlog, la planificación, el desarrollo con pruebas y la revisión con el cliente, y termina con un **incremento desplegado**. Lo que el cliente nos dice en la revisión vuelve al backlog.

Hay tres puntos clave:
- **Fase 0, descubrimiento:** antes de programar, validamos con el cliente las reglas que todavía están abiertas, como la lista oficial de requisitos, el manejo de documentos, el flujo de estados y el cálculo de la nota final, y registramos cada decisión en un log.
- **Primero los datos:** la primera migración reproduce el esquema heredado y luego aplicamos las correcciones.
- **Definición de terminado:** una funcionalidad está lista solo si está implementada, probada, documentada en OpenAPI y se mostró en la revisión.

### Diapositiva 13 · Plan de sprints
El plan tiene siete incrementos. El sprint 0 cubre la validación con el cliente, el repositorio, la integración continua y la migración base. En el sprint 1 corregimos el esquema e implementamos usuarios y autenticación. En el 2 registramos estudiantes, profesores, periodos, tesis y tutores. En el 3, el flujo de estados con su historial y el comité revisor. En el 4, el plagio, los requisitos administrativos y el filtro previo a la defensa. En el 5, las aulas, la programación de defensas sin choques y la calificación del tribunal. Y en el 6, los reportes, las pruebas finales y el despliegue en producción.

Cada incremento incluye su API, su interfaz y sus pruebas, así que en cada sprint entregamos algo usable. Las fechas exactas las ajustaremos al calendario de la materia.

### Diapositiva 14 · Próximos pasos
Para cerrar, estos son nuestros próximos pasos:
1. Validar con el cliente los requisitos, los documentos y el flujo de estados.
2. Cerrar el modelo de datos y el registro de decisiones.
3. Arrancar el sprint 0 con el repositorio, la integración continua y la migración base.

Muchas gracias por su atención. Quedamos atentos a sus preguntas.

---

## Preguntas probables (para preparar en equipo)

| Pregunta | Respuesta sugerida |
| :-- | :-- |
| ¿Por qué no reutilizan el código Flask del proyecto anterior? | Casi todos los endpoints cambian con las correcciones del modelo. Además, el código no tenía capa de servicios, manejo de transacciones ni pruebas. Conservamos los modelos como base de la migración inicial. |
| ¿Por qué FastAPI y no Flask? | Es el framework que mejor domina el equipo. Además trae validación con Pydantic y documentación OpenAPI integradas, y usa el mismo SQLAlchemy y Alembic. |
| ¿Qué pasa si el cliente cambia los requisitos? | Para eso está la Fase 0 y el log de decisiones. Lo que depende del cliente se planifica después de validarlo, y las migraciones permiten cambiar el esquema sin perder datos. |
| ¿Cómo evitan dos defensas a la misma hora en la misma aula? | Antes de guardar, la API comprueba con bloqueo si hay solapamiento de horario en el aula y entre los miembros del tribunal. |
| ¿Por qué validar reglas en la base de datos y no solo en la API? | Porque así ningún camino, ni siquiera un script o un error de código, puede dejar datos inválidos. La API vuelve a validar para dar mensajes claros. | Fernando |
