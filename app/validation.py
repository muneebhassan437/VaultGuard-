from pydantic import BaseModel, Field

class TransactionInput(BaseModel):
    amount: float = Field(min=0, max=1e7, description="Transaction amount", example=1000)
    dest_prev_amount_sum: float = Field(min=0, description="Sum of previous amounts for the destination account", example=50000)
    dest_prev_txn_count: int = Field(min=0, description="Count of previous transactions for the destination account", example=5)
    dest_txn_count_24h: int = Field(min=0, description="Count of transactions for the destination account in the last 24 hours", example=2)
    type: str = Field(description="Type of transaction", example="TRANSFER")
    is_night: int = Field(ge=0, le=1, description="Flag indicating if the transaction occurred at night (1 for yes, 0 for no)", example=0)
    dest_is_first_txn: int = Field(ge=0, le=1, description="Flag indicating if this is the first transaction for the destination account (1 for yes, 0 for no)", example=0)
    amount_1M_to_10M: int = Field(ge=0, le=1, description="Flag indicating if the amount is between 1M and 10M (1 for yes, 0 for no)", example=0)
    amount_is_10M: int = Field(ge=0, le=1, description="Flag indicating if the amount is 10M or more (1 for yes, 0 for no)", example=0)
 