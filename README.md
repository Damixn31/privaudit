# PRIVAUDIT

## Objetivo General

Crear una herramienta que analice archivos y sistemas locales en busca de datos sensibles expuestos, combinando expresiones regulares y lógica útil para seguridad digital personal, compliance o privacidad.

---

## Concepto del Proyecto

Herramienta que:
1. Escanea directorios o archivos específicos.
2. Detecta datos sensibles como:
  - Correo electrónicos.
  - Teléfonos
  - Tarjeta de crédito
  - Contraseñas débiles
  - Tokens/API Keys
  - CUIL/CUIT o DNIs (Argentina)
  - URLs con credenciales embebidas
3. Clasifica por nivel de riesgo (bajo, medio, alto).
4. Puede ejecutarse en:
  - .txt, .log, .csv, .env, .json, .html, etc.
5. Exporta resultados en: 
  - .json o .html para reportes visuales.

---

## Casos de uso posibles

- Auditar tu propio sistema para ver si dejaste datos sensibles en archivos olvidados.
- Analizar dumps de datos filtrados.
- Revisar logs de desarrollo antes de subir a producción.
- Escanear  backups, volcados, historial de comandos, configuraciones.
