import time
import os
import urllib.request
from playwright.sync_api import sync_playwright

def run():
    target_dir = r"d:\ANTIGRAVITY PROJETOS\TESTE\my-first-project\Projetos\Tiquinhos Pet\fotos"
    os.makedirs(target_dir, exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        images_found = set()
        
        # Intercept network requests to capture images
        def handle_response(response):
            if response.request.resource_type == "image":
                url = response.url
                if "lh5.googleusercontent.com/p/" in url or "lh3.googleusercontent.com/p/" in url:
                    # Strip any size parameters to get full resolution if possible, or just keep it
                    images_found.add(url)
                    
        page.on("response", handle_response)
        
        print("Navigating to Google Search...")
        page.goto("https://www.google.com/search?q=tiquinhos+pet&rlz=1C1HKFL_enBR1220BR1220&oq=tiqui&gs_lcrp=EgZjaHJvbWUqCAgAEEUYJxg7MggIABBFGCcYOzIICAEQRRgnGDsyBggCEEUYOTIGCAMQRRg7Mg0IBBAAGIMBGLEDGIAEMgYIBRBFGDwyBggGEEUYPDIGCAcQRRg80gEIMTA4M2owajeoAgCwAgA&sourceid=chrome&source=chrome.ob&ie=UTF-8")
        time.sleep(3)
        
        print("Looking for photo gallery link...")
        # Try to click on the main photo or "Ver fotos" in the knowledge panel
        try:
            # Click the main image in knowledge panel
            page.click("g-img.BA0A6c", timeout=3000)
            time.sleep(3)
        except:
            pass
            
        print("Scrolling to load more images...")
        for _ in range(5):
            page.mouse.wheel(0, 1000)
            time.sleep(1)
            
        browser.close()
        
        print(f"Found {len(images_found)} images. Downloading...")
        
        count = 0
        for i, url in enumerate(images_found):
            try:
                # Some URLs might need =s1600 appended to get larger size
                if "=" in url:
                    url = url.split("=")[0] + "=s800"
                
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                img_data = urllib.request.urlopen(req).read()
                
                filepath = os.path.join(target_dir, f"google_photo_{i}.jpg")
                with open(filepath, "wb") as f:
                    f.write(img_data)
                count += 1
            except Exception as e:
                print(f"Failed to download {url}: {e}")
                
        print(f"Downloaded {count} photos successfully.")

if __name__ == "__main__":
    run()
