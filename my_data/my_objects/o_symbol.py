'''
    Type	symbol_id pattern
    SPOT	{exchange_id}_SPOT_{asset_id_base}_{asset_id_quote}
    FUTURES	{exchange_id}_FTS_{asset_id_base}_{asset_id_quote}_{YYMMDD of future_delivery_time}
    OPTION	{exchange_id}_OPT_{asset_id_base}_{asset_id_quote}_{YYMMDD of option_expiration_time}_{option_strike_price}_{option_type_is_call as C/P}
    PERPETUAL	{exchange_id}_PERP_{asset_id_base}_{asset_id_quote}
    INDEX	{exchange_id}_IDX_{index_id}
    CREDIT	{exchange_id}_CRE_{asset_id_base}
    CONTACT	{exchange_id}_COT_{contract_id}

    EJEMPLO 1 DE SYMBOL INFO

  {
    "symbol_id": "BITSTAMP_SPOT_BTC_USD",
    "exchange_id": "BITSTAMP",
    "symbol_type": "SPOT",
    "asset_id_base": "BTC",
    "asset_id_quote": "USD",
    "data_start": "2011-09-13",
    "data_end": "2023-12-07",
    "data_quote_start": "2014-02-24T00:00:00.0000000Z",
    "data_quote_end": "2023-12-07T00:00:00.0000000Z",
    "data_orderbook_start": "2014-02-24T17:43:05.0000000Z",
    "data_orderbook_end": "2023-07-06T00:00:00.0000000Z",
    "data_trade_start": "2011-09-13T00:00:00.0000000Z",
    "data_trade_end": "2023-12-07T00:00:00.0000000Z",
    "volume_1hrs": 49.64863342,
    "volume_1hrs_usd": 2161664.79,
    "volume_1day": 1582.56516325,
    "volume_1day_usd": 68903717.03,
    "volume_1mth": 49929.25473874,
    "volume_1mth_usd": 2173882832.7,
    "price": 43538.5,
    "symbol_id_exchange": "BTCUSD",
    "asset_id_base_exchange": "BTC",
    "asset_id_quote_exchange": "USD",
    "price_precision": 1.0,
    "size_precision": 1e-08
  }

    EJEMPLO 2 DE SYMBOL INFO
  {
    "symbol_id": "BYBITUSDC_PERP_SWEAT_USD",
    "exchange_id": "BYBITUSDC",
    "symbol_type": "PERPETUAL",
    "asset_id_base": "SWEAT",
    "asset_id_quote": "USD",
    "future_contract_unit": 1.0,
    "future_contract_unit_asset": "SWEAT",
    "symbol_id_exchange": "SWEATPERP",
    "asset_id_base_exchange": "SWEAT",
    "asset_id_quote_exchange": "USD"
  }
    EJEMPLO DE SYMBOL DATA
{
    "symbol_id": "BINANCE_SPOT_BTC_USDT",
    "time_exchange": "2023-01-02T00:00:00.8086162Z",
    "time_coinapi": "2023-01-02T00:00:00.8086162Z",
    "ask_price": 16617.52,
    "ask_size": 0.03423,
    "bid_price": 16617.03,
    "bid_size": 0.02001
  },
  {
    "symbol_id": "BINANCE_SPOT_BTC_USDT",
    "time_exchange": "2023-01-02T00:00:00.8086281Z",
    "time_coinapi": "2023-01-02T00:00:00.8086281Z",
    "ask_price": 16617.52,
    "ask_size": 0.03423,
    "bid_price": 16617.04,
    "bid_size": 0.00942
  },
  {
    "symbol_id": "BINANCE_SPOT_BTC_USDT",
    "time_exchange": "2023-01-02T00:00:00.8086338Z",
    "time_coinapi": "2023-01-02T00:00:00.8086338Z",
    "ask_price": 16617.52,
    "ask_size": 0.08188,
    "bid_price": 16617.04,
    "bid_size": 0.00942
  }


  '''
from .o_generic import O_Generic

class O_Symbol(O_Generic):

    def some_abstract_method(self):
        # Implementación específica para O_Symbol
        pass

