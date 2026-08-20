import random, json, math
from datetime import date, timedelta
from pathlib import Path
random.seed(11082026)

MONTHS=[]
y,m=2024,7
for _ in range(24):
    MONTHS.append(f'{y:04d}-{m:02d}')
    m+=1
    if m==13: y+=1;m=1

segments_names=['Moda Feminina','Moda Masculina','Calçados','Acessórios','Moda Infantil','Jeans','Fitness','Íntima','Casual','Premium']
segments=[{'id':10+i*10,'name':n} for i,n in enumerate(segments_names)]
rp_names=['Renata Prado','Marcelo Nunes','Camila Torres','Juliana Castro','Eduardo Lima','Patrícia Mello','Rafael Duarte','Bianca Freitas']
rps=[{'id':301+i,'name':n} for i,n in enumerate(rp_names)]

guide_a=['Norte','Rota','Conexão','Ponto','Vale','Central','Horizonte','Elo','Portal','Aliança','Vértice','Prime','Sul','Estrela','Origem','Trilha','Ponte','Avante','Caminho','Núcleo','Atlas','Viva','Real','Integra']
guide_b=['Sul','Noroeste','Regional','Certo','Comercial','Compras','Negócios','Atacado','Shopping','Mercantil','Cianorte','Representações','Paraná','Moda','Leste','Oeste','Parceiros','Brasil','Premium','Center','Rede','Mais','Trade','Hub']
guides=[]
for i in range(24):
    guides.append({'id':201+i,'legalName':f'{guide_a[i]} {guide_b[i]} Representações Ltda.','tradeName':f'{guide_a[i]} {guide_b[i]}','currentRpId':301+(i%8)})

store_a=['Aurora','Clássico','Passo','Brilho','Pequenos','Estação','Linha','Caminho','Vitrine','Essência','Ponto','Alameda','Prime','Viva','Portal','Ritmo','Nobre','Solar','Urban','Bela','Forma','Trend','Mix','Única','Nativa','Studio','Rosa','Lumi','Ícone','Verso']
store_b=['Moda','Homem','Livre','Acessórios','Encantos','Feminina','Nobre','Leve','Central','Fashion','Chic','Cores','Store','Fit','Jeans','Kids','Concept','Premium','Casual','Bella','Atacado','Wear','Center','Intima','Style','Fashion','Moda','Store','Atacado','Concept']
stores=[]
for i in range(30):
    seg=segments[i%len(segments)]['id']
    stores.append({'id':501+i,'legalName':f'{store_a[i]} {store_b[i]} Atacado Ltda.','tradeName':f'{store_a[i]} {store_b[i]}','segmentId':seg})

cust_a=['Horizonte','Estilo','Casa','Bela','Vitrine','Ponto','Rosa','Essência','Portal','Nova','Alameda','Linha','Vale','Encanto','Pérola','Via','Estação','Viva','Serena','Bella','Lume','Tendência','Primavera','Verde','Nobre','Urban','Trama','Íris','Mosaico','Plural','Lótus','Canto']
cust_b=['Boutique','Livre','Nobre','Trama','Central','Elegante','dos Ventos','Urbana','Fashion','Estação','das Cores','& Forma','Têxtil','Catarina','do Vale','Serena','do Sul','Cor','Concept','Moda','Store','Chic','Fashion','Rosa','Mix','Style','Varejo','Moda','Fashion','Store','Atacado','Comercial']
customers=[]
for i in range(96):
    a=cust_a[i%len(cust_a)]; b=cust_b[(i*7)%len(cust_b)]; suffix=(i//len(cust_a))+1
    trade=f'{a} {b}' + (f' {suffix}' if suffix>1 else '')
    currentGuideId=201+((i*5+3)%24)
    customers.append({'id':1001+i,'legalName':f'{trade} Comércio Ltda.','tradeName':trade,'currentGuideId':currentGuideId,'city':['Maringá','Londrina','Cascavel','Umuarama','Campo Mourão','Paranavaí','Cianorte','Apucarana'][i%8],'uf':'PR'})

categories=[{'id':x,'description':f'Categoria {x} — classificação interna de crédito do cenário fictício'} for x in 'ABCDE']
# latent profiles
profiles={}
for c in customers:
    i=c['id']-1001
    start=max(0, random.choice([0,0,0,1,2,3,5,7,9]))
    # some new late customers
    if i%17==0: start=random.randint(10,18)
    end=23
    if i%11==0: end=random.randint(16,21)
    base=random.uniform(16000,85000)
    trend=random.uniform(-0.018,0.022)
    if i%9==0: trend=random.uniform(0.02,0.045)
    if i%13==0: trend=random.uniform(-0.05,-0.025)
    risk=max(0,min(1,random.betavariate(2.2,4.0)+(0.22 if i%14==0 else 0)))
    transfer_month=random.choice([None,None,None,8,12,15,18])
    old_guide=201+((i*7+9)%24)
    profiles[c['id']]={'start':start,'end':end,'base':base,'trend':trend,'risk':risk,'transfer':transfer_month,'oldGuide':old_guide}

billings=[]; bid=1
customer_month_revenue={}
for c in customers:
    p=profiles[c['id']]
    for mi,mon in enumerate(MONTHS):
        if mi<p['start'] or mi>p['end']: continue
        season=1+0.13*math.sin((mi%12)/12*2*math.pi)+ (0.14 if mon.endswith('-11') else 0.0)+(0.08 if mon.endswith('-12') else 0.0)
        growth=(1+p['trend'])**max(0,mi-p['start'])
        noise=random.uniform(.78,1.22)
        monthly=max(2500,p['base']*season*growth*noise)
        if random.random()<0.06: monthly*=0.28
        customer_month_revenue[(c['id'],mon)]=round(monthly,2)
        n=random.choice([1,2,2,2,3])
        weights=[random.uniform(.2,1) for _ in range(n)]; sw=sum(weights)
        histGuide=p['oldGuide'] if p['transfer'] is not None and mi<p['transfer'] else c['currentGuideId']
        prefs=[stores[(c['id']+k*7)%30] for k in range(3)]
        for ti,w in enumerate(weights):
            maxday=24 if mon=='2026-06' else 28
            day=min(maxday,3+((c['id']*3+mi*5+ti*7)%maxday))
            st=random.choice(prefs if random.random()<.75 else stores)
            value=round(monthly*w/sw,2)
            billings.append({'id':f'FAT-{bid:06d}','date':f'{mon}-{day:02d}','customerId':c['id'],'storeId':st['id'],'saleGuideId':histGuide,'value':value})
            bid+=1

# classifications quarterly-ish, risk can evolve
classifications=[]
for c in customers:
    p=profiles[c['id']]
    for mi in range(0,24,3):
        r=max(0,min(1,p['risk']+0.06*math.sin(mi/5)+(0.12 if mi>15 and c['id']%13==0 else 0)-(.10 if mi>12 and c['id']%9==0 else 0)))
        cat='A' if r<.18 else 'B' if r<.36 else 'C' if r<.58 else 'D' if r<.78 else 'E'
        classifications.append({'customerId':c['id'],'date':f'{MONTHS[mi]}-01','categoryId':cat})

# limit extra movements
limit_movements=[]; rev=1
initial_extra={}; extra_by_month={}
for c in customers:
    cid=c['id']; p=profiles[cid]
    cur=random.choice([0,0,5000,10000,15000,20000,30000])
    initial_extra[cid]=cur
    event_months=sorted(random.sample(range(max(0,p['start']),24), k=min(random.randint(3,8),24-max(0,p['start']))))
    if cid%10==0: event_months=sorted(set(event_months+[18,20,22]))
    by_m={}
    for mi in range(24):
        if mi in event_months:
            direction=1 if random.random()<.68 else -1
            amount=random.choice([5000,7500,10000,12500,15000,20000,25000])
            if cid%10==0 and mi>=18: direction=1
            movement=amount*direction
            new=max(0,cur+movement)
            movement=new-cur
            known=not (rev%37==0)
            limit_movements.append({'reviewId':f'REV-{rev:05d}','customerId':cid,'guideId':c['currentGuideId'],'date':f'{MONTHS[mi]}-{min(24,4+(cid+mi*3)%22):02d}','previousLimit':cur if known else None,'newLimit':new,'movement':movement,'type':'AUMENTO' if movement>0 else 'REDUCAO' if movement<0 else 'SEM ALTERACAO','previousHistoryKnown':known})
            rev+=1; cur=new
        by_m[MONTHS[mi]]=cur
    extra_by_month[cid]=by_m

# credit snapshots; fields follow historical reference scenario, explicitly marked reference in UI
credit=[]
for c in customers:
    cid=c['id']; p=profiles[cid]
    for mi,mon in enumerate(MONTHS):
        revm=customer_month_revenue.get((cid,mon),0)
        # 3m avg
        vals=[customer_month_revenue.get((cid,MONTHS[j]),0) for j in range(max(0,mi-2),mi+1)]
        avg3=sum(vals)/max(1,len(vals))
        risk=p['risk']
        base_limit=max(15000, min(160000, avg3*random.uniform(1.1,1.9)+25000*(1-risk)))
        limit_current=round(base_limit/1000)*1000
        extra=extra_by_month[cid][mon]
        total=limit_current+extra
        util=max(0.05,min(1.35, random.gauss(.62+risk*.35, .16)))
        if cid%16==0 and mi>18: util=min(1.35,util+.25)
        openv=round(total*util*random.uniform(.48,.76),2)
        recent=round(total*util*random.uniform(.18,.38),2)
        # occasionally force negative available
        if cid%19==0 and mi>=20:
            openv=round(total*.92,2); recent=round(total*.24,2)
        delinquent=0
        if risk>.66 and random.random()<.28:
            delinquent=round(random.uniform(1200,18000),2)
        returned_hist=round((risk*random.uniform(8000,50000)) + (delinquent*random.uniform(1,3)),2)
        av_no_recent=round(total-openv,2)
        av_with_recent=round(total-openv-recent,2)
        credit.append({'snapshotDate':f'{mon}-{24 if mon=="2026-06" else 28:02d}','customerId':cid,'limitCurrent':limit_current,'limitExtra':extra,'valueOpen':openv,'valueRecent':recent,'riskTotal':round(openv+recent,2),'delinquent':delinquent,'returnedHistorical':returned_hist,'availableWithoutRecent':av_no_recent,'availableWithRecent':av_with_recent})

# monthly band rows customer total
bands=[]
def band(v):
    if v<=0:return 'SEM FATURAMENTO'
    if v<=20000:return 'ATÉ 20 MIL'
    if v<=30000:return '20 A 30 MIL'
    if v<=40000:return '30 A 40 MIL'
    if v<=50000:return '40 A 50 MIL'
    return 'ACIMA DE 50 MIL'
for c in customers:
    for mon in MONTHS:
        v=customer_month_revenue.get((c['id'],mon),0)
        bands.append({'month':mon,'customerId':c['id'],'revenue':round(v,2),'band':band(v)})

obj={
 'meta':{'contractVersion':'2.0.0-integrated-prototype','fictitious':True,'analysisDate':'2026-08-18','minimumDate':'2024-07-01','maximumDate':'2026-06-24','months':MONTHS,'creditRuleStatus':'historical-reference-scenario'},
 'dimensions':{'customers':customers,'guides':guides,'rps':rps,'stores':stores,'segments':segments,'categories':categories},
 'parameters':{'customerStatus':[{'status':'ATIVO','minimumDays':0,'maximumDays':60},{'status':'ATENCAO','minimumDays':61,'maximumDays':90},{'status':'INATIVO','minimumDays':91,'maximumDays':None}], 'revenueBands':['SEM FATURAMENTO','ATÉ 20 MIL','20 A 30 MIL','30 A 40 MIL','40 A 50 MIL','ACIMA DE 50 MIL']},
 'facts':{'billings':sorted(billings,key=lambda x:(x['date'],x['id'])),'classifications':classifications,'limitExtraMovements':sorted(limit_movements,key=lambda x:(x['date'],x['reviewId'])),'creditSnapshots':credit,'revenueBands':bands}
}
obj['meta']['totals']={'customers':len(customers),'guides':len(guides),'rps':len(rps),'stores':len(stores),'billings':len(billings),'classifications':len(classifications),'limitExtraMovements':len(limit_movements),'creditSnapshots':len(credit),'revenueBands':len(bands),'revenue':round(sum(x['value'] for x in billings),2)}
path=Path('/mnt/data/master_hub_v11_source/data.json')
path.write_text(json.dumps(obj,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print(json.dumps(obj['meta']['totals'],ensure_ascii=False,indent=2))
