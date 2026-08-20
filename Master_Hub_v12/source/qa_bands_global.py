from pathlib import Path
import json
from playwright.sync_api import sync_playwright
html=Path('/mnt/data/Master_Hub_v12_Integrado.html').read_text(encoding='utf-8')
R={}
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 pg=b.new_page(viewport={'width':1366,'height':768});pg.set_default_timeout(8000)
 errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
 pg.set_content(html,wait_until='domcontentloaded',timeout=25000);pg.wait_for_timeout(200)
 # bands overview
 pg.evaluate("state.module='bands';state.tabs.bands='overview';clearUnsupportedFilters('bands');render()")
 R['bands_tabs']=[pg.locator('[data-tab]').nth(i).inner_text() for i in range(pg.locator('[data-tab]').count())]
 R['overview_cards']=pg.locator('.score article').count()
 R['overview_no_full_table']=pg.locator('.table-panel').count()==0
 R['matrix']=pg.locator('.matrix').count()>0
 R['initial_final_explained']=all(x in pg.locator('main').inner_text() for x in ['Faixa inicial','Faixa final'])
 # customers
 pg.evaluate("state.tabs.bands='customers';renderMain()")
 R['customers_chart']=pg.locator('.chart').count()>0
 R['metric_toggle']=pg.locator('[data-bands-metric]').count()==2
 R['table']=pg.locator('.table-panel').count()==1
 R['table_toggle']=pg.locator('[data-table-mode]').count()==2
 pg.locator('[data-table-mode="detail"]').click();pg.wait_for_timeout(50)
 h=[pg.locator('.data th').nth(i).inner_text() for i in range(pg.locator('.data th').count())]
 R['bands_detail']=all(any(k in x for x in h) for k in ['Guia atual','Limite total','Limite extra','Risco total','Média mensal','Primeira referência','Última referência'])
 cid=pg.locator('.entity-link').first.get_attribute('data-id');pg.evaluate("id=>{state.drawer={kind:'customer',id};renderOverlay()}",cid);txt=pg.locator('.drawer').inner_text();R['bands_drawer']=all(x in txt for x in ['Evolução mensal de faixa','Crédito e risco','Faturamento ao longo da trajetória']);pg.evaluate("state.drawer=null;renderOverlay()")
 # phase2 preserved
 pg.evaluate("state.module='executive';render()")
 R['executive_accessible']=pg.locator('main').count()==1 and 'Fase 2' in pg.locator('main').inner_text()
 pg.evaluate("state.module='customer';render()")
 R['customer_accessible']=pg.locator('.customer-head').count()>0 and 'Fase 2' in pg.locator('main').inner_text()
 # advanced filter toggle on all main pages by module
 adv={}
 for mod,tabs in {'revenue':['overview','guides','customers','stores','segments'],'credit':['overview','customers','guides'],'extra':['overview','movements','customers','guides'],'bands':['overview','customers']}.items():
  vals=[]
  for tab in tabs:
   pg.evaluate("([m,t])=>{state.module=m;state.tabs[m]=t;clearUnsupportedFilters(m);state.advancedOpen=false;render()}",[mod,tab])
   vals.append({'tab':tab,'toggle':pg.locator('[data-action="advanced"]').count()==1,'cards':pg.locator('.score article').count()})
  adv[mod]=vals
 R['all_pages_global_pattern']=adv
 # status & ABC accessible text/icon check
 pg.evaluate("state.module='revenue';state.tabs.revenue='customers';render()")
 R['abc_text_icon']=pg.locator('.abc-a').count()>0 and any('★' in pg.locator('.abc-a').nth(i).inner_text() for i in range(pg.locator('.abc-a').count()))
 pg.evaluate("setTableMode('revenue-customers','detail');renderMain()")
 R['status_text']=pg.locator('.badge[class*="status-"]').count()>0 and any(('Ativo' in pg.locator('.badge[class*="status-"]').nth(i).inner_text() or 'Atenção' in pg.locator('.badge[class*="status-"]').nth(i).inner_text() or 'Inativo' in pg.locator('.badge[class*="status-"]').nth(i).inner_text()) for i in range(pg.locator('.badge[class*="status-"]').count()))
 # overflow/screenshots
 out=Path('/mnt/data/v12_validation')
 pg.evaluate("state.module='revenue';state.tabs.revenue='overview';render()")
 for name,w,h in [('desktop',1366,768),('tablet',768,1024),('mobile',390,844)]:
  pg.set_viewport_size({'width':w,'height':h});pg.wait_for_timeout(100)
  R[name+'_overflow']=pg.evaluate('document.documentElement.scrollWidth-innerWidth')
  pg.screenshot(path=str(out/f'{name}.png'),full_page=False)
 R['errors']=errs
 b.close()
Path('/mnt/data/v12_validation/qa_bands_global.json').write_text(json.dumps(R,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(R,ensure_ascii=False,indent=2))
