# Navegación y Binding de Datos en MAUI

## Navegación entre páginas

### Tipos de navegación

#### 1. **Navegación Push/Pop**
```csharp
// Navegar a una nueva página
await Navigation.PushAsync(new DetailPage());

// Regresar a la página anterior
await Navigation.PopAsync();

// Regresar a la página raíz
await Navigation.PopToRootAsync();
```

#### 2. **Navegación Modal**
```csharp
// Mostrar página como modal
await Navigation.PushModalAsync(new ModalPage());

// Cerrar modal
await Navigation.PopModalAsync();
```

### Ejemplo de navegación

#### MainPage.xaml
```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="MyApp.MainPage">

    <StackLayout Padding="20" Spacing="15">
        <Label Text="Página Principal" 
               FontSize="24" 
               HorizontalOptions="Center" />

        <Button Text="Ir a Detalles" 
                Clicked="OnNavigateToDetails" />

        <Button Text="Mostrar Modal" 
                Clicked="OnShowModal" />

        <Button Text="Ir a Lista" 
                Clicked="OnNavigateToList" />
    </StackLayout>

</ContentPage>
```

#### MainPage.xaml.cs
```csharp
namespace MyApp;

public partial class MainPage : ContentPage
{
    public MainPage()
    {
        InitializeComponent();
    }

    private async void OnNavigateToDetails(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new DetailPage());
    }

    private async void OnShowModal(object sender, EventArgs e)
    {
        await Navigation.PushModalAsync(new ModalPage());
    }

    private async void OnNavigateToList(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new ListPage());
    }
}
```

## Binding de datos

### Conceptos básicos

#### 1. **Data Binding**
```xml
<!-- Binding simple -->
<Label Text="{Binding Name}" />

<!-- Binding con formato -->
<Label Text="{Binding Price, StringFormat='Precio: {0:C}'}" />

<!-- Binding con conversor -->
<Label Text="{Binding IsActive, Converter={StaticResource BoolToTextConverter}}" />
```

#### 2. **ViewModel básico**
```csharp
public class MainViewModel : INotifyPropertyChanged
{
    private string _name;
    private double _price;
    private bool _isActive;

    public string Name
    {
        get => _name;
        set
        {
            _name = value;
            OnPropertyChanged();
        }
    }

    public double Price
    {
        get => _price;
        set
        {
            _price = value;
            OnPropertyChanged();
        }
    }

    public bool IsActive
    {
        get => _isActive;
        set
        {
            _isActive = value;
            OnPropertyChanged();
        }
    }

    public event PropertyChangedEventHandler PropertyChanged;

    protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

### Ejemplo completo con MVVM

#### ProductViewModel.cs
```csharp
using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Input;

namespace MyApp.ViewModels;

public class ProductViewModel : INotifyPropertyChanged
{
    private string _name;
    private string _description;
    private double _price;
    private bool _isAvailable;

    public string Name
    {
        get => _name;
        set
        {
            _name = value;
            OnPropertyChanged();
        }
    }

    public string Description
    {
        get => _description;
        set
        {
            _description = value;
            OnPropertyChanged();
        }
    }

    public double Price
    {
        get => _price;
        set
        {
            _price = value;
            OnPropertyChanged();
        }
    }

    public bool IsAvailable
    {
        get => _isAvailable;
        set
        {
            _isAvailable = value;
            OnPropertyChanged();
        }
    }

    public ICommand SaveCommand { get; }
    public ICommand ResetCommand { get; }

    public ProductViewModel()
    {
        SaveCommand = new Command(OnSave);
        ResetCommand = new Command(OnReset);
        
        // Datos de ejemplo
        Name = "Producto Ejemplo";
        Description = "Descripción del producto";
        Price = 99.99;
        IsAvailable = true;
    }

    private async void OnSave()
    {
        // Lógica para guardar
        await Application.Current.MainPage.DisplayAlert("Éxito", "Producto guardado", "OK");
    }

    private void OnReset()
    {
        Name = "";
        Description = "";
        Price = 0;
        IsAvailable = false;
    }

    public event PropertyChangedEventHandler PropertyChanged;

    protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

#### ProductPage.xaml
```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="MyApp.ProductPage"
             Title="Producto">

    <ScrollView>
        <StackLayout Padding="20" Spacing="15">
            
            <Label Text="Información del Producto" 
                   FontSize="24" 
                   HorizontalOptions="Center" 
                   Margin="0,0,0,20" />

            <!-- Campos del formulario -->
            <Label Text="Nombre:" />
            <Entry Text="{Binding Name}" 
                   Placeholder="Ingrese el nombre" />

            <Label Text="Descripción:" />
            <Editor Text="{Binding Description}" 
                    Placeholder="Ingrese la descripción"
                    HeightRequest="100" />

            <Label Text="Precio:" />
            <Entry Text="{Binding Price}" 
                   Placeholder="0.00"
                   Keyboard="Numeric" />

            <StackLayout Orientation="Horizontal" Spacing="10">
                <Label Text="Disponible:" VerticalOptions="Center" />
                <Switch IsToggled="{Binding IsAvailable}" />
            </StackLayout>

            <!-- Información mostrada -->
            <Frame Padding="15" Margin="0,20,0,0">
                <StackLayout>
                    <Label Text="Vista previa:" FontAttributes="Bold" />
                    <Label Text="{Binding Name, StringFormat='Nombre: {0}'}" />
                    <Label Text="{Binding Description, StringFormat='Descripción: {0}'}" />
                    <Label Text="{Binding Price, StringFormat='Precio: {0:C}'}" />
                    <Label Text="{Binding IsAvailable, StringFormat='Disponible: {0}'}" />
                </StackLayout>
            </Frame>

            <!-- Botones -->
            <Grid ColumnDefinitions="*,*" ColumnSpacing="10" Margin="0,20,0,0">
                <Button Text="Guardar" 
                        Grid.Column="0" 
                        Command="{Binding SaveCommand}" />
                <Button Text="Resetear" 
                        Grid.Column="1" 
                        Command="{Binding ResetCommand}" />
            </Grid>

        </StackLayout>
    </ScrollView>

</ContentPage>
```

#### ProductPage.xaml.cs
```csharp
namespace MyApp;

public partial class ProductPage : ContentPage
{
    public ProductPage()
    {
        InitializeComponent();
        BindingContext = new ProductViewModel();
    }
}
```

## Colecciones y ListView

### ObservableCollection
```csharp
public class ProductListViewModel : INotifyPropertyChanged
{
    public ObservableCollection<Product> Products { get; set; }

    public ProductListViewModel()
    {
        Products = new ObservableCollection<Product>
        {
            new Product { Name = "Producto 1", Price = 10.99 },
            new Product { Name = "Producto 2", Price = 20.50 },
            new Product { Name = "Producto 3", Price = 15.75 }
        };
    }

    public event PropertyChangedEventHandler PropertyChanged;

    protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}

public class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
}
```

### ListView con Binding
```xml
<ListView ItemsSource="{Binding Products}">
    <ListView.ItemTemplate>
        <DataTemplate>
            <ViewCell>
                <Grid Padding="10">
                    <Grid.ColumnDefinitions>
                        <ColumnDefinition Width="*" />
                        <ColumnDefinition Width="Auto" />
                    </Grid.ColumnDefinitions>
                    
                    <StackLayout Grid.Column="0">
                        <Label Text="{Binding Name}" FontAttributes="Bold" />
                        <Label Text="{Binding Price, StringFormat='Precio: {0:C}'}" 
                               TextColor="Gray" />
                    </StackLayout>
                    
                    <Button Grid.Column="1" 
                            Text="Ver" 
                            Command="{Binding Source={RelativeSource AncestorType={x:Type local:ProductListViewModel}}, Path=ViewProductCommand}"
                            CommandParameter="{Binding .}" />
                </Grid>
            </ViewCell>
        </DataTemplate>
    </ListView.ItemTemplate>
</ListView>
```

## Comandos (Commands)

### ICommand básico
```csharp
public class RelayCommand : ICommand
{
    private readonly Action<object> _execute;
    private readonly Func<object, bool> _canExecute;

    public RelayCommand(Action<object> execute, Func<object, bool> canExecute = null)
    {
        _execute = execute ?? throw new ArgumentNullException(nameof(execute));
        _canExecute = canExecute;
    }

    public event EventHandler CanExecuteChanged
    {
        add { CommandManager.RequerySuggested += value; }
        remove { CommandManager.RequerySuggested -= value; }
    }

    public bool CanExecute(object parameter) => _canExecute?.Invoke(parameter) ?? true;

    public void Execute(object parameter) => _execute(parameter);
}
```

### Uso de comandos
```csharp
public ICommand AddProductCommand { get; }
public ICommand DeleteProductCommand { get; }

public ProductListViewModel()
{
    AddProductCommand = new RelayCommand(OnAddProduct);
    DeleteProductCommand = new RelayCommand(OnDeleteProduct, CanDeleteProduct);
}

private void OnAddProduct(object parameter)
{
    Products.Add(new Product { Name = "Nuevo Producto", Price = 0 });
}

private void OnDeleteProduct(object parameter)
{
    if (parameter is Product product)
    {
        Products.Remove(product);
    }
}

private bool CanDeleteProduct(object parameter)
{
    return parameter is Product && Products.Count > 1;
}
```

## Ejercicios prácticos

### Ejercicio 1: Navegación básica
1. Crea tres páginas: Main, Detail y Settings
2. Implementa navegación entre ellas
3. Pasa datos entre páginas

### Ejercicio 2: MVVM con formulario
1. Crea un ViewModel para un formulario de usuario
2. Implementa validación de datos
3. Usa comandos para las acciones

### Ejercicio 3: Lista con datos
1. Crea una ObservableCollection de elementos
2. Implementa un ListView con DataTemplate
3. Añade funcionalidad de agregar/eliminar elementos
