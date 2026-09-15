# Проект (Electric Bikes)

Короткая инструкция по подготовке и публикации этого Django-проекта на GitHub.

1) Создать и активировать виртуальное окружение:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2) Установить зависимости и сгенерировать точный `requirements.txt`:

```powershell
pip install -r requirements.txt
# Или пока нет точного файла:
pip install Django Pillow
pip freeze > requirements.txt
```

3) Миграции и статика:

```powershell
python manage.py migrate
python manage.py collectstatic --noinput
```

4) Локальный запуск:

```powershell
python manage.py runserver
```

5) Инициализация Git и публикация на GitHub:

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo>.git
git push -u origin main
```

Что уже сделано: добавлен `.gitignore` (игнорирует `venv/`, `db.sqlite3`, `media/` и IDE-папки).

Если нужно, могу автоматически создать репозиторий на GitHub и запушить (попросит токен).
