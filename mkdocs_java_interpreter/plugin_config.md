# 🔧 Configuración del Plugin Java Interpreter

## Instalación

Para usar el plugin de intérprete de Java en tu proyecto MkDocs:

### 1. Instalar el Plugin

```bash
pip install mkdocs-java-interpreter
```

### 2. Configurar mkdocs.yml

Añade el plugin a tu archivo `mkdocs.yml`:

```yaml
plugins:
  - search
  - java-interpreter:
      enabled: true
      theme: dark
      examples_path: examples/
```

### 3. Usar en Páginas

Para añadir el intérprete a una página específica, incluye este metadato:

```yaml
---
plugins:
  - java-interpreter
---

# Tu contenido aquí

{{java-interpreter}}
```

## Opciones de Configuración

| Opción | Tipo | Por defecto | Descripción |
|--------|------|-------------|-------------|
| `enabled` | boolean | `true` | Habilita o deshabilita el plugin |
| `theme` | string | `dark` | Tema del editor (`dark` o `light`) |
| `examples_path` | string | `examples/` | Ruta a archivos de ejemplos |

## Ejemplos de Uso

### Ejemplo Básico

```yaml
# mkdocs.yml
site_name: Mi Documentación Java
plugins:
  - java-interpreter

nav:
  - Inicio: index.md
  - Intérprete: java-page.md
```

```markdown
# java-page.md
---
plugins:
  - java-interpreter
---

# Página con Intérprete

{{java-interpreter}}

## Ejemplos de Código

Aquí puedes probar los conceptos que aprendes...
```

### Ejemplo Avanzado

```yaml
# mkdocs.yml
site_name: Tutorial Java Completo
plugins:
  - search
  - java-interpreter:
      enabled: true
      theme: light
      examples_path: docs/examples/

nav:
  - Inicio: index.md
  - Conceptos Básicos:
    - Variables: variables.md
    - Bucles: bucles.md
  - Práctica:
    - Intérprete Online: practice.md
```

## Personalización

### CSS Personalizado

Puedes personalizar el estilo del intérprete añadiendo CSS:

```css
/* docs/stylesheets/extra.css */
.java-interpreter {
    border: 2px solid #007bff;
    border-radius: 15px;
}

.btn-primary {
    background: linear-gradient(45deg, #007bff, #0056b3);
}
```

### JavaScript Personalizado

Añade funcionalidades adicionales:

```javascript
// docs/javascripts/extra.js
document.addEventListener('DOMContentLoaded', function() {
    // Tu código personalizado aquí
    console.log('Intérprete Java cargado');
});
```

## Integración con Temas

### Material for MkDocs

```yaml
theme:
  name: material
  custom_dir: overrides
  extra_css:
    - stylesheets/extra.css
  extra_javascript:
    - javascripts/extra.js
```

### Otros Temas

El plugin es compatible con cualquier tema de MkDocs que soporte plugins.

## Solución de Problemas

### El intérprete no aparece

1. Verifica que el plugin esté instalado:
   ```bash
   pip list | grep java-interpreter
   ```

2. Confirma la configuración en `mkdocs.yml`

3. Verifica que la página tenga el metadato correcto

### Errores de JavaScript

1. Abre la consola del navegador (F12)
2. Busca errores relacionados con el intérprete
3. Verifica que no haya conflictos con otros scripts

### Problemas de Estilo

1. Verifica que el CSS personalizado no entre en conflicto
2. Usa herramientas de desarrollador para inspeccionar elementos
3. Considera usar `!important` para estilos críticos

## Desarrollo

### Estructura del Plugin

```
mkdocs_java_interpreter/
├── __init__.py          # Plugin principal
├── setup.py            # Configuración de instalación
├── plugin_config.md    # Esta documentación
└── examples/           # Ejemplos de código
    ├── basic/
    ├── intermediate/
    └── advanced/
```

### Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature
3. Haz tus cambios
4. Añade tests si es necesario
5. Envía un pull request

## Licencia

Este plugin está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.

---

Para más información, visita el [repositorio del plugin](https://github.com/tu-usuario/mkdocs-java-interpreter).
