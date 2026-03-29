

## Qué es Cloud Shell

Es una terminal que Google pone a tu disposición directamente en el navegador desde la consola de GCP (`console.cloud.google.com`). Viene preinstalada con todas las herramientas de Google Cloud (`gsutil`, `gcloud`, etc.) y ya tiene autenticación con tu cuenta, sin necesidad de configurar credenciales.



## Configurar política de CORS

Crea un archivo llamado `cors.json` en la terminal con el contenido entre `EOF` y `EOF`. Es una forma rápida de escribir un archivo sin abrir un editor.



Define la política CORS:

- `origin`: qué dominios pueden hacer peticiones al bucket

- `method`: solo permite peticiones `GET` (leer archivos, no escribir)

- `responseHeader`: qué headers del response puede leer el browser

- `maxAgeSeconds`: cuánto tiempo el browser cachea esta política (1 hora) antes de volver a preguntar

```bash
cat > cors.json << 'EOF'
[
  {
    "origin": [
      "https://angelgarciadatablog.com",
      "https://www.angelgarciadatablog.com",
      "http://127.0.0.1:5501",
      "http://localhost:5500"
    ],
    "method": ["GET"],
    "responseHeader": ["Content-Type"],
    "maxAgeSeconds": 3600
  }
]
EOF

gsutil cors set cors.json gs://angelgarciadatablog-analytics

```

*`gsutil` es la herramienta de línea de comandos para gestionar GCS. Este comando aplica la política del archivo `cors.json` al bucket `angelgarciadatablog-analytics`.



```bash
cat > cors.json << 'EOF'
[
  {
    "origin": ["*"],
    "method": ["GET"],
    "responseHeader": ["Content-Type"],
    "maxAgeSeconds": 3600
  }
]
EOF

gsutil cors set cors.json gs://angelgarciadatablog-analytics

```

*Para dar acceso a cualquier link se debe poner * dentro de origin





verificar

```bash
gsutil cors get gs://angelgarciadatablog-analytics
```



---





## Por qué necesitamos CORS

CORS es una restricción **del navegador**, no del servidor. Cuando un browser hace un `fetch()` desde `http://127.0.0.1:5500` hacia `storage.googleapis.com`, el browser primero pregunta al servidor "¿permites peticiones desde este origen?". Si el servidor no responde con el header `Access-Control-Allow-Origin`, el browser bloquea la respuesta — aunque el archivo sea público.

## Por qué no afecta a otras herramientas

- **Pegar la URL en el navegador**: el browser no aplica CORS porque no hay un origen "solicitante", navegas directamente al recurso

- **Power BI, Postman, curl, Python**: son clientes que no implementan la política CORS — hacen la petición directamente sin ese chequeo previo

- **Cualquier backend**: mismo caso, CORS solo aplica en peticiones cross-origin desde código JavaScript en el browser

## En resumen

Los datos son públicos para todos. CORS solo controla si **un script JavaScript en el browser** puede consumirlos, como protección que implementan los propios navegadores.

