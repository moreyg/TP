
'''
    EJEMPLO DE ASSET
  {
    "asset_id": "USD",
    "name": "US Dollar",
    "type_is_crypto": 0,
    "data_quote_start": "2014-02-24T00:00:00.0000000Z",
    "data_quote_end": "2023-12-07T00:00:00.0000000Z",
    "data_orderbook_start": "2014-02-24T17:43:05.0000000Z",
    "data_orderbook_end": "2023-07-07T00:00:00.0000000Z",
    "data_trade_start": "2010-07-17T00:00:00.0000000Z",
    "data_trade_end": "2023-12-07T00:00:00.0000000Z",
    "data_symbols_count": 220523,
    "volume_1hrs_usd": 1110405592136.49,
    "volume_1day_usd": 20611359250760.62,
    "volume_1mth_usd": 1379017163014976.8,
    "id_icon": "0a4185f2-1a03-4a7c-b866-ba7076d8c73b",
    "data_start": "2010-07-17",
    "data_end": "2023-12-07"
  }
  '''
  class O_Asset(O_Generic):
    def some_abstract_method(self):
        # Implementación específica para O_Asset
        pass
