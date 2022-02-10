from pydantic import BaseModel, Field


class CMCPlatformSchema(BaseModel):
    id: int = Field(example=1027)
    name: str = Field(example="Ethereum")
    symbol: str = Field(example="ETH")
    slug: str = Field(example="ethereum")
    token_address: str = Field(example="0xdac17f958d2ee523a2206206994597c13d831ec7")
