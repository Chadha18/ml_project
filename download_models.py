import os
import gdown

models = {
    'best_model_knn_phi.pkl': '1tde9yEjIeufkXNlyHesxIgWpDhuu2zja',
    'best_model_knn_sw.pkl':  '1KzIKAuDF68MCk0tkDrzGwcbPdbUDk81Z',
    'best_model_rf_phi.pkl':  '1Y6BJ3cJjOs03lL469Nfowr9iUFaUr5pJ',
    'best_model_rf_sw.pkl':   '1qP1m99U3bZqeuzKa5j5YxfaKnkRZG2Wb',
    'best_model_xgb_phi.pkl': '1BTuBL2ohotR52XtWMjYQdK4wpQgck7N_',
    'best_model_xgb_sw.pkl':  '1F5Sco-oR48cLlck93ccZDdOnNwERXqG2',
}

def download_models():
    for filename, file_id in models.items():
        if not os.path.exists(filename):
            print(f"Downloading {filename}...")
            gdown.download(f"https://drive.google.com/uc?id={file_id}", filename, quiet=False)
        else:
            print(f"✅ {filename} already exists")