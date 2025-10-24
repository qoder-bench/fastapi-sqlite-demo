export PATH := join(justfile_directory(), ".venv", "bin") + ":" + env_var('PATH')
db_url := "sqlite:///db/demo.sqlite3"

# start server
start:
    python3 -m uvicorn app.main:app --reload

# generate sqlmodels from database
gen-sqlmodels:
    sqlacodegen --generator sqlmodels --outfile app/domain/models.py --tables "hero" "{{ db_url }}"

