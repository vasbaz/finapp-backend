from pydantic import BaseModel


class CMCPlatform(BaseModel):
    id = int
    name = str
    symbol = str
    slug = str
    token_address = str
