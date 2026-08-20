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
 # credit overview
 pg.evaluate("state.module='credit';state.tabs.credit='overview';clearUnsupportedFilters('credit');render()")
 R['credit_tabs']=[pg.locator('[data-tab]').nth(i).inner_text() for i in range(pg.locator('[data-tab]').count())]
 R['credit_cards']=pg.locator('.score article').count()
 R['saturation']=pg.locator('[data-saturation-click]').count()>0
 R['risk_toggle']=pg.locator('[data-risk-entity]').count()==2
 R['rule_explain']=all(x in pg.locator('main').inner_text() for x in ['Risco total','Recente','Crédito disponível','Saturação'])
 # advanced
 pg.locator('[data-action="advanced"]').click(); pg.wait_for_timeout(50); R['credit_advanced']=pg.locator('.advanced .filter-slot').count(); pg.locator('[data-action="advanced"]').click()
 # credit customers detail
 pg.evaluate("state.tabs.credit='customers';setTableMode('credit-customers','detail');renderMain()")
 h=[pg.locator('.data th').nth(i).inner_text() for i in range(pg.locator('.data th').count())]
 R['credit_context']=all(any(k in x for x in h) for k in ['Faturamento 3m','Faturamento 6m','Faturamento 12m','Média mensal','Limite / compra média','Em aberto / compra média','Recente'])
 R['ratio_x']=pg.locator('.data tbody tr').first.inner_text().count('×')>=1
 cid=pg.locator('.entity-link').first.get_attribute('data-id');pg.evaluate("id=>{state.drawer={kind:'customer',id};renderOverlay()}",cid);txt=pg.locator('.drawer').inner_text();R['credit_customer_drawer']=all(x in txt for x in ['Resumo de crédito','Contexto de compra','Relações','Contexto comercial']);pg.evaluate("state.drawer=null;renderOverlay()")
 # guide
 pg.evaluate("state.tabs.credit='guides';renderMain()")
 gid=pg.locator('.entity-link').first.get_attribute('data-id');pg.evaluate("id=>{state.drawer={kind:'guide',id};renderOverlay()}",gid);txt=pg.locator('.drawer').inner_text();R['credit_guide_drawer']=all(x in txt for x in ['Resumo da carteira','Principais clientes do Guia']);pg.evaluate("state.drawer=null;renderOverlay()")
 # invariants
 R['invariants']=pg.evaluate("""() => {const ids=[...dims.customers.keys()];let e=0,r=0,t=0;for(const id of ids){const c=creditView(id);if(!c)continue;e=Math.max(e,Math.abs(c.limitExtra-currentExtra(id)));r=Math.max(r,Math.abs(c.riskTotal-(c.valueOpen+c.valueRecent)));t=Math.max(t,Math.abs(c.limitTotal-(c.limitNormal+c.limitExtra)));}return{extra:e,risk:r,total:t}}""")
 # extra overview
 pg.evaluate("state.module='extra';state.tabs.extra='overview';clearUnsupportedFilters('extra');render()")
 R['extra_tabs']=[pg.locator('[data-tab]').nth(i).inner_text() for i in range(pg.locator('[data-tab]').count())]
 txt=pg.locator('main').inner_text();R['effect_method']=all(x in txt for x in ['Efeito após aumento','associação temporal'])
 # verify data method directly
 R['effect_complete_logic']=pg.evaluate("""() => {const a=extraEffectRows();const incomplete=a.filter(x=>!x.completeAfter);return {events:a.length,incomplete:incomplete.length,bad:incomplete.filter(x=>x.afterAvg!==null||x.deltaAbs!==null||x.delta!==null).length,withOther:a.filter(x=>x.otherMovements>0).length}}""")
 # effect drawer first event
 rid=pg.evaluate("extraEffectRows()[0]?.reviewId")
 if rid:
  pg.evaluate("id=>{state.drawer={kind:'extraEffect',id:String(id)};renderOverlay()}",rid);txt=pg.locator('.drawer').inner_text();R['effect_drawer']=all(x in txt for x in ['Evento de aumento','Faturamento antes × depois','Situação atual de Crédito']);pg.evaluate("state.drawer=null;renderOverlay()")
 # movements
 pg.evaluate("state.tabs.extra='movements';renderMain()")
 R['mov_cards']=pg.locator('.score article').count(); R['mov_table']=pg.locator('.data').count()==1
 # customer drawer all movements selected period compare count
 pg.evaluate("state.tabs.extra='customers';renderMain()")
 cid=pg.locator('.entity-link').first.get_attribute('data-id'); expected=pg.evaluate("id=>{id=Number(id);const p=periodInfo();return (limitByCustomer.get(id)||[]).filter(x=>x.date>=p.start&&x.date<=p.end).length}",cid)
 pg.evaluate("id=>{state.drawer={kind:'customer',id};renderOverlay()}",cid);txt=pg.locator('.drawer').inner_text();R['extra_customer_history']='Histórico de movimentações' in txt; R['extra_customer_expected_moves']=expected; R['extra_customer_drawer_rows']=pg.locator('.drawer .mini-table tbody tr').count();pg.evaluate("state.drawer=null;renderOverlay()")
 # guide drawer
 pg.evaluate("state.tabs.extra='guides';renderMain()")
 gid=pg.locator('.entity-link').first.get_attribute('data-id');pg.evaluate("id=>{state.drawer={kind:'guide',id};renderOverlay()}",gid);txt=pg.locator('.drawer').inner_text();R['extra_guide_drawer']=all(x in txt for x in ['Clientes e origem da variação','Variação no período']);
 R['errors']=errs;b.close()
Path('/mnt/data/v12_validation/qa_credit_extra.json').write_text(json.dumps(R,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(R,ensure_ascii=False,indent=2))
