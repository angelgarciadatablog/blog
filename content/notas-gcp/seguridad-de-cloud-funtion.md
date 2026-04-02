## 🔐 Cómo funciona la seguridad:

### **URL pública ≠ Ejecución pública**

**La URL es "visible":**

`https://youtube-v3-weekly-1052480639778.us-central1.run.app`

Cualquiera que la conozca puede **intentar** llamarla.

---

### **PERO la ejecución está protegida:**

Tu función tiene:

`✅ Autenticación: Necesita autenticación (IAM)
✅ Ingress: Interno`

Y el scheduler usa:

`✅ Token de OIDC
✅ Service Account: youtube-pipeline-sa`

---

## 🛡️ ¿Qué pasa si alguien intenta ejecutarla sin permisos?

bash

`# Alguien random intenta:
curl https://youtube-v3-weekly-1052480639778.us-central1.run.app

# Respuesta:
403 Forbidden
Your client does not have permission to get URL`

---

## ✅ Solo pueden ejecutarla:

1. **Cloud Scheduler** (con cuenta de servicio `youtube-pipeline-sa`)
1. **Tu cuenta** (porque eres owner del proyecto)
1. Cualquier otra cuenta que tenga el rol `Cloud Run Invoker`