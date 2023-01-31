# google-translator-cli

Google Translator that works in terminal

## How to use

Install all requirements with `pip install -r requirements.txt`

By default translates from English to Portuguese, example:

```
> python gtcli.py "Hello World"
Olá Mundo
```

Can pass `-d` to specify the output language:

```
> python gtcli.py "Teste" -d en
Test
```
