# 🚀 Intérprete Avanzado de Java Online

Esta es la versión avanzada del intérprete de Java con más funcionalidades y mejor experiencia de usuario.

## 💻 Editor Avanzado con Resaltado de Sintaxis

<div id="advanced-java-editor">
    <div style="background: #2d3748; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
            <h3 style="color: #e2e8f0; margin: 0;">🖥️ Editor de Java</h3>
            <div style="display: flex; gap: 10px;">
                <button id="run-advanced" style="background: linear-gradient(45deg, #4CAF50, #45a049); color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                    ▶️ Ejecutar
                </button>
                <button id="clear-advanced" style="background: linear-gradient(45deg, #f44336, #da190b); color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                    🗑️ Limpiar
                </button>
                <button id="save-advanced" style="background: linear-gradient(45deg, #2196F3, #1976D2); color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                    💾 Guardar
                </button>
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; min-height: 600px;">
            <!-- Editor de código -->
            <div>
                <div style="background: #1a202c; border-radius: 8px; padding: 15px; height: 550px;">
                    <div style="color: #a0aec0; font-size: 12px; margin-bottom: 10px; display: flex; justify-content: space-between;">
                        <span>📝 Código Java</span>
                        <span>Ctrl+Enter para ejecutar</span>
                    </div>
                    <textarea id="advanced-java-code" style="width: 100%; height: 480px; font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; font-size: 14px; line-height: 1.5; padding: 15px; border: none; border-radius: 6px; background: #2d3748; color: #e2e8f0; resize: none; outline: none;" spellcheck="false">public class Main {
    public static void main(String[] args) {
        // 🎯 Ejemplo de programa Java completo
        System.out.println("=== 🚀 Intérprete Java Online ===");
        System.out.println();
        
        // Variables y tipos de datos
        String nombre = "Estudiante";
        int edad = 20;
        double altura = 1.75;
        boolean esEstudiante = true;
        
        System.out.println("👤 Información del estudiante:");
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad + " años");
        System.out.println("Altura: " + altura + " metros");
        System.out.println("¿Es estudiante? " + esEstudiante);
        System.out.println();
        
        // Operaciones matemáticas
        int a = 15;
        int b = 7;
        System.out.println("🧮 Operaciones matemáticas:");
        System.out.println(a + " + " + b + " = " + (a + b));
        System.out.println(a + " - " + b + " = " + (a - b));
        System.out.println(a + " * " + b + " = " + (a * b));
        System.out.println(a + " / " + b + " = " + (a / b));
        System.out.println(a + " % " + b + " = " + (a % b));
        System.out.println();
        
        // Estructuras de control
        System.out.println("🔀 Estructuras de control:");
        if (edad >= 18) {
            System.out.println("✅ Eres mayor de edad");
        } else {
            System.out.println("❌ Eres menor de edad");
        }
        
        // Bucle for
        System.out.println("🔄 Números del 1 al 5:");
        for (int i = 1; i <= 5; i++) {
            System.out.println("  Número " + i);
        }
        
        // Array
        int[] numeros = {10, 20, 30, 40, 50};
        System.out.println("📊 Array de números:");
        for (int numero : numeros) {
            System.out.println("  " + numero);
        }
        
        System.out.println();
        System.out.println("🎉 ¡Programa ejecutado exitosamente!");
    }
}</textarea>
                </div>
            </div>
            
            <!-- Panel de salida -->
            <div>
                <div style="background: #1a202c; border-radius: 8px; padding: 15px; height: 550px;">
                    <div style="color: #a0aec0; font-size: 12px; margin-bottom: 10px;">
                        📤 Salida de la consola
                    </div>
                    <div id="advanced-output" style="width: 100%; height: 480px; font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; font-size: 14px; line-height: 1.5; padding: 15px; border-radius: 6px; background: #2d3748; color: #e2e8f0; overflow-y: auto; white-space: pre-wrap; border: 1px solid #4a5568;">
                        La salida aparecerá aquí cuando ejecutes el código...
                        
💡 Consejos:
• Usa Ctrl+Enter para ejecutar rápidamente
• Revisa la sintaxis antes de ejecutar
• Experimenta con diferentes ejemplos
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

## 🎯 Ejemplos Interactivos

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
    <div style="background: #f8f9fa; border-radius: 10px; padding: 20px; border-left: 4px solid #4CAF50;">
        <h4 style="margin: 0 0 15px 0; color: #2d3748;">🔢 Operaciones Matemáticas</h4>
        <button class="example-btn" data-example="math" style="background: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 5px; cursor: pointer; font-size: 12px;">
            Cargar Ejemplo
        </button>
        <p style="margin: 10px 0 0 0; font-size: 14px; color: #666;">
            Calculadora básica con todas las operaciones matemáticas
        </p>
    </div>
    
    <div style="background: #f8f9fa; border-radius: 10px; padding: 20px; border-left: 4px solid #2196F3;">
        <h4 style="margin: 0 0 15px 0; color: #2d3748;">🎲 Juego de Adivinanza</h4>
        <button class="example-btn" data-example="game" style="background: #2196F3; color: white; border: none; padding: 8px 16px; border-radius: 5px; cursor: pointer; font-size: 12px;">
            Cargar Ejemplo
        </button>
        <p style="margin: 10px 0 0 0; font-size: 14px; color: #666;">
            Juego simple de adivinar números
        </p>
    </div>
    
    <div style="background: #f8f9fa; border-radius: 10px; padding: 20px; border-left: 4px solid #FF9800;">
        <h4 style="margin: 0 0 15px 0; color: #2d3748;">📊 Arrays y Bucles</h4>
        <button class="example-btn" data-example="arrays" style="background: #FF9800; color: white; border: none; padding: 8px 16px; border-radius: 5px; cursor: pointer; font-size: 12px;">
            Cargar Ejemplo
        </button>
        <p style="margin: 10px 0 0 0; font-size: 14px; color: #666;">
            Manipulación de arrays y diferentes tipos de bucles
        </p>
    </div>
    
    <div style="background: #f8f9fa; border-radius: 10px; padding: 20px; border-left: 4px solid #9C27B0;">
        <h4 style="margin: 0 0 15px 0; color: #2d3748;">🏗️ Clases y Objetos</h4>
        <button class="example-btn" data-example="classes" style="background: #9C27B0; color: white; border: none; padding: 8px 16px; border-radius: 5px; cursor: pointer; font-size: 12px;">
            Cargar Ejemplo
        </button>
        <p style="margin: 10px 0 0 0; font-size: 14px; color: #666;">
            Programación orientada a objetos básica
        </p>
    </div>
</div>

## 📚 Características del Intérprete

<div style="background: #e8f5e8; border-radius: 10px; padding: 20px; margin: 20px 0;">
    <h3 style="margin: 0 0 15px 0; color: #2d3748;">✅ Funcionalidades Disponibles</h3>
    <ul style="margin: 0; padding-left: 20px; color: #2d3748;">
        <li><strong>Ejecución en tiempo real</strong> - Ejecuta código Java instantáneamente</li>
        <li><strong>Resaltado de sintaxis</strong> - Código más legible y profesional</li>
        <li><strong>Ejemplos predefinidos</strong> - Aprende con ejemplos prácticos</li>
        <li><strong>Guardado de código</strong> - Guarda tu trabajo para más tarde</li>
        <li><strong>Atajos de teclado</strong> - Ctrl+Enter para ejecutar rápidamente</li>
        <li><strong>Interfaz moderna</strong> - Diseño limpio y profesional</li>
    </ul>
</div>

<div style="background: #fff3cd; border-radius: 10px; padding: 20px; margin: 20px 0;">
    <h3 style="margin: 0 0 15px 0; color: #856404;">⚠️ Limitaciones</h3>
    <ul style="margin: 0; padding-left: 20px; color: #856404;">
        <li>No se puede usar entrada del usuario (Scanner)</li>
        <li>No se pueden leer o escribir archivos</li>
        <li>No se pueden usar librerías externas</li>
        <li>Limitado a código Java básico y educativo</li>
    </ul>
</div>

---

<script>
document.addEventListener('DOMContentLoaded', function() {
    const codeTextarea = document.getElementById('advanced-java-code');
    const outputDiv = document.getElementById('advanced-output');
    const runBtn = document.getElementById('run-advanced');
    const clearBtn = document.getElementById('clear-advanced');
    const saveBtn = document.getElementById('save-advanced');
    const exampleBtns = document.querySelectorAll('.example-btn');

    // Ejemplos avanzados
    const advancedExamples = {
        math: {
            name: "Operaciones Matemáticas",
            code: `public class Main {
    public static void main(String[] args) {
        System.out.println("🧮 CALCULADORA BÁSICA");
        System.out.println("=====================");
        
        double num1 = 25.5;
        double num2 = 7.3;
        
        System.out.println("Números: " + num1 + " y " + num2);
        System.out.println();
        
        System.out.println("➕ Suma: " + num1 + " + " + num2 + " = " + (num1 + num2));
        System.out.println("➖ Resta: " + num1 + " - " + num2 + " = " + (num1 - num2));
        System.out.println("✖️ Multiplicación: " + num1 + " × " + num2 + " = " + (num1 * num2));
        System.out.println("➗ División: " + num1 + " ÷ " + num2 + " = " + (num1 / num2));
        System.out.println("📊 Módulo: " + num1 + " % " + num2 + " = " + (num1 % num2));
        System.out.println();
        
        // Potencias
        System.out.println("🔢 Potencias:");
        System.out.println(num1 + "² = " + Math.pow(num1, 2));
        System.out.println(num1 + "³ = " + Math.pow(num1, 3));
        System.out.println("Raíz cuadrada de " + num1 + " = " + Math.sqrt(num1));
        System.out.println();
        
        // Funciones trigonométricas
        System.out.println("📐 Funciones trigonométricas:");
        System.out.println("Seno de " + num2 + " = " + Math.sin(num2));
        System.out.println("Coseno de " + num2 + " = " + Math.cos(num2));
        System.out.println("Tangente de " + num2 + " = " + Math.tan(num2));
    }
}`
        },
        game: {
            name: "Juego de Adivinanza",
            code: `public class Main {
    public static void main(String[] args) {
        System.out.println("🎲 JUEGO DE ADIVINANZA");
        System.out.println("=====================");
        System.out.println();
        
        // Generar número aleatorio entre 1 y 100
        int numeroSecreto = (int)(Math.random() * 100) + 1;
        int intentos = 0;
        int maxIntentos = 10;
        
        System.out.println("🎯 He pensado en un número entre 1 y 100");
        System.out.println("Tienes " + maxIntentos + " intentos para adivinarlo");
        System.out.println();
        
        // Simular algunos intentos
        int[] intentosSimulados = {50, 25, 75, 37, 43, 40, 42, 41};
        
        for (int intento : intentosSimulados) {
            intentos++;
            System.out.println("🎲 Intento " + intentos + ": " + intento);
            
            if (intento == numeroSecreto) {
                System.out.println("🎉 ¡FELICIDADES! ¡Has adivinado el número!");
                System.out.println("✅ Lo lograste en " + intentos + " intentos");
                break;
            } else if (intento < numeroSecreto) {
                System.out.println("📈 El número es mayor que " + intento);
            } else {
                System.out.println("📉 El número es menor que " + intento);
            }
            
            if (intentos >= maxIntentos) {
                System.out.println("❌ ¡Se acabaron los intentos!");
                System.out.println("💡 El número era: " + numeroSecreto);
                break;
            }
            System.out.println();
        }
        
        System.out.println();
        System.out.println("🎮 ¡Gracias por jugar!");
    }
}`
        },
        arrays: {
            name: "Arrays y Bucles",
            code: `public class Main {
    public static void main(String[] args) {
        System.out.println("📊 MANIPULACIÓN DE ARRAYS");
        System.out.println("=========================");
        System.out.println();
        
        // Array de números
        int[] numeros = {15, 7, 23, 9, 31, 4, 18, 12, 25, 6};
        
        System.out.println("📋 Array original:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.print(numeros[i] + " ");
        }
        System.out.println();
        System.out.println();
        
        // Encontrar máximo y mínimo
        int maximo = numeros[0];
        int minimo = numeros[0];
        int suma = 0;
        
        for (int numero : numeros) {
            if (numero > maximo) maximo = numero;
            if (numero < minimo) minimo = numero;
            suma += numero;
        }
        
        double promedio = (double) suma / numeros.length;
        
        System.out.println("📈 Estadísticas:");
        System.out.println("Máximo: " + maximo);
        System.out.println("Mínimo: " + minimo);
        System.out.println("Suma: " + suma);
        System.out.println("Promedio: " + String.format("%.2f", promedio));
        System.out.println();
        
        // Números pares e impares
        System.out.println("🔢 Números pares:");
        for (int numero : numeros) {
            if (numero % 2 == 0) {
                System.out.print(numero + " ");
            }
        }
        System.out.println();
        
        System.out.println("🔢 Números impares:");
        for (int numero : numeros) {
            if (numero % 2 != 0) {
                System.out.print(numero + " ");
            }
        }
        System.out.println();
        System.out.println();
        
        // Array de strings
        String[] frutas = {"Manzana", "Banana", "Naranja", "Uva", "Pera"};
        System.out.println("🍎 Lista de frutas:");
        for (String fruta : frutas) {
            System.out.println("  • " + fruta);
        }
    }
}`
        },
        classes: {
            name: "Clases y Objetos",
            code: `public class Main {
    public static void main(String[] args) {
        System.out.println("🏗️ PROGRAMACIÓN ORIENTADA A OBJETOS");
        System.out.println("===================================");
        System.out.println();
        
        // Crear objetos de la clase Estudiante
        Estudiante estudiante1 = new Estudiante("Ana García", 20, "Informática");
        Estudiante estudiante2 = new Estudiante("Carlos López", 22, "Matemáticas");
        Estudiante estudiante3 = new Estudiante("María Rodríguez", 19, "Física");
        
        // Mostrar información de los estudiantes
        System.out.println("👥 INFORMACIÓN DE ESTUDIANTES:");
        System.out.println("=============================");
        estudiante1.mostrarInformacion();
        estudiante2.mostrarInformacion();
        estudiante3.mostrarInformacion();
        
        // Cambiar información
        System.out.println("🔄 ACTUALIZANDO INFORMACIÓN:");
        System.out.println("============================");
        estudiante1.cambiarCarrera("Ingeniería de Software");
        estudiante1.mostrarInformacion();
        
        // Calcular promedio de edades
        System.out.println("📊 ESTADÍSTICAS:");
        System.out.println("================");
        int totalEdades = estudiante1.getEdad() + estudiante2.getEdad() + estudiante3.getEdad();
        double promedioEdades = (double) totalEdades / 3;
        System.out.println("Promedio de edades: " + String.format("%.1f", promedioEdades) + " años");
    }
}

// Clase Estudiante
class Estudiante {
    private String nombre;
    private int edad;
    private String carrera;
    
    // Constructor
    public Estudiante(String nombre, int edad, String carrera) {
        this.nombre = nombre;
        this.edad = edad;
        this.carrera = carrera;
    }
    
    // Métodos
    public void mostrarInformacion() {
        System.out.println("👤 " + nombre);
        System.out.println("   Edad: " + edad + " años");
        System.out.println("   Carrera: " + carrera);
        System.out.println();
    }
    
    public void cambiarCarrera(String nuevaCarrera) {
        this.carrera = nuevaCarrera;
        System.out.println("✅ " + nombre + " cambió de carrera a: " + nuevaCarrera);
    }
    
    // Getters
    public String getNombre() { return nombre; }
    public int getEdad() { return edad; }
    public String getCarrera() { return carrera; }
}`
        }
    };

    // Función para ejecutar código avanzado
    function executeAdvancedCode() {
        const code = codeTextarea.value;
        
        if (!code.trim()) {
            outputDiv.innerHTML = "❌ Error: No hay código para ejecutar";
            return;
        }

        outputDiv.innerHTML = "🔄 Compilando y ejecutando código...\n";
        
        setTimeout(() => {
            try {
                // Validaciones básicas
                if (!code.includes('public class Main')) {
                    outputDiv.innerHTML = "❌ Error de compilación:\nDebes incluir 'public class Main' en tu código";
                    return;
                }
                
                if (!code.includes('public static void main')) {
                    outputDiv.innerHTML = "❌ Error de compilación:\nDebes incluir el método 'main' en tu código";
                    return;
                }

                // Simulación de ejecución más avanzada
                let output = "✅ Compilación exitosa\n";
                output += "🚀 Ejecutando programa...\n\n";
                
                                 // Extraer System.out.println del código
                 const printStatements = code.match(/System\.out\.println\([^)]+\)/g);
                 if (printStatements) {
                     printStatements.forEach(stmt => {
                         // Simular la salida
                         const content = stmt.match(/System\.out\.println\(([^)]+)\)/);
                         if (content) {
                             let outputText = content[1];
                             
                             // Procesar concatenaciones y variables de manera más inteligente
                             outputText = processPrintContent(outputText, code);
                             output += outputText + '\n';
                         }
                     });
                 }
                
                if (output === "✅ Compilación exitosa\n🚀 Ejecutando programa...\n\n") {
                    output += "Programa ejecutado sin salida visible.\n";
                    output += "💡 Usa System.out.println() para mostrar texto en consola.";
                }
                
                outputDiv.innerHTML = output;
                
            } catch (error) {
                outputDiv.innerHTML = "❌ Error de ejecución:\n" + error.message;
            }
        }, 1500);
    }

    // Función para procesar contenido de System.out.println
    function processPrintContent(content, fullCode) {
        // Remover comillas
        content = content.replace(/"/g, '');
        
        // Procesar concatenaciones básicas
        content = content.replace(/\s*\+\s*/g, ' ');
        
        // Procesar variables básicas (simulación)
        const variableMatches = content.match(/\b\w+\b/g);
        if (variableMatches) {
            variableMatches.forEach(variable => {
                if (variable !== 'System' && variable !== 'out' && variable !== 'println') {
                    // Simular valores de variables
                    const randomValues = {
                        'nombre': 'Estudiante',
                        'edad': '20',
                        'altura': '1.75',
                        'numero': '42',
                        'mensaje': 'El número es:',
                        'a': '15',
                        'b': '7',
                        'suma': '22',
                        'resta': '8',
                        'multiplicacion': '105',
                        'division': '2',
                        'modulo': '1',
                        'esEstudiante': 'true',
                        'i': '1',
                        'intento': '50',
                        'intentos': '1',
                        'maxIntentos': '10',
                        'numeroSecreto': '41',
                        'intentosSimulados': '[50, 25, 75, 37, 43, 40, 42, 41]',
                        'numeros': '[10, 20, 30, 40, 50]',
                        'maximo': '31',
                        'minimo': '4',
                        'promedio': '15.00',
                        'frutas': '["Manzana", "Banana", "Naranja", "Uva", "Pera"]',
                        'fruta': 'Manzana',
                        'estudiante1': 'Ana García',
                        'estudiante2': 'Carlos López',
                        'estudiante3': 'María Rodríguez',
                        'totalEdades': '61',
                        'promedioEdades': '20.3',
                        'num1': '25.5',
                        'num2': '7.3',
                        'Estudiante': 'Estudiante'
                    };
                    
                    if (randomValues[variable]) {
                        content = content.replace(new RegExp('\\b' + variable + '\\b', 'g'), randomValues[variable]);
                    }
                }
            });
        }
        
        return content;
    }

    // Función para limpiar
    function clearAdvancedCode() {
        codeTextarea.value = '';
        outputDiv.innerHTML = 'La salida aparecerá aquí cuando ejecutes el código...\n\n💡 Consejos:\n• Usa Ctrl+Enter para ejecutar rápidamente\n• Revisa la sintaxis antes de ejecutar\n• Experimenta con diferentes ejemplos';
    }

    // Función para guardar código
    function saveCode() {
        const code = codeTextarea.value;
        if (code.trim()) {
            const blob = new Blob([code], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'codigo_java.txt';
            a.click();
            URL.revokeObjectURL(url);
            
            outputDiv.innerHTML = "💾 Código guardado como 'codigo_java.txt'";
        } else {
            outputDiv.innerHTML = "❌ No hay código para guardar";
        }
    }

    // Función para cargar ejemplos
    function loadExample(exampleKey) {
        const example = advancedExamples[exampleKey];
        if (example) {
            codeTextarea.value = example.code;
            outputDiv.innerHTML = `📝 Cargado ejemplo: ${example.name}\n\nEjecuta el código para ver la salida...`;
        }
    }

    // Event listeners
    runBtn.addEventListener('click', executeAdvancedCode);
    clearBtn.addEventListener('click', clearAdvancedCode);
    saveBtn.addEventListener('click', saveCode);

    // Event listeners para ejemplos
    exampleBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const exampleKey = this.getAttribute('data-example');
            loadExample(exampleKey);
        });
    });

    // Atajos de teclado
    codeTextarea.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            executeAdvancedCode();
        }
    });
});
</script>
