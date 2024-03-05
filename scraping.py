import requests
import pandas as pd

cookie= "_gcl_au=1.1.1870522609.1706678526; BVBRANDID=44bd90f1-c5b6-4f2a-b533-a2aa621c15aa; _fbp=fb.1.1706678528061.2114288924; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; ajs_anonymous_id=7b482cc6-9dd7-4f91-806b-2206e1d21a77; _pin_unauth=dWlkPU9UaGhNVGswTWpFdFpHWmpPUzAwWVdOa0xUZ3dZMkl0TW1FeVpqTTFaVGM0TXpBMg; ajs_anonymous_id=7b482cc6-9dd7-4f91-806b-2206e1d21a77; __stripe_mid=69b2421c-f664-47b0-8ada-3194ed0b62d7f36b12; loyaltyID=null; dotcomSearchId=339d85b0-eba3-445b-b399-59dfbec0ff0c; _gid=GA1.2.1055005303.1709014968; _gat_UA-47434162-1=1; BVBRANDSID=da36fe03-5527-43fc-827a-1858eccc6160; __cf_bm=.gLWBVrhZ81yCGEEfr0S_1Vhdp7kuLpZDJvvsjl7E5w-1709014970-1.0-AU03+BQk2kqJO3g+z/lSJO0mct4Vs7Cj4uvuQgtw4AFssNiel8fCsD642gg6Fl4UYvLu5o+6//HtvJJS24N0diU=; session-sprouts=.eJwdjk1vgjAAQP9Lz8aUD5lwW8AsZVCCAQtcCEKR1oJKQaXL_vvIDu_yLu_9gLIdqeyA01ZC0g0o73Tsq4EOE3CmcV6NpFKy21BOtysdgAPo4nfnr5pFzEepQhpmvr1dpVbrp2VF1bp4noV9L1xkoT59FyQ1w6Tpg0TwgucT9g4KM7jDSQ0D4vOCxEauYhjqRxa5SKLhpIrMbysSs4gjiNXnG_PDC7MXy8lxqsjuv5Xp4or4fW7IWwbuOtXbMyXas8lCFg3HpSGpRL3omvUjTOoX5rkReakKM7j9DgwfdoH34MUji2WI8_3ehpVpdReRaHlgXsTl0et72l7BBsySjiVrgKObH1CzNGj9_gF5x2nU.GL8ROg.neVxQ32GdZmnq9Qtx-9hM3zdwmU; _ga_LPZ816BHL5=GS1.1.1709014967.14.1.1709014992.35.0.0; _ga=GA1.1.1479835951.1706678528; _uetsid=a187f340d53811eeaa3f1532ece08ef3; _uetvid=b021a2c0bff811ee97982b12ce0f9533"
      
HEADERS={
    

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie   
    
    
}

jio_mart=pd.read_excel("jio_mart.xlsx",sheet_name="Sheet1")


for i in range(0,len(jio_mart)):
    search_term=jio_mart.loc[i]['NAME']

    URL= f"https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=9&offset=0&search_provider=ic&search_term={search_term}&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false"
    responses=requests.get(URL,headers=HEADERS)
    data =responses.json()

    items=data['items']
    
    df_items=pd.DataFrame(items)
    cleaned_items=df_items[['name','base_price']]

    cleaned_items.to_excel(f"scraped/{search_term}.xlsx",index=False)



