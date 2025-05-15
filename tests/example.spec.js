// @ts-check
import { test, expect } from '@playwright/test';

test('first test', async ({ page }) => {
  // Открытие веб-страницы
  await page.goto('https://example.com');

  // Проверка заголовка на наличие слова "Example"
  await expect(page).toHaveTitle(/Example/);

  // Поиск элемента и клик
  await page.click('a:has-text("More information")');

  // Проверка, что произошло перенаправление на необходимый URL
  await page.waitForURL('https://www.iana.org/help/example-domains')
});

