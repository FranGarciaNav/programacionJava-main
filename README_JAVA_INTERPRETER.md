# 🚀 Intérprete de Java Online para MkDocs

Un proyecto completo que añade un intérprete de Java online a tu documentación MkDocs, permitiendo a los usuarios ejecutar código Java directamente en el navegador.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Instalación](#-instalación)
- [Uso Rápido](#-uso-rápido)
- [Documentación](#-documentación)
- [Ejemplos](#-ejemplos)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

## ✨ Características

### 🎯 Funcionalidades Principales

- **🖥️ Editor de código integrado** - Escribe código Java con resaltado de sintaxis
- **⚡ Ejecución instantánea** - Ejecuta tu código con un solo clic
- **📤 Salida en tiempo real** - Ve los resultados inmediatamente
- **📝 Ejemplos predefinidos** - Aprende con ejemplos prácticos
- **💾 Guardado de código** - Guarda tu trabajo para más tarde
- **⌨️ Atajos de teclado** - Ctrl+Enter para ejecutar rápidamente
- **📱 Diseño responsive** - Funciona en computadoras, tablets y móviles

### 🎨 Versiones Disponibles

1. **Versión Básica** - Para principiantes y conceptos fundamentales
2. **Versión Avanzada** - Con más funcionalidades y ejemplos complejos
3. **Plugin MkDocs** - Integración completa con MkDocs

## 🚀 Instalación

### Opción 1: Páginas Estáticas (Recomendado para empezar)

1. **Clona o descarga** este repositorio
2. **Navega** a las páginas del intérprete:
   - [Intérprete Básico](docs/java-online-interpreter.md)
   - [Intérprete Avanzado](docs/java-interpreter-advanced.md)
   - [Guía Completa](docs/java-interpreter-guide.md)

### Opción 2: Plugin MkDocs (Para desarrolladores)

1. **Instala el plugin**:
   ```bash
   pip install mkdocs-java-interpreter
   ```

2. **Configura mkdocs.yml**:
   ```yaml
   plugins:
     - search
     - java-interpreter:
         enabled: true
         theme: dark
   ```

3. **Usa en tus páginas**:
   ```markdown
   ---
   plugins:
     - java-interpreter
   ---
   
   # Mi Página con Intérprete
   
   {{java-interpreter}}
   ```

## ⚡ Uso Rápido

### 1. Escribir Código

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("¡Hola Mundo desde Java!");
        
        int numero = 42;
        System.out.println("El número es: " + numero);
    }
}
```

### 2. Ejecutar

- **Botón "Ejecutar"** - Haz clic en el botón verde
- **Atajo de teclado** - Presiona `Ctrl + Enter`

### 3. Ver Resultados

La salida aparecerá en el panel derecho:
```
¡Hola Mundo desde Java!
El número es: 42
```

## 📚 Documentación

### Guías Disponibles

- **[Guía Completa](docs/java-interpreter-guide.md)** - Tutorial paso a paso
- **[Configuración del Plugin](mkdocs_java_interpreter/plugin_config.md)** - Para desarrolladores
- **[Ejemplos de Código](docs/java-interpreter-guide.md#-ejemplos-de-código)** - Código de ejemplo

### Conceptos Cubiertos

- ✅ Variables y tipos de datos
- ✅ Operadores matemáticos
- ✅ Estructuras de control (if, else, switch)
- ✅ Bucles (for, while, do-while)
- ✅ Arrays y colecciones
- ✅ Programación orientada a objetos básica
- ✅ Métodos y funciones

## 🎯 Ejemplos

### Ejemplo 1: Variables y Operadores

```java
public class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
    }
}
```

### Ejemplo 2: Estructuras de Control

```java
public class Main {
    public static void main(String[] args) {
        int edad = 18;
        
        if (edad >= 18) {
            System.out.println("Eres mayor de edad");
        } else {
            System.out.println("Eres menor de edad");
        }
        
        for (int i = 1; i <= 5; i++) {
            System.out.println("Número " + i);
        }
    }
}
```

### Ejemplo 3: Arrays

```java
public class Main {
    public static void main(String[] args) {
        int[] numeros = {1, 2, 3, 4, 5};
        
        System.out.println("Elementos del array:");
        for (int numero : numeros) {
            System.out.println(numero);
        }
    }
}
```

## 🛠️ Limitaciones

### ⚠️ Restricciones por Seguridad

- **Solo código básico** - Diseñado para aprendizaje y práctica
- **Sin entrada de usuario** - No se puede usar `Scanner` para entrada
- **Sin archivos** - No se pueden leer o escribir archivos
- **Sin librerías externas** - Solo clases básicas de Java disponibles

### 🎓 Propósito Educativo

Este intérprete está diseñado específicamente para:
- Aprender conceptos básicos de Java
- Practicar programación sin instalar software
- Experimentar con código de manera segura
- Complementar tutoriales y documentación

## 🔧 Solución de Problemas

### Errores Comunes

1. **"Debes incluir 'public class Main'"**
   - Asegúrate de que tu código tenga la estructura correcta

2. **"Debes incluir el método 'main'"**
   - Verifica que tengas el método main

3. **No aparece salida**
   - Usa `System.out.println()` para mostrar texto

### Obtener Ayuda

1. **Revisa la [Guía Completa](docs/java-interpreter-guide.md)**
2. **Verifica la sintaxis** de tu código
3. **Usa ejemplos simples** para empezar
4. **Experimenta** - La mejor manera de aprender

## 🤝 Contribuir

### Cómo Contribuir

1. **Fork** este repositorio
2. **Crea una rama** para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. **Haz tus cambios** y añade tests si es necesario
4. **Commit** tus cambios (`git commit -am 'Añadir nueva funcionalidad'`)
5. **Push** a la rama (`git push origin feature/nueva-funcionalidad`)
6. **Crea un Pull Request**

### Áreas de Mejora

- [ ] Soporte para más tipos de datos
- [ ] Mejores mensajes de error
- [ ] Más ejemplos de código
- [ ] Integración con más temas de MkDocs
- [ ] Soporte para múltiples archivos
- [ ] Ejecución de código más realista

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- **MkDocs** - Por el excelente framework de documentación
- **Material for MkDocs** - Por el tema que hace todo posible
- **Comunidad Java** - Por mantener vivo el lenguaje
- **Contribuidores** - Por hacer este proyecto mejor cada día

## 📞 Contacto

- **Issues**: [GitHub Issues](https://github.com/tu-usuario/mkdocs-java-interpreter/issues)
- **Discusiones**: [GitHub Discussions](https://github.com/tu-usuario/mkdocs-java-interpreter/discussions)
- **Email**: tu@email.com

---

**¡Disfruta aprendiendo Java con el intérprete online! 🎉**

---

<div align="center">

[![MkDocs](https://img.shields.io/badge/MkDocs-1.4.0+-blue.svg)](https://www.mkdocs.org/)
[![Python](https://img.shields.io/badge/Python-3.6+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>
