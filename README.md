# MLflow course

Repository for the Liora MLflow course exercises.

## Local environment

The exercises were tested with Python 3.12 and MLflow 2.12.2. The project uses a
local virtual environment so that the course dependencies stay next to the
repository.

```bash
cd mlflow-course
python3 -m venv env_mlflow
source env_mlflow/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Check the installation:

```bash
mlflow --version
python -m pip check
```

The tracking examples expect an MLflow server at `http://127.0.0.1:8080`.
Start it in a separate terminal from the project directory:

```bash
source env_mlflow/bin/activate
mlflow server --host 127.0.0.1 --port 8080
```

Then run the tracking example from the repository root:

```bash
python src/experiment.py
```
