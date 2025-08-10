import os

# Define directory structure
structure = {
    "iris-mlops": [
        "data/iris.csv",
        "src/data_preprocessing.py",
        "src/train_model.py",
        "src/predict.py",
        "api/main.py",
        "models/",
        "logs/prediction_logs.db",
        "Dockerfile",
        "requirements.txt",
        "README.md",
        ".github/workflows/ci-cd.yml"
    ]
}

def create_project_structure(base_structure):
    for root_dir, paths in base_structure.items():
        print(f"Creating project root: {root_dir}")
        os.makedirs(root_dir, exist_ok=True)
        for path in paths:
            full_path = os.path.join(root_dir, path)
            if path.endswith("/"):
                os.makedirs(full_path, exist_ok=True)
                print(f"  - Created directory: {full_path}")
            else:
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, "w") as f:
                    f.write("")  # Create empty file
                print(f"  - Created file: {full_path}")

if __name__ == "__main__":
    create_project_structure(structure)
