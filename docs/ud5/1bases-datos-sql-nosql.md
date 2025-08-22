# Bases de Datos SQL y NoSQL

## Introducción

Las bases de datos son el corazón de cualquier aplicación moderna. En esta unidad exploraremos dos tipos fundamentales de bases de datos: **bases de datos SQL** (relacionales) y **bases de datos NoSQL** (no relacionales), con ejemplos prácticos usando PostgreSQL y MongoDB.

### ¿Por qué aprender sobre bases de datos?

- **Almacenamiento persistente**: Las aplicaciones necesitan guardar datos de forma permanente
- **Escalabilidad**: Las bases de datos permiten manejar grandes volúmenes de información
- **Integridad**: Garantizan la consistencia y validez de los datos
- **Consultas eficientes**: Permiten buscar y recuperar información rápidamente

## Bases de Datos SQL: PostgreSQL

### ¿Qué es PostgreSQL?

PostgreSQL es un sistema de gestión de bases de datos relacionales (RDBMS) de código abierto, robusto y escalable. Es conocido por su conformidad con los estándares SQL y su capacidad para manejar cargas de trabajo complejas.

#### Características principales

##### 🎯 **Conformidad con estándares**
- Soporte completo para SQL estándar
- Transacciones ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad)
- Integridad referencial
- Triggers y procedimientos almacenados

##### 🚀 **Rendimiento y escalabilidad**
```sql
-- PostgreSQL soporta consultas complejas y optimizaciones avanzadas
SELECT 
    u.nombre,
    COUNT(p.id) as total_posts,
    AVG(p.puntuacion) as puntuacion_promedio
FROM usuarios u
LEFT JOIN posts p ON u.id = p.usuario_id
WHERE u.fecha_registro > '2023-01-01'
GROUP BY u.id, u.nombre
HAVING COUNT(p.id) > 5
ORDER BY puntuacion_promedio DESC;
```

##### 🎨 **Tipos de datos avanzados**
```sql
-- PostgreSQL soporta tipos de datos complejos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2),
    categorias TEXT[], -- Array de texto
    metadata JSONB,    -- Datos JSON binarios
    ubicacion POINT,   -- Coordenadas geográficas
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Configuración básica con .NET

#### Instalación de Npgsql
```bash
# Instalar el driver de PostgreSQL para .NET
dotnet add package Npgsql
dotnet add package Npgsql.EntityFrameworkCore
```

#### Conexión básica
```csharp
using Npgsql;
using System.Data;

public class DatabaseService
{
    private readonly string _connectionString;

    public DatabaseService(string connectionString)
    {
        _connectionString = connectionString;
    }

    public async Task<List<Usuario>> ObtenerUsuariosAsync()
    {
        var usuarios = new List<Usuario>();
        
        using var connection = new NpgsqlConnection(_connectionString);
        await connection.OpenAsync();
        
        using var command = new NpgsqlCommand(
            "SELECT id, nombre, email, fecha_registro FROM usuarios", 
            connection);
        
        using var reader = await command.ExecuteReaderAsync();
        while (await reader.ReadAsync())
        {
            usuarios.Add(new Usuario
            {
                Id = reader.GetInt32("id"),
                Nombre = reader.GetString("nombre"),
                Email = reader.GetString("email"),
                FechaRegistro = reader.GetDateTime("fecha_registro")
            });
        }
        
        return usuarios;
    }
}
```

#### Entity Framework Core con PostgreSQL
```csharp
using Microsoft.EntityFrameworkCore;

public class ApplicationDbContext : DbContext
{
    public DbSet<Usuario> Usuarios { get; set; }
    public DbSet<Post> Posts { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseNpgsql(
            "Host=localhost;Database=mibasededatos;Username=usuario;Password=contraseña");
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Usuario>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.Property(e => e.Nombre).IsRequired().HasMaxLength(100);
            entity.Property(e => e.Email).IsRequired().HasMaxLength(255);
            entity.HasIndex(e => e.Email).IsUnique();
        });
    }
}
```

## Bases de Datos NoSQL: MongoDB

### ¿Qué es MongoDB?

MongoDB es una base de datos NoSQL orientada a documentos que almacena datos en formato JSON flexible (BSON). Es ideal para aplicaciones que requieren escalabilidad horizontal y flexibilidad en el esquema de datos.

#### Características principales

##### 🎯 **Flexibilidad de esquema**
```json
// Los documentos pueden tener estructuras diferentes
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "nombre": "Juan Pérez",
  "email": "juan@ejemplo.com",
  "edad": 30,
  "direccion": {
    "calle": "Calle Principal 123",
    "ciudad": "Madrid",
    "codigo_postal": "28001"
  },
  "intereses": ["programación", "música", "deportes"],
  "fecha_registro": ISODate("2023-01-15T10:30:00Z")
}
```

##### 🚀 **Consultas potentes**
```javascript
// MongoDB soporta consultas complejas y agregaciones
db.usuarios.aggregate([
  {
    $match: {
      fecha_registro: { $gte: new Date("2023-01-01") }
    }
  },
  {
    $lookup: {
      from: "posts",
      localField: "_id",
      foreignField: "usuario_id",
      as: "posts"
    }
  },
  {
    $project: {
      nombre: 1,
      total_posts: { $size: "$posts" },
      puntuacion_promedio: { $avg: "$posts.puntuacion" }
    }
  },
  {
    $match: {
      total_posts: { $gt: 5 }
    }
  },
  {
    $sort: { puntuacion_promedio: -1 }
  }
])
```

##### 🎨 **Escalabilidad horizontal**
- **Sharding**: Distribución automática de datos
- **Replicación**: Alta disponibilidad
- **Índices**: Optimización de consultas

### Configuración básica con .NET

#### Instalación del driver de MongoDB
```bash
# Instalar el driver oficial de MongoDB para .NET
dotnet add package MongoDB.Driver
```

#### Conexión y operaciones básicas
```csharp
using MongoDB.Driver;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

public class Usuario
{
    [BsonId]
    public ObjectId Id { get; set; }
    
    [BsonElement("nombre")]
    public string Nombre { get; set; }
    
    [BsonElement("email")]
    public string Email { get; set; }
    
    [BsonElement("edad")]
    public int Edad { get; set; }
    
    [BsonElement("fecha_registro")]
    public DateTime FechaRegistro { get; set; }
}

public class MongoService
{
    private readonly IMongoCollection<Usuario> _usuarios;

    public MongoService(string connectionString, string databaseName)
    {
        var client = new MongoClient(connectionString);
        var database = client.GetDatabase(databaseName);
        _usuarios = database.GetCollection<Usuario>("usuarios");
    }

    public async Task<List<Usuario>> ObtenerUsuariosAsync()
    {
        return await _usuarios.Find(_ => true).ToListAsync();
    }

    public async Task<Usuario> ObtenerUsuarioPorEmailAsync(string email)
    {
        var filter = Builders<Usuario>.Filter.Eq(u => u.Email, email);
        return await _usuarios.Find(filter).FirstOrDefaultAsync();
    }

    public async Task CrearUsuarioAsync(Usuario usuario)
    {
        await _usuarios.InsertOneAsync(usuario);
    }

    public async Task ActualizarUsuarioAsync(ObjectId id, Usuario usuario)
    {
        var filter = Builders<Usuario>.Filter.Eq(u => u.Id, id);
        var update = Builders<Usuario>.Update
            .Set(u => u.Nombre, usuario.Nombre)
            .Set(u => u.Email, usuario.Email)
            .Set(u => u.Edad, usuario.Edad);
        
        await _usuarios.UpdateOneAsync(filter, update);
    }

    public async Task EliminarUsuarioAsync(ObjectId id)
    {
        var filter = Builders<Usuario>.Filter.Eq(u => u.Id, id);
        await _usuarios.DeleteOneAsync(filter);
    }
}
```

## Comparación: PostgreSQL vs MongoDB

| Característica | PostgreSQL | MongoDB |
|----------------|------------|---------|
| **Tipo** | Relacional (SQL) | NoSQL (Documentos) |
| **Esquema** | Fijo y estructurado | Flexible y dinámico |
| **Transacciones** | ACID completas | ACID limitadas |
| **Escalabilidad** | Vertical | Horizontal |
| **Consultas** | SQL estándar | MongoDB Query Language |
| **Casos de uso** | Datos estructurados, relaciones complejas | Datos no estructurados, escalabilidad |
| **Complejidad** | Media-Alta | Baja-Media |

## Casos de uso recomendados

### ✅ **PostgreSQL es ideal para:**
- Aplicaciones empresariales con datos estructurados
- Sistemas que requieren transacciones ACID
- Aplicaciones con relaciones complejas entre entidades
- Sistemas de gestión de recursos empresariales (ERP)
- Aplicaciones financieras y contables

### ✅ **MongoDB es ideal para:**
- Aplicaciones con datos no estructurados o semi-estructurados
- Sistemas que requieren escalabilidad horizontal
- Aplicaciones de contenido y gestión de documentos
- Sistemas de análisis de datos en tiempo real
- Aplicaciones IoT con datos de sensores

## Ejemplo práctico: Sistema de blog

### Estructura en PostgreSQL
```sql
-- Tabla de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de categorías
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);

-- Tabla de posts
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    contenido TEXT NOT NULL,
    usuario_id INTEGER REFERENCES usuarios(id),
    categoria_id INTEGER REFERENCES categorias(id),
    fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(20) DEFAULT 'borrador'
);

-- Tabla de comentarios
CREATE TABLE comentarios (
    id SERIAL PRIMARY KEY,
    contenido TEXT NOT NULL,
    post_id INTEGER REFERENCES posts(id),
    usuario_id INTEGER REFERENCES usuarios(id),
    fecha_comentario TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Estructura en MongoDB
```javascript
// Colección de usuarios
{
  "_id": ObjectId("..."),
  "nombre": "Ana García",
  "email": "ana@ejemplo.com",
  "fecha_registro": ISODate("2023-01-15T10:30:00Z"),
  "perfil": {
    "bio": "Desarrolladora de software",
    "avatar": "https://ejemplo.com/avatar.jpg",
    "redes_sociales": {
      "twitter": "@anagarcia",
      "linkedin": "anagarcia"
    }
  }
}

// Colección de posts
{
  "_id": ObjectId("..."),
  "titulo": "Introducción a MongoDB",
  "contenido": "MongoDB es una base de datos NoSQL...",
  "autor": {
    "id": ObjectId("..."),
    "nombre": "Ana García"
  },
  "categoria": {
    "id": ObjectId("..."),
    "nombre": "Bases de Datos"
  },
  "etiquetas": ["mongodb", "nosql", "bases-de-datos"],
  "fecha_publicacion": ISODate("2023-02-20T14:00:00Z"),
  "estado": "publicado",
  "comentarios": [
    {
      "id": ObjectId("..."),
      "contenido": "Excelente artículo",
      "autor": {
        "id": ObjectId("..."),
        "nombre": "Carlos López"
      },
      "fecha": ISODate("2023-02-21T09:15:00Z")
    }
  ],
  "estadisticas": {
    "vistas": 1250,
    "likes": 45,
    "compartidos": 12
  }
}
```

## Configuración de desarrollo

### PostgreSQL con Docker
```yaml
# docker-compose.yml
version: '3.8'
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: mibasededatos
      POSTGRES_USER: usuario
      POSTGRES_PASSWORD: contraseña
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### MongoDB con Docker
```yaml
# docker-compose.yml
version: '3.8'
services:
  mongodb:
    image: mongo:6
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: contraseña
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db

volumes:
  mongodb_data:
```

## Patrones de diseño comunes

### Repository Pattern
```csharp
public interface IUsuarioRepository
{
    Task<List<Usuario>> ObtenerTodosAsync();
    Task<Usuario> ObtenerPorIdAsync(int id);
    Task<Usuario> CrearAsync(Usuario usuario);
    Task<Usuario> ActualizarAsync(Usuario usuario);
    Task EliminarAsync(int id);
}

public class UsuarioRepository : IUsuarioRepository
{
    private readonly ApplicationDbContext _context;

    public UsuarioRepository(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<List<Usuario>> ObtenerTodosAsync()
    {
        return await _context.Usuarios.ToListAsync();
    }

    public async Task<Usuario> ObtenerPorIdAsync(int id)
    {
        return await _context.Usuarios.FindAsync(id);
    }

    public async Task<Usuario> CrearAsync(Usuario usuario)
    {
        _context.Usuarios.Add(usuario);
        await _context.SaveChangesAsync();
        return usuario;
    }

    public async Task<Usuario> ActualizarAsync(Usuario usuario)
    {
        _context.Usuarios.Update(usuario);
        await _context.SaveChangesAsync();
        return usuario;
    }

    public async Task EliminarAsync(int id)
    {
        var usuario = await _context.Usuarios.FindAsync(id);
        if (usuario != null)
        {
            _context.Usuarios.Remove(usuario);
            await _context.SaveChangesAsync();
        }
    }
}
```

### Unit of Work Pattern
```csharp
public interface IUnitOfWork : IDisposable
{
    IUsuarioRepository Usuarios { get; }
    IPostRepository Posts { get; }
    Task<int> SaveChangesAsync();
}

public class UnitOfWork : IUnitOfWork
{
    private readonly ApplicationDbContext _context;
    private IUsuarioRepository _usuarios;
    private IPostRepository _posts;

    public UnitOfWork(ApplicationDbContext context)
    {
        _context = context;
    }

    public IUsuarioRepository Usuarios => 
        _usuarios ??= new UsuarioRepository(_context);

    public IPostRepository Posts => 
        _posts ??= new PostRepository(_context);

    public async Task<int> SaveChangesAsync()
    {
        return await _context.SaveChangesAsync();
    }

    public void Dispose()
    {
        _context?.Dispose();
    }
}
```

## Mejores prácticas

### 1. **Manejo de conexiones**
```csharp
// ✅ Correcto: Usar using para liberar recursos
using var connection = new NpgsqlConnection(connectionString);
await connection.OpenAsync();

// ❌ Incorrecto: No liberar recursos
var connection = new NpgsqlConnection(connectionString);
await connection.OpenAsync();
```

### 2. **Parámetros preparados**
```csharp
// ✅ Correcto: Usar parámetros para prevenir SQL injection
var command = new NpgsqlCommand(
    "SELECT * FROM usuarios WHERE email = @email", connection);
command.Parameters.AddWithValue("@email", email);

// ❌ Incorrecto: Concatenación de strings
var command = new NpgsqlCommand(
    $"SELECT * FROM usuarios WHERE email = '{email}'", connection);
```

### 3. **Transacciones**
```csharp
// ✅ Correcto: Usar transacciones para operaciones múltiples
using var transaction = await connection.BeginTransactionAsync();
try
{
    // Operaciones de base de datos
    await transaction.CommitAsync();
}
catch
{
    await transaction.RollbackAsync();
    throw;
}
```

### 4. **Índices**
```sql
-- ✅ Crear índices para mejorar el rendimiento
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_posts_fecha ON posts(fecha_publicacion);
CREATE INDEX idx_comentarios_post_id ON comentarios(post_id);
```

## Recursos adicionales

### PostgreSQL
- [Documentación oficial](https://www.postgresql.org/docs/)
- [Npgsql (Driver .NET)](https://www.npgsql.org/)
- [Entity Framework Core con PostgreSQL](https://docs.microsoft.com/en-us/ef/core/providers/npgsql/)

### MongoDB
- [Documentación oficial](https://docs.mongodb.com/)
- [MongoDB .NET Driver](https://docs.mongodb.com/drivers/csharp/)
- [MongoDB University (cursos gratuitos)](https://university.mongodb.com/)

### Herramientas de administración
- **PostgreSQL**: pgAdmin, DBeaver, DataGrip
- **MongoDB**: MongoDB Compass, Studio 3T, Robo 3T

---

## Ejercicios prácticos

### Ejercicio 1: Configurar PostgreSQL
1. Instala PostgreSQL en tu sistema
2. Crea una base de datos de prueba
3. Configura Entity Framework Core
4. Crea las tablas básicas para un sistema de blog

### Ejercicio 2: Configurar MongoDB
1. Instala MongoDB en tu sistema
2. Crea una base de datos de prueba
3. Configura el driver de MongoDB para .NET
4. Crea las colecciones básicas para un sistema de blog

### Ejercicio 3: Comparar rendimiento
1. Crea la misma aplicación usando PostgreSQL y MongoDB
2. Mide el rendimiento de las consultas básicas
3. Analiza las diferencias en el desarrollo
4. Documenta tus conclusiones

### Ejercicio 4: Sistema de gestión de tareas
1. Diseña un sistema de gestión de tareas
2. Implementa el modelo de datos en ambas bases de datos
3. Crea las operaciones CRUD básicas
4. Añade funcionalidades avanzadas como búsqueda y filtros
