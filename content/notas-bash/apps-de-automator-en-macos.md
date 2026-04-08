# Qué es realmente una app de Automator

Cuando exportas una automatización como **“Aplicación” en Automator**, macOS genera un archivo con extensión:

```
nombre.app
```

Aunque parece un archivo normal, en realidad es un **bundle de aplicación**.

Un bundle es **una carpeta especial que macOS trata como si fuera una aplicación**.

Por ejemplo:

```
mi-script.app
```

En realidad contiene una estructura interna similar a esta:

```
mi-script.app
└── Contents
    ├── Info.plist
    ├── MacOS
    ├── Resources
    └── document.wflow
```

Componentes principales:

- **Info.plist** → metadatos de la aplicación.
- **MacOS/** → ejecutable que lanza la app.
- **Resources/** → recursos como iconos u otros archivos.
- **document.wflow** → workflow de Automator que contiene la lógica de la automatización.

En las apps creadas con Automator, **la lógica del flujo se encuentra dentro del archivo**:

```
Contents/document.wflow
```

---





# Cómo identificar apps creadas con Automator

Una forma fiable de identificar si una aplicación fue creada con Automator es comprobar si contiene el archivo:

```
document.wflow
```

Puedes buscarlo dentro de la carpeta `/Applications` usando el comando:

```
find /Applications-name"document.wflow"
```

Si una app contiene ese archivo, significa que fue generada por Automator.

Ejemplo de resultado:

```
/Applications/notas-automator.app/Contents/document.wflow
```

---



# Consideración sobre la ubicación de las apps

El comando anterior solo busca dentro de:

```
/Applications
```

Si la aplicación fue guardada en otra carpeta (por ejemplo `Desktop` o `Documents`), no será encontrada.

Para evitar esto, suele ser buena práctica **guardar las apps de Automator en****`/Applications`**, porque:

- aparecen en **Launchpad**
- pueden abrirse fácilmente con **Spotlight**
- se comportan como cualquier otra aplicación del sistema

---

# Flujo de trabajo recomendado para proyectos de Automator

Para mantener las automatizaciones organizadas, es útil separar los distintos componentes del proyecto.

Ejemplo de estructura:

```
automator-apps
└── pendientes
    ├── workflow
    │   └── notas-automator.workflow
    │
    ├── resources
    │   └── pendientes.html
    │
    └── build
        └── notas-automator.app
```

Descripción de cada carpeta:

### workflow

Contiene el **workflow editable de Automator**.

Es el equivalente al **código fuente del proyecto**.

### resources

Archivos externos utilizados por la automatización:

- HTML
- scripts
- iconos
- archivos auxiliares

### build

Contiene la **app final generada por Automator**.

Esta separación permite:

- modificar el workflow sin perder la app
- regenerar la aplicación si se elimina
- mantener los recursos organizados
- versionar el proyecto fácilmente

