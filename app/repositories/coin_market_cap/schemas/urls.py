from pydantic import BaseModel, Field


class CMCUrlsSchema(BaseModel):
    website: list[str] = Field(example=["https://api.nomics.com/v1"])
    technical_doc: list[str] = Field(
        example=["https://github.com/ethereum/wiki/wiki/White-Paper"]
    )
    twitter: list[str] = Field(example=["https://twitter.com/ethereum"])
    reddit: list[str] = Field(example=["https://reddit.com/r/ethereum"])
    message_board: list[str] = Field(
        example=["https://bitcointalk.org/index.php?topic=428589.0"]
    )
    chat: list[str] = Field(example=["https://gitter.im/orgs/ethereum/rooms"])
    explorer: list[str] = Field(
        example=[
            "https://blockchain.coinmarketcap.com/chain/ethereum",
            "https://etherscan.io/",
            "https://ethplorer.io/",
        ]
    )
    source_code: list[str] = Field(example=["https://github.com/ethereum"])
