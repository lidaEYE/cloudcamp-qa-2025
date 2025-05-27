import pytest
from playwright.sync_api import sync_playwright

def test_example_domain_redirect():
    with sync_playwright() as p:
        # Запуск браузера (можно изменить на 'chromium' или 'webkit')
        browser = p.chromium.launch()
        page = browser.new_page()
        
        try:
            # Установка таймаута (60 секунд)
            page.set_default_timeout(60000)
            
            # Открытие веб-страницы
            page.goto('https://example.com')
            
            # Проверка заголовка
            assert "Example" in page.title()
            
            # Клик по ссылке
            page.click('a:has-text("More information")')
            
            # Проверка URL
            assert "iana.org/help/example-domains" in page.url()
            
            # Проверка финального URL с учетом особенностей WebKit
            final_url = page.url()
            if p.browser.name == 'webkit':
                if final_url != 'https://www.iana.org/help/example-domains':
                    pytest.warns(UserWarning, f"WebKit: редирект на '{final_url}' вместо 'https://...'")
            else:
                assert final_url == 'https://www.iana.org/help/example-domains'
                
        finally:
            browser.close()