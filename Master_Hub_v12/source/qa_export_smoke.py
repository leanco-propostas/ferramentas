from pathlib import Path
import json
from playwright.sync_api import sync_playwright
html=Path('/mnt/data/Master_Hub_v12_Integrado.html').read_text(encoding='utf-8')
R={}
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 pg=b.new_page(viewport={'width':1366,'height':768}); errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
 pg.set_content(html,wait_until='domcontentloaded',timeout=25000);pg.wait_for_timeout(200)
 pg.evaluate("state.module='revenue';state.tabs.revenue='overview';render()")
 with pg.expect_download(timeout=5000) as d1: pg.locator('[data-export="csv"]').click()
 dl1=d1.value; path1=dl1.save_as('/mnt/data/v12_validation/test.csv')
 with pg.expect_download(timeout=5000) as d2: pg.locator('[data-export="xlsx"]').click()
 dl2=d2.value; dl2.save_as('/mnt/data/v12_validation/test.xls')
 R['csv_name']=dl1.suggested_filename;R['excel_name']=dl2.suggested_filename;R['csv_size']=Path('/mnt/data/v12_validation/test.csv').stat().st_size;R['excel_size']=Path('/mnt/data/v12_validation/test.xls').stat().st_size;R['errors']=errs
 b.close()
Path('/mnt/data/v12_validation/qa_export.json').write_text(json.dumps(R,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(R,ensure_ascii=False,indent=2))
