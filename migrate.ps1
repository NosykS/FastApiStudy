# migrate.ps1
echo "Checking for pending migrations..."
alembic check
if ($LASTEXITCODE -ne 0) {
    echo "Warning: Models and migrations are out of sync!"
}

echo "Running Alembic migrations..."
alembic upgrade head