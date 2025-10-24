db_url := "sqlite:///./demo.sqlite3"

gen-sqlmodels:
    sqlacodegen --generator sqlmodels --outfile app/domain/models.py --tables "hero" "{{ db_url }}"
