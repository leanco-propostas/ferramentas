from pathlib import Path
from playwright.sync_api import sync_playwright
html=Path('/mnt/data/Master_Hub_v12_Integrado.html').read_text(encoding='utf-8')
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 pg=b.new_page(viewport={'width':1366,'height':768}); pg.set_default_timeout(3000)
 errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
 print('set content'); pg.set_content(html,wait_until='domcontentloaded',timeout=15000); pg.wait_for_timeout(200)
 print('boot',pg.locator('[data-module]').count(),errs)
 for mod in ['revenue','credit','extra','bands','executive','customer']:
  print('click',mod); pg.locator(f'[data-module="{mod}"]').click(); pg.wait_for_timeout(100); print('h1',pg.locator('h1').first.inner_text() if pg.locator('h1').count() else 'no h1','errors',errs[-2:])
 b.close()
