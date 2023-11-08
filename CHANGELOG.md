## 0.3.1 (2023-11-08)

### Fix

- **deps**: allow every 0.* version of mongoflex to be used together

## 0.3.0 (2023-08-30)

### Feat

- add utility function to connect to mongo
- add utility function mongourl_replace
- add media processing config model

### Fix

- entrypoint to work with `with`

## 0.2.1 (2023-08-21)

### Refactor

- allow to import models from top level module

## 0.2.0 (2023-08-21)

### Feat

- use distinct client name on models to allow usage with other systems

## 0.1.0 (2023-08-21)

### Feat

- add Entrypoint utility class
- dockerize and add cron for cra shard keys
- add job to flip shard keys for cra aliases

### Fix

- collection cra name
