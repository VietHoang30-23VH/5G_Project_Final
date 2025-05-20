import pandas as pd
import logging
from sqlalchemy import create_engine

# Thiết lập logging
logger = logging.getLogger('Database')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] %(message)s', "%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Kết nối tới SQLite database
engine = create_engine('sqlite:///5g_monitor.db')

# Hàm load dữ liệu từ bảng raw_network_traffic
def load_raw_network_traffic():
    try:
        df = pd.read_sql_table('raw_network_traffic', con=engine)
        return df
    except Exception as e:
        logger.error(f"Lỗi khi load dữ liệu raw_network_traffic: {str(e)}")
        return pd.DataFrame()  # Trả về DataFrame rỗng nếu lỗi

# Hàm load dữ liệu từ bảng processed_network_traffic
def load_processed_network_traffic():
    try:
        df = pd.read_sql_table('processed_network_traffic', con=engine)
        return df
    except Exception as e:
        logger.error(f"Lỗi khi load dữ liệu processed_network_traffic: {str(e)}")
        return pd.DataFrame()  # Trả về DataFrame rỗng nếu lỗi
