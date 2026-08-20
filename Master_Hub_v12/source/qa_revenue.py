from pathlib import Path
import json
from playwright.sync_api import sync_playwright
html=Path('/mnt/data/Master_Hub_v12_Integrado.html').read_text(encoding='utf-8')
R={}
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 pg=b.new_page(viewport={'width':1366,'height':768}); pg.set_default_timeout(8000)
 errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
 pg.set_content(html,wait_until='domcontentloaded',timeout=25000); pg.wait_for_timeout(200)
 pg.evaluate("state.module='revenue';state.tabs.revenue='overview';clearUnsupportedFilters('revenue');render()")
 R['tabs']=[pg.locator('[data-tab]').nth(i).inner_text() for i in range(pg.locator('[data-tab]').count())]
 R['five_tabs']=R['tabs']==['Visão Geral','Guias','Clientes','Lojas','Segmentos']
 R['advanced_toggle']=pg.locator('[data-action="advanced"]').count()==1
 R['comparison_explicit']='Período atual:' in pg.locator('.compare-line').inner_text() and 'Comparação:' in pg.locator('.compare-line').inner_text()
 R['concentration_4']=pg.locator('[data-concentration]').count()==4
 pages={}
 for tab in ['guides','customers','stores','segments']:
  pg.evaluate(f"state.tabs.revenue='{tab}';state.tableSearch='';state.sort={{key:null,dir:'desc'}};renderMain()")
  headers=[pg.locator('.data th').nth(i).inner_text() for i in range(pg.locator('.data th').count())]
  pages[tab]={'cards':pg.locator('.score article').count(),'headers':headers,'abc':all(any(k in h for h in headers) for k in ['Representatividade','Acumulado','Curva'])}
 R['pages']=pages
 # customer detailed fields
 pg.evaluate("state.tabs.revenue='customers';setTableMode('revenue-customers','detail');renderMain()")
 headers=[pg.locator('.data th').nth(i).inner_text() for i in range(pg.locator('.data th').count())]
 R['customer_detail']=all(any(k in h for h in headers) for k in ['Primeira compra','Última compra','Dias sem compra','Intervalo médio','Inadimplência'])
 # drawers direct first ids
 for tab,kind,need,key in [
  ('guides','guide',['Crédito da carteira atual','Top 10 clientes'],'guide_drawer'),
  ('customers','customer',['Crédito e risco','Comportamento de compra'],'customer_drawer'),
  ('stores','store',['Top 10 clientes','Top 10 Guias'],'store_drawer'),
  ('segments','segment',['Principais Lojas','Principais Clientes','Principais Guias'],'segment_drawer')]:
  pg.evaluate(f"state.tabs.revenue='{tab}';renderMain()")
  idv=pg.locator('.entity-link').first.get_attribute('data-id')
  pg.evaluate("([k,id])=>{state.drawer={kind:k,id:id};renderOverlay()}",[kind,idv])
  txt=pg.locator('.drawer').inner_text()
  R[key]=all(x in txt for x in need)
  pg.evaluate("state.drawer=null;renderOverlay()")
 R['errors']=errs
 b.close()
print(json.dumps(R,ensure_ascii=False,indent=2))
Path('/mnt/data/v12_validation/qa_revenue.json').write_text(json.dumps(R,ensure_ascii=False,indent=2),encoding='utf-8')
