# Data Manager

Sistema Central de Gerenciamento de Dados.

## Instalação

Para instalar esse repositório como dependencia é necessário ter configurado localmente uma chave ssh com acesso a esse repositório.

```bash
pip install git+ssh://github.com/palverdata/data-manager.git@0.3.0
```

Observação: caso o app que usa esse repositorio como depencia rode dentro de uma imagem de container, é necessário buildar a imagem usando uma chave ssh com acesso a esse repositório.

Para configurar olhe os repositórios:

1. [News Crawler](https://github.com/palverdata/news-crawler/)
2. [WhatsApp Data Palver](https://github.com/palverdata/whatsapp-data-palver/commit/20846503337c25186a09f4b54872d72b2594e629)

## Uso

Para usar a lib é necessário criar uma conexão no mongo na collection `data_manager`. Por padrão a função `connect` vai alterar o nome do banco na url antes de conectar, caso queira desabilitar esse comportamento basta passar o parâmetro `ignore_database_name` como `True`.

```python
from data_manager.connection import connect

connect("mongodb://localhost:27017/database_name")
```
> this will connect to mongodb://localhost:27017/**data_manager**

Fazendo isso basta usar os models disponíveis.

```python
from data_manager.models import MediaProcessingConfig

config = MediaProcessingConfig.find_one({"source": "whatsapp.message_media"})

>>> config.solr_collection
"whatsapp_messages"

>>> config.mongo_collection
"palver_whatsapp.messages"

>>> config.primary_key
"id"
```
