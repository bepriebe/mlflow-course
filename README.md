# MLflow course

Repository for the Liora MLflow course exercises.

## Local environment

The exercises were tested with the system Python 3.12 interpreter and MLflow
2.12.2. The project uses a local virtual environment so that the course
dependencies stay next to the repository. The environment directory is named
`env_mlflow` and is intentionally excluded from version control.

```bash
cd mlflow-course
python3 -m pip install --user virtualenv
/usr/bin/virtualenv --python=/usr/bin/python3 env_mlflow
source env_mlflow/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The activation changes `python` and `pip` to the project-local executables:

```bash
which python
python --version
python -m pip --version
```

These commands should report paths below `mlflow-course/env_mlflow/` and Python
3.12. To leave the environment again, run:

```bash
deactivate
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

## MLflow Project

The same experiment can be launched through the `MLproject` definition while
using the already activated environment:

```bash
mlflow run . --env-manager local --experiment-name Apple_Models
```

The tracking server at `http://127.0.0.1:8080` must be running before starting
the project.

## Serve a registered model

To expose version 1 of the registered model as a local REST API, start a second
MLflow process. The tracking URI must be exported because this command runs in
a separate process:

```bash
export MLFLOW_TRACKING_URI=http://127.0.0.1:8080
mlflow models serve \
  --model-uri "models:/AppleDemandModel/1" \
  --host 127.0.0.1 \
  --port 5002 \
  --env-manager local
```

With that process running, test the endpoint from another terminal:

```bash
python src/07_test_api.py
```
