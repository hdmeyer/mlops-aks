import os
import mlflow
from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository

def get_model_from_mlflow_registry(model_name:str, stage: str, dst_path: str) -> None:

    mlflow.set_tracking_uri("databricks")
    os.makedirs(dst_path, exist_ok=True)
    client = mlflow.MlflowClient()
    print(client.get_latest_versions(model_name))
    #local_path = mlflow.artifacts.download_artifacts(artifact_uri=f"models:/{model_name}/{stage}", dst_path=dst_path)
    # local_path = ModelsArtifactRepository(
    #     f"models:/{model_name}/{stage}").download_artifacts("", dst_path=dst_path)
    print(f'{stage} Model {model_name} is downloaded at {local_path}')


def main():
    model_name = "employee_attrition"
    stage = "Staging"
    dst_path = f"../service/{model_name}_model"
    get_model_from_mlflow_registry(model_name, stage, dst_path)

if __name__ == "__main__":
    main()
