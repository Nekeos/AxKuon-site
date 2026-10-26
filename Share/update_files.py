import os
import json
from datetime import datetime

# Папка, где лежит скрипт (Share)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, 'files.json')

# Игнорируемые файлы (не показываем их в списке)
IGNORE = ['index.html', 'files.json', 'update_files.py', '.git', '.DS_Store', 'desktop.ini', 'Thumbs.db']

files = []

for filename in os.listdir(BASE_DIR):
    if filename in IGNORE or filename.startswith('.'):
        continue
    
    filepath = os.path.join(BASE_DIR, filename)
    
    if os.path.isfile(filepath):
        size = os.path.getsize(filepath)
        # Время последнего изменения файла
        mtime = os.path.getmtime(filepath)
        date = datetime.fromtimestamp(mtime).isoformat() + 'Z'
        
        files.append({
            'name': filename,
            'url': filename,
            'size': size,
            'date': date
        })

# Сортируем по дате (новые сверху)
files.sort(key=lambda x: x['date'], reverse=True)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(files, f, ensure_ascii=False, indent=2)

print(f"✅ Обновлено! Найдено файлов: {len(files)}")
print(f"📄 Сохранено в: {OUTPUT_FILE}")
