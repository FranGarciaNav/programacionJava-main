"""
MkDocs Java Interpreter Plugin

Un plugin para MkDocs que añade un intérprete de Java online a la documentación.
"""

import os
import re
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options


class JavaInterpreterPlugin(BasePlugin):
    """Plugin para añadir un intérprete de Java online a MkDocs."""
    
    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
        ('theme', config_options.Type(str, default='dark')),
        ('examples_path', config_options.Type(str, default='examples/')),
    )
    
    def on_page_content(self, html, page, config, files):
        """Procesa el contenido de la página para añadir el intérprete."""
        if 'java-interpreter' in page.meta.get('plugins', []):
            html = self._inject_interpreter(html, page)
        return html
    
    def on_page_markdown(self, markdown, page, config, files):
        """Procesa el markdown para añadir bloques de código ejecutables."""
        if '{{java-interpreter}}' in markdown:
            markdown = self._replace_interpreter_placeholder(markdown, page)
        return markdown
    
    def _inject_interpreter(self, html, page):
        """Inyecta el intérprete en el HTML de la página."""
        interpreter_html = self._get_interpreter_html()
        
        # Buscar el placeholder y reemplazarlo
        if '{{java-interpreter}}' in html:
            html = html.replace('{{java-interpreter}}', interpreter_html)
        
        return html
    
    def _replace_interpreter_placeholder(self, markdown, page):
        """Reemplaza el placeholder del intérprete en el markdown."""
        interpreter_markdown = self._get_interpreter_markdown()
        return markdown.replace('{{java-interpreter}}', interpreter_markdown)
    
    def _get_interpreter_html(self):
        """Genera el HTML del intérprete."""
        return '''
<div id="java-interpreter-container" class="java-interpreter">
    <div class="interpreter-header">
        <h3>🚀 Intérprete de Java Online</h3>
        <div class="interpreter-controls">
            <button id="run-java" class="btn btn-primary">▶️ Ejecutar</button>
            <button id="clear-java" class="btn btn-secondary">🗑️ Limpiar</button>
            <button id="example-java" class="btn btn-info">📝 Ejemplo</button>
        </div>
    </div>
    
    <div class="interpreter-content">
        <div class="editor-panel">
            <h4>📝 Código Java:</h4>
            <textarea id="java-code-editor" placeholder="Escribe tu código Java aquí...">public class Main {
    public static void main(String[] args) {
        System.out.println("¡Hola Mundo desde Java!");
    }
}</textarea>
        </div>
        
        <div class="output-panel">
            <h4>📤 Salida:</h4>
            <div id="java-output" class="output-display">
                La salida aparecerá aquí cuando ejecutes el código...
            </div>
        </div>
    </div>
</div>

<style>
.java-interpreter {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 20px;
    margin: 20px 0;
    border: 1px solid #dee2e6;
}

.interpreter-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 2px solid #e9ecef;
}

.interpreter-header h3 {
    margin: 0;
    color: #495057;
}

.interpreter-controls {
    display: flex;
    gap: 10px;
}

.btn {
    padding: 8px 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    transition: all 0.3s ease;
}

.btn-primary {
    background: #007bff;
    color: white;
}

.btn-primary:hover {
    background: #0056b3;
}

.btn-secondary {
    background: #6c757d;
    color: white;
}

.btn-secondary:hover {
    background: #545b62;
}

.btn-info {
    background: #17a2b8;
    color: white;
}

.btn-info:hover {
    background: #117a8b;
}

.interpreter-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    min-height: 400px;
}

.editor-panel, .output-panel {
    display: flex;
    flex-direction: column;
}

.editor-panel h4, .output-panel h4 {
    margin: 0 0 10px 0;
    color: #495057;
    font-size: 16px;
}

#java-code-editor {
    flex: 1;
    font-family: 'Courier New', monospace;
    font-size: 14px;
    padding: 15px;
    border: 2px solid #dee2e6;
    border-radius: 8px;
    resize: none;
    background: #ffffff;
    line-height: 1.5;
}

#java-code-editor:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.output-display {
    flex: 1;
    font-family: 'Courier New', monospace;
    font-size: 14px;
    padding: 15px;
    border: 2px solid #dee2e6;
    border-radius: 8px;
    background: #ffffff;
    overflow-y: auto;
    white-space: pre-wrap;
    line-height: 1.5;
    color: #495057;
}

@media (max-width: 768px) {
    .interpreter-content {
        grid-template-columns: 1fr;
    }
    
    .interpreter-header {
        flex-direction: column;
        gap: 15px;
        align-items: stretch;
    }
    
    .interpreter-controls {
        justify-content: center;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const editor = document.getElementById('java-code-editor');
    const output = document.getElementById('java-output');
    const runBtn = document.getElementById('run-java');
    const clearBtn = document.getElementById('clear-java');
    const exampleBtn = document.getElementById('example-java');
    
    if (!editor || !output) return;
    
    const examples = [
        {
            name: "Hola Mundo",
            code: `public class Main {
    public static void main(String[] args) {
        System.out.println("¡Hola Mundo desde Java!");
        System.out.println("Bienvenido al intérprete online");
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
    }
}`
        },
        {
            name: "Bucles",
            code: `public class Main {
    public static void main(String[] args) {
        System.out.println("Números del 1 al 10:");
        for (int i = 1; i <= 10; i++) {
            System.out.println("Número " + i);
        }
    }
}`
        }
    ];
    
    let currentExample = 0;
    
    function executeCode() {
        const code = editor.value;
        
        if (!code.trim()) {
            output.textContent = "❌ Error: No hay código para ejecutar";
            return;
        }
        
        output.textContent = "🔄 Ejecutando código...";
        
        setTimeout(() => {
            try {
                if (!code.includes('public class Main')) {
                    output.textContent = "❌ Error: Debes incluir 'public class Main' en tu código";
                    return;
                }
                
                if (!code.includes('public static void main')) {
                    output.textContent = "❌ Error: Debes incluir el método 'main' en tu código";
                    return;
                }
                
                let result = "✅ Código ejecutado exitosamente:\\n\\n";
                
                const printStatements = code.match(/System\\.out\\.println\\([^)]+\\)/g);
                if (printStatements) {
                    printStatements.forEach(stmt => {
                        const content = stmt.match(/System\\.out\\.println\\(([^)]+)\\)/);
                        if (content) {
                            let text = content[1].replace(/"/g, '').replace(/\\+/g, ' ');
                            result += text + "\\n";
                        }
                    });
                }
                
                if (result === "✅ Código ejecutado exitosamente:\\n\\n") {
                    result += "Programa ejecutado sin salida visible.\\n";
                    result += "Usa System.out.println() para mostrar texto en consola.";
                }
                
                output.textContent = result;
                
            } catch (error) {
                output.textContent = "❌ Error de ejecución: " + error.message;
            }
        }, 1000);
    }
    
    function clearCode() {
        editor.value = '';
        output.textContent = 'La salida aparecerá aquí cuando ejecutes el código...';
    }
    
    function loadExample() {
        const example = examples[currentExample];
        editor.value = example.code;
        output.textContent = `📝 Cargado ejemplo: ${example.name}\\n\\nEjecuta el código para ver la salida...`;
        currentExample = (currentExample + 1) % examples.length;
    }
    
    runBtn.addEventListener('click', executeCode);
    clearBtn.addEventListener('click', clearCode);
    exampleBtn.addEventListener('click', loadExample);
    
    editor.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            executeCode();
        }
    });
});
</script>
        '''
    
    def _get_interpreter_markdown(self):
        """Genera el markdown del intérprete."""
        return '''
## 🚀 Intérprete de Java Online

{{java-interpreter}}

### 💡 Cómo usar:

1. **Escribe tu código** en el editor de la izquierda
2. **Haz clic en "Ejecutar"** para ver la salida
3. **Usa "Limpiar"** para borrar todo
4. **Usa "Ejemplo"** para cargar un código de ejemplo

### ⚠️ Limitaciones:

- Solo código Java básico y educativo
- No se puede usar entrada del usuario (Scanner)
- No se pueden leer o escribir archivos
- No se pueden usar librerías externas
        '''
