import hashlib
from . import BlockMetadata

class Block:

    def __init__(self, metadata):
        self.index = metadata.index
        self.previous_hash = params.previous_hash
        self.timestamp = params.timestamp
        self.data = params.data
        self.hash = self.calc_hash()

    def metadata(self):
        return BlockMetadata.BlockMetadata(
            self.index,
            self.previous_hash,
            self.timestamp,
            self.data
        )
