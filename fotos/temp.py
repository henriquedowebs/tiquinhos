from playwright.sync_api import sync_playwright
import urllib.request
import os

target_dir = r"d:\ANTIGRAVITY PROJETOS\TESTE\my-first-project\Projetos\Tiquinhos Pet\fotos"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.google.com/search?q=tiquinhos+pet+guarulhos')
        page.wait_for_timeout(3000)
        
        # Extract images from knowledge panel
        imgs = page.evaluate('''
            Array.from(document.querySelectorAll('img')).map(i => i.src).filter(src => src && (src.includes('encrypted-tbn0.gstatic.com') || src.includes('lh3.googleusercontent.com') || src.startsWith('data:image')))
        ''')
        
        print(f"Found {len(imgs)} images.")
        count = 0
        for i, src in enumerate(imgs):
            try:
                filepath = os.path.join(target_dir, f"google_photo_scrape_{i}.jpg")
                if src.startsWith('data:image'):
                    import base64
                    header, encoded = src.split(",", 1)
                    with open(filepath, "wb") as f:
                        f.write(base64.b64decode(encoded))
                    count += 1
                else:
                    req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
                    img_data = urllib.request.urlopen(req).read()
                    with open(filepath, "wb") as f:
                        f.write(img_data)
                    count += 1
            except Exception as e:
                pass
        print(f"Downloaded {count} images successfully.")
        browser.close()

if __name__ == '__main__':
    run()
