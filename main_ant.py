#!/home/gmorey/Downloads/Repositorios_GitHub/TP/tpfinal/bin/python
# main.py

from tp_utils import *
from my_data.my_requests.coinApi_symbols                import COIN_API_SYMBOLS
from my_data.my_manager_objects.list_manager_symbols    import SymbolManager
from plot_shower_class import PlotShower



# Set up logging
logger = setup_logging()

# Create the Tkinter root window and run the GUI
if __name__ == "__main__":
    logging.info('Main Starting...')
    #Coin_Api
    coin_Api_Key='4B82844F-2761-494A-A92F-DC0C8EB93910'
#    coin_Api_Key='4B82844F-2761-494A-A92F-DC0C8EB93910'
    # Crear instancias y utilizar métodos específicos
    coin_api_symbols = COIN_API_SYMBOLS(coin_Api_Key)
    Symbol_Manager_Coin_Api = SymbolManager(coin_api_symbols)
    Symbol_Manager_Coin_Api.load_symbols()
    Symbol_Manager_Coin_Api.listIDs()
    print(Symbol_Manager_Coin_Api.cantidad())

    # Now you can use global_data to make specific requests
    # For example, if you need a key from global data to make another request:
    # specific_data = api_handler.get_data("specific_endpoint", params={"key": global_data["endpoint1"]["key"]})
    #if specific_data:
    #    print("Specific Data:", specific_data)

    root = create_tkinter_root()
    app = PlotShower(root)
    root.mainloop()
