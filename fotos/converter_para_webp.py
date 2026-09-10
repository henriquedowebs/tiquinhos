import glob
import os
from PIL import Image

def convert_to_webp(folder_path):
    print(f"Buscando imagens em {folder_path}...")
    
    # Encontra todos os arquivos de imagem suportados
    images = []
    for ext in ('*.jpg', '*.jpeg', '*.png'):
        images.extend(glob.glob(os.path.join(folder_path, ext)))
        
    if not images:
        print("Nenhuma imagem para converter.")
        return

    converted_count = 0
    for file_path in images:
        try:
            webp_path = file_path.rsplit('.', 1)[0] + '.webp'
            if not os.path.exists(webp_path):
                img = Image.open(file_path)
                img.save(webp_path, 'webp')
                print(f"Convertido: {os.path.basename(file_path)} -> {os.path.basename(webp_path)}")
                converted_count += 1
            else:
                print(f"Já existe: {os.path.basename(webp_path)}")
        except Exception as e:
            print(f"Erro ao converter {os.path.basename(file_path)}: {e}")

    print(f"Concluído! {converted_count} imagens convertidas.")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    convert_to_webp(current_dir)
