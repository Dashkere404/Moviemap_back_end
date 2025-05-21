import os
import gdown

def download_with_gdown(file_id, output_path):
    if os.path.exists(output_path):
        print(f"✅ {output_path} уже существует. Пропускаю загрузку.")
        return True

    try:
        url = f"https://drive.google.com/uc?id={file_id}"
        print(f"📥 Начинаю загрузку: {output_path}")
        gdown.download(url, output_path, quiet=False, fuzzy=True)
        print(f"✅ Загрузка завершена: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Ошибка при загрузке файла {output_path}: {e}")
        return False

def main():
    os.makedirs("data", exist_ok=True)

    # ID файлов из Google Drive
    csv_downloaded = download_with_gdown("14DgwFqU7KtCNd-FX99AYFFVfw-MDJLtB", "data/ratings.csv")
    pkl_downloaded = download_with_gdown("12elbhNAR7NA3U_aMj7-__nKXENNJPz76", "data/fasttext_tfidf_cosine.pkl")

    if csv_downloaded and pkl_downloaded:
        print("🎉 Все файлы готовы — можно запускать FastAPI!")
    else:
        print("⚠️ Один или несколько файлов не загружены — сервер может работать некорректно.")

main()