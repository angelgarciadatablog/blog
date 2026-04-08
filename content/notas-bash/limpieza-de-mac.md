

```bash
# Ver TODO el espacio usado en tu carpeta de usuario
du -sh ~
```

81G	/Users/angelgarciachanga



```bash
#No suelen haber muchos archivos pesados
du -sh ~/Documents
du -sh ~/Downloads
du -sh ~/Desktop
```



# 1) Lybrary

```bash
#Archivos pesados
du -sh ~/Library
```

Esta carpeta es el **corazón de macOS** donde las apps guardan:

- ✅ Cachés (seguros de borrar)
- ✅ Logs (seguros de borrar)
- ⚠️ Datos de apps (algunos seguros, otros NO)
- ⚠️ Archivos de Xcode/Developer (pueden ser enormes)





## Los 3 Grandes Culpables en ~/Library:

| Carpeta | Tamaño | ¿Qué es? | ¿Se puede limpiar? |
| --- | --- | --- | --- |
| **Application Support** | **21 GB** | Datos de apps | ⚠️ Depende (revisar) |
| **Caches** | **9.4 GB** | Cachés temporales | ✅ **SÍ (muy seguro)** |
| **Containers** | **3 GB** | Apps sandboxed | ⚠️ Depende |
| **Group Containers** | **2.7 GB** | Datos compartidos | ⚠️ Depende |

**Total: ~36 GB** de los 38 GB ✓



## 🔴Application Support

## ¿Qué apps ocupan en Application Support?

```bash
du -sh ~/Library/Application\ Support/* 2>/dev/null | sort -hr | head -15
```

---

## ¿Qué apps tienen cachés enormes?

```bash
du -sh ~/Library/Caches/* 2>/dev/null | sort -hr | head -15
```

#### Application Support (21 GB):

| App | Tamaño | ¿Qué hacer? |
| --- | --- | --- |
| **Google** | **11 GB** | 🔴 Chrome (perfiles, extensiones, caché) |
| **MobileSync** | **4.8 GB** | 🟡 Backups de iPhone/iPad |
| **Notion** | 1 GB | 🟡 Caché de Notion |
| **Code** | 695 MB | 🟢 VS Code (normal) |
| **Filmora** | 560 MB | 🟡 Editor de video |
| **TikTok LIVE** | 474 MB | ⚠️ ¿Usas esto? |



## 🔴 Cachés (9 GB):

5.4G	/Users/angelgarciachanga/Library/Caches/Google
2.1G	/Users/angelgarciachanga/Library/Caches/com.spotify.client

otros..

## ACCIÓN → Borra cachés que se regeneran automáticamente:

```bash
rm -rf ~/Library/Caches/Google/*
rm -rf ~/Library/Caches/com.spotify.client/*
```





## ACCIÓN → Borra copia de seguridad de iphone (solo si lo tienes activo en icloud)

```bash
rm -rf ~/Library/Application\ Support/MobileSync/Backup/*
```



## Revisar Application suport

```bash
du -sh ~/Library/Application\ Support/Google/Chrome/* 2>/dev/null | sort -hr | head -10
```

| Item | Tamaño | ¿Qué es? | ¿Se puede borrar? |
| --- | --- | --- | --- |
| **OptGuideOnDeviceModel** | **4 GB** | Modelo IA de Chrome | ✅ **SÍ (seguro)** |
| **Profile 1** | 4 GB | Tu perfil 1 de Chrome | ⚠️ Solo si no lo usas |
| **Profile 6** | 1.4 GB | Tu perfil 6 de Chrome | ⚠️ Solo si no lo usas |
| **Profile 2** | 916 MB | Tu perfil 2 de Chrome | ⚠️ Solo si no lo usa |
|   |   |   |   |

### **ACCIÓN → Borrar modelo de IA (4 GB libres):**

Este archivo es para sugerencias de Chrome y se regenera automáticamente:

```bash
rm -rf ~/Library/Application\ Support/Google/Chrome/OptGuideOnDeviceModel
```

✅ **Totalmente seguro, libera 4 GB al instante**





---

# 2) Pictures

```bash
#Archivos pesados
du -sh ~/Pictures
```

```bash
du -sh ~/Pictures/* 2>/dev/null | sort -hr | head -10
```

