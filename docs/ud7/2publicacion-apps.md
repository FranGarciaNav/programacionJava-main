# Publicación de Aplicaciones MAUI

## Preparación para publicación

### Configuración del proyecto

#### Android
```xml
<!-- Platforms/Android/AndroidManifest.xml -->
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application android:allowBackup="true" 
                 android:icon="@mipmap/appicon" 
                 android:roundIcon="@mipmap/appicon_round" 
                 android:supportsRtl="true">
    </application>
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.INTERNET" />
</manifest>
```

#### iOS
```xml
<!-- Platforms/iOS/Info.plist -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDisplayName</key>
    <string>Mi Aplicación</string>
    <key>CFBundleIdentifier</key>
    <string>com.miempresa.miapp</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>NSCameraUsageDescription</key>
    <string>Esta app necesita acceso a la cámara para tomar fotos</string>
    <key>NSLocationWhenInUseUsageDescription</key>
    <string>Esta app necesita acceso a la ubicación para mostrar tu posición</string>
</dict>
</plist>
```

## Compilación para Release

### Comandos de compilación
```bash
# Android APK
dotnet build -c Release -f net7.0-android

# Android AAB (App Bundle)
dotnet publish -c Release -f net7.0-android

# iOS
dotnet build -c Release -f net7.0-ios

# Windows
dotnet build -c Release -f net7.0-windows10.0.19041.0

# macOS
dotnet build -c Release -f net7.0-maccatalyst
```

### Optimizaciones de Release
```xml
<!-- .csproj -->
<PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Release|AnyCPU'">
    <Optimize>true</Optimize>
    <DebugType>none</DebugType>
    <DebugSymbols>false</DebugSymbols>
    <EnableCompressionInSingleFile>true</EnableCompressionInSingleFile>
    <EnableUnsafeBinaryFormatterSerialization>false</EnableUnsafeBinaryFormatterSerialization>
    <EnableUnsafeUTF7Encoding>false</EnableUnsafeUTF7Encoding>
    <EventSourceSupport>false</EventSourceSupport>
    <HttpActivityPropagationSupport>false</HttpActivityPropagationSupport>
    <InvariantGlobalization>true</InvariantGlobalization>
    <MetadataUpdaterSupport>false</MetadataUpdaterSupport>
    <UseSystemResourceKeys>true</UseSystemResourceKeys>
</PropertyGroup>
```

## Publicación en tiendas

### Google Play Store

#### Preparar APK/AAB
```bash
# Generar AAB firmado
dotnet publish -c Release -f net7.0-android -p:AndroidPackageFormat=apk

# Ubicación del archivo
# bin/Release/net7.0-android/com.miempresa.miapp-Signed.apk
```

#### Subir a Google Play Console
1. Crear cuenta de desarrollador ($25)
2. Crear nueva aplicación
3. Subir APK/AAB
4. Completar información de la app
5. Configurar precios y distribución
6. Enviar para revisión

### Apple App Store

#### Preparar IPA
```bash
# Usar Visual Studio o Xcode
# Archivo -> Publicar -> App Store
```

#### Subir a App Store Connect
1. Crear cuenta de desarrollador ($99/año)
2. Crear nueva aplicación
3. Subir IPA
4. Completar metadatos
5. Configurar precios
6. Enviar para revisión

### Microsoft Store

#### Preparar MSIX
```bash
# Generar paquete para Windows
dotnet publish -c Release -f net7.0-windows10.0.19041.0
```

#### Subir a Microsoft Partner Center
1. Crear cuenta de desarrollador ($19)
2. Crear nueva aplicación
3. Subir paquete MSIX
4. Completar información
5. Enviar para certificación

## Testing y QA

### Testing en dispositivos
```csharp
// Implementar testing automático
[Test]
public void TestMainPageNavigation()
{
    var mainPage = new MainPage();
    Assert.IsNotNull(mainPage);
}

[Test]
public void TestViewModelBinding()
{
    var viewModel = new MainViewModel();
    viewModel.Name = "Test";
    Assert.AreEqual("Test", viewModel.Name);
}
```

### Testing de UI
```csharp
// Usar Xamarin.UITest o Appium
[Test]
public void TestButtonClick()
{
    app.Tap("myButton");
    app.WaitForElement("resultLabel");
    Assert.IsTrue(app.Query("resultLabel").First().Text.Contains("Success"));
}
```

## Monitoreo y Analytics

### Implementar Analytics
```csharp
// Usar servicios como Firebase Analytics o App Center
public class AnalyticsService
{
    public void TrackEvent(string eventName, Dictionary<string, string> properties = null)
    {
        // Implementar tracking
    }

    public void TrackException(Exception exception)
    {
        // Implementar crash reporting
    }
}
```

### Monitoreo de rendimiento
```csharp
public class PerformanceService
{
    public void TrackPageLoad(string pageName)
    {
        var stopwatch = Stopwatch.StartNew();
        // Medir tiempo de carga
        stopwatch.Stop();
        // Enviar métricas
    }
}
```

## Ejercicios prácticos

### Ejercicio 1: Configurar firma
1. Genera un keystore para Android
2. Configura la firma en el proyecto
3. Compila una versión Release

### Ejercicio 2: Preparar para tienda
1. Configura los manifiestos necesarios
2. Genera los paquetes de distribución
3. Prepara los assets (iconos, screenshots)

### Ejercicio 3: Testing completo
1. Implementa tests unitarios
2. Realiza testing en dispositivos reales
3. Configura CI/CD para builds automáticos
