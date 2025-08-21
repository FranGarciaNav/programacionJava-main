# Layouts y Controles en MAUI

## Layouts principales

### StackLayout
Organiza elementos en una línea horizontal o vertical.

```xml
<!-- Vertical StackLayout -->
<StackLayout Orientation="Vertical" Spacing="10">
    <Label Text="Elemento 1" />
    <Label Text="Elemento 2" />
    <Label Text="Elemento 3" />
</StackLayout>

<!-- Horizontal StackLayout -->
<StackLayout Orientation="Horizontal" Spacing="5">
    <Button Text="Aceptar" />
    <Button Text="Cancelar" />
</StackLayout>
```

### Grid
Organiza elementos en filas y columnas.

```xml
<Grid RowDefinitions="Auto,Auto,*" ColumnDefinitions="*,*">
    <Label Text="Título" Grid.Row="0" Grid.ColumnSpan="2" />
    <Entry Placeholder="Usuario" Grid.Row="1" Grid.Column="0" />
    <Entry Placeholder="Contraseña" Grid.Row="1" Grid.Column="1" />
    <Button Text="Login" Grid.Row="2" Grid.ColumnSpan="2" />
</Grid>
```

### FlexLayout
Layout flexible que se adapta al contenido.

```xml
<FlexLayout Direction="Row" Wrap="Wrap" JustifyContent="SpaceEvenly">
    <Button Text="Botón 1" />
    <Button Text="Botón 2" />
    <Button Text="Botón 3" />
    <Button Text="Botón 4" />
</FlexLayout>
```

### AbsoluteLayout
Posicionamiento absoluto de elementos.

```xml
<AbsoluteLayout>
    <BoxView Color="Red" AbsoluteLayout.LayoutBounds="0,0,100,100" />
    <Label Text="Centro" AbsoluteLayout.LayoutBounds="0.5,0.5,AutoSize,AutoSize" 
           AbsoluteLayout.LayoutFlags="PositionProportional" />
</AbsoluteLayout>
```

## Controles básicos

### Label
```xml
<Label Text="Texto simple" />
<Label Text="Texto con formato" FontSize="20" TextColor="Blue" />
<Label Text="Texto multilínea" LineBreakMode="WordWrap" />
```

### Entry
```xml
<Entry Placeholder="Escribe aquí..." />
<Entry Text="{Binding UserName}" />
<Entry IsPassword="True" Placeholder="Contraseña" />
```

### Button
```xml
<Button Text="Clic aquí" Clicked="OnButtonClicked" />
<Button Text="Botón con imagen" ImageSource="icon.png" />
<Button Text="Botón deshabilitado" IsEnabled="False" />
```

### Image
```xml
<Image Source="logo.png" />
<Image Source="{Binding ImageUrl}" Aspect="AspectFit" />
<Image Source="https://example.com/image.jpg" />
```

### Switch
```xml
<Switch IsToggled="{Binding IsEnabled}" />
<Switch IsToggled="True" Toggled="OnSwitchToggled" />
```

### Slider
```xml
<Slider Value="{Binding Volume}" Maximum="100" Minimum="0" />
<Slider Value="50" ValueChanged="OnSliderChanged" />
```

### Picker
```xml
<Picker Title="Selecciona una opción">
    <Picker.Items>
        <x:String>Opción 1</x:String>
        <x:String>Opción 2</x:String>
        <x:String>Opción 3</x:String>
    </Picker.Items>
</Picker>
```

## Ejemplo completo: Formulario de registro

```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="MyApp.RegistrationPage">

    <ScrollView>
        <StackLayout Padding="20" Spacing="15">
            
            <!-- Título -->
            <Label Text="Registro de Usuario" 
                   FontSize="24" 
                   HorizontalOptions="Center" 
                   Margin="0,0,0,20" />

            <!-- Campos del formulario -->
            <Entry Placeholder="Nombre completo" 
                   x:Name="NameEntry" />

            <Entry Placeholder="Email" 
                   x:Name="EmailEntry" 
                   Keyboard="Email" />

            <Entry Placeholder="Contraseña" 
                   x:Name="PasswordEntry" 
                   IsPassword="True" />

            <Entry Placeholder="Confirmar contraseña" 
                   x:Name="ConfirmPasswordEntry" 
                   IsPassword="True" />

            <!-- Opciones -->
            <StackLayout Orientation="Horizontal" Spacing="10">
                <Label Text="Acepto los términos:" VerticalOptions="Center" />
                <Switch x:Name="TermsSwitch" />
            </StackLayout>

            <StackLayout Orientation="Horizontal" Spacing="10">
                <Label Text="Recibir notificaciones:" VerticalOptions="Center" />
                <Switch x:Name="NotificationsSwitch" IsToggled="True" />
            </StackLayout>

            <!-- Botones -->
            <Grid ColumnDefinitions="*,*" ColumnSpacing="10" Margin="0,20,0,0">
                <Button Text="Cancelar" 
                        Grid.Column="0" 
                        Clicked="OnCancelClicked" />
                <Button Text="Registrar" 
                        Grid.Column="1" 
                        Clicked="OnRegisterClicked" />
            </Grid>

        </StackLayout>
    </ScrollView>

</ContentPage>
```

### Code-behind del formulario

```csharp
namespace MyApp;

public partial class RegistrationPage : ContentPage
{
    public RegistrationPage()
    {
        InitializeComponent();
    }

    private async void OnRegisterClicked(object sender, EventArgs e)
    {
        // Validación básica
        if (string.IsNullOrEmpty(NameEntry.Text))
        {
            await DisplayAlert("Error", "El nombre es requerido", "OK");
            return;
        }

        if (string.IsNullOrEmpty(EmailEntry.Text))
        {
            await DisplayAlert("Error", "El email es requerido", "OK");
            return;
        }

        if (PasswordEntry.Text != ConfirmPasswordEntry.Text)
        {
            await DisplayAlert("Error", "Las contraseñas no coinciden", "OK");
            return;
        }

        if (!TermsSwitch.IsToggled)
        {
            await DisplayAlert("Error", "Debes aceptar los términos", "OK");
            return;
        }

        // Procesar registro
        await DisplayAlert("Éxito", "Usuario registrado correctamente", "OK");
    }

    private async void OnCancelClicked(object sender, EventArgs e)
    {
        bool answer = await DisplayAlert("Confirmar", 
                                       "¿Estás seguro de cancelar?", 
                                       "Sí", "No");
        if (answer)
        {
            await Navigation.PopAsync();
        }
    }
}
```

## Estilos y temas

### Definir estilos
```xml
<ContentPage.Resources>
    <ResourceDictionary>
        <!-- Estilo para botones -->
        <Style x:Key="PrimaryButton" TargetType="Button">
            <Setter Property="BackgroundColor" Value="#007AFF" />
            <Setter Property="TextColor" Value="White" />
            <Setter Property="CornerRadius" Value="8" />
            <Setter Property="Padding" Value="20,10" />
        </Style>

        <!-- Estilo para entradas -->
        <Style x:Key="EntryStyle" TargetType="Entry">
            <Setter Property="BackgroundColor" Value="#F2F2F7" />
            <Setter Property="PlaceholderColor" Value="#8E8E93" />
            <Setter Property="Margin" Value="0,5" />
        </Style>
    </ResourceDictionary>
</ContentPage.Resources>
```

### Aplicar estilos
```xml
<Button Text="Botón primario" Style="{StaticResource PrimaryButton}" />
<Entry Placeholder="Texto" Style="{StaticResource EntryStyle}" />
```

## Responsive Design

### Adaptación a diferentes tamaños
```xml
<Grid>
    <Grid.RowDefinitions>
        <RowDefinition Height="Auto" />
        <RowDefinition Height="*" />
    </Grid.RowDefinitions>
    
    <!-- Header que se adapta -->
    <StackLayout Grid.Row="0" 
                 Orientation="{OnPlatform Default=Horizontal, 
                                          Phone=Vertical}">
        <Label Text="Título" />
        <Button Text="Acción" />
    </StackLayout>
    
    <!-- Contenido principal -->
    <ScrollView Grid.Row="1">
        <StackLayout>
            <!-- Contenido aquí -->
        </StackLayout>
    </ScrollView>
</Grid>
```

## Ejercicios prácticos

### Ejercicio 1: Crear un formulario de contacto
1. Usa Grid para organizar los campos
2. Incluye validación de campos
3. Aplica estilos personalizados

### Ejercicio 2: Layout responsive
1. Crea una interfaz que se adapte a diferentes tamaños
2. Usa FlexLayout para elementos dinámicos
3. Implementa orientación condicional

### Ejercicio 3: Dashboard personalizado
1. Combina diferentes tipos de layouts
2. Usa controles avanzados como Picker y Slider
3. Implementa navegación entre secciones
