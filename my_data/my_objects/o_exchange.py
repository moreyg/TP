'''
    Ejemplo de EXCHANGE
  {
    "exchange_id": "BINANCE",
    "website": "https://www.binance.com/",
    "name": "Binance",
    "data_quote_start": "2017-12-18T00:00:00.0000000Z",
    "data_quote_end": "2023-12-07T00:00:00.0000000Z",
    "data_orderbook_start": "2017-12-18T21:50:58.3910192Z",
    "data_orderbook_end": "2023-07-07T00:00:00.0000000Z",
    "data_trade_start": "2017-07-14T00:00:00.0000000Z",
    "data_trade_end": "2023-12-07T00:00:00.0000000Z",
    "data_symbols_count": 2408,
    "volume_1hrs_usd": 536537842.66,
    "volume_1day_usd": 15973843145.87,
    "volume_1mth_usd": 379464250886.64
  }
  '''
  class O_Exchange(O_Generic):
    def some_abstract_method(self):
        # Implementación específica para O_Exchange
        pass
