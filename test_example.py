from playwright.sync_api import sync_playwright, expect

def test_google_homepage():
    # Test otevře stránku Google a ověří, že se správně načetla 
    with sync_playwright() as p:
        # Spustí prohlížeč 
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Otevře Google
        page.goto("https://www.google.com/")
        
        # Přijme cookies
        if page.locator("Přijmout vše").is_visible():
            page.click("Přijmout vše")

        # Ověří, že se stránka správně načetla podle titulku
        expect(page).to_have_title("Google")

        # Zavře prohlížeč
        browser.close()
    
def test_wikipedia_homepage():
    #Zjistí jestli má stránka v nadpisu 'Wikipedia'
    with sync_playwright() as p:
        # Spustí prohlížeč
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Otevře Wikipedii
        page.goto("https://www.wikipedia.org/")


        # Ověří, že stránka má v nadpisu Wikipedia
        expect(page.locator('h1')).to_contain_text("Wikipedia")

        # Zavře prohlížeč
        browser.close()
      
def test_set_language_to_czech():
    #Test nastaví jazyk Wikipedie na češtinu
    with sync_playwright() as p:
        # Spustí prohlížeč
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Otevře hlavní stránku
        page.goto("https://www.wikipedia.org/")
        
        # Klikne češtinu
        page.click('a#js-link-box-cs')
        
        # Ověří, že se stránka načetla v češtině
        expect(page).to_have_url("https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana")
        expect(page.locator('h1')).to_contain_text("Hlavní strana")
        
        # Zavře prohlížeč
        browser.close()