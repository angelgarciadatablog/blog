**¿Qué es Claude CLI?**

Es la interfaz de línea de comandos de Anthropic que permite interactuar con Claude directamente desde la terminal. Vimos que tienes la carpeta `.claude` en tu usuario, lo que indica que está instalado y configurado.



**Verifiquemos el estado:**

```bash
claude auth status
```

Respuesta

{
"loggedIn": true,
"authMethod": "claude.ai",
"apiProvider": "firstParty",
"email": "correo-de-cuenta-claude@gmail.com",
"orgId": "90cb726d-7665-4813-b442-44e598666694",
"orgName": null,
"subscriptionType": "max"
}





Con Claude CLI puedes cambiar de cuenta con:

```bash
claude auth logout
claude auth login
```

No soporta múltiples cuentas simultáneas como gh — es una sola sesión activa a la vez. Si quieres cambiar, haces logout y login con la otra cuenta.

