from typing import NewType

from .metadata import CMCMetadataSchema

CMCMetadataResponse = NewType("CMCMetadataResponse", dict[str, CMCMetadataSchema])
