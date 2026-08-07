!pip install gspread
import gspread
from google.colab import auth
from google.auth import default
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)
sheet_id = '1N2QkvkYJN9LpBNkQXz_Xm0dWTL5m5IvZP7EubA6bzEg'  
sh = gc.open_by_key(sheet_id)
worksheet = sh.sheet1
client_data = ["Алексей", "500", "+7-999-123-45-67", "2026-08-07"]
worksheet.append_row(client_data)
print("✅ Данные успешно добавлены в таблицу!")
