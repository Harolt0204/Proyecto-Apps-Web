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

Este repositorio contiene la documentación inicial. La API todavía no está implementada.

El primer avance de desarrollo corresponde al Workshop 6: una API mínima, pruebas automatizadas y un flujo de integración continua con GitHub Actions.

## Trabajo en equipo

La rama principal es `main`. Los cambios de desarrollo se realizarán en ramas separadas y se revisarán mediante pull requests. El laboratorio incorporará las comprobaciones automáticas antes de fusionar cambios.

Los entornos de Python y los archivos `.env` se excluyen mediante `.gitignore`. No se deben guardar contraseñas ni tokens en el repositorio.
