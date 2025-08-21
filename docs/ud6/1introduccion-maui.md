# Introducción a .NET MAUI

## ¿Qué es .NET MAUI?

.NET MAUI (Multi-platform App UI) es un framework de Microsoft que permite desarrollar aplicaciones nativas para múltiples plataformas desde una sola base de código.

### Plataformas soportadas
- **Android**
- **iOS** 
- **Windows**
- **macOS**

## Ventajas de MAUI

### 🔄 Código compartido
```csharp
// Un solo archivo XAML para todas las plataformas
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="MyApp.MainPage">
    <StackLayout>
        <Label Text="¡Hola MAUI!" />
        <Button Text="Clic aquí" />
    </StackLayout>
</ContentPage>
```

### 🚀 Rendimiento nativo
- Compilación nativa para cada plataforma
- Acceso directo a APIs nativas
- Optimización específica por plataforma

### 🛠️ Herramientas integradas
- Visual Studio 2022
- Hot Reload
- IntelliSense completo
- Debugging multiplataforma

## Estructura de un proyecto MAUI

```
MyMauiApp/
├── Platforms/
│   ├── Android/
│   ├── iOS/
│   ├── Windows/
│   └── MacCatalyst/
├── Resources/
│   ├── Images/
│   ├── Fonts/
│   └── Raw/
├── App.xaml
├── App.xaml.cs
├── MainPage.xaml
└── MainPage.xaml.cs
```

## Configuración inicial

### Requisitos previos
- Visual Studio 2022 17.3 o superior
- .NET 7.0 SDK o superior
- Workloads específicos por plataforma

### Crear un nuevo proyecto
```bash
dotnet new maui -n MiPrimeraApp
```

## Ejemplo básico

### MainPage.xaml
```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="MiPrimeraApp.MainPage">

    <ScrollView>
        <VerticalStackLayout Spacing="25" Padding="30,0" VerticalOptions="Center">

            <Label 
                Text="¡Bienvenido a .NET MAUI!"
                SemanticProperties.HeadingLevel="Level1"
                FontSize="32"
                HorizontalOptions="Center" />

            <Label 
                Text="Hello, World!"
                SemanticProperties.Description="Welcome to dot net Multi platform App U I"
                SemanticProperties.HeadingLevel="Level2"
                SemanticProperties.DescriptionLevel="Level1"
                FontSize="18"
                HorizontalOptions="Center" />

            <Button 
                x:Name="CounterBtn"
                Text="Click me"
                SemanticProperties.Hint="Counts the number of times you click"
                Clicked="OnCounterClicked"
                HorizontalOptions="Center" />

        </VerticalStackLayout>
    </ScrollView>

</ContentPage>
```

### MainPage.xaml.cs
```csharp
namespace MiPrimeraApp;

public partial class MainPage : ContentPage
{
    int count = 0;

    public MainPage()
    {
        InitializeComponent();
    }

    private void OnCounterClicked(object sender, EventArgs e)
    {
        count++;
        CounterBtn.Text = $"Clicked {count} time{(count == 1 ? "" : "s")}";

        SemanticScreenReader.Announce(CounterBtn.Text);
    }
}
```

## Conceptos clave

### 1. **XAML (eXtensible Application Markup Language)**
- Lenguaje de marcado para definir interfaces de usuario
- Separación de diseño y lógica
- Binding de datos declarativo

### 2. **Code-behind**
- Lógica de programación en C#
- Manejo de eventos
- Acceso a controles XAML

### 3. **Controles multiplataforma**
- Controles que se adaptan automáticamente
- Comportamiento nativo en cada plataforma
- Personalización específica por plataforma

## Próximos pasos

En las siguientes unidades aprenderemos:
- **Layouts y controles básicos**
- **Navegación entre páginas**
- **Binding de datos**
- **Acceso a APIs nativas**
- **Publicación de aplicaciones**

---

## Ejercicios prácticos

### Ejercicio 1: Crear tu primera app
1. Crea un nuevo proyecto MAUI
2. Modifica el texto de bienvenida
3. Añade un nuevo botón con funcionalidad personalizada

### Ejercicio 2: Explorar la estructura
1. Examina los archivos en la carpeta Platforms
2. Identifica las diferencias entre plataformas
3. Modifica un recurso específico de plataforma

### Ejercicio 3: Hot Reload
1. Ejecuta la aplicación
2. Modifica el XAML mientras se ejecuta
3. Observa los cambios en tiempo real
