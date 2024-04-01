# google-tradutor-cli

Google Tradutor de terminal

## Como Usar

Instale todos os pacotes necessários com `pip install -r requirements.txt`

Por padrão traduz do Inglês para o Português (Brasil), exemplo:

```
> python gtcli.py "Hello World"
Olá Mundo
```

Passe o argumento `-d` para especificar para qual idioma será traduzido:

```
> python gtcli.py "Teste" -d en
Test
```
