

### 1) Hosting compartido (el que venden para webs)

- Compras un **espacio en una carpeta** dentro de un servidor
- No tienes acceso al sistema operativo
- Solo subes archivos (HTML, PHP) a través de un panel (cPanel)
- No puedes instalar nada — usas lo que ya viene instalado
- Ejemplo: pagas $5/mes en GoDaddy, subes tu web y listo
- están encendidos 24/7.
- Sirven para : Webs estáticas (HTML, CSS, JS),  WordPress, Webs con PHP
- **No sirven para:**Apps con **Node.js,**Apps con **Python** (Django, Flask), Apps que necesiten **bases de datos modernas,**Cualquier cosa que requiera instalar algo en el servidor
| Proveedor | Conocido por |
| --- | --- |
| **GoDaddy** | El más popular, también vende dominios |
| **HostGator** | Barato, popular en Latinoamérica |
| **Bluehost** | Recomendado por WordPress |
| **Namecheap** | Dominios baratos + hosting |
| **SiteGround** | Buen soporte técnico |



### 2) Hosting dedicado (**Servidor dedicado)**

- Te dan un **servidor físico completo** exclusivamente para ti
- Tienes acceso total al sistema operativo, igual que un VPS
- Nadie más comparte tu máquina — todos los recursos (CPU, RAM, disco) son 100% tuyos
- Rendimiento garantizado, sin sorpresas por vecinos que consuman mucho
- Lo usan empresas con alto tráfico o regulaciones que exigen hardware exclusivo
- Ejemplo: pagas $80-200+/mes en OVH, Hetzner o proveedores cloud
- Están encendidos 24/7



### 3) VPS (Máquina visual) (vm)

- Te dan una **computadora virtual completa** con su propio sistema operativo (Linux)
- Tú entras por terminal, instalas programas, configuras todo
- Es como tener tu propia PC remota
- Ejemplo: pagas $5/mes en DigitalOcean, te conectas por SSH y haces lo que quieras
- Un VPS es una computadora tuya en internet, encendida 24/7, donde corres lo que quieras:
- Un VPS pagas un monto fijo mensual, esté encendido o apagado, lo uses o no. Es como el alquiler de un departamento.

```bash
Aplicaciones web — dashboards como el tuyo, e-commerce, APIs 
Bots — bots de Discord, Telegram, WhatsApp que necesitan estar siempre activos
Bases de datos — MongoDB, PostgreSQL, MySQL propio
Servidores de juegos — Minecraft, Counter-Strike
VPN propia — para navegación privada
Automatizaciones — scripts que se ejecutan cada cierto tiempo (scraping, reportes)
Correo propio — tu propio servidor de email
```

| Proveedor | Conocido por |
| --- | --- |
| **AWS** (Amazon) | El más grande del mercado |
| **Google Cloud** | BigQuery, IA — el que usas tú |
| **Azure** (Microsoft) | Popular en empresas que usan Microsoft |

*Los proveedores de cloud también ofrecen VPS/VMs, pero van más allá — incluyen bases de datos, IA, contenedores, y cientos de servicios adicionales.



| Proveedor | Conocido por |
| --- | --- |
| **DigitalOcean** | El más popular entre desarrolladores |
| **Hetzner** | El más barato, servidores en Europa |
| **Vultr** | Muchas ubicaciones, barato |
| **Linode** | Ahora es de Akamai, buen rendimiento |
| **OVH** | Europeo, buena relación precio/calidad |
| **Contabo** | Mucha RAM/disco por poco preci |

### ¿VPS  vs Hosting dedicado?

La diferencia es **rendimiento garantizado**.

`VPS:
🖥️ Servidor físico
┌──────────────────────────────┐
│  🖥️ Tu VPS (virtual)         │
│  🖥️ Otro VPS (virtual)       │  ← comparten la misma máquina física
│  🖥️ Otro VPS (virtual)       │
└──────────────────────────────┘
Si otro VPS consume mucho, puede afectarte

Dedicado:
🖥️ Servidor físico
┌──────────────────────────────┐
│                              │
│  Solo tú                     │  ← nadie te quita recursos
│                              │
└──────────────────────────────┘`



### ¿Cómo cambiar de proveedor de vps?

`🖥️ Tu VPS ($6/mes)
┌──────────────────────────────────┐
│                                  │
│  📦 Contenedor 1: n8n            │
│  📦 Contenedor 2: tu app web    │
│  📦 Contenedor 3: base de datos │
│  📦 Contenedor 4: otro proyecto │
│                                  │
│  Cada uno aislado del otro       │
└──────────────────────────────────┘`

**Ventajas de tenerlos separados**

- Si uno falla, **los demás siguen funcionando**
- Cada uno tiene sus propias dependencias sin conflictos
- Puedes apagar, reiniciar o actualizar uno sin tocar los demás
- Para migrar, copias los contenedores que quieras al nuevo VPS

**Herramienta clave: Docker Compose**

Con un solo archivo defines todos tus contenedores y los levantas con un comando:

`docker compose up`

Y todo arranca. Es la forma estándar de manejar varios contenedores en un VPS.





### **4) Contenedores por demanda**

Subes tu app empaquetada, se enciende/apaga sola. Pagas por uso.

| Servicio | Proveedor |
| --- | --- |
| **Cloud Run** | Google |
| **Fargate** | Amazon (AWS) |
| **Container Apps** | Microsoft (Azure) |
| **Railway** | Independiente |
| **Render** | Independiente |
| **Fly.io** | Independiente |



### 5) Serverless / Plataformas

Solo subes código, ni siquiera piensas en contenedores. Ideal para frontends y funciones simples.

| Servicio | Ideal para |
| --- | --- |
| **Vercel** | Frontends (React, Next.js) |
| **Netlify** | Frontends + formularios |
| **Cloudflare Pages** | Frontends con CDN global |



### 6) PaaS (Platform as a Service)

Subes tu código directo, sin Docker ni contenedores. La plataforma se encarga de todo.

| Servicio | Nota |
| --- | --- |
| **Heroku** | El pionero, muy fácil |
| **AWS Elastic Beanstalk** | Lo mismo pero en Amazon |

