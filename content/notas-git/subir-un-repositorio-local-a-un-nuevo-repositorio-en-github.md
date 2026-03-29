

```bash
##revisar los cambios que se han hecho en el repositorio local
git status

#Guardar los cambios
git add .

#Revisar lo que se va a guardar en el historial
git status

#Realizar el primer commit para guardar en el historial
git commit -m "este es un primero commit que se guardará según los cambios hechos"

#"cuando se crea un primer commit, se creará automáticamente una rama llamada main". 
#Pero hasta que no haya ese primer commit, la rama no existe de verdad
#Para verificar que se creo la rama ejecutar el siguiente comando
git branch
```





Conectar el repositorio local con un repositorio remoto ya credo en github

```bash
#conectar al repositorio remoto
git remote add origin https://github.com/angelgarciadatablog/angel-notebooks.git

#verificar la conexión
git remote -v

#hacer el push de lo que está en local hacia lo remoto
git push origin main
```

*Esa ruta se utiliza siempre y cuando estes autenticado vía https





Si es primera vez que te harás un push te pedirá identificarte:

Esta identificación solo se añade al usuario actual del ordenador

```bash
# Configurar nombre (usa tu nombre real o de GitHub)
git config --global user.name "Angel García"

# Configurar email (usa el mismo email de tu cuenta GitHub)
git config --global user.email "tu-email@gmail.com"

# Verificar que se guardó
git config --global user.name
git config --global user.email
```





El primer push pedirá autenticación con la cuenta de GitHub

```bash
#hacer el push de lo que está en local hacia lo remoto
git push origin main
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/6b281738-50d0-43c2-a8cc-55b5fbef85ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR7B6GMM%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T070146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDC6l59Fn1Y8Sv9cKw%2BWPj7ljlUDWqWXc0It35qs6XsSAIhAMW7KMtXjtHzKM2pdHPqgy5T5RIDzE5K9CtXCjTdtK80Kv8DCAgQABoMNjM3NDIzMTgzODA1IgzThPaALHCrTZfPWloq3AOMt%2BvXpnFSvGULiRhmjRHvcbhl2bo0exwr6Zsg4khf3KfgWBDfTv%2BgU46TTWtiu40Zd%2FiE8RUW0peRwRVOAGdjZFZb2m3F9NBzD3DWs0TF5%2BZRegf4RaS8Hnyngmi1cKyN9tkcWS6BlCRLA%2FXHHFVRnEim2Jjx%2B8AiaTO2XtimyRpjTMLzstwHZ4wBeusMLSgK88lYKiaBQ0Dukzcex%2FG1voQY4zSYefwNx6KqQHMP7A4UpOh%2FpZKBndWnShk%2BEf2cQoo3huT3xKaZvaeVzlCaac0ImBTJfRowTGJo6wu7yEN%2BONw4RlEheIRuJdI9%2FresqVDxP4MZzSe%2FkcPMMPicCa6EiQfJCMkOpAhIdndMYm7eFKZtJsdEUrhRIym30B%2BQX5%2Bmf%2BUAcnFNB04m4auND%2BGRUXIodYwGCuZcAHe0uGNwbvvRaeEfxKzcwJ4y48UqEhl9R8yChKj%2Fm3gIY6ykhq%2B1hGiV6jO2sfpdJ3TlGVeZrU5jKWBnnI7TIpv%2Bxj7V7skn6R898xcBTiO25Xc9hbU7ktE3n3M9pb6ASb2oNaeSb8oBuYqm5iT0UQ4TdaGXjkBD21usBBCbBhD6rJHz5zivLbEz8%2BU9YTLpVV1jzWnW9szZNIIFV%2FV6NjDxlqPOBjqkAbvZgXXGmkG9OJA3kbmKjqzMFoj3657rqLL2YXlHizGKLRKPd6wcOCfhZbi%2BbE9Hp8S1h6h8MVTJUWH%2BPl7zQ9uk8TjLoLb3x7PfJpmL1%2BnpzE%2FiVHioFJMmYZR5LRuukpjWSYu9gQ%2Fpi6tCxOHX1BcLg7t1aAZKYLuU2aIuX%2FYYXW0hyZAj%2BGSq8fzoarUzHBiN7yZ95QojpuULcqsOAFjC5uAD&X-Amz-Signature=0590db7f2fa89651085cb3aafc39082f2565bde22b4b83b2a53eae76a51a1551&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/6777a3e4-8bfc-492a-8dc5-bb9cc05a541d/a6cbe2c4-cb47-438c-a02c-2ad695ee991a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR7B6GMM%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T070146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDC6l59Fn1Y8Sv9cKw%2BWPj7ljlUDWqWXc0It35qs6XsSAIhAMW7KMtXjtHzKM2pdHPqgy5T5RIDzE5K9CtXCjTdtK80Kv8DCAgQABoMNjM3NDIzMTgzODA1IgzThPaALHCrTZfPWloq3AOMt%2BvXpnFSvGULiRhmjRHvcbhl2bo0exwr6Zsg4khf3KfgWBDfTv%2BgU46TTWtiu40Zd%2FiE8RUW0peRwRVOAGdjZFZb2m3F9NBzD3DWs0TF5%2BZRegf4RaS8Hnyngmi1cKyN9tkcWS6BlCRLA%2FXHHFVRnEim2Jjx%2B8AiaTO2XtimyRpjTMLzstwHZ4wBeusMLSgK88lYKiaBQ0Dukzcex%2FG1voQY4zSYefwNx6KqQHMP7A4UpOh%2FpZKBndWnShk%2BEf2cQoo3huT3xKaZvaeVzlCaac0ImBTJfRowTGJo6wu7yEN%2BONw4RlEheIRuJdI9%2FresqVDxP4MZzSe%2FkcPMMPicCa6EiQfJCMkOpAhIdndMYm7eFKZtJsdEUrhRIym30B%2BQX5%2Bmf%2BUAcnFNB04m4auND%2BGRUXIodYwGCuZcAHe0uGNwbvvRaeEfxKzcwJ4y48UqEhl9R8yChKj%2Fm3gIY6ykhq%2B1hGiV6jO2sfpdJ3TlGVeZrU5jKWBnnI7TIpv%2Bxj7V7skn6R898xcBTiO25Xc9hbU7ktE3n3M9pb6ASb2oNaeSb8oBuYqm5iT0UQ4TdaGXjkBD21usBBCbBhD6rJHz5zivLbEz8%2BU9YTLpVV1jzWnW9szZNIIFV%2FV6NjDxlqPOBjqkAbvZgXXGmkG9OJA3kbmKjqzMFoj3657rqLL2YXlHizGKLRKPd6wcOCfhZbi%2BbE9Hp8S1h6h8MVTJUWH%2BPl7zQ9uk8TjLoLb3x7PfJpmL1%2BnpzE%2FiVHioFJMmYZR5LRuukpjWSYu9gQ%2Fpi6tCxOHX1BcLg7t1aAZKYLuU2aIuX%2FYYXW0hyZAj%2BGSq8fzoarUzHBiN7yZ95QojpuULcqsOAFjC5uAD&X-Amz-Signature=133dd9e876e75e81ca19d86a49aeb4b13150f707f308cb2dce8cf8327f9bfc99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)