### **🛠️ ¿Qué vamos a hacer?**

1. **Instalar Homebrew** → un gestor de paquetes que facilita instalar herramientas técnicas desde la terminal.
1. **Usar Homebrew para instalar ngrok** → una herramienta que crea una **URL pública temporal** (HTTPS) que apunta a tu localhost.

Así podremos probar webhooks **como si estuviéramos en producción**, pero sin subir nada a la nube.



### **⚙️ ¿Qué implica hacer esto?**

- Instalar **Homebrew** ocupa ~300 MB, pero **te servirá a futuro** para instalar herramientas como:
    - jq, git, httpie, mysql, ffmpeg, python, etc.
- Instalar **ngrok** ocupa ~25 MB y te servirá para:
    - Exponer webhooks de n8n
    - Probar APIs locales desde móviles, Zapier, Airtable, Shopify, etc.



### **🔒 ¿Es seguro?**

Sí. ngrok crea una conexión segura **solo durante el tiempo que está activo**.

No es recomendable para producción, pero **sí es seguro para pruebas y desarrollo**.

**comando actualizado para instalar Homebrew**

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

**comando para instalar ngrok**

brew install ngrok