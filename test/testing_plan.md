# Plan de Pruebas Automatizadas - NewUserApp

Este documento describe el plan de pruebas automatizadas para la aplicación de registro basada en Flet, Fleting y Supabase, asegurando que se cumplan los requisitos de seguridad, i18n y funcionalidad.

## Estrategia de Pruebas

Se propone un enfoque de pirámide de pruebas:
1.  **Pruebas Unitarias (Unit Tests)**: Validación de lógica en controladores y modelos sin dependencias externas.
2.  **Pruebas de Integración (Integration Tests)**: Verificación de la comunicación con Supabase (Auth y Base de Datos) utilizando mocks.
3.  **Pruebas de Interfaz de Usuario (UI/Functional Tests)**: Validación de navegación y componentes usando el módulo `flet.testing`.

## User Review Required

> [!IMPORTANT]
> Se recomienda el uso de **pytest** como framework principal de ejecución.
> Para las pruebas de UI, se utilizará el soporte nativo de **flet.testing** para simular interacciones sin necesidad de un navegador pesado.

## Escenarios de Prueba Propuestos

### 1. Autenticación y Seguridad
- **Registro de Usuario**: Validar que el flujo de registro captura correctamente los datos y lanza el evento de confirmación de email.
- **Validación de Contraseñas**: Verificar que las contraseñas cumplen con los criterios de seguridad (8+ caracteres, min/may, número, especial).
- **Login**: Validar acceso exitoso y manejo de errores (credenciales inválidas, email no confirmado).

### 2. Gestión de Perfil
- **Redirección de Perfil Incompleto**: Verificar que un usuario con perfil incompleto sea redirigido forzosamente a `ProfileCompletionView`.
- **Dashboard**: Validar que los datos del perfil se muestran correctamente según el `UserProfile`.

### 3. Internacionalización (i18n)
- **Cambio de Idioma**: Comprobar que al cambiar el estado global a 'en' o 'es', las etiquetas de la UI se actualizan correctamente usando `I18n.t()`.

### 4. Responsividad
- **Dimensiones Móviles**: Verificar que la aplicación mantiene sus dimensiones tipo iPhone (~390x844px) en diferentes entornos.

---

## Cambio Propuestos (Estructura de Directorios)

### [Componente de Pruebas]

#### [NEW] [tests/](file:///c:/Users/USUARIO/Documents/Proyectos/NewUserApp/tests/)
- Carpeta raíz para todos los archivos de prueba.

#### [NEW] [conftest.py](file:///c:/Users/USUARIO/Documents/Proyectos/NewUserApp/tests/conftest.py)
- Configuración global de pytest y fixtures (muecas de Supabase, inicialización de AppState).

#### [NEW] [test_auth.py](file:///c:/Users/USUARIO/Documents/Proyectos/NewUserApp/tests/test_auth.py)
- Pruebas de lógica de registro, login y recuperación.

#### [NEW] [test_ui_flows.py](file:///c:/Users/USUARIO/Documents/Proyectos/NewUserApp/tests/test_ui_flows.py)
- Pruebas de navegación y renderizado de componentes Flet.

---

## Plan de Verificación

### Pruebas Automatizadas
Para ejecutar las pruebas una vez implementadas, se utilizarán los siguientes comandos:

```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar pruebas con reporte de cobertura
pytest --cov=core --cov=controllers
```

### Verificación Manual
- El usuario podrá verificar la integración enviando correos reales de prueba a través de la consola de Supabase y observando la respuesta en la UI.
- Validar visualmente que el "Contenedor Móvil" se mantiene centrado en pantallas de escritorio.
