
#!/usr/bin/env bash
flask --app tracker db init
flask --app tracker db upgrade
flask run --host=0.0.0.0