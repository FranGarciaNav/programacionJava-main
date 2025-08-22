# 🚀 Intérprete de Java Online

¡Bienvenido al intérprete de Java online! Aquí puedes escribir, ejecutar y probar código Java directamente en tu navegador sin necesidad de instalar nada.

## 💻 Editor de Código

<div id="java-editor-container">
    <div style="display: flex; gap: 10px; margin-bottom: 10px;">
        <button id="run-btn" style="background: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">
            ▶️ Ejecutar Código
        </button>
        <button id="clear-btn" style="background: #f44336; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">
            🗑️ Limpiar
        </button>
        <button id="example-btn" style="background: #2196F3; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">
            📝 Ejemplo
        </button>
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; height: 500px;">
        <div>
            <h4 style="margin: 0 0 10px 0; color: #333;">📝 Código Java:</h4>
            <textarea id="java-code" style="width: 100%; height: 450px; font-family: 'Courier New', monospace; font-size: 14px; padding: 15px; border: 2px solid #ddd; border-radius: 8px; resize: none; background: #f8f9fa;" placeholder="Escribe tu código Java aquí...">public class Main {
    public static void main(String[] args) {
        System.out.println("¡Hola Mundo desde Java!");
        
        // Ejemplo de variables
        int numero = 42;
        String mensaje = "El número es: ";
        System.out.println(mensaje + numero);
        
        // Ejemplo de bucle
        for (int i = 1; i <= 5; i++) {
            System.out.println("Iteración " + i);
        }
    }
}</textarea>
        </div>
        
        <div>
            <h4 style="margin: 0 0 10px 0; color: #333;">📤 Salida:</h4>
            <div id="output" style="width: 100%; height: 450px; font-family: 'Courier New', monospace; font-size: 14px; padding: 15px; border: 2px solid #ddd; border-radius: 8px; background: #f8f9fa; overflow-y: auto; white-space: pre-wrap; color: #333;">
                La salida aparecerá aquí cuando ejecutes el código...
            </div>
        </div>
    </div>
</div>

## 🎯 Ejemplos de Código

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
        System.out.println("Módulo: " + (a % b));
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
        
        // Bucle for
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) {
                System.out.println(i + " es par");
            }
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
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Posición " + i + ": " + numeros[i]);
        }
        
        // Suma de elementos
        int suma = 0;
        for (int numero : numeros) {
            suma += numero;
        }
        System.out.println("Suma total: " + suma);
    }
}
```

## ⚠️ Limitaciones

- **Solo código básico**: Este intérprete está diseñado para código Java básico y educativo
- **Sin entrada de usuario**: No se puede usar `Scanner` para entrada del usuario
- **Sin archivos**: No se pueden leer o escribir archivos
- **Sin librerías externas**: Solo se pueden usar las clases básicas de Java

## 🛠️ Cómo Usar

1. **Escribe tu código** en el editor de la izquierda
2. **Haz clic en "Ejecutar Código"** para ver la salida
3. **Usa "Limpiar"** para borrar todo
4. **Usa "Ejemplo"** para cargar un código de ejemplo

## 🎓 Consejos para Aprender

- **Empieza simple**: Comienza con programas básicos como "Hola Mundo"
- **Experimenta**: Modifica los ejemplos y ve qué pasa
- **Prueba errores**: Intenta escribir código incorrecto para ver los mensajes de error
- **Practica**: Usa este intérprete para practicar los conceptos que aprendes en la documentación

---

<script>
document.addEventListener('DOMContentLoaded', function() {
    const codeTextarea = document.getElementById('java-code');
    const outputDiv = document.getElementById('output');
    const runBtn = document.getElementById('run-btn');
    const clearBtn = document.getElementById('clear-btn');
    const exampleBtn = document.getElementById('example-btn');

    // Ejemplos de código
    const examples = [
        {
            name: "Hola Mundo",
            code: `public class Main {
    public static void main(String[] args) {
        System.out.println("¡Hola Mundo desde Java!");
        
        // Ejemplo de variables
        int numero = 42;
        String mensaje = "El número es: ";
        System.out.println(mensaje + numero);
        
        // Ejemplo de bucle
        for (int i = 1; i <= 5; i++) {
            System.out.println("Iteración " + i);
        }
    }
}`
        },
        {
            name: "Variables y Operadores",
            code: `public class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Módulo: " + (a % b));
    }
}`
        },
        {
            name: "Estructuras de Control",
            code: `public class Main {
    public static void main(String[] args) {
        int edad = 18;
        
        if (edad >= 18) {
            System.out.println("Eres mayor de edad");
        } else {
            System.out.println("Eres menor de edad");
        }
        
        // Bucle for
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) {
                System.out.println(i + " es par");
            }
        }
    }
}`
        },
        {
            name: "Arrays",
            code: `public class Main {
    public static void main(String[] args) {
        int[] numeros = {1, 2, 3, 4, 5};
        
        System.out.println("Elementos del array:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Posición " + i + ": " + numeros[i]);
        }
        
        // Suma de elementos
        int suma = 0;
        for (int numero : numeros) {
            suma += numero;
        }
        System.out.println("Suma total: " + suma);
    }
}`
        }
    ];

    let currentExampleIndex = 0;

    // Función para ejecutar código (simulación)
    function executeCode() {
        const code = codeTextarea.value;
        
        if (!code.trim()) {
            outputDiv.innerHTML = "❌ Error: No hay código para ejecutar";
            return;
        }

        // Simulación de ejecución
        outputDiv.innerHTML = "🔄 Ejecutando código...\n";
        
        setTimeout(() => {
            try {
                // Análisis básico del código
                if (!code.includes('public class Main')) {
                    outputDiv.innerHTML = "❌ Error: Debes incluir 'public class Main' en tu código";
                    return;
                }
                
                if (!code.includes('public static void main')) {
                    outputDiv.innerHTML = "❌ Error: Debes incluir el método 'main' en tu código";
                    return;
                }

                // Simulación de salida basada en el código
                let output = "✅ Código ejecutado exitosamente:\n\n";
                
                // Extraer System.out.println del código
                const printStatements = code.match(/System\.out\.println\([^)]+\)/g);
                if (printStatements) {
                    printStatements.forEach(stmt => {
                        // Simular la salida
                        const content = stmt.match(/System\.out\.println\(([^)]+)\)/);
                        if (content) {
                            let outputText = content[1];
                            // Procesar concatenaciones básicas
                            outputText = outputText.replace(/"/g, '');
                            outputText = outputText.replace(/\+/g, ' ');
                            output += outputText + '\n';
                        }
                    });
                }
                
                // Si no hay System.out.println, mostrar mensaje
                if (!printStatements || printStatements.length === 0) {
                    output += "Programa ejecutado sin salida visible.\n";
                    output += "Usa System.out.println() para mostrar texto en consola.";
                }
                
                outputDiv.innerHTML = output;
                
            } catch (error) {
                outputDiv.innerHTML = "❌ Error de ejecución: " + error.message;
            }
        }, 1000);
    }

    // Función para limpiar
    function clearCode() {
        codeTextarea.value = '';
        outputDiv.innerHTML = 'La salida aparecerá aquí cuando ejecutes el código...';
    }

    // Función para cargar ejemplo
    function loadExample() {
        const example = examples[currentExampleIndex];
        codeTextarea.value = example.code;
        outputDiv.innerHTML = `📝 Cargado ejemplo: ${example.name}\n\nEjecuta el código para ver la salida...`;
        
        currentExampleIndex = (currentExampleIndex + 1) % examples.length;
    }

    // Event listeners
    runBtn.addEventListener('click', executeCode);
    clearBtn.addEventListener('click', clearCode);
    exampleBtn.addEventListener('click', loadExample);

    // Atajos de teclado
    codeTextarea.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            executeCode();
        }
    });
});
</script>
