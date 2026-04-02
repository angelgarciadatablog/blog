Revisar los proyectos (configuración de cuenta-proyecto)

```bash
gcloud config configurations list
```



Activar una configuración en específica

```bash
gcloud config configurations activate NOMBRE_DE_LA_CONFIG
```



Windows/Mac

```bash
gcloud iam service-accounts create sa-nombre-service-account --display-name="Angelgarciadatablog - Dashboards" --description="SA dedicada para el backend maestro de dashboards" --project=nombre-proyecto

```

| Parte | Valor | Descripción |
| --- | --- | --- |
| Comando base | `gcloud iam service-accounts create` | Crea una nueva Service Account |
| ID de la SA | `nombre-service-account` | Genera el email: `nombre-service-account@proyecto.iam.gserviceaccount.com` |
| `--display-name` | `"Angelgarciadatablog- Dashboards"` | Nombre legible en la consola de GCP (visual, opcional) |
| `--description` | `"SA dedicada para el backend..."` | Descripción en la consola (informativo, opcional) |
| `--project`  | `nombre-proyecto` | Proyecto donde se crea la SA. Sin esto usa el proyecto activo de tu config |



Mac

