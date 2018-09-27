import uuid 

class Transaction():
    def __init__(self, timestamp, source):
        self.timestamp = timestamp
        self.source = source
        self.id = uuid.uuid4().hex[0:10]

        self.pool_block_timestamp = None
        self.main_chain_timestamp = None
        self.finalization_timestamps = None

    def set_pool_block_timestamp(self, pool_block_timestamp):
        self.pool_block_timestamp = pool_block_timestamp

    def set_main_chain_arrival_timestamp(self, main_chain_timestamp):
        self.main_chain_timestamp = main_chain_timestamp

    def add_finalization_timestamp(self, finalization_timestamp):
        if self.finalization_timestamps is None:
            self.finalization_timestamps = []
        self.finalization_timestamps.append(finalization_timestamp)

class Proposal():
    def __init__(self, timestamp, proposal_type ='tree'):
        self.timestamp = timestamp
        self.id = uuid.uuid4().hex[0:6]
        self.proposal_type = proposal_type

    def set_block(self, block):
        self.block = block
