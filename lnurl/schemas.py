from pydantic import BaseModel, HttpUrl

class ResponseErrorSchema(BaseModel):
    status: str = "ERROR"
    reason: str

class WithdrawRequestSchema(BaseModel):
    tag: str = "withdrawRequest"
    callback: HttpUrl
    k1: str
    minWithdrawable: int
    maxWithdrawable: int

class PayRequestSchema(BaseModel):
    tag: str = "payRequest"
    callback: HttpUrl
    maxSendable: str
    minSendable: str
    metadata: str