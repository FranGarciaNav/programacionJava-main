# APIs Nativas en MAUI

## Acceso a funcionalidades nativas

### Geolocalización
```csharp
public class LocationService
{
    public async Task<Location> GetCurrentLocationAsync()
    {
        try
        {
            var location = await Geolocation.GetLocationAsync();
            return location;
        }
        catch (FeatureNotEnabledException)
        {
            // GPS no está habilitado
            return null;
        }
        catch (PermissionException)
        {
            // Permisos no concedidos
            return null;
        }
    }

    public async Task<Location> GetLastKnownLocationAsync()
    {
        return await Geolocation.GetLastKnownLocationAsync();
    }
}
```

### Cámara y Galería
```csharp
public class MediaService
{
    public async Task<FileResult> TakePhotoAsync()
    {
        if (MediaPicker.IsCaptureSupported)
        {
            var photo = await MediaPicker.CapturePhotoAsync();
            return photo;
        }
        return null;
    }

    public async Task<FileResult> PickPhotoAsync()
    {
        var photo = await MediaPicker.PickPhotoAsync();
        return photo;
    }
}
```

### Almacenamiento local
```csharp
public class StorageService
{
    public async Task SaveTextAsync(string fileName, string text)
    {
        var localPath = Path.Combine(FileSystem.AppDataDirectory, fileName);
        await File.WriteAllTextAsync(localPath, text);
    }

    public async Task<string> LoadTextAsync(string fileName)
    {
        var localPath = Path.Combine(FileSystem.AppDataDirectory, fileName);
        if (File.Exists(localPath))
        {
            return await File.ReadAllTextAsync(localPath);
        }
        return null;
    }
}
```

### Conectividad
```csharp
public class NetworkService
{
    public bool IsConnected => Connectivity.NetworkAccess == NetworkAccess.Internet;

    public IEnumerable<ConnectionProfile> GetConnectionProfiles()
    {
        return Connectivity.ConnectionProfiles;
    }

    public void ConnectivityChanged(object sender, ConnectivityChangedEventArgs e)
    {
        var access = e.NetworkAccess;
        var profiles = e.ConnectionProfiles;
    }
}
```

## Ejemplo completo: App con funcionalidades nativas

### MainViewModel.cs
```csharp
public class MainViewModel : INotifyPropertyChanged
{
    private readonly LocationService _locationService;
    private readonly MediaService _mediaService;
    private readonly StorageService _storageService;
    private readonly NetworkService _networkService;

    private string _currentLocation;
    private string _selectedImagePath;
    private bool _isConnected;

    public string CurrentLocation
    {
        get => _currentLocation;
        set
        {
            _currentLocation = value;
            OnPropertyChanged();
        }
    }

    public string SelectedImagePath
    {
        get => _selectedImagePath;
        set
        {
            _selectedImagePath = value;
            OnPropertyChanged();
        }
    }

    public bool IsConnected
    {
        get => _isConnected;
        set
        {
            _isConnected = value;
            OnPropertyChanged();
        }
    }

    public ICommand GetLocationCommand { get; }
    public ICommand TakePhotoCommand { get; }
    public ICommand PickPhotoCommand { get; }
    public ICommand SaveDataCommand { get; }

    public MainViewModel()
    {
        _locationService = new LocationService();
        _mediaService = new MediaService();
        _storageService = new StorageService();
        _networkService = new NetworkService();

        GetLocationCommand = new Command(async () => await GetLocation());
        TakePhotoCommand = new Command(async () => await TakePhoto());
        PickPhotoCommand = new Command(async () => await PickPhoto());
        SaveDataCommand = new Command(async () => await SaveData());

        // Verificar conectividad
        IsConnected = _networkService.IsConnected;
        Connectivity.ConnectivityChanged += OnConnectivityChanged;
    }

    private async Task GetLocation()
    {
        var location = await _locationService.GetCurrentLocationAsync();
        if (location != null)
        {
            CurrentLocation = $"Lat: {location.Latitude:F4}, Lon: {location.Longitude:F4}";
        }
        else
        {
            CurrentLocation = "No se pudo obtener la ubicación";
        }
    }

    private async Task TakePhoto()
    {
        var photo = await _mediaService.TakePhotoAsync();
        if (photo != null)
        {
            SelectedImagePath = photo.FullPath;
        }
    }

    private async Task PickPhoto()
    {
        var photo = await _mediaService.PickPhotoAsync();
        if (photo != null)
        {
            SelectedImagePath = photo.FullPath;
        }
    }

    private async Task SaveData()
    {
        var data = $"Location: {CurrentLocation}\nImage: {SelectedImagePath}\nConnected: {IsConnected}";
        await _storageService.SaveTextAsync("app_data.txt", data);
    }

    private void OnConnectivityChanged(object sender, ConnectivityChangedEventArgs e)
    {
        IsConnected = e.NetworkAccess == NetworkAccess.Internet;
    }

    public event PropertyChangedEventHandler PropertyChanged;

    protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

### MainPage.xaml
```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="MyApp.MainPage">

    <ScrollView>
        <StackLayout Padding="20" Spacing="15">
            
            <Label Text="APIs Nativas" 
                   FontSize="24" 
                   HorizontalOptions="Center" 
                   Margin="0,0,0,20" />

            <!-- Estado de conectividad -->
            <Frame Padding="10" BackgroundColor="{Binding IsConnected, Converter={StaticResource BoolToColorConverter}}">
                <StackLayout Orientation="Horizontal">
                    <Label Text="Conectividad:" VerticalOptions="Center" />
                    <Label Text="{Binding IsConnected, StringFormat='{0}'}" 
                           VerticalOptions="Center" 
                           FontAttributes="Bold" />
                </StackLayout>
            </Frame>

            <!-- Ubicación -->
            <Label Text="Ubicación actual:" />
            <Label Text="{Binding CurrentLocation}" 
                   BackgroundColor="LightGray" 
                   Padding="10" />
            <Button Text="Obtener ubicación" 
                    Command="{Binding GetLocationCommand}" />

            <!-- Imagen -->
            <Label Text="Imagen seleccionada:" />
            <Image Source="{Binding SelectedImagePath}" 
                   HeightRequest="200" 
                   Aspect="AspectFit" 
                   BackgroundColor="LightGray" />
            
            <StackLayout Orientation="Horizontal" Spacing="10">
                <Button Text="Tomar foto" 
                        Command="{Binding TakePhotoCommand}" />
                <Button Text="Seleccionar foto" 
                        Command="{Binding PickPhotoCommand}" />
            </StackLayout>

            <!-- Guardar datos -->
            <Button Text="Guardar datos" 
                    Command="{Binding SaveDataCommand}" 
                    Margin="0,20,0,0" />

        </StackLayout>
    </ScrollView>

</ContentPage>
```

## Permisos

### Solicitar permisos
```csharp
public class PermissionService
{
    public async Task<bool> RequestLocationPermissionAsync()
    {
        var status = await Permissions.CheckStatusAsync<Permissions.LocationWhenInUse>();
        
        if (status == PermissionStatus.Granted)
            return true;

        if (status == PermissionStatus.Denied && DeviceInfo.Platform == DevicePlatform.iOS)
        {
            // En iOS, mostrar alerta para ir a configuración
            return false;
        }

        status = await Permissions.RequestAsync<Permissions.LocationWhenInUse>();
        return status == PermissionStatus.Granted;
    }

    public async Task<bool> RequestCameraPermissionAsync()
    {
        var status = await Permissions.CheckStatusAsync<Permissions.Camera>();
        
        if (status == PermissionStatus.Granted)
            return true;

        status = await Permissions.RequestAsync<Permissions.Camera>();
        return status == PermissionStatus.Granted;
    }
}
```

## Ejercicios prácticos

### Ejercicio 1: App de ubicación
1. Implementa geolocalización
2. Muestra la ubicación en un mapa
3. Guarda ubicaciones favoritas

### Ejercicio 2: App de fotos
1. Toma fotos con la cámara
2. Selecciona fotos de la galería
3. Guarda las fotos localmente

### Ejercicio 3: App de conectividad
1. Monitorea el estado de la red
2. Sincroniza datos cuando hay conexión
3. Muestra alertas de conectividad
