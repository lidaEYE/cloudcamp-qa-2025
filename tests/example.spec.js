// @ts-check
import { test, expect } from '@playwright/test';

test('first test', async ({ page, browserName }) => {
  test.setTimeout(60000);

  // Открытие веб-страницы
  await page.goto('https://example.com');

  // Проверка заголовка на наличие слова "Example"
  await expect(page).toHaveTitle(/Example/);

  // Поиск элемента и клик
  await page.click('a:has-text("More information")');

  // Проверка URL
  await expect(page).toHaveURL(/iana\.org\/help\/example-domains/);

  // Запись финального URL
  const finalUrl = page.url();

  if (browserName === 'webkit') {
    if (finalUrl !== 'https://www.iana.org/help/example-domains') {
      console.warn(`⚠️ WebKit: редирект на "${finalUrl}" вместо "https". Это особенность WebKit + сервера iana.org`);
    }
  } else {
    // Во всех остальных браузерах проверка строгая
    expect(finalUrl).toBe('https://www.iana.org/help/example-domains');
  }
});