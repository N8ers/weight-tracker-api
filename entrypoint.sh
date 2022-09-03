
#!/usr/bin/env bash
# flask --app tracker db init
echo "entrypoint.sh file started..."

flask --app tracker db upgrade
echo "db upgraded"

echo "starting flask server..."
flask run --host=0.0.0.0