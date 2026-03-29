



> Áreas de git

**Paso previo:**
git init
Inicializa un repositorio Git en la carpeta del proyecto (crea la carpeta .git).



**Áreas de Git**

1. **Working Directory (Directorio de trabajo):**
Donde editas y modificas tus archivos. (por ejemplo, usando VS Code).

1. **Staging Area (Área de preparación):**
(git add)
Donde seleccionas los cambios que irán al próximo commit.

1. **Local Repository (Repositorio local):**
(git commit)
Donde Git guarda los commits dentro de la carpeta .git.

1. **Remote Repository (Repositorio remoto):**
(git push)
Donde se envían los commits a un repositorio remoto (GitHub, GitLab, etc.).





**Working Directory**
↓ git add
**Staging Area**
↓ git commit
**Local Repository**
↓ git push
**Remote Repository**





> Estados de git





![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/99053d1a-b49d-43a2-934d-76b9db375962/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M5XHP2W%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T070320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQD6FWzrylHRgRZnGGifxy%2FleVdIi3bWi9vVJgDfXU%2BcWwIgSV2upAG2gDuUeLs%2BH%2Bp1JFcnbf2O%2FLZdxOMc9BAlwv8q%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDILxyIzSk%2F8XG2QzXircA2BwYVo1x3i3YoPvgzMFs3gEpyCFpzm2mQuEPYEVvVjy8u4BQJnwitEkVLwk6yBpK6hvIIM%2FwqiR%2BSqh7AoPzyyTob6iAxGsQ2cC1IBDsotXMcYZtRlkOnchpQzKUfyokok7wsz5vXg5PWUVGShvgr623SlAru6uw6sC40MRmnGe7g6DXEdcs8NsFSvEUYNiptb3HaRw5SoC3LZ3vdY0G4wmmNvVVH4ORaQoSxhdcLfQlrYXgmKyDy8ahPb5Tdzn2SZrJjk1ZM5w4tGYSEliQLjkRJrSi5YhkG1oMGlOWIjYSyHt93M4p7RkjX%2BergDFSNs8LIoxTm79s1kk4mfp3245CUGu%2B%2B99Yz%2FUQXMkOWNKUkbWq8REFcD6i4WfpmyVSStpT4ubkNkM%2B1Si4s7xuz1R3963tC14ICf2h7Uj%2FZruO3rhjz4FEBItASiFCntsDOu66YXEXy%2Bh4ZgJbTTV3JCJFAfjreGF4YHPw1SZTO9SkjHxmL%2BOnnuCY3%2F8QjDNsVfaKv1c3gldcDAMo%2FFoGDN18vrRZZqcxhcVS9rVH2jf0s3ue4ByJDN0L3Ya0Bu3OZX83G9INOZqg5tCMvN8P9Yec3j7Y3hGSdOpPK64I2387MltnVjKg%2B55p8qzMJmWo84GOqUBev1CzTMFnMKxy%2BLlpevaYUbTwEu6rJWWlNckquElUuPxJj94NWdIa4CLEJEAD9YWochHBffg1VzP0mD6mkxC%2BpvBl2HxWheje23aFKUjV3aa0rIOd0zrLYvy0EzdYMMOAb5xo3FSvQDbKe%2FWT8PtuLB3j4VOndhbGW%2BOM2XbHvl3BN%2BjlA8vX%2BOkzQFRN3ZOb7ESagAWOHUOP9dQAlJeddz3F9hc&X-Amz-Signature=623eb2661cc121c925fc4f14fdb44e43dbc85c5b5fb3b1abffd90b3f248da073&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/db1a1314-616b-4d4e-a16d-612639f4c99f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M5XHP2W%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T070320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQD6FWzrylHRgRZnGGifxy%2FleVdIi3bWi9vVJgDfXU%2BcWwIgSV2upAG2gDuUeLs%2BH%2Bp1JFcnbf2O%2FLZdxOMc9BAlwv8q%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDILxyIzSk%2F8XG2QzXircA2BwYVo1x3i3YoPvgzMFs3gEpyCFpzm2mQuEPYEVvVjy8u4BQJnwitEkVLwk6yBpK6hvIIM%2FwqiR%2BSqh7AoPzyyTob6iAxGsQ2cC1IBDsotXMcYZtRlkOnchpQzKUfyokok7wsz5vXg5PWUVGShvgr623SlAru6uw6sC40MRmnGe7g6DXEdcs8NsFSvEUYNiptb3HaRw5SoC3LZ3vdY0G4wmmNvVVH4ORaQoSxhdcLfQlrYXgmKyDy8ahPb5Tdzn2SZrJjk1ZM5w4tGYSEliQLjkRJrSi5YhkG1oMGlOWIjYSyHt93M4p7RkjX%2BergDFSNs8LIoxTm79s1kk4mfp3245CUGu%2B%2B99Yz%2FUQXMkOWNKUkbWq8REFcD6i4WfpmyVSStpT4ubkNkM%2B1Si4s7xuz1R3963tC14ICf2h7Uj%2FZruO3rhjz4FEBItASiFCntsDOu66YXEXy%2Bh4ZgJbTTV3JCJFAfjreGF4YHPw1SZTO9SkjHxmL%2BOnnuCY3%2F8QjDNsVfaKv1c3gldcDAMo%2FFoGDN18vrRZZqcxhcVS9rVH2jf0s3ue4ByJDN0L3Ya0Bu3OZX83G9INOZqg5tCMvN8P9Yec3j7Y3hGSdOpPK64I2387MltnVjKg%2B55p8qzMJmWo84GOqUBev1CzTMFnMKxy%2BLlpevaYUbTwEu6rJWWlNckquElUuPxJj94NWdIa4CLEJEAD9YWochHBffg1VzP0mD6mkxC%2BpvBl2HxWheje23aFKUjV3aa0rIOd0zrLYvy0EzdYMMOAb5xo3FSvQDbKe%2FWT8PtuLB3j4VOndhbGW%2BOM2XbHvl3BN%2BjlA8vX%2BOkzQFRN3ZOb7ESagAWOHUOP9dQAlJeddz3F9hc&X-Amz-Signature=a2007247a2b404d6e5d73fc57e2448ad1e6001b7bba0bbdb620a6d118a8e59aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

*Solo sale después de hacer un git add

*Antes de ello el archivo tendrá el estado de U(untracked)



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/3df1900b-9108-459c-ae56-1281df4ba59d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M5XHP2W%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T070320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQD6FWzrylHRgRZnGGifxy%2FleVdIi3bWi9vVJgDfXU%2BcWwIgSV2upAG2gDuUeLs%2BH%2Bp1JFcnbf2O%2FLZdxOMc9BAlwv8q%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDILxyIzSk%2F8XG2QzXircA2BwYVo1x3i3YoPvgzMFs3gEpyCFpzm2mQuEPYEVvVjy8u4BQJnwitEkVLwk6yBpK6hvIIM%2FwqiR%2BSqh7AoPzyyTob6iAxGsQ2cC1IBDsotXMcYZtRlkOnchpQzKUfyokok7wsz5vXg5PWUVGShvgr623SlAru6uw6sC40MRmnGe7g6DXEdcs8NsFSvEUYNiptb3HaRw5SoC3LZ3vdY0G4wmmNvVVH4ORaQoSxhdcLfQlrYXgmKyDy8ahPb5Tdzn2SZrJjk1ZM5w4tGYSEliQLjkRJrSi5YhkG1oMGlOWIjYSyHt93M4p7RkjX%2BergDFSNs8LIoxTm79s1kk4mfp3245CUGu%2B%2B99Yz%2FUQXMkOWNKUkbWq8REFcD6i4WfpmyVSStpT4ubkNkM%2B1Si4s7xuz1R3963tC14ICf2h7Uj%2FZruO3rhjz4FEBItASiFCntsDOu66YXEXy%2Bh4ZgJbTTV3JCJFAfjreGF4YHPw1SZTO9SkjHxmL%2BOnnuCY3%2F8QjDNsVfaKv1c3gldcDAMo%2FFoGDN18vrRZZqcxhcVS9rVH2jf0s3ue4ByJDN0L3Ya0Bu3OZX83G9INOZqg5tCMvN8P9Yec3j7Y3hGSdOpPK64I2387MltnVjKg%2B55p8qzMJmWo84GOqUBev1CzTMFnMKxy%2BLlpevaYUbTwEu6rJWWlNckquElUuPxJj94NWdIa4CLEJEAD9YWochHBffg1VzP0mD6mkxC%2BpvBl2HxWheje23aFKUjV3aa0rIOd0zrLYvy0EzdYMMOAb5xo3FSvQDbKe%2FWT8PtuLB3j4VOndhbGW%2BOM2XbHvl3BN%2BjlA8vX%2BOkzQFRN3ZOb7ESagAWOHUOP9dQAlJeddz3F9hc&X-Amz-Signature=c90f1eb14507dd2c435da96803723a89cb852d4fd7194345a9e667b7f2025e2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

