from pydantic import BaseModel
from typing import List


class Currency(BaseModel):
    code: str
    count: int
    name: str
    price: float


class DatedCurrency(BaseModel):
    date: str
    count: int
    price: float


class CurrencyForPeriod(BaseModel):
    code: str
    name: str
    currencies: List[DatedCurrency]


class Metal(BaseModel):
    code: str
    name: str
    price: float


class DatedMetal(BaseModel):
    date: str
    price: float


class MetalForPeriod(BaseModel):
    code: str
    name: str
    metals: List[DatedMetal]


class Company(BaseModel):
    ticker: str
    name: str


class DatedCandle(BaseModel):
    date: str
    close: float
    volume: int
