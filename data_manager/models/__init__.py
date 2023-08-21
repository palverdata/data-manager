from mongoflex import Model as BaseModel

CLIENT_NAME = "data_manager"


class Model(BaseModel):
    class Meta:
        client_name = CLIENT_NAME
