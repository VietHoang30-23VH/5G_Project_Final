from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, insert, select
import hashlib

# Tạo kết nối đến cơ sở dữ liệu SQLite
engine = create_engine('sqlite:///users.db')
metadata = MetaData()

# Định nghĩa bảng users
users = Table('users', metadata, 
    Column('id', Integer, primary_key=True),
    Column('username', String, unique=True),
    Column('password', String),
)

# Tạo bảng nếu chưa tồn tại
metadata.create_all(engine)

# Thêm người dùng mẫu khi chưa có người dùng nào trong DB
def init_users():
    conn = engine.connect()
    result = conn.execute(select(users))
    user_exists = result.fetchone()
    if not user_exists:
        # Mã hóa mật khẩu bằng sha256
        conn.execute(insert(users).values(
            username='viethoang',
            password=hashlib.sha256('22520471'.encode()).hexdigest()
        ))
        conn.execute(insert(users).values(
            username='bacan',
            password=hashlib.sha256('22520143'.encode()).hexdigest()
        ))
        conn.commit()
    conn.close()

# Khởi tạo người dùng mẫu
init_users()