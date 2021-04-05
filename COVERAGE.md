# Cities Coverage

Current coverage of territories with already implemented spiders.

If a spider is implemented for a territory it doesn't mean the whole of publication
systems for that territory is fully covered. In other words, a city can publish in many
different systems along their online publication timespan, and for the whole coverage
we should have spiders implemented for each one. Because of that, the
[census](https://censo.ok.org.br/) exists to analyze the whole of publication systems
for each brazilian territory. You can contribute there yourself or use it as a source
if you want to build a spider here and the census has already mapped the publication
systems for the territory you are interested.

> Note: spiders still in development may be found in this project's *issues* and/or
*pull requests*.

## Milestones

### Cover all capitals
<details>
  <summary>Click to expand</summary>

  | IBGE code | City name  | State | Implemented spiders |
  | :-------: | :--------  | :---- | :------------------ |
  | 2800308 | Aracaju | SE | |
  | 1501402 | Belém | PA | [pa_belem](data_collection/gazette/spiders/pa_belem.py) |
  | 3106200 | Belo Horizonte | MG | |
  | 1400100 | Boa Vista | RR | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py), [rr_boa_vista](data_collection/gazette/spiders/rr_boa_vista.py) |
  | 5300108 | Brasília | DF | [df_brasilia](data_collection/gazette/spiders/df_brasilia.py) |
  | 5002704 | Campo Grande | MS | [ms_campo_grande](data_collection/gazette/spiders/ms_campo_grande.py) |
  | 5103403 | Cuiabá | MT | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py), [mt_cuiaba](data_collection/gazette/spiders/mt_cuiaba.py) |
  | 4106902 | Curitiba | PR | [pr_curitiba](data_collection/gazette/spiders/pr_curitiba.py) |
  | 4205407 | Florianópolis | SC | [sc_florianopolis](data_collection/gazette/spiders/sc_florianopolis.py) |
  | 2304400 | Fortaleza | CE | [ce_fortaleza](data_collection/gazette/spiders/ce_fortaleza.py) |
  | 5208707 | Goiânia | GO | [go_goiania](data_collection/gazette/spiders/go_goiania.py) |
  | 2507507 | João Pessoa | PB | [pb_joao_pessoa](data_collection/gazette/spiders/pb_joao_pessoa.py) |
  | 1600303 | Macapá | AP | [ap_macapa](data_collection/gazette/spiders/ap_macapa.py) |
  | 2704302 | Maceió | AL | [al_maceio](data_collection/gazette/spiders/al_maceio.py) |
  | 1302603 | Manaus | AM | [am_manaus](data_collection/gazette/spiders/am_manaus.py) |
  | 2408102 | Natal | RN | [rn_natal](data_collection/gazette/spiders/rn_natal.py) |
  | 1721000 | Palmas | TO | [to_palmas](data_collection/gazette/spiders/to_palmas.py) |
  | 4314902 | Porto Alegre | RS | [rs_porto_alegre](data_collection/gazette/spiders/rs_porto_alegre.py) |
  | 1100205 | Porto Velho | RO | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py), [ro_porto_velho](data_collection/gazette/spiders/ro_porto_velho.py) |
  | 2611606 | Recife | PE | [pe_recife](data_collection/gazette/spiders/pe_recife.py) |
  | 1200401 | Rio Branco | AC | |
  | 3304557 | Rio de Janeiro | RJ | [rj_rio_de_janeiro](data_collection/gazette/spiders/rj_rio_de_janeiro.py) |
  | 2927408 | Salvador | BA | [ba_salvador](data_collection/gazette/spiders/ba_salvador.py) |
  | 2111300 | São Luís | MA | |
  | 3550308 | São Paulo | SP | [sp_sao_paulo](data_collection/gazette/spiders/sp_sao_paulo.py) |
  | 2211001 | Teresina | PI | [pi_teresina](data_collection/gazette/spiders/pi_teresina.py) |
  | 3205309 | Vitória | ES | |
</details>

### Cover all territories with population above 100k
<details>
  <summary>Click to expand</summary>

  | IBGE code | City name  | State | Population | Implemented spiders |
  | :-------: | :--------  | :---- | :--------- | :------------------ |
  | 3550308 | São Paulo | SP | 12325232 | [sp_sao_paulo](data_collection/gazette/spiders/sp_sao_paulo.py) |
  | 3304557 | Rio de Janeiro | RJ | 6747815 | [rj_rio_de_janeiro](data_collection/gazette/spiders/rj_rio_de_janeiro.py) |
  | 5300108 | Brasília | DF | 3055149 | [df_brasilia](data_collection/gazette/spiders/df_brasilia.py) |
  | 2927408 | Salvador | BA | 2886698 | [ba_salvador](data_collection/gazette/spiders/ba_salvador.py) |
  | 2304400 | Fortaleza | CE | 2686612 | [ce_fortaleza](data_collection/gazette/spiders/ce_fortaleza.py) |
  | 3106200 | Belo Horizonte | MG | 2521564 | |
  | 1302603 | Manaus | AM | 2219580 | [am_manaus](data_collection/gazette/spiders/am_manaus.py) |
  | 4106902 | Curitiba | PR | 1948626 | [pr_curitiba](data_collection/gazette/spiders/pr_curitiba.py) |
  | 2611606 | Recife | PE | 1653461 | [pe_recife](data_collection/gazette/spiders/pe_recife.py) |
  | 5208707 | Goiânia | GO | 1536097 | [go_goiania](data_collection/gazette/spiders/go_goiania.py) |
  | 1501402 | Belém | PA | 1499641 | [pa_belem](data_collection/gazette/spiders/pa_belem.py) |
  | 4314902 | Porto Alegre | RS | 1488252 | [rs_porto_alegre](data_collection/gazette/spiders/rs_porto_alegre.py) |
  | 3518800 | Guarulhos | SP | 1392121 | [sp_guarulhos](data_collection/gazette/spiders/sp_guarulhos.py) |
  | 3509502 | Campinas | SP | 1213792 | [sp_campinas](data_collection/gazette/spiders/sp_campinas.py) |
  | 2111300 | São Luís | MA | 1108975 | |
  | 3304904 | São Gonçalo | RJ | 1091737 | |
  | 2704302 | Maceió | AL | 1025360 | [al_maceio](data_collection/gazette/spiders/al_maceio.py) |
  | 3301702 | Duque de Caxias | RJ | 924624 | |
  | 5002704 | Campo Grande | MS | 906092 | [ms_campo_grande](data_collection/gazette/spiders/ms_campo_grande.py) |
  | 2408102 | Natal | RN | 890480 | [rn_natal](data_collection/gazette/spiders/rn_natal.py) |
  | 2211001 | Teresina | PI | 868075 | [pi_teresina](data_collection/gazette/spiders/pi_teresina.py) |
  | 3548708 | São Bernardo do Campo | SP | 844483 | |
  | 3303500 | Nova Iguaçu | RJ | 823302 | [rj_nova_iguacu](data_collection/gazette/spiders/rj_nova_iguacu.py) |
  | 2507507 | João Pessoa | PB | 817511 | [pb_joao_pessoa](data_collection/gazette/spiders/pb_joao_pessoa.py) |
  | 3549904 | São José dos Campos | SP | 729737 | [sp_sao_jose_dos_campos](data_collection/gazette/spiders/sp_sao_jose_dos_campos.py) |
  | 3547809 | Santo André | SP | 721368 | |
  | 3543402 | Ribeirão Preto | SP | 711825 | |
  | 2607901 | Jaboatão dos Guararapes | PE | 706867 | |
  | 3534401 | Osasco | SP | 699944 | |
  | 3170206 | Uberlândia | MG | 699097 | |
  | 3552205 | Sorocaba | SP | 687357 | |
  | 3118601 | Contagem | MG | 668949 | [mg_contagem](data_collection/gazette/spiders/mg_contagem.py) |
  | 2800308 | Aracaju | SE | 664908 | |
  | 2910800 | Feira de Santana | BA | 619609 | [ba_feira_de_santana](data_collection/gazette/spiders/ba_feira_de_santana.py) |
  | 5103403 | Cuiabá | MT | 618124 | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py), [mt_cuiaba](data_collection/gazette/spiders/mt_cuiaba.py) |
  | 4209102 | Joinville | SC | 597658 | [sc_joinville](data_collection/gazette/spiders/sc_joinville.py) |
  | 5201405 | Aparecida de Goiânia | GO | 590146 | [go_aparecida_de_goiania](data_collection/gazette/spiders/go_aparecida_de_goiania.py) |
  | 4113700 | Londrina | PR | 575377 | [pr_londrina](data_collection/gazette/spiders/pr_londrina.py) |
  | 3136702 | Juiz de Fora | MG | 573285 | |
  | 1100205 | Porto Velho | RO | 539354 | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py), [ro_porto_velho](data_collection/gazette/spiders/ro_porto_velho.py) |
  | 1500800 | Ananindeua | PA | 535547 | [pa_ananindeua](data_collection/gazette/spiders/pa_ananindeua.py) |
  | 3205002 | Serra | ES | 527240 | |
  | 4305108 | Caxias do Sul | RS | 517451 | [rs_caxias_do_sul](data_collection/gazette/spiders/rs_caxias_do_sul.py) |
  | 3303302 | Niterói | RJ | 515317 | [rj_niteroi](data_collection/gazette/spiders/rj_niteroi.py) |
  | 3300456 | Belford Roxo | RJ | 513118 | |
  | 1600303 | Macapá | AP | 512902 | [ap_macapa](data_collection/gazette/spiders/ap_macapa.py) |
  | 3301009 | Campos dos Goytacazes | RJ | 511168 | [rj_campos_goytacazes](data_collection/gazette/spiders/rj_campos_goytacazes.py) |
  | 4205407 | Florianópolis | SC | 508826 | [sc_florianopolis](data_collection/gazette/spiders/sc_florianopolis.py) |
  | 3205200 | Vila Velha | ES | 501325 | |
  | 3529401 | Mauá | SP | 477552 | |
  | 3305109 | São João de Meriti | RJ | 472906 | |
  | 3549805 | São José do Rio Preto | SP | 464983 | |
  | 3530607 | Mogi das Cruzes | SP | 450785 | |
  | 3106705 | Betim | MG | 444784 | |
  | 3548500 | Santos | SP | 433656 | [sp_santos](data_collection/gazette/spiders/sp_santos.py) |
  | 4115200 | Maringá | PR | 430157 | [pr_maringa](data_collection/gazette/spiders/pr_maringa.py) |
  | 3513801 | Diadema | SP | 426757 | |
  | 3525904 | Jundiaí | SP | 423006 | [sp_jundiai](data_collection/gazette/spiders/sp_jundiai.py) |
  | 1400100 | Boa Vista | RR | 419652 | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py), [rr_boa_vista](data_collection/gazette/spiders/rr_boa_vista.py) |
  | 3143302 | Montes Claros | MG | 413487 | |
  | 1200401 | Rio Branco | AC | 413418 | |
  | 2504009 | Campina Grande | PB | 411807 | [pb_campina_grande](data_collection/gazette/spiders/pb_campina_grande.py) |
  | 3538709 | Piracicaba | SP | 407252 | [sp_piracicaba](data_collection/gazette/spiders/sp_piracicaba.py) |
  | 3510609 | Carapicuíba | SP | 403183 | |
  | 2609600 | Olinda | PE | 393115 | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 5201108 | Anápolis | GO | 391772 | |
  | 3201308 | Cariacica | ES | 383917 | |
  | 3506003 | Bauru | SP | 379297 | [sp_bauru](data_collection/gazette/spiders/sp_bauru.py) |
  | 3523107 | Itaquaquecetuba | SP | 375011 | |
  | 3551009 | São Vicente | SP | 368355 | |
  | 3205309 | Vitória | ES | 365855 | |
  | 2604106 | Caruaru | PE | 365278 | |
  | 2303709 | Caucaia | CE | 365212 | [ce_caucaia](data_collection/gazette/spiders/ce_caucaia.py) |
  | 4202404 | Blumenau | SC | 361855 | [sc_blumenau](data_collection/gazette/spiders/sc_blumenau.py) |
  | 3516200 | Franca | SP | 355901 | [sp_franca](data_collection/gazette/spiders/sp_franca.py) |
  | 4119905 | Ponta Grossa | PR | 355336 | [pr_ponta_grossa](data_collection/gazette/spiders/pr_ponta_grossa.py) |
  | 2611101 | Petrolina | PE | 354317 | |
  | 4304606 | Canoas | RS | 348208 | [rs_canoas](data_collection/gazette/spiders/rs_canoas.py) |
  | 4314407 | Pelotas | RS | 343132 | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 2933307 | Vitória da Conquista | BA | 341128 | [ba_vitoria_da_conquista](data_collection/gazette/spiders/ba_vitoria_da_conquista.py) |
  | 3154606 | Ribeirão das Neves | MG | 338197 | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3170107 | Uberaba | MG | 337092 | [mg_uberaba](data_collection/gazette/spiders/mg_uberaba.py) |
  | 2610707 | Paulista | PE | 334376 | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 4104808 | Cascavel | PR | 332333 | [pr_cascavel](data_collection/gazette/spiders/pr_cascavel.py) |
  | 3541000 | Praia Grande | SP | 330845 | |
  | 4125506 | São José dos Pinhais | PR | 329058 | [pr_sao_jose_pinhais](data_collection/gazette/spiders/pr_sao_jose_pinhais.py) |
  | 3518701 | Guarujá | SP | 322750 | [sp_guaruja](data_collection/gazette/spiders/sp_guaruja.py) |
  | 3554102 | Taubaté | SP | 317915 | |
  | 3526902 | Limeira | SP | 308482 | |
  | 3303906 | Petrópolis | RJ | 306678 | |
  | 1506807 | Santarém | PA | 306480 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1721000 | Palmas | TO | 306296 | [to_palmas](data_collection/gazette/spiders/to_palmas.py) |
  | 2905701 | Camaçari | BA | 304302 | |
  | 2408003 | Mossoró | RN | 300618 | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py), [rn_mossoro](data_collection/gazette/spiders/rn_mossoro.py) |
  | 3552502 | Suzano | SP | 300559 | |
  | 3552809 | Taboão da Serra | SP | 293652 | |
  | 5108402 | Várzea Grande | MT | 287526 | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 3552403 | Sumaré | SP | 286211 | |
  | 4316907 | Santa Maria | RS | 283677 | |
  | 4309209 | Gravataí | RS | 283620 | [rs_gravatai](data_collection/gazette/spiders/rs_gravatai.py) |
  | 1504208 | Marabá | PA | 283542 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 3127701 | Governador Valadares | MG | 281046 | [mg_governador_valadares](data_collection/gazette/spiders/mg_governador_valadares.py) |
  | 3505708 | Barueri | SP | 276982 | |
  | 3515004 | Embu das Artes | SP | 276535 | |
  | 2307304 | Juazeiro do Norte | CE | 276264 | |
  | 3306305 | Volta Redonda | RJ | 273988 | |
  | 2403251 | Parnamirim | RN | 267036 | |
  | 3131307 | Ipatinga | MG | 265409 | |
  | 3302403 | Macaé | RJ | 261501 | |
  | 2105302 | Imperatriz | MA | 259337 | |
  | 4108304 | Foz do Iguaçu | PR | 258248 | [pr_foz_do_iguacu](data_collection/gazette/spiders/pr_foz_do_iguacu.py) |
  | 4323002 | Viamão | RS | 256302 | |
  | 3520509 | Indaiatuba | SP | 256223 | |
  | 3548906 | São Carlos | SP | 254484 | |
  | 3513009 | Cotia | SP | 253608 | |
  | 4216602 | São José | SC | 250181 | [sc_sao_jose](data_collection/gazette/spiders/sc_sao_jose.py) |
  | 4313409 | Novo Hamburgo | RS | 247032 | |
  | 4105805 | Colombo | PR | 246540 | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 3302502 | Magé | RJ | 246433 | |
  | 3301900 | Itaboraí | RJ | 242543 | |
  | 3501608 | Americana | SP | 242018 | |
  | 3167202 | Sete Lagoas | MG | 241835 | |
  | 5218805 | Rio Verde | GO | 241518 | |
  | 3522505 | Itapevi | SP | 240961 | |
  | 3529005 | Marília | SP | 240590 | [sp_marilia](data_collection/gazette/spiders/sp_marilia.py) |
  | 3122306 | Divinópolis | MG | 240408 | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 4318705 | São Leopoldo | RS | 238648 | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 3503208 | Araraquara | SP | 238339 | |
  | 5107602 | Rondonópolis | MT | 236042 | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 3524402 | Jacareí | SP | 235416 | |
  | 3519071 | Hortolândia | SP | 234259 | |
  | 2700300 | Arapiraca | AL | 233047 | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 3300704 | Cabo Frio | RJ | 230378 | |
  | 3541406 | Presidente Prudente | SP | 230371 | [sp_presidente_prudente](data_collection/gazette/spiders/sp_presidente_prudente.py) |
  | 2307650 | Maracanaú | CE | 229458 | |
  | 5003702 | Dourados | MS | 225495 | |
  | 4204202 | Chapecó | SC | 224013 | [sc_chapeco](data_collection/gazette/spiders/sc_chapeco.py) |
  | 4208203 | Itajaí | SC | 223112 | [sc_itajai](data_collection/gazette/spiders/sc_itajai.py) |
  | 3157807 | Santa Luzia | MG | 220444 | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 2918407 | Juazeiro | BA | 218162 | |
  | 5200258 | Águas Lindas de Goiás | GO | 217698 | |
  | 4204608 | Criciúma | SC | 217311 | [sc_criciuma](data_collection/gazette/spiders/sc_criciuma.py) |
  | 2914802 | Itabuna | BA | 213685 | |
  | 1505536 | Parauapebas | PA | 213576 | |
  | 4315602 | Rio Grande | RS | 211965 | |
  | 5212501 | Luziânia | GO | 211508 | |
  | 4300604 | Alvorada | RS | 211352 | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 2312908 | Sobral | CE | 210711 | |
  | 3201209 | Cachoeiro de Itapemirim | ES | 210589 | |
  | 2602902 | Cabo de Santo Agostinho | PE | 208944 | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 3543907 | Rio Claro | SP | 208008 | |
  | 3300100 | Angra dos Reis | RJ | 207044 | |
  | 4314100 | Passo Fundo | RS | 204722 | |
  | 1502400 | Castanhal | PA | 203251 | |
  | 2919207 | Lauro de Freitas | BA | 201635 | |
  | 3502804 | Araçatuba | SP | 198129 | |
  | 3515707 | Ferraz de Vasconcelos | SP | 196500 | |
  | 3545803 | Santa Bárbara d'Oeste | SP | 194390 | |
  | 3303401 | Nova Friburgo | RJ | 191158 | |
  | 2804805 | Nossa Senhora do Socorro | SE | 185706 | |
  | 3300407 | Barra Mansa | RJ | 184833 | |
  | 3305802 | Teresópolis | RJ | 184240 | |
  | 1702109 | Araguaína | TO | 183381 | [to_araguaina](data_collection/gazette/spiders/to_araguaina.py) |
  | 4109401 | Guarapuava | PR | 182644 | |
  | 3129806 | Ibirité | MG | 182153 | |
  | 4208906 | Jaraguá do Sul | SC | 181173 | [sc_jaragua_do_sul](data_collection/gazette/spiders/sc_jaragua_do_sul.py) |
  | 2111201 | São José de Ribamar | MA | 179028 | |
  | 3522208 | Itapecerica da Serra | SP | 177662 | |
  | 3516309 | Francisco Morato | SP | 177633 | |
  | 3203205 | Linhares | ES | 176688 | |
  | 3302858 | Mesquita | RJ | 176569 | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3523909 | Itu | SP | 175568 | [sp_associacao_municipios](data_collection/gazette/spiders/sp_associacao_municipios.py), [sp_itu](data_collection/gazette/spiders/sp_itu.py) |
  | 4211900 | Palhoça | SC | 175272 | [sc_palhoca](data_collection/gazette/spiders/sc_palhoca.py) |
  | 5221858 | Valparaíso de Goiás | GO | 172135 | |
  | 3507605 | Bragança Paulista | SP | 170533 | |
  | 2112209 | Timon | MA | 170222 | |
  | 3538006 | Pindamonhangaba | SP | 170132 | |
  | 3151800 | Poços de Caldas | MG | 168641 | |
  | 3522307 | Itapetininga | SP | 165526 | |
  | 2103000 | Caxias | MA | 165525 | |
  | 3302700 | Maricá | RJ | 164504 | |
  | 3303203 | Nilópolis | RJ | 162693 | |
  | 2931350 | Teixeira de Freitas | BA | 162438 | |
  | 3548807 | São Caetano do Sul | SP | 161957 | |
  | 2913606 | Ilhéus | BA | 159923 | |
  | 1500107 | Abaetetuba | PA | 159080 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 2603454 | Camaragibe | PE | 158899 | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 4209300 | Lages | SC | 157349 | [sc_lages](data_collection/gazette/spiders/sc_lages.py) |
  | 2903201 | Barreiras | BA | 156975 | |
  | 3516408 | Franco da Rocha | SP | 156492 | |
  | 4118204 | Paranaguá | PR | 156174 | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 2918001 | Jequié | BA | 156126 | |
  | 3304524 | Rio das Ostras | RJ | 155193 | |
  | 3148004 | Patos de Minas | MG | 153585 | |
  | 2207702 | Parnaíba | PI | 153482 | |
  | 3530706 | Mogi Guaçu | SP | 153033 | |
  | 3152501 | Pouso Alegre | MG | 152549 | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 2900702 | Alagoinhas | BA | 152327 | |
  | 3525300 | Jaú | SP | 151881 | [sp_jau](data_collection/gazette/spiders/sp_jau.py) |
  | 3304144 | Queimados | RJ | 151335 | |
  | 2925303 | Porto Seguro | BA | 150658 | |
  | 3507506 | Botucatu | SP | 148130 | |
  | 4101804 | Araucária | PR | 146214 | |
  | 5107909 | Sinop | MT | 146005 | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 4202008 | Balneário Camboriú | SC | 145796 | [sc_balneario_camboriu](data_collection/gazette/spiders/sc_balneario_camboriu.py) |
  | 3504107 | Atibaia | SP | 144088 | |
  | 4127700 | Toledo | PR | 142645 | |
  | 3547304 | Santana de Parnaíba | SP | 142301 | |
  | 4320008 | Sapucaia do Sul | RS | 141808 | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 3168606 | Teófilo Otoni | MG | 140937 | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 2606002 | Garanhuns | PE | 140577 | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2616407 | Vitória de Santo Antão | PE | 139583 | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 1502103 | Cametá | PA | 139364 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 3105608 | Barbacena | MG | 138204 | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 4202909 | Brusque | SC | 137689 | [sc_brusque](data_collection/gazette/spiders/sc_brusque.py) |
  | 2513703 | Santa Rita | PB | 137349 | |
  | 3156700 | Sabará | MG | 137125 | |
  | 3170701 | Varginha | MG | 136602 | |
  | 4101408 | Apucarana | PR | 136234 | |
  | 2930709 | Simões Filho | BA | 135783 | |
  | 3503307 | Araras | SP | 135506 | |
  | 3302007 | Itaguaí | RJ | 134819 | |
  | 3300209 | Araruama | RJ | 134293 | |
  | 4104204 | Campo Largo | PR | 133865 | |
  | 1504422 | Marituba | PA | 133685 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 4119152 | Pinhais | PR | 133490 | |
  | 2304202 | Crato | CE | 133031 | |
  | 3204906 | São Mateus | ES | 132642 | |
  | 3304201 | Resende | RJ | 132312 | |
  | 1507300 | São Félix do Xingu | PA | 132138 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 3513504 | Cubatão | SP | 131626 | |
  | 4316808 | Santa Cruz do Sul | RS | 131365 | |
  | 4303103 | Cachoeirinha | RS | 131240 | |
  | 3556206 | Valinhos | SP | 131210 | |
  | 2306405 | Itapipoca | CE | 130539 | |
  | 2307700 | Maranguape | CE | 130346 | |
  | 1100122 | Ji-Paraná | RO | 130009 | |
  | 5221403 | Trindade | GO | 129823 | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 3171204 | Vespasiano | MG | 129765 | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3118304 | Conselheiro Lafaiete | MG | 129606 | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 1501709 | Bragança | PA | 128914 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 3551702 | Sertãozinho | SP | 127142 | |
  | 1501303 | Barcarena | PA | 127027 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 4322400 | Uruguaiana | RS | 126866 | |
  | 3202405 | Guarapari | ES | 126701 | |
  | 3525003 | Jandira | SP | 126356 | |
  | 3506508 | Birigui | SP | 124883 | |
  | 4101507 | Arapongas | PR | 124810 | |
  | 3543303 | Ribeirão Pires | SP | 124159 | |
  | 2107506 | Paço do Lumiar | MA | 123747 | |
  | 5208004 | Formosa | GO | 123684 | |
  | 3557006 | Votorantim | SP | 123599 | [sp_votorantim](data_collection/gazette/spiders/sp_votorantim.py) |
  | 3201506 | Colatina | ES | 123400 | |
  | 3510500 | Caraguatatuba | SP | 123389 | |
  | 5008305 | Três Lagoas | MS | 123281 | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 2103307 | Codó | MA | 123116 | |
  | 1600600 | Santana | AP | 123096 | |
  | 3556503 | Várzea Paulista | SP | 123071 | |
  | 3554003 | Tatuí | SP | 122967 | |
  | 3505500 | Barretos | SP | 122833 | |
  | 3523404 | Itatiba | SP | 122581 | |
  | 3518404 | Guaratinguetá | SP | 122505 | |
  | 3511102 | Catanduva | SP | 122497 | |
  | 4302105 | Bento Gonçalves | RS | 121803 | |
  | 4301602 | Bagé | RS | 121335 | |
  | 3131703 | Itabira | MG | 120904 | |
  | 4100400 | Almirante Tamandaré | PR | 120041 | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 3545209 | Salto | SP | 119736 | |
  | 2924009 | Paulo Afonso | BA | 118516 | |
  | 5220454 | Senador Canedo | GO | 118451 | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 2606804 | Igarassu | PE | 118370 | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 3539806 | Poá | SP | 118349 | |
  | 3103504 | Araguari | MG | 117825 | |
  | 5215231 | Novo Gama | GO | 117703 | |
  | 3169901 | Ubá | MG | 116797 | |
  | 1500602 | Altamira | PA | 115969 | |
  | 1303403 | Parintins | AM | 115363 | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 3147907 | Passos | MG | 115337 | |
  | 1508100 | Tucuruí | PA | 115144 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 4119509 | Piraquara | PR | 114970 | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 1505502 | Paragominas | PA | 114503 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 2910727 | Eunápolis | BA | 114396 | |
  | 3534708 | Ourinhos | SP | 114352 | |
  | 2613701 | São Lourenço da Mata | PE | 114079 | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2100055 | Açailândia | MA | 113121 | |
  | 4128104 | Umuarama | PR | 112500 | |
  | 5003207 | Corumbá | MS | 112058 | |
  | 3536505 | Paulínia | SP | 112003 | |
  | 5205109 | Catalão | GO | 110983 | |
  | 3119401 | Coronel Fabriciano | MG | 110290 | |
  | 2612505 | Santa Cruz do Capibaribe | PE | 109897 | |
  | 1100023 | Ariquemes | RO | 109523 | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 3143906 | Muriaé | MG | 109392 | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 1507953 | Tailândia | PA | 108969 | |
  | 2510808 | Patos | PB | 108192 | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 4103701 | Cambé | PR | 107341 | |
  | 3104007 | Araxá | MG | 107337 | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 4307005 | Erechim | RS | 106633 | |
  | 4218707 | Tubarão | SC | 106422 | [sc_tubarao](data_collection/gazette/spiders/sc_tubarao.py) |
  | 3305208 | São Pedro da Aldeia | RJ | 106049 | |
  | 5211503 | Itumbiara | GO | 105809 | |
  | 5107958 | Tangará da Serra | MT | 105711 | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 3302270 | Japeri | RJ | 105548 | |
  | 3145208 | Nova Serrana | MG | 105520 | [mg_nova_serrana](data_collection/gazette/spiders/mg_nova_serrana.py) |
  | 3134202 | Ituiutaba | MG | 105255 | |
  | 2803500 | Lagarto | SE | 105221 | |
  | 3504008 | Assis | SP | 105087 | |
  | 2101202 | Bacabal | MA | 104790 | |
  | 3138203 | Lavras | MG | 104783 | |
  | 3526704 | Leme | SP | 104346 | |
  | 3302205 | Itaperuna | RJ | 103800 | |
  | 2412005 | São Gonçalo do Amarante | RN | 103672 | [rn_sao_goncalo_do_amarante](data_collection/gazette/spiders/rn_sao_goncalo_do_amarante.py) |
  | 1501808 | Breves | PA | 103497 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 3522109 | Itanhaém | SP | 103102 | |
  | 3200607 | Aracruz | ES | 103101 | |
  | 2305506 | Iguatu | CE | 103074 | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 3509007 | Caieiras | SP | 102775 | |
  | 1301902 | Itacoatiara | AM | 102701 | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 2928703 | Santo Antônio de Jesus | BA | 102380 | |
  | 1100304 | Vilhena | RO | 102211 | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 5211909 | Jataí | GO | 102065 | |
  | 4107652 | Fazenda Rio Grande | PR | 102004 | |
  | 3528502 | Mairiporã | SP | 101937 | |
  | 1503606 | Itaituba | PA | 101395 | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 3300308 | Barra do Piraí | RJ | 100764 | |
  | 2600054 | Abreu e Lima | PE | 100346 | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
</details>

## All Territories


### Acre

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 1200013 | Acrelândia | |
  | 1200054 | Assis Brasil | |
  | 1200104 | Brasiléia | |
  | 1200138 | Bujari | |
  | 1200179 | Capixaba | |
  | 1200203 | Cruzeiro do Sul | |
  | 1200252 | Epitaciolândia | |
  | 1200302 | Feijó | |
  | 1200328 | Jordão | |
  | 1200336 | Mâncio Lima | |
  | 1200344 | Manoel Urbano | |
  | 1200351 | Marechal Thaumaturgo | |
  | 1200385 | Plácido de Castro | |
  | 1200807 | Porto Acre | |
  | 1200393 | Porto Walter | |
  | 1200401 | Rio Branco | |
  | 1200427 | Rodrigues Alves | |
  | 1200435 | Santa Rosa do Purus | |
  | 1200500 | Sena Madureira | |
  | 1200450 | Senador Guiomard | |
  | 1200609 | Tarauacá | |
  | 1200708 | Xapuri | |
</details>


### Alagoas

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 2700102 | Água Branca | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2700201 | Anadia | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2700300 | Arapiraca | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2700409 | Atalaia | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2700508 | Barra de Santo Antônio | |
  | 2700607 | Barra de São Miguel | |
  | 2700706 | Batalha | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2700805 | Belém | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2700904 | Belo Monte | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701001 | Boca da Mata | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701100 | Branquinha | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701209 | Cacimbinhas | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701308 | Cajueiro | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701357 | Campestre | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701407 | Campo Alegre | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701506 | Campo Grande | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701605 | Canapi | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701704 | Capela | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701803 | Carneiros | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2701902 | Chã Preta | |
  | 2702009 | Coité do Nóia | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702108 | Colônia Leopoldina | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702207 | Coqueiro Seco | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702306 | Coruripe | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702355 | Craíbas | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702405 | Delmiro Gouveia | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702504 | Dois Riachos | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702553 | Estrela de Alagoas | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702603 | Feira Grande | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702702 | Feliz Deserto | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702801 | Flexeiras | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2702900 | Girau do Ponciano | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2703007 | Ibateguara | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2703106 | Igaci | |
  | 2703205 | Igreja Nova | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2703304 | Inhapi | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2703403 | Jacaré dos Homens | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2703502 | Jacuípe | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2703601 | Japaratinga | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2703700 | Jaramataia | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2703759 | Jequiá da Praia | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2703809 | Joaquim Gomes | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2703908 | Jundiá | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2704005 | Junqueiro | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2704104 | Lagoa da Canoa | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2704203 | Limoeiro de Anadia | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2704302 | Maceió | [al_maceio](data_collection/gazette/spiders/al_maceio.py) |
  | 2704401 | Major Isidoro | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2704906 | Mar Vermelho | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2704500 | Maragogi | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2704609 | Maravilha | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2704708 | Marechal Deodoro | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2704807 | Maribondo | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2705002 | Mata Grande | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2705101 | Matriz de Camaragibe | |
  | 2705200 | Messias | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2705309 | Minador do Negrão | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2705408 | Monteirópolis | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2705507 | Murici | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2705606 | Novo Lino | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2705804 | Olho d'Água do Casado | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2705705 | Olho d'Água das Flores | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2705903 | Olho d'Água Grande | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2706000 | Olivença | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2706109 | Ouro Branco | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2706208 | Palestina | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2706307 | Palmeira dos Índios | |
  | 2706406 | Pão de Açúcar | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2706422 | Pariconha | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2706448 | Paripueira | |
  | 2706505 | Passo de Camaragibe | |
  | 2706604 | Paulo Jacinto | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2706703 | Penedo | |
  | 2706802 | Piaçabuçu | |
  | 2706901 | Pilar | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2707008 | Pindoba | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2707107 | Piranhas | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2707206 | Poço das Trincheiras | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2707305 | Porto Calvo | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2707404 | Porto de Pedras | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2707503 | Porto Real do Colégio | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2707602 | Quebrangulo | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2707701 | Rio Largo | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2707800 | Roteiro | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2707909 | Santa Luzia do Norte | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2708006 | Santana do Ipanema | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2708105 | Santana do Mundaú | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2708204 | São Brás | |
  | 2708303 | São José da Laje | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2708402 | São José da Tapera | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2708501 | São Luís do Quitunde | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2708600 | São Miguel dos Campos | |
  | 2708709 | São Miguel dos Milagres | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2708808 | São Sebastião | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2708907 | Satuba | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2708956 | Senador Rui Palmeira | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2709004 | Tanque d'Arca | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2709103 | Taquarana | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2709152 | Teotônio Vilela | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2709202 | Traipu | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
  | 2709301 | União dos Palmares | |
  | 2709400 | Viçosa | [al_associacao_municipios](data_collection/gazette/spiders/al_associacao_municipios.py) |
</details>


### Amapá

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 1600105 | Amapá | |
  | 1600204 | Calçoene | |
  | 1600212 | Cutias | |
  | 1600238 | Ferreira Gomes | |
  | 1600253 | Itaubal | |
  | 1600279 | Laranjal do Jari | |
  | 1600303 | Macapá | [ap_macapa](data_collection/gazette/spiders/ap_macapa.py) |
  | 1600402 | Mazagão | |
  | 1600501 | Oiapoque | |
  | 1600154 | Pedra Branca do Amapari | |
  | 1600535 | Porto Grande | |
  | 1600550 | Pracuúba | |
  | 1600600 | Santana | |
  | 1600055 | Serra do Navio | |
  | 1600709 | Tartarugalzinho | |
  | 1600808 | Vitória do Jari | |
</details>


### Amazonas

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 1300029 | Alvarães | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300060 | Amaturá | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300086 | Anamã | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300102 | Anori | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300144 | Apuí | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300201 | Atalaia do Norte | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300300 | Autazes | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300409 | Barcelos | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300508 | Barreirinha | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300607 | Benjamin Constant | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300631 | Beruri | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300680 | Boa Vista do Ramos | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300706 | Boca do Acre | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300805 | Borba | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300839 | Caapiranga | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1300904 | Canutama | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301001 | Carauari | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301100 | Careiro | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301159 | Careiro da Várzea | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301209 | Coari | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301308 | Codajás | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301407 | Eirunepé | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301506 | Envira | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301605 | Fonte Boa | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301654 | Guajará | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301704 | Humaitá | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301803 | Ipixuna | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301852 | Iranduba | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301902 | Itacoatiara | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1301951 | Itamarati | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1302009 | Itapiranga | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1302108 | Japurá | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1302207 | Juruá | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1302306 | Jutaí | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1302405 | Lábrea | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1302504 | Manacapuru | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1302553 | Manaquiri | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1302603 | Manaus | [am_manaus](data_collection/gazette/spiders/am_manaus.py) |
  | 1302702 | Manicoré | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1302801 | Maraã | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1302900 | Maués | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303007 | Nhamundá | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303106 | Nova Olinda do Norte | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303205 | Novo Airão | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303304 | Novo Aripuanã | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303403 | Parintins | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303502 | Pauini | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303536 | Presidente Figueiredo | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303569 | Rio Preto da Eva | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303601 | Santa Isabel do Rio Negro | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303700 | Santo Antônio do Içá | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303809 | São Gabriel da Cachoeira | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303908 | São Paulo de Olivença | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1303957 | São Sebastião do Uatumã | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1304005 | Silves | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1304062 | Tabatinga | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1304104 | Tapauá | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1304203 | Tefé | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1304237 | Tonantins | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1304260 | Uarini | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1304302 | Urucará | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
  | 1304401 | Urucurituba | [am_associacao_municipios](data_collection/gazette/spiders/am_associacao_municipios.py) |
</details>


### Bahia

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 2900108 | Abaíra | |
  | 2900207 | Abaré | |
  | 2900306 | Acajutiba | [ba_acajutiba](data_collection/gazette/spiders/ba_acajutiba.py) |
  | 2900355 | Adustina | |
  | 2900405 | Água Fria | |
  | 2900603 | Aiquara | |
  | 2900702 | Alagoinhas | |
  | 2900801 | Alcobaça | |
  | 2900900 | Almadina | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2901007 | Amargosa | |
  | 2901106 | Amélia Rodrigues | |
  | 2901155 | América Dourada | |
  | 2901205 | Anagé | |
  | 2901304 | Andaraí | |
  | 2901353 | Andorinha | |
  | 2901403 | Angical | |
  | 2901502 | Anguera | |
  | 2901601 | Antas | |
  | 2901700 | Antônio Cardoso | |
  | 2901809 | Antônio Gonçalves | |
  | 2901908 | Aporá | |
  | 2901957 | Apuarema | |
  | 2902054 | Araças | |
  | 2902005 | Aracatu | |
  | 2902104 | Araci | |
  | 2902203 | Aramari | |
  | 2902252 | Arataca | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2902302 | Aratuípe | |
  | 2902401 | Aurelino Leal | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2902500 | Baianópolis | |
  | 2902609 | Baixa Grande | |
  | 2902658 | Banzaê | |
  | 2902708 | Barra | |
  | 2902906 | Barra do Choça | |
  | 2902807 | Barra da Estiva | |
  | 2903003 | Barra do Mendes | |
  | 2903102 | Barra do Rocha | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2903201 | Barreiras | |
  | 2903235 | Barro Alto | |
  | 2903300 | Barro Preto | |
  | 2903276 | Barrocas | |
  | 2903409 | Belmonte | |
  | 2903508 | Belo Campo | |
  | 2903607 | Biritinga | |
  | 2903706 | Boa Nova | |
  | 2903805 | Boa Vista do Tupim | |
  | 2903904 | Bom Jesus da Lapa | |
  | 2903953 | Bom Jesus da Serra | |
  | 2904001 | Boninal | |
  | 2904050 | Bonito | |
  | 2904100 | Boquira | |
  | 2904209 | Botuporã | |
  | 2904308 | Brejões | |
  | 2904407 | Brejolândia | |
  | 2904506 | Brotas de Macaúbas | |
  | 2904605 | Brumado | |
  | 2904704 | Buerarema | |
  | 2904753 | Buritirama | |
  | 2904803 | Caatiba | |
  | 2904852 | Cabaceiras do Paraguaçu | |
  | 2904902 | Cachoeira | |
  | 2905008 | Caculé | |
  | 2905107 | Caém | |
  | 2905156 | Caetanos | |
  | 2905206 | Caetité | |
  | 2905305 | Cafarnaum | |
  | 2905404 | Cairu | |
  | 2905503 | Caldeirão Grande | |
  | 2905602 | Camacan | |
  | 2905701 | Camaçari | |
  | 2905800 | Camamu | |
  | 2905909 | Campo Alegre de Lourdes | |
  | 2906006 | Campo Formoso | |
  | 2906105 | Canápolis | |
  | 2906204 | Canarana | |
  | 2906303 | Canavieiras | |
  | 2906402 | Candeal | |
  | 2906501 | Candeias | |
  | 2906600 | Candiba | |
  | 2906709 | Cândido Sales | |
  | 2906808 | Cansanção | |
  | 2906824 | Canudos | |
  | 2906857 | Capela do Alto Alegre | |
  | 2906873 | Capim Grosso | |
  | 2906899 | Caraíbas | |
  | 2906907 | Caravelas | |
  | 2907004 | Cardeal da Silva | |
  | 2907103 | Carinhanha | |
  | 2907202 | Casa Nova | |
  | 2907301 | Castro Alves | |
  | 2907400 | Catolândia | |
  | 2907509 | Catu | |
  | 2907558 | Caturama | |
  | 2907608 | Central | |
  | 2907707 | Chorrochó | |
  | 2907806 | Cícero Dantas | |
  | 2907905 | Cipó | |
  | 2908002 | Coaraci | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2908101 | Cocos | |
  | 2908309 | Conceição do Almeida | |
  | 2908408 | Conceição do Coité | |
  | 2908200 | Conceição da Feira | |
  | 2908507 | Conceição do Jacuípe | |
  | 2908606 | Conde | |
  | 2908705 | Condeúba | |
  | 2908804 | Contendas do Sincorá | |
  | 2908903 | Coração de Maria | |
  | 2909000 | Cordeiros | |
  | 2909109 | Coribe | |
  | 2909208 | Coronel João Sá | |
  | 2909307 | Correntina | |
  | 2909406 | Cotegipe | |
  | 2909505 | Cravolândia | |
  | 2909604 | Crisópolis | |
  | 2909703 | Cristópolis | |
  | 2909802 | Cruz das Almas | |
  | 2909901 | Curaçá | |
  | 2910008 | Dário Meira | |
  | 2910057 | Dias d'Ávila | |
  | 2910107 | Dom Basílio | |
  | 2910206 | Dom Macedo Costa | |
  | 2910305 | Elísio Medrado | |
  | 2910404 | Encruzilhada | |
  | 2910503 | Entre Rios | |
  | 2900504 | Érico Cardoso | |
  | 2910602 | Esplanada | |
  | 2910701 | Euclides da Cunha | |
  | 2910727 | Eunápolis | |
  | 2910750 | Fátima | |
  | 2910776 | Feira da Mata | |
  | 2910800 | Feira de Santana | [ba_feira_de_santana](data_collection/gazette/spiders/ba_feira_de_santana.py) |
  | 2910859 | Filadélfia | |
  | 2910909 | Firmino Alves | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2911006 | Floresta Azul | |
  | 2911105 | Formosa do Rio Preto | |
  | 2911204 | Gandu | |
  | 2911253 | Gavião | |
  | 2911303 | Gentio do Ouro | |
  | 2911402 | Glória | |
  | 2911501 | Gongogi | |
  | 2911600 | Governador Mangabeira | |
  | 2911659 | Guajeru | |
  | 2911709 | Guanambi | |
  | 2911808 | Guaratinga | |
  | 2911857 | Heliópolis | |
  | 2911907 | Iaçu | |
  | 2912004 | Ibiassucê | |
  | 2912103 | Ibicaraí | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2912202 | Ibicoara | |
  | 2912301 | Ibicuí | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2912400 | Ibipeba | |
  | 2912509 | Ibipitanga | |
  | 2912608 | Ibiquera | |
  | 2912707 | Ibirapitanga | |
  | 2912806 | Ibirapuã | |
  | 2912905 | Ibirataia | |
  | 2913002 | Ibitiara | |
  | 2913101 | Ibititá | |
  | 2913200 | Ibotirama | |
  | 2913309 | Ichu | |
  | 2913408 | Igaporã | |
  | 2913457 | Igrapiúna | |
  | 2913507 | Iguaí | |
  | 2913606 | Ilhéus | |
  | 2913705 | Inhambupe | |
  | 2913804 | Ipecaetá | |
  | 2913903 | Ipiaú | |
  | 2914000 | Ipirá | |
  | 2914109 | Ipupiara | |
  | 2914208 | Irajuba | |
  | 2914307 | Iramaia | |
  | 2914406 | Iraquara | |
  | 2914505 | Irará | |
  | 2914604 | Irecê | |
  | 2914653 | Itabela | |
  | 2914703 | Itaberaba | |
  | 2914802 | Itabuna | |
  | 2914901 | Itacaré | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2915007 | Itaeté | |
  | 2915106 | Itagi | |
  | 2915205 | Itagibá | |
  | 2915304 | Itagimirim | |
  | 2915353 | Itaguaçu da Bahia | |
  | 2915403 | Itaju do Colônia | |
  | 2915502 | Itajuípe | |
  | 2915601 | Itamaraju | |
  | 2915700 | Itamari | |
  | 2915809 | Itambé | |
  | 2915908 | Itanagra | |
  | 2916005 | Itanhém | |
  | 2916104 | Itaparica | |
  | 2916203 | Itapé | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2916302 | Itapebi | |
  | 2916401 | Itapetinga | |
  | 2916500 | Itapicuru | |
  | 2916609 | Itapitanga | |
  | 2916708 | Itaquara | |
  | 2916807 | Itarantim | |
  | 2916856 | Itatim | |
  | 2916906 | Itiruçu | |
  | 2917003 | Itiúba | |
  | 2917102 | Itororó | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2917201 | Ituaçu | |
  | 2917300 | Ituberá | |
  | 2917334 | Iuiú | |
  | 2917359 | Jaborandi | |
  | 2917409 | Jacaraci | |
  | 2917508 | Jacobina | |
  | 2917607 | Jaguaquara | |
  | 2917706 | Jaguarari | |
  | 2917805 | Jaguaripe | |
  | 2917904 | Jandaíra | |
  | 2918001 | Jequié | |
  | 2918100 | Jeremoabo | |
  | 2918209 | Jiquiriçá | |
  | 2918308 | Jitaúna | |
  | 2918357 | João Dourado | |
  | 2918407 | Juazeiro | |
  | 2918456 | Jucuruçu | |
  | 2918506 | Jussara | |
  | 2918555 | Jussari | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2918605 | Jussiape | |
  | 2918704 | Lafaiete Coutinho | |
  | 2918803 | Lagoa Real | |
  | 2918902 | Laje | |
  | 2919009 | Lajedão | |
  | 2919058 | Lajedinho | |
  | 2918753 | Lajedo do Tabocal | |
  | 2919108 | Lamarão | |
  | 2919157 | Lapão | |
  | 2919207 | Lauro de Freitas | |
  | 2919306 | Lençóis | |
  | 2919405 | Licínio de Almeida | |
  | 2919504 | Livramento de Nossa Senhora | |
  | 2919553 | Luís Eduardo Magalhães | |
  | 2919603 | Macajuba | |
  | 2919702 | Macarani | |
  | 2919801 | Macaúbas | |
  | 2919900 | Macururé | |
  | 2919926 | Madre de Deus | |
  | 2919959 | Maetinga | |
  | 2920007 | Maiquinique | |
  | 2920106 | Mairi | |
  | 2920205 | Malhada | |
  | 2920304 | Malhada de Pedras | |
  | 2920403 | Manoel Vitorino | |
  | 2920452 | Mansidão | |
  | 2920502 | Maracás | |
  | 2920601 | Maragogipe | |
  | 2920700 | Maraú | |
  | 2920809 | Marcionílio Souza | |
  | 2920908 | Mascote | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2921005 | Mata de São João | |
  | 2921054 | Matina | |
  | 2921104 | Medeiros Neto | |
  | 2921203 | Miguel Calmon | |
  | 2921302 | Milagres | |
  | 2921401 | Mirangaba | |
  | 2921450 | Mirante | |
  | 2921500 | Monte Santo | |
  | 2921609 | Morpará | |
  | 2921708 | Morro do Chapéu | |
  | 2921807 | Mortugaba | |
  | 2921906 | Mucugê | |
  | 2922003 | Mucuri | |
  | 2922052 | Mulungu do Morro | |
  | 2922102 | Mundo Novo | |
  | 2922201 | Muniz Ferreira | |
  | 2922250 | Muquém de São Francisco | |
  | 2922300 | Muritiba | |
  | 2922409 | Mutuípe | |
  | 2922508 | Nazaré | |
  | 2922607 | Nilo Peçanha | |
  | 2922656 | Nordestina | |
  | 2922706 | Nova Canaã | |
  | 2922730 | Nova Fátima | |
  | 2922755 | Nova Ibiá | |
  | 2922805 | Nova Itarana | |
  | 2922854 | Nova Redenção | |
  | 2922904 | Nova Soure | |
  | 2923001 | Nova Viçosa | |
  | 2923035 | Novo Horizonte | |
  | 2923050 | Novo Triunfo | |
  | 2923100 | Olindina | |
  | 2923209 | Oliveira dos Brejinhos | |
  | 2923308 | Ouriçangas | |
  | 2923357 | Ourolândia | |
  | 2923407 | Palmas de Monte Alto | |
  | 2923506 | Palmeiras | |
  | 2923605 | Paramirim | |
  | 2923704 | Paratinga | |
  | 2923803 | Paripiranga | |
  | 2923902 | Pau Brasil | |
  | 2924009 | Paulo Afonso | |
  | 2924058 | Pé de Serra | |
  | 2924108 | Pedrão | |
  | 2924207 | Pedro Alexandre | |
  | 2924306 | Piatã | |
  | 2924405 | Pilão Arcado | |
  | 2924504 | Pindaí | |
  | 2924603 | Pindobaçu | |
  | 2924652 | Pintadas | |
  | 2924678 | Piraí do Norte | |
  | 2924702 | Piripá | |
  | 2924801 | Piritiba | |
  | 2924900 | Planaltino | |
  | 2925006 | Planalto | |
  | 2925105 | Poções | |
  | 2925204 | Pojuca | |
  | 2925253 | Ponto Novo | |
  | 2925303 | Porto Seguro | |
  | 2925402 | Potiraguá | |
  | 2925501 | Prado | |
  | 2925600 | Presidente Dutra | |
  | 2925709 | Presidente Jânio Quadros | |
  | 2925758 | Presidente Tancredo Neves | |
  | 2925808 | Queimadas | |
  | 2925907 | Quijingue | |
  | 2925931 | Quixabeira | |
  | 2925956 | Rafael Jambeiro | |
  | 2926004 | Remanso | |
  | 2926103 | Retirolândia | |
  | 2926301 | Riachão do Jacuípe | |
  | 2926202 | Riachão das Neves | |
  | 2926400 | Riacho de Santana | |
  | 2926509 | Ribeira do Amparo | |
  | 2926608 | Ribeira do Pombal | |
  | 2926657 | Ribeirão do Largo | |
  | 2926806 | Rio do Antônio | |
  | 2926707 | Rio de Contas | |
  | 2926905 | Rio do Pires | |
  | 2927002 | Rio Real | |
  | 2927101 | Rodelas | |
  | 2927200 | Ruy Barbosa | |
  | 2927309 | Salinas da Margarida | |
  | 2927408 | Salvador | [ba_salvador](data_collection/gazette/spiders/ba_salvador.py) |
  | 2927507 | Santa Bárbara | |
  | 2927606 | Santa Brígida | |
  | 2927705 | Santa Cruz Cabrália | |
  | 2927804 | Santa Cruz da Vitória | |
  | 2927903 | Santa Inês | |
  | 2928059 | Santa Luzia | |
  | 2928109 | Santa Maria da Vitória | |
  | 2928406 | Santa Rita de Cássia | |
  | 2928505 | Santa Teresinha | |
  | 2928000 | Santaluz | |
  | 2928208 | Santana | |
  | 2928307 | Santanópolis | |
  | 2928604 | Santo Amaro | |
  | 2928703 | Santo Antônio de Jesus | |
  | 2928802 | Santo Estêvão | |
  | 2928901 | São Desidério | |
  | 2928950 | São Domingos | |
  | 2929107 | São Felipe | |
  | 2929008 | São Félix | |
  | 2929057 | São Félix do Coribe | |
  | 2929206 | São Francisco do Conde | |
  | 2929255 | São Gabriel | |
  | 2929305 | São Gonçalo dos Campos | |
  | 2929370 | São José do Jacuípe | |
  | 2929354 | São José da Vitória | |
  | 2929404 | São Miguel das Matas | |
  | 2929503 | São Sebastião do Passé | |
  | 2929602 | Sapeaçu | |
  | 2929701 | Sátiro Dias | |
  | 2929750 | Saubara | |
  | 2929800 | Saúde | |
  | 2929909 | Seabra | |
  | 2930006 | Sebastião Laranjeiras | |
  | 2930105 | Senhor do Bonfim | |
  | 2930204 | Sento Sé | |
  | 2930303 | Serra Dourada | |
  | 2930402 | Serra Preta | |
  | 2930154 | Serra do Ramalho | |
  | 2930501 | Serrinha | |
  | 2930600 | Serrolândia | |
  | 2930709 | Simões Filho | |
  | 2930758 | Sítio do Mato | |
  | 2930766 | Sítio do Quinto | |
  | 2930774 | Sobradinho | |
  | 2930808 | Souto Soares | |
  | 2930907 | Tabocas do Brejo Velho | |
  | 2931004 | Tanhaçu | |
  | 2931053 | Tanque Novo | |
  | 2931103 | Tanquinho | |
  | 2931202 | Taperoá | |
  | 2931301 | Tapiramutá | |
  | 2931350 | Teixeira de Freitas | |
  | 2931400 | Teodoro Sampaio | |
  | 2931509 | Teofilândia | |
  | 2931608 | Teolândia | |
  | 2931707 | Terra Nova | |
  | 2931806 | Tremedal | |
  | 2931905 | Tucano | |
  | 2932002 | Uauá | |
  | 2932101 | Ubaíra | |
  | 2932200 | Ubaitaba | |
  | 2932309 | Ubatã | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2932408 | Uibaí | |
  | 2932457 | Umburanas | |
  | 2932507 | Una | |
  | 2932606 | Urandi | |
  | 2932705 | Uruçuca | [ba_associacao_municipios](data_collection/gazette/spiders/ba_associacao_municipios.py) |
  | 2932804 | Utinga | |
  | 2932903 | Valença | |
  | 2933000 | Valente | |
  | 2933158 | Várzea Nova | |
  | 2933109 | Várzea do Poço | |
  | 2933059 | Várzea da Roça | |
  | 2933174 | Varzedo | |
  | 2933208 | Vera Cruz | |
  | 2933257 | Vereda | |
  | 2933307 | Vitória da Conquista | [ba_vitoria_da_conquista](data_collection/gazette/spiders/ba_vitoria_da_conquista.py) |
  | 2933406 | Wagner | |
  | 2933455 | Wanderley | |
  | 2933505 | Wenceslau Guimarães | |
  | 2933604 | Xique-Xique | |
</details>


### Ceará

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 2300101 | Abaiara | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2300150 | Acarape | |
  | 2300200 | Acaraú | |
  | 2300309 | Acopiara | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2300408 | Aiuaba | |
  | 2300507 | Alcântaras | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2300606 | Altaneira | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2300705 | Alto Santo | |
  | 2300754 | Amontada | |
  | 2300804 | Antonina do Norte | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2300903 | Apuiarés | |
  | 2301000 | Aquiraz | |
  | 2301109 | Aracati | |
  | 2301208 | Aracoiaba | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2301257 | Ararendá | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2301307 | Araripe | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2301406 | Aratuba | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2301505 | Arneiroz | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2301604 | Assaré | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2301703 | Aurora | |
  | 2301802 | Baixio | |
  | 2301851 | Banabuiú | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2301901 | Barbalha | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2301950 | Barreira | |
  | 2302008 | Barro | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2302057 | Barroquinha | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2302107 | Baturité | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2302206 | Beberibe | |
  | 2302305 | Bela Cruz | |
  | 2302404 | Boa Viagem | |
  | 2302503 | Brejo Santo | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2302602 | Camocim | |
  | 2302701 | Campos Sales | |
  | 2302800 | Canindé | |
  | 2302909 | Capistrano | |
  | 2303006 | Caridade | |
  | 2303105 | Cariré | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2303204 | Caririaçu | |
  | 2303303 | Cariús | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2303402 | Carnaubal | |
  | 2303501 | Cascavel | |
  | 2303600 | Catarina | |
  | 2303659 | Catunda | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2303709 | Caucaia | [ce_caucaia](data_collection/gazette/spiders/ce_caucaia.py) |
  | 2303808 | Cedro | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2303907 | Chaval | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2303931 | Choró | |
  | 2303956 | Chorozinho | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304004 | Coreaú | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304103 | Crateús | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304202 | Crato | |
  | 2304236 | Croatá | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304251 | Cruz | |
  | 2304269 | Deputado Irapuan Pinheiro | |
  | 2304277 | Ererê | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304285 | Eusébio | |
  | 2304301 | Farias Brito | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304350 | Forquilha | |
  | 2304400 | Fortaleza | [ce_fortaleza](data_collection/gazette/spiders/ce_fortaleza.py) |
  | 2304459 | Fortim | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304509 | Frecheirinha | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304608 | General Sampaio | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304657 | Graça | |
  | 2304707 | Granja | |
  | 2304806 | Granjeiro | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304905 | Groaíras | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2304954 | Guaiúba | |
  | 2305001 | Guaraciaba do Norte | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305100 | Guaramiranga | |
  | 2305209 | Hidrolândia | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305233 | Horizonte | |
  | 2305266 | Ibaretama | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305308 | Ibiapina | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305332 | Ibicuitinga | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305357 | Icapuí | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305407 | Icó | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305506 | Iguatu | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305605 | Independência | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305654 | Ipaporanga | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305704 | Ipaumirim | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2305803 | Ipu | |
  | 2305902 | Ipueiras | |
  | 2306009 | Iracema | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2306108 | Irauçuba | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2306207 | Itaiçaba | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2306256 | Itaitinga | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2306306 | Itapajé | |
  | 2306405 | Itapipoca | |
  | 2306504 | Itapiúna | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2306553 | Itarema | |
  | 2306603 | Itatira | |
  | 2306702 | Jaguaretama | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2306801 | Jaguaribara | |
  | 2306900 | Jaguaribe | |
  | 2307007 | Jaguaruana | |
  | 2307106 | Jardim | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2307205 | Jati | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2307254 | Jijoca de Jericoacoara | |
  | 2307304 | Juazeiro do Norte | |
  | 2307403 | Jucás | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2307502 | Lavras da Mangabeira | |
  | 2307601 | Limoeiro do Norte | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2307635 | Madalena | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2307650 | Maracanaú | |
  | 2307700 | Maranguape | |
  | 2307809 | Marco | |
  | 2307908 | Martinópole | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2308005 | Massapê | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2308104 | Mauriti | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2308203 | Meruoca | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2308302 | Milagres | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2308351 | Milhã | |
  | 2308377 | Miraíma | |
  | 2308401 | Missão Velha | |
  | 2308500 | Mombaça | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2308609 | Monsenhor Tabosa | |
  | 2308708 | Morada Nova | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2308807 | Moraújo | |
  | 2308906 | Morrinhos | |
  | 2309003 | Mucambo | |
  | 2309102 | Mulungu | |
  | 2309201 | Nova Olinda | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2309300 | Nova Russas | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2309409 | Novo Oriente | |
  | 2309458 | Ocara | |
  | 2309508 | Orós | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2309607 | Pacajus | |
  | 2309706 | Pacatuba | |
  | 2309805 | Pacoti | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2309904 | Pacujá | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2310001 | Palhano | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2310100 | Palmácia | |
  | 2310209 | Paracuru | |
  | 2310258 | Paraipaba | |
  | 2310308 | Parambu | |
  | 2310407 | Paramoti | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2310506 | Pedra Branca | |
  | 2310605 | Penaforte | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2310704 | Pentecoste | |
  | 2310803 | Pereiro | |
  | 2310852 | Pindoretama | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2310902 | Piquet Carneiro | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2310951 | Pires Ferreira | |
  | 2311009 | Poranga | |
  | 2311108 | Porteiras | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2311207 | Potengi | |
  | 2311231 | Potiretama | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2311264 | Quiterianópolis | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2311306 | Quixadá | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2311355 | Quixelô | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2311405 | Quixeramobim | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2311504 | Quixeré | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2311603 | Redenção | |
  | 2311702 | Reriutaba | |
  | 2311801 | Russas | |
  | 2311900 | Saboeiro | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2311959 | Salitre | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2312205 | Santa Quitéria | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2312007 | Santana do Acaraú | |
  | 2312106 | Santana do Cariri | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2312304 | São Benedito | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2312403 | São Gonçalo do Amarante | |
  | 2312502 | São João do Jaguaribe | |
  | 2312601 | São Luís do Curu | |
  | 2312700 | Senador Pompeu | |
  | 2312809 | Senador Sá | |
  | 2312908 | Sobral | |
  | 2313005 | Solonópole | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2313104 | Tabuleiro do Norte | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2313203 | Tamboril | |
  | 2313252 | Tarrafas | |
  | 2313302 | Tauá | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2313351 | Tejuçuoca | |
  | 2313401 | Tianguá | |
  | 2313500 | Trairi | |
  | 2313559 | Tururu | |
  | 2313609 | Ubajara | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2313708 | Umari | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2313757 | Umirim | |
  | 2313807 | Uruburetama | |
  | 2313906 | Uruoca | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2313955 | Varjota | |
  | 2314003 | Várzea Alegre | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
  | 2314102 | Viçosa do Ceará | [ce_associacao_municipios](data_collection/gazette/spiders/ce_associacao_municipios.py) |
</details>


### Distrito Federal

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 5300108 | Brasília | [df_brasilia](data_collection/gazette/spiders/df_brasilia.py) |
</details>


### Espírito Santo

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 3200102 | Afonso Cláudio | |
  | 3200169 | Água Doce do Norte | |
  | 3200136 | Águia Branca | |
  | 3200201 | Alegre | |
  | 3200300 | Alfredo Chaves | |
  | 3200359 | Alto Rio Novo | |
  | 3200409 | Anchieta | |
  | 3200508 | Apiacá | |
  | 3200607 | Aracruz | |
  | 3200706 | Atilio Vivacqua | |
  | 3200805 | Baixo Guandu | |
  | 3200904 | Barra de São Francisco | |
  | 3201001 | Boa Esperança | |
  | 3201100 | Bom Jesus do Norte | |
  | 3201159 | Brejetuba | |
  | 3201209 | Cachoeiro de Itapemirim | |
  | 3201308 | Cariacica | |
  | 3201407 | Castelo | |
  | 3201506 | Colatina | |
  | 3201605 | Conceição da Barra | |
  | 3201704 | Conceição do Castelo | |
  | 3201803 | Divino de São Lourenço | |
  | 3201902 | Domingos Martins | |
  | 3202009 | Dores do Rio Preto | |
  | 3202108 | Ecoporanga | |
  | 3202207 | Fundão | |
  | 3202256 | Governador Lindenberg | |
  | 3202306 | Guaçuí | |
  | 3202405 | Guarapari | |
  | 3202454 | Ibatiba | |
  | 3202504 | Ibiraçu | |
  | 3202553 | Ibitirama | |
  | 3202603 | Iconha | |
  | 3202652 | Irupi | |
  | 3202702 | Itaguaçu | |
  | 3202801 | Itapemirim | |
  | 3202900 | Itarana | |
  | 3203007 | Iúna | |
  | 3203056 | Jaguaré | |
  | 3203106 | Jerônimo Monteiro | |
  | 3203130 | João Neiva | |
  | 3203163 | Laranja da Terra | |
  | 3203205 | Linhares | |
  | 3203304 | Mantenópolis | |
  | 3203320 | Marataízes | |
  | 3203346 | Marechal Floriano | |
  | 3203353 | Marilândia | |
  | 3203403 | Mimoso do Sul | |
  | 3203502 | Montanha | |
  | 3203601 | Mucurici | |
  | 3203700 | Muniz Freire | |
  | 3203809 | Muqui | |
  | 3203908 | Nova Venécia | |
  | 3204005 | Pancas | |
  | 3204054 | Pedro Canário | |
  | 3204104 | Pinheiros | |
  | 3204203 | Piúma | |
  | 3204252 | Ponto Belo | |
  | 3204302 | Presidente Kennedy | |
  | 3204351 | Rio Bananal | |
  | 3204401 | Rio Novo do Sul | |
  | 3204500 | Santa Leopoldina | |
  | 3204559 | Santa Maria de Jetibá | |
  | 3204609 | Santa Teresa | |
  | 3204658 | São Domingos do Norte | |
  | 3204708 | São Gabriel da Palha | |
  | 3204807 | São José do Calçado | |
  | 3204906 | São Mateus | |
  | 3204955 | São Roque do Canaã | |
  | 3205002 | Serra | |
  | 3205010 | Sooretama | |
  | 3205036 | Vargem Alta | |
  | 3205069 | Venda Nova do Imigrante | |
  | 3205101 | Viana | |
  | 3205150 | Vila Pavão | |
  | 3205176 | Vila Valério | |
  | 3205200 | Vila Velha | |
  | 3205309 | Vitória | |
</details>


### Goiás

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 5200050 | Abadia de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5200100 | Abadiânia | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5200134 | Acreúna | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py), [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5200159 | Adelândia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5200175 | Água Fria de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5200209 | Água Limpa | |
  | 5200258 | Águas Lindas de Goiás | |
  | 5200308 | Alexânia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5200506 | Aloândia | |
  | 5200555 | Alto Horizonte | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5200605 | Alto Paraíso de Goiás | |
  | 5200803 | Alvorada do Norte | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5200829 | Amaralina | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5200852 | Americano do Brasil | |
  | 5200902 | Amorinópolis | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5201108 | Anápolis | |
  | 5201207 | Anhanguera | |
  | 5201306 | Anicuns | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5201405 | Aparecida de Goiânia | [go_aparecida_de_goiania](data_collection/gazette/spiders/go_aparecida_de_goiania.py) |
  | 5201454 | Aparecida do Rio Doce | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5201504 | Aporé | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5201603 | Araçu | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5201702 | Aragarças | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5201801 | Aragoiânia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5202155 | Araguapaz | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5202353 | Arenópolis | |
  | 5202502 | Aruanã | |
  | 5202601 | Aurilândia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py), [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5202809 | Avelinópolis | |
  | 5203104 | Baliza | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5203203 | Barro Alto | |
  | 5203302 | Bela Vista de Goiás | |
  | 5203401 | Bom Jardim de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5203500 | Bom Jesus de Goiás | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5203559 | Bonfinópolis | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5203575 | Bonópolis | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5203609 | Brazabrantes | |
  | 5203807 | Britânia | |
  | 5203906 | Buriti Alegre | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5203939 | Buriti de Goiás | |
  | 5203962 | Buritinópolis | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5204003 | Cabeceiras | |
  | 5204102 | Cachoeira Alta | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5204250 | Cachoeira Dourada | |
  | 5204201 | Cachoeira de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py), [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5204300 | Caçu | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py), [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5204409 | Caiapônia | |
  | 5204508 | Caldas Novas | |
  | 5204557 | Caldazinha | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5204607 | Campestre de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5204656 | Campinaçu | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5204706 | Campinorte | |
  | 5204805 | Campo Alegre de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5204854 | Campo Limpo de Goiás | |
  | 5204904 | Campos Belos | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5204953 | Campos Verdes | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5205000 | Carmo do Rio Verde | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5205059 | Castelândia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5205109 | Catalão | |
  | 5205208 | Caturaí | |
  | 5205307 | Cavalcante | |
  | 5205406 | Ceres | |
  | 5205455 | Cezarina | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5205471 | Chapadão do Céu | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5205497 | Cidade Ocidental | |
  | 5205513 | Cocalzinho de Goiás | |
  | 5205521 | Colinas do Sul | |
  | 5205703 | Córrego do Ouro | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5205802 | Corumbá de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5205901 | Corumbaíba | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5206206 | Cristalina | |
  | 5206305 | Cristianópolis | |
  | 5206404 | Crixás | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5206503 | Cromínia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5206602 | Cumari | |
  | 5206701 | Damianópolis | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5206800 | Damolândia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5206909 | Davinópolis | |
  | 5207105 | Diorama | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5208301 | Divinópolis de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5207253 | Doverlândia | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5207352 | Edealina | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5207402 | Edéia | |
  | 5207501 | Estrela do Norte | |
  | 5207535 | Faina | |
  | 5207600 | Fazenda Nova | |
  | 5207808 | Firminópolis | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5207907 | Flores de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5208004 | Formosa | |
  | 5208103 | Formoso | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5208152 | Gameleira de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5208400 | Goianápolis | |
  | 5208509 | Goiandira | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5208608 | Goianésia | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5208707 | Goiânia | [go_goiania](data_collection/gazette/spiders/go_goiania.py) |
  | 5208806 | Goianira | |
  | 5208905 | Goiás | |
  | 5209101 | Goiatuba | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5209150 | Gouvelândia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5209200 | Guapó | |
  | 5209291 | Guaraíta | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5209408 | Guarani de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5209457 | Guarinos | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5209606 | Heitoraí | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py), [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5209705 | Hidrolândia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5209804 | Hidrolina | |
  | 5209903 | Iaciara | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5209937 | Inaciolândia | |
  | 5209952 | Indiara | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5210000 | Inhumas | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5210109 | Ipameri | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5210158 | Ipiranga de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5210208 | Iporá | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5210307 | Israelândia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5210406 | Itaberaí | |
  | 5210562 | Itaguari | |
  | 5210604 | Itaguaru | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5210802 | Itajá | |
  | 5210901 | Itapaci | |
  | 5211008 | Itapirapuã | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5211206 | Itapuranga | |
  | 5211305 | Itarumã | |
  | 5211404 | Itauçu | |
  | 5211503 | Itumbiara | |
  | 5211602 | Ivolândia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5211701 | Jandaia | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5211800 | Jaraguá | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5211909 | Jataí | |
  | 5212006 | Jaupaci | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5212055 | Jesúpolis | |
  | 5212105 | Joviânia | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5212204 | Jussara | |
  | 5212253 | Lagoa Santa | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5212303 | Leopoldo de Bulhões | |
  | 5212501 | Luziânia | |
  | 5212600 | Mairipotaba | |
  | 5212709 | Mambaí | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5212808 | Mara Rosa | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5212907 | Marzagão | |
  | 5212956 | Matrinchã | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5213004 | Maurilândia | |
  | 5213053 | Mimoso de Goiás | |
  | 5213087 | Minaçu | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5213103 | Mineiros | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5213400 | Moiporá | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5213509 | Monte Alegre de Goiás | |
  | 5213707 | Montes Claros de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5213756 | Montividiu | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5213772 | Montividiu do Norte | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5213806 | Morrinhos | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5213855 | Morro Agudo de Goiás | |
  | 5213905 | Mossâmedes | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5214002 | Mozarlândia | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5214051 | Mundo Novo | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5214101 | Mutunópolis | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5214408 | Nazário | |
  | 5214507 | Nerópolis | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5214606 | Niquelândia | |
  | 5214705 | Nova América | |
  | 5214804 | Nova Aurora | |
  | 5214838 | Nova Crixás | |
  | 5214861 | Nova Glória | |
  | 5214879 | Nova Iguaçu de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5214903 | Nova Roma | |
  | 5215009 | Nova Veneza | |
  | 5215207 | Novo Brasil | |
  | 5215231 | Novo Gama | |
  | 5215256 | Novo Planalto | |
  | 5215306 | Orizona | |
  | 5215405 | Ouro Verde de Goiás | |
  | 5215504 | Ouvidor | |
  | 5215603 | Padre Bernardo | |
  | 5215652 | Palestina de Goiás | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5215702 | Palmeiras de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5215801 | Palmelo | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5215900 | Palminópolis | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5216007 | Panamá | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5216304 | Paranaiguara | |
  | 5216403 | Paraúna | |
  | 5216452 | Perolândia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5216809 | Petrolina de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5216908 | Pilar de Goiás | |
  | 5217104 | Piracanjuba | |
  | 5217203 | Piranhas | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5217302 | Pirenópolis | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5217401 | Pires do Rio | |
  | 5217609 | Planaltina | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5217708 | Pontalina | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5218003 | Porangatu | |
  | 5218052 | Porteirão | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5218102 | Portelândia | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5218300 | Posse | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5218391 | Professor Jamil | |
  | 5218508 | Quirinópolis | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5218607 | Rialma | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5218706 | Rianápolis | |
  | 5218789 | Rio Quente | |
  | 5218805 | Rio Verde | |
  | 5218904 | Rubiataba | |
  | 5219001 | Sanclerlândia | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5219100 | Santa Bárbara de Goiás | |
  | 5219209 | Santa Cruz de Goiás | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5219258 | Santa Fé de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5219308 | Santa Helena de Goiás | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5219357 | Santa Isabel | |
  | 5219407 | Santa Rita do Araguaia | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5219456 | Santa Rita do Novo Destino | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5219506 | Santa Rosa de Goiás | |
  | 5219605 | Santa Tereza de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5219704 | Santa Terezinha de Goiás | |
  | 5219712 | Santo Antônio da Barra | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5219753 | Santo Antônio do Descoberto | |
  | 5219738 | Santo Antônio de Goiás | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5219803 | São Domingos | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5219902 | São Francisco de Goiás | |
  | 5220009 | São João d'Aliança | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5220058 | São João da Paraúna | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5220108 | São Luís de Montes Belos | |
  | 5220157 | São Luiz do Norte | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5220207 | São Miguel do Araguaia | |
  | 5220264 | São Miguel do Passa Quatro | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5220280 | São Patrício | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5220405 | São Simão | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5220454 | Senador Canedo | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5220504 | Serranópolis | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5220603 | Silvânia | |
  | 5220686 | Simolândia | |
  | 5220702 | Sítio d'Abadia | |
  | 5221007 | Taquaral de Goiás | |
  | 5221080 | Teresina de Goiás | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5221197 | Terezópolis de Goiás | |
  | 5221304 | Três Ranchos | |
  | 5221403 | Trindade | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5221452 | Trombas | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5221502 | Turvânia | |
  | 5221551 | Turvelândia | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5221577 | Uirapuru | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5221601 | Uruaçu | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5221700 | Uruana | [go_associacao_municipios_agm](data_collection/gazette/spiders/go_associacao_municipios_agm.py) |
  | 5221809 | Urutaí | |
  | 5221858 | Valparaíso de Goiás | |
  | 5221908 | Varjão | [go_associacao_municipios_fgm](data_collection/gazette/spiders/go_associacao_municipios_fgm.py) |
  | 5222005 | Vianópolis | |
  | 5222054 | Vicentinópolis | |
  | 5222203 | Vila Boa | |
  | 5222302 | Vila Propício | |
</details>


### Maranhão

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 2100055 | Açailândia | |
  | 2100105 | Afonso Cunha | |
  | 2100154 | Água Doce do Maranhão | |
  | 2100204 | Alcântara | |
  | 2100303 | Aldeias Altas | |
  | 2100402 | Altamira do Maranhão | |
  | 2100436 | Alto Alegre do Maranhão | |
  | 2100477 | Alto Alegre do Pindaré | |
  | 2100501 | Alto Parnaíba | |
  | 2100550 | Amapá do Maranhão | |
  | 2100600 | Amarante do Maranhão | |
  | 2100709 | Anajatuba | |
  | 2100808 | Anapurus | |
  | 2100832 | Apicum-Açu | |
  | 2100873 | Araguanã | |
  | 2100907 | Araioses | |
  | 2100956 | Arame | |
  | 2101004 | Arari | |
  | 2101103 | Axixá | |
  | 2101202 | Bacabal | |
  | 2101251 | Bacabeira | |
  | 2101301 | Bacuri | |
  | 2101350 | Bacurituba | |
  | 2101400 | Balsas | |
  | 2101509 | Barão de Grajaú | |
  | 2101608 | Barra do Corda | |
  | 2101707 | Barreirinhas | |
  | 2101772 | Bela Vista do Maranhão | |
  | 2101731 | Belágua | |
  | 2101806 | Benedito Leite | |
  | 2101905 | Bequimão | |
  | 2101939 | Bernardo do Mearim | |
  | 2101970 | Boa Vista do Gurupi | |
  | 2102002 | Bom Jardim | |
  | 2102036 | Bom Jesus das Selvas | |
  | 2102077 | Bom Lugar | |
  | 2102101 | Brejo | |
  | 2102150 | Brejo de Areia | |
  | 2102200 | Buriti | |
  | 2102309 | Buriti Bravo | |
  | 2102325 | Buriticupu | |
  | 2102358 | Buritirana | |
  | 2102374 | Cachoeira Grande | |
  | 2102408 | Cajapió | |
  | 2102507 | Cajari | |
  | 2102556 | Campestre do Maranhão | |
  | 2102606 | Cândido Mendes | |
  | 2102705 | Cantanhede | |
  | 2102754 | Capinzal do Norte | |
  | 2102804 | Carolina | |
  | 2102903 | Carutapera | |
  | 2103000 | Caxias | |
  | 2103109 | Cedral | |
  | 2103125 | Central do Maranhão | |
  | 2103158 | Centro do Guilherme | |
  | 2103174 | Centro Novo do Maranhão | |
  | 2103208 | Chapadinha | |
  | 2103257 | Cidelândia | |
  | 2103307 | Codó | |
  | 2103406 | Coelho Neto | |
  | 2103505 | Colinas | |
  | 2103554 | Conceição do Lago-Açu | |
  | 2103604 | Coroatá | |
  | 2103703 | Cururupu | |
  | 2103752 | Davinópolis | |
  | 2103802 | Dom Pedro | |
  | 2103901 | Duque Bacelar | |
  | 2104008 | Esperantinópolis | |
  | 2104057 | Estreito | |
  | 2104073 | Feira Nova do Maranhão | |
  | 2104081 | Fernando Falcão | |
  | 2104099 | Formosa da Serra Negra | |
  | 2104107 | Fortaleza dos Nogueiras | |
  | 2104206 | Fortuna | |
  | 2104305 | Godofredo Viana | |
  | 2104404 | Gonçalves Dias | |
  | 2104503 | Governador Archer | |
  | 2104552 | Governador Edison Lobão | |
  | 2104602 | Governador Eugênio Barros | |
  | 2104628 | Governador Luiz Rocha | |
  | 2104651 | Governador Newton Bello | |
  | 2104677 | Governador Nunes Freire | |
  | 2104701 | Graça Aranha | |
  | 2104800 | Grajaú | |
  | 2104909 | Guimarães | |
  | 2105005 | Humberto de Campos | |
  | 2105104 | Icatu | |
  | 2105203 | Igarapé Grande | |
  | 2105153 | Igarapé do Meio | |
  | 2105302 | Imperatriz | |
  | 2105351 | Itaipava do Grajaú | |
  | 2105401 | Itapecuru Mirim | |
  | 2105427 | Itinga do Maranhão | |
  | 2105450 | Jatobá | |
  | 2105476 | Jenipapo dos Vieiras | |
  | 2105500 | João Lisboa | |
  | 2105609 | Joselândia | |
  | 2105658 | Junco do Maranhão | |
  | 2105807 | Lago do Junco | |
  | 2105708 | Lago da Pedra | |
  | 2105948 | Lago dos Rodrigues | |
  | 2105906 | Lago Verde | |
  | 2105963 | Lagoa Grande do Maranhão | |
  | 2105922 | Lagoa do Mato | |
  | 2105989 | Lajeado Novo | |
  | 2106003 | Lima Campos | |
  | 2106102 | Loreto | |
  | 2106201 | Luís Domingues | |
  | 2106300 | Magalhães de Almeida | |
  | 2106326 | Maracaçumé | |
  | 2106359 | Marajá do Sena | |
  | 2106375 | Maranhãozinho | |
  | 2106409 | Mata Roma | |
  | 2106508 | Matinha | |
  | 2106607 | Matões | |
  | 2106631 | Matões do Norte | |
  | 2106672 | Milagres do Maranhão | |
  | 2106706 | Mirador | |
  | 2106755 | Miranda do Norte | |
  | 2106805 | Mirinzal | |
  | 2106904 | Monção | |
  | 2107001 | Montes Altos | |
  | 2107100 | Morros | |
  | 2107209 | Nina Rodrigues | |
  | 2107258 | Nova Colinas | |
  | 2107308 | Nova Iorque | |
  | 2107357 | Nova Olinda do Maranhão | |
  | 2107407 | Olho d'Água das Cunhãs | |
  | 2107456 | Olinda Nova do Maranhão | |
  | 2107506 | Paço do Lumiar | |
  | 2107605 | Palmeirândia | |
  | 2107704 | Paraibano | |
  | 2107803 | Parnarama | |
  | 2107902 | Passagem Franca | |
  | 2108009 | Pastos Bons | |
  | 2108058 | Paulino Neves | |
  | 2108108 | Paulo Ramos | |
  | 2108207 | Pedreiras | |
  | 2108256 | Pedro do Rosário | |
  | 2108306 | Penalva | |
  | 2108405 | Peri Mirim | |
  | 2108454 | Peritoró | |
  | 2108504 | Pindaré-Mirim | |
  | 2108603 | Pinheiro | |
  | 2108702 | Pio XII | |
  | 2108801 | Pirapemas | |
  | 2108900 | Poção de Pedras | |
  | 2109007 | Porto Franco | |
  | 2109056 | Porto Rico do Maranhão | |
  | 2109106 | Presidente Dutra | |
  | 2109205 | Presidente Juscelino | |
  | 2109239 | Presidente Médici | |
  | 2109270 | Presidente Sarney | |
  | 2109304 | Presidente Vargas | |
  | 2109403 | Primeira Cruz | |
  | 2109452 | Raposa | |
  | 2109502 | Riachão | |
  | 2109551 | Ribamar Fiquene | |
  | 2109601 | Rosário | |
  | 2109700 | Sambaíba | |
  | 2109759 | Santa Filomena do Maranhão | |
  | 2109809 | Santa Helena | |
  | 2109908 | Santa Inês | |
  | 2110005 | Santa Luzia | |
  | 2110039 | Santa Luzia do Paruá | |
  | 2110104 | Santa Quitéria do Maranhão | |
  | 2110203 | Santa Rita | |
  | 2110237 | Santana do Maranhão | |
  | 2110278 | Santo Amaro do Maranhão | |
  | 2110302 | Santo Antônio dos Lopes | |
  | 2110401 | São Benedito do Rio Preto | |
  | 2110500 | São Bento | |
  | 2110609 | São Bernardo | |
  | 2110658 | São Domingos do Azeitão | |
  | 2110708 | São Domingos do Maranhão | |
  | 2110807 | São Félix de Balsas | |
  | 2110856 | São Francisco do Brejão | |
  | 2110906 | São Francisco do Maranhão | |
  | 2111003 | São João Batista | |
  | 2111029 | São João do Carú | |
  | 2111052 | São João do Paraíso | |
  | 2111102 | São João dos Patos | |
  | 2111078 | São João do Soter | |
  | 2111250 | São José dos Basílios | |
  | 2111201 | São José de Ribamar | |
  | 2111300 | São Luís | |
  | 2111409 | São Luís Gonzaga do Maranhão | |
  | 2111508 | São Mateus do Maranhão | |
  | 2111532 | São Pedro da Água Branca | |
  | 2111573 | São Pedro dos Crentes | |
  | 2111631 | São Raimundo do Doca Bezerra | |
  | 2111607 | São Raimundo das Mangabeiras | |
  | 2111672 | São Roberto | |
  | 2111706 | São Vicente Ferrer | |
  | 2111722 | Satubinha | |
  | 2111748 | Senador Alexandre Costa | |
  | 2111763 | Senador La Rocque | |
  | 2111789 | Serrano do Maranhão | |
  | 2111805 | Sítio Novo | |
  | 2111904 | Sucupira do Norte | |
  | 2111953 | Sucupira do Riachão | |
  | 2112001 | Tasso Fragoso | |
  | 2112100 | Timbiras | |
  | 2112209 | Timon | |
  | 2112233 | Trizidela do Vale | |
  | 2112274 | Tufilândia | |
  | 2112308 | Tuntum | |
  | 2112407 | Turiaçu | |
  | 2112456 | Turilândia | |
  | 2112506 | Tutóia | |
  | 2112605 | Urbano Santos | |
  | 2112704 | Vargem Grande | |
  | 2112803 | Viana | |
  | 2112852 | Vila Nova dos Martírios | |
  | 2112902 | Vitória do Mearim | |
  | 2113009 | Vitorino Freire | |
  | 2114007 | Zé Doca | |
</details>


### Mato Grosso

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 5100102 | Acorizal | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5100201 | Água Boa | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5100250 | Alta Floresta | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5100300 | Alto Araguaia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5100359 | Alto Boa Vista | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5100409 | Alto Garças | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5100508 | Alto Paraguai | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5100607 | Alto Taquari | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5100805 | Apiacás | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5101001 | Araguaiana | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5101209 | Araguainha | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5101258 | Araputanga | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5101308 | Arenápolis | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5101407 | Aripuanã | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5101605 | Barão de Melgaço | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5101704 | Barra do Bugres | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5101803 | Barra do Garças | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5101852 | Bom Jesus do Araguaia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5101902 | Brasnorte | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5102504 | Cáceres | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5102603 | Campinápolis | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5102637 | Campo Novo do Parecis | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5102678 | Campo Verde | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5102686 | Campos de Júlio | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5102694 | Canabrava do Norte | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5102702 | Canarana | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5102793 | Carlinda | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5102850 | Castanheira | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103007 | Chapada dos Guimarães | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103056 | Cláudia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103106 | Cocalinho | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103205 | Colíder | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103254 | Colniza | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103304 | Comodoro | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103353 | Confresa | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103361 | Conquista D'Oeste | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103379 | Cotriguaçu | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103403 | Cuiabá | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py), [mt_cuiaba](data_collection/gazette/spiders/mt_cuiaba.py) |
  | 5103437 | Curvelândia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103452 | Denise | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103502 | Diamantino | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103601 | Dom Aquino | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103700 | Feliz Natal | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103809 | Figueirópolis D'Oeste | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103858 | Gaúcha do Norte | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103908 | General Carneiro | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5103957 | Glória D'Oeste | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5104104 | Guarantã do Norte | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5104203 | Guiratinga | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5104500 | Indiavaí | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5104526 | Ipiranga do Norte | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5104542 | Itanhangá | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5104559 | Itaúba | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5104609 | Itiquira | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5104807 | Jaciara | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5104906 | Jangada | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105002 | Jauru | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105101 | Juara | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105150 | Juína | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105176 | Juruena | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105200 | Juscimeira | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105234 | Lambari D'Oeste | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105259 | Lucas do Rio Verde | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105309 | Luciara | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105580 | Marcelândia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105606 | Matupá | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105622 | Mirassol d'Oeste | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105903 | Nobres | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106000 | Nortelândia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106109 | Nossa Senhora do Livramento | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106158 | Nova Bandeirantes | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106208 | Nova Brasilândia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106216 | Nova Canaã do Norte | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108808 | Nova Guarita | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106182 | Nova Lacerda | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108857 | Nova Marilândia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108907 | Nova Maringá | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108956 | Nova Monte Verde | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106224 | Nova Mutum | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106174 | Nova Nazaré | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106232 | Nova Olímpia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106190 | Nova Santa Helena | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106240 | Nova Ubiratã | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106257 | Nova Xavantina | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106273 | Novo Horizonte do Norte | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106265 | Novo Mundo | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106315 | Novo Santo Antônio | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106281 | Novo São Joaquim | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106299 | Paranaíta | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106307 | Paranatinga | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106372 | Pedra Preta | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106422 | Peixoto de Azevedo | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106455 | Planalto da Serra | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106505 | Poconé | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106653 | Pontal do Araguaia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106703 | Ponte Branca | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106752 | Pontes e Lacerda | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106778 | Porto Alegre do Norte | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106828 | Porto Esperidião | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106851 | Porto Estrela | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5106802 | Porto dos Gaúchos | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107008 | Poxoréu | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107040 | Primavera do Leste | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107065 | Querência | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107156 | Reserva do Cabaçal | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107180 | Ribeirão Cascalheira | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107198 | Ribeirãozinho | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107206 | Rio Branco | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107578 | Rondolândia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107602 | Rondonópolis | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107701 | Rosário Oeste | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107750 | Salto do Céu | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107248 | Santa Carmem | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107743 | Santa Cruz do Xingu | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107768 | Santa Rita do Trivelato | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107776 | Santa Terezinha | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107263 | Santo Afonso | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107792 | Santo Antônio do Leste | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107800 | Santo Antônio do Leverger | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107859 | São Félix do Araguaia | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107297 | São José do Povo | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107107 | São José dos Quatro Marcos | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107305 | São José do Rio Claro | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107354 | São José do Xingu | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107404 | São Pedro da Cipa | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107875 | Sapezal | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107883 | Serra Nova Dourada | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107909 | Sinop | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107925 | Sorriso | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107941 | Tabaporã | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5107958 | Tangará da Serra | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108006 | Tapurah | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108055 | Terra Nova do Norte | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108105 | Tesouro | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108204 | Torixoréu | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108303 | União do Sul | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108352 | Vale de São Domingos | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108402 | Várzea Grande | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108501 | Vera | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5105507 | Vila Bela da Santíssima Trindade | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5108600 | Vila Rica | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
</details>


### Mato Grosso do Sul

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 5000203 | Água Clara | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5000252 | Alcinópolis | |
  | 5000609 | Amambai | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5000708 | Anastácio | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5000807 | Anaurilândia | |
  | 5000856 | Angélica | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5000906 | Antônio João | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5001003 | Aparecida do Taboado | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5001102 | Aquidauana | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5001243 | Aral Moreira | |
  | 5001508 | Bandeirantes | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5001904 | Bataguassu | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5002001 | Batayporã | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5002100 | Bela Vista | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5002159 | Bodoquena | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5002209 | Bonito | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5002308 | Brasilândia | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5002407 | Caarapó | |
  | 5002605 | Camapuã | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5002704 | Campo Grande | [ms_campo_grande](data_collection/gazette/spiders/ms_campo_grande.py) |
  | 5002803 | Caracol | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5002902 | Cassilândia | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5002951 | Chapadão do Sul | |
  | 5003108 | Corguinho | |
  | 5003157 | Coronel Sapucaia | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5003207 | Corumbá | |
  | 5003256 | Costa Rica | |
  | 5003306 | Coxim | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5003454 | Deodápolis | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5003488 | Dois Irmãos do Buriti | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5003504 | Douradina | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5003702 | Dourados | |
  | 5003751 | Eldorado | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5003801 | Fátima do Sul | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5003900 | Figueirão | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5004007 | Glória de Dourados | |
  | 5004106 | Guia Lopes da Laguna | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5004304 | Iguatemi | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5004403 | Inocência | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py), [ms_inocencia](data_collection/gazette/spiders/ms_inocencia.py) |
  | 5004502 | Itaporã | |
  | 5004601 | Itaquiraí | |
  | 5004700 | Ivinhema | |
  | 5004809 | Japorã | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5004908 | Jaraguari | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5005004 | Jardim | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5005103 | Jateí | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5005152 | Juti | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5005202 | Ladário | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5005251 | Laguna Carapã | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5005400 | Maracaju | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py), [ms_maracaju](data_collection/gazette/spiders/ms_maracaju.py) |
  | 5005608 | Miranda | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5005681 | Mundo Novo | |
  | 5005707 | Naviraí | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5005806 | Nioaque | |
  | 5006002 | Nova Alvorada do Sul | |
  | 5006200 | Nova Andradina | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5006259 | Novo Horizonte do Sul | |
  | 5006275 | Paraíso das Águas | |
  | 5006309 | Paranaíba | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5006358 | Paranhos | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5006408 | Pedro Gomes | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5006606 | Ponta Porã | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5006903 | Porto Murtinho | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5007109 | Ribas do Rio Pardo | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5007208 | Rio Brilhante | |
  | 5007307 | Rio Negro | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5007406 | Rio Verde de Mato Grosso | [mt_associacao_municipios](data_collection/gazette/spiders/mt_associacao_municipios.py) |
  | 5007505 | Rochedo | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5007554 | Santa Rita do Pardo | |
  | 5007695 | São Gabriel do Oeste | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5007802 | Selvíria | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5007703 | Sete Quedas | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5007901 | Sidrolândia | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5007935 | Sonora | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5007950 | Tacuru | |
  | 5007976 | Taquarussu | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5008008 | Terenos | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5008305 | Três Lagoas | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
  | 5008404 | Vicentina | [ms_associacao_municipios](data_collection/gazette/spiders/ms_associacao_municipios.py) |
</details>


### Minas Gerais

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 3100104 | Abadia dos Dourados | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3100203 | Abaeté | |
  | 3100302 | Abre Campo | |
  | 3100401 | Acaiaca | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3100500 | Açucena | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3100609 | Água Boa | |
  | 3100708 | Água Comprida | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3100807 | Aguanil | |
  | 3100906 | Águas Formosas | |
  | 3101003 | Águas Vermelhas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3101102 | Aimorés | |
  | 3101201 | Aiuruoca | |
  | 3101300 | Alagoa | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3101409 | Albertina | |
  | 3101508 | Além Paraíba | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3101607 | Alfenas | |
  | 3101631 | Alfredo Vasconcelos | |
  | 3101706 | Almenara | |
  | 3101805 | Alpercata | |
  | 3101904 | Alpinópolis | |
  | 3102001 | Alterosa | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3102050 | Alto Caparaó | |
  | 3153509 | Alto Jequitibá | |
  | 3102100 | Alto Rio Doce | |
  | 3102209 | Alvarenga | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3102308 | Alvinópolis | |
  | 3102407 | Alvorada de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3102506 | Amparo do Serra | |
  | 3102605 | Andradas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3102803 | Andrelândia | |
  | 3102852 | Angelândia | |
  | 3102902 | Antônio Carlos | |
  | 3103009 | Antônio Dias | |
  | 3103108 | Antônio Prado de Minas | |
  | 3103207 | Araçaí | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3103306 | Aracitaba | |
  | 3103405 | Araçuaí | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3103504 | Araguari | |
  | 3103603 | Arantina | |
  | 3103702 | Araponga | |
  | 3103751 | Araporã | |
  | 3103801 | Arapuá | |
  | 3103900 | Araújos | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3104007 | Araxá | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3104106 | Arceburgo | |
  | 3104205 | Arcos | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3104304 | Areado | |
  | 3104403 | Argirita | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3104452 | Aricanduva | |
  | 3104502 | Arinos | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3104601 | Astolfo Dutra | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3104700 | Ataléia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3104809 | Augusto de Lima | |
  | 3104908 | Baependi | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3105004 | Baldim | |
  | 3105103 | Bambuí | |
  | 3105202 | Bandeira | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3105301 | Bandeira do Sul | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3105400 | Barão de Cocais | |
  | 3105509 | Barão de Monte Alto | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3105608 | Barbacena | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3105707 | Barra Longa | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3105905 | Barroso | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3106002 | Bela Vista de Minas | |
  | 3106101 | Belmiro Braga | |
  | 3106200 | Belo Horizonte | |
  | 3106309 | Belo Oriente | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3106408 | Belo Vale | |
  | 3106507 | Berilo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3106655 | Berizal | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3106606 | Bertópolis | |
  | 3106705 | Betim | |
  | 3106804 | Bias Fortes | |
  | 3106903 | Bicas | |
  | 3107000 | Biquinhas | |
  | 3107109 | Boa Esperança | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3107208 | Bocaina de Minas | |
  | 3107307 | Bocaiúva | |
  | 3107406 | Bom Despacho | |
  | 3107505 | Bom Jardim de Minas | |
  | 3107703 | Bom Jesus do Amparo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3107802 | Bom Jesus do Galho | |
  | 3107604 | Bom Jesus da Penha | |
  | 3107901 | Bom Repouso | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3108008 | Bom Sucesso | |
  | 3108107 | Bonfim | |
  | 3108206 | Bonfinópolis de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3108255 | Bonito de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3108305 | Borda da Mata | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3108404 | Botelhos | |
  | 3108503 | Botumirim | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3108701 | Brás Pires | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3108552 | Brasilândia de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3108602 | Brasília de Minas | |
  | 3108800 | Braúnas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3108909 | Brazópolis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3109006 | Brumadinho | |
  | 3109105 | Bueno Brandão | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3109204 | Buenópolis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3109253 | Bugre | |
  | 3109303 | Buritis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3109402 | Buritizeiro | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3109451 | Cabeceira Grande | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3109501 | Cabo Verde | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3109808 | Cachoeira Dourada | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3109709 | Cachoeira de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3102704 | Cachoeira de Pajeú | |
  | 3109600 | Cachoeira da Prata | |
  | 3109907 | Caetanópolis | |
  | 3110004 | Caeté | |
  | 3110103 | Caiana | |
  | 3110202 | Cajuri | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3110301 | Caldas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3110400 | Camacho | |
  | 3110509 | Camanducaia | |
  | 3110608 | Cambuí | |
  | 3110707 | Cambuquira | |
  | 3110806 | Campanário | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3110905 | Campanha | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3111002 | Campestre | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3111101 | Campina Verde | |
  | 3111150 | Campo Azul | |
  | 3111200 | Campo Belo | [mg_campo_belo](data_collection/gazette/spiders/mg_campo_belo.py) |
  | 3111408 | Campo Florido | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3111309 | Campo do Meio | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3111507 | Campos Altos | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3111606 | Campos Gerais | |
  | 3111903 | Cana Verde | |
  | 3111705 | Canaã | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3111804 | Canápolis | |
  | 3112000 | Candeias | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py), [mg_candeias](data_collection/gazette/spiders/mg_candeias.py) |
  | 3112059 | Cantagalo | |
  | 3112109 | Caparaó | |
  | 3112208 | Capela Nova | |
  | 3112307 | Capelinha | |
  | 3112406 | Capetinga | |
  | 3112505 | Capim Branco | |
  | 3112604 | Capinópolis | |
  | 3112653 | Capitão Andrade | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3112703 | Capitão Enéas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3112802 | Capitólio | |
  | 3112901 | Caputira | |
  | 3113008 | Caraí | |
  | 3113107 | Caranaíba | |
  | 3113206 | Carandaí | |
  | 3113305 | Carangola | |
  | 3113404 | Caratinga | |
  | 3113503 | Carbonita | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3113602 | Careaçu | |
  | 3113701 | Carlos Chagas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3113800 | Carmésia | |
  | 3113909 | Carmo da Cachoeira | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py), [mg_carmo_da_cachoeira](data_collection/gazette/spiders/mg_carmo_da_cachoeira.py) |
  | 3114204 | Carmo do Cajuru | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3114006 | Carmo da Mata | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3114105 | Carmo de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3114303 | Carmo do Paranaíba | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3114402 | Carmo do Rio Claro | |
  | 3114501 | Carmópolis de Minas | |
  | 3114550 | Carneirinho | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3114600 | Carrancas | |
  | 3114709 | Carvalhópolis | |
  | 3114808 | Carvalhos | |
  | 3114907 | Casa Grande | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3115003 | Cascalho Rico | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3115102 | Cássia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3115300 | Cataguases | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3115359 | Catas Altas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3115409 | Catas Altas da Noruega | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3115458 | Catuji | |
  | 3115474 | Catuti | |
  | 3115508 | Caxambu | |
  | 3115607 | Cedro do Abaeté | |
  | 3115706 | Central de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3115805 | Centralina | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3115904 | Chácara | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3116001 | Chalé | |
  | 3116159 | Chapada Gaúcha | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3116100 | Chapada do Norte | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3116209 | Chiador | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3116308 | Cipotânea | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3116407 | Claraval | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3116506 | Claro dos Poções | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3116605 | Cláudio | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3116704 | Coimbra | |
  | 3116803 | Coluna | |
  | 3116902 | Comendador Gomes | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3117009 | Comercinho | |
  | 3117306 | Conceição das Alagoas | |
  | 3117108 | Conceição da Aparecida | |
  | 3115201 | Conceição da Barra de Minas | |
  | 3117405 | Conceição de Ipanema | |
  | 3117504 | Conceição do Mato Dentro | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3117801 | Conceição dos Ouros | |
  | 3117603 | Conceição do Pará | |
  | 3117207 | Conceição das Pedras | |
  | 3117702 | Conceição do Rio Verde | |
  | 3117836 | Cônego Marinho | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3117876 | Confins | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3117900 | Congonhal | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3118007 | Congonhas | |
  | 3118106 | Congonhas do Norte | |
  | 3118205 | Conquista | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3118304 | Conselheiro Lafaiete | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3118403 | Conselheiro Pena | |
  | 3118502 | Consolação | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3118601 | Contagem | [mg_contagem](data_collection/gazette/spiders/mg_contagem.py) |
  | 3118700 | Coqueiral | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3118809 | Coração de Jesus | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3118908 | Cordisburgo | |
  | 3119005 | Cordislândia | |
  | 3119104 | Corinto | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3119203 | Coroaci | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3119302 | Coromandel | |
  | 3119401 | Coronel Fabriciano | |
  | 3119500 | Coronel Murta | |
  | 3119609 | Coronel Pacheco | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3119708 | Coronel Xavier Chaves | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3119906 | Córrego do Bom Jesus | |
  | 3119807 | Córrego Danta | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3119955 | Córrego Fundo | |
  | 3120003 | Córrego Novo | |
  | 3120102 | Couto de Magalhães de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3120151 | Crisólita | |
  | 3120201 | Cristais | |
  | 3120300 | Cristália | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3120409 | Cristiano Otoni | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3120508 | Cristina | |
  | 3120607 | Crucilândia | [mg_crucilandia](data_collection/gazette/spiders/mg_crucilandia.py) |
  | 3120706 | Cruzeiro da Fortaleza | |
  | 3120805 | Cruzília | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3120839 | Cuparaque | |
  | 3120870 | Curral de Dentro | |
  | 3120904 | Curvelo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3121001 | Datas | |
  | 3121100 | Delfim Moreira | |
  | 3121209 | Delfinópolis | |
  | 3121258 | Delta | |
  | 3121308 | Descoberto | |
  | 3121407 | Desterro de Entre Rios | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3121506 | Desterro do Melo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3121605 | Diamantina | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3121704 | Diogo de Vasconcelos | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3121803 | Dionísio | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3121902 | Divinésia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3122009 | Divino | |
  | 3122108 | Divino das Laranjeiras | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3122207 | Divinolândia de Minas | |
  | 3122306 | Divinópolis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3122355 | Divisa Alegre | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3122405 | Divisa Nova | |
  | 3122454 | Divisópolis | |
  | 3122470 | Dom Bosco | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3122504 | Dom Cavati | |
  | 3122603 | Dom Joaquim | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3122702 | Dom Silvério | |
  | 3122801 | Dom Viçoso | |
  | 3122900 | Dona Eusébia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3123007 | Dores de Campos | |
  | 3123106 | Dores de Guanhães | |
  | 3123205 | Dores do Indaiá | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3123304 | Dores do Turvo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3123403 | Doresópolis | |
  | 3123502 | Douradoquara | |
  | 3123528 | Durandé | |
  | 3123601 | Elói Mendes | |
  | 3123700 | Engenheiro Caldas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3123809 | Engenheiro Navarro | |
  | 3123858 | Entre Folhas | |
  | 3123908 | Entre Rios de Minas | |
  | 3124005 | Ervália | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3124104 | Esmeraldas | |
  | 3124203 | Espera Feliz | |
  | 3124302 | Espinosa | |
  | 3124401 | Espírito Santo do Dourado | |
  | 3124500 | Estiva | |
  | 3124609 | Estrela Dalva | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3124708 | Estrela do Indaiá | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3124807 | Estrela do Sul | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3124906 | Eugenópolis | |
  | 3125002 | Ewbank da Câmara | |
  | 3125101 | Extrema | |
  | 3125200 | Fama | |
  | 3125309 | Faria Lemos | |
  | 3125408 | Felício dos Santos | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3125606 | Felisburgo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3125705 | Felixlândia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3125804 | Fernandes Tourinho | |
  | 3125903 | Ferros | |
  | 3125952 | Fervedouro | |
  | 3126000 | Florestal | |
  | 3126109 | Formiga | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3126208 | Formoso | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3126307 | Fortaleza de Minas | |
  | 3126406 | Fortuna de Minas | |
  | 3126505 | Francisco Badaró | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3126604 | Francisco Dumont | |
  | 3126703 | Francisco Sá | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3126752 | Franciscópolis | |
  | 3126802 | Frei Gaspar | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3126901 | Frei Inocêncio | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3126950 | Frei Lagonegro | |
  | 3127008 | Fronteira | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3127057 | Fronteira dos Vales | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3127073 | Fruta de Leite | |
  | 3127107 | Frutal | |
  | 3127206 | Funilândia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3127305 | Galiléia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3127339 | Gameleiras | |
  | 3127354 | Glaucilândia | |
  | 3127370 | Goiabeira | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3127388 | Goianá | |
  | 3127404 | Gonçalves | |
  | 3127503 | Gonzaga | |
  | 3127602 | Gouveia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3127701 | Governador Valadares | [mg_governador_valadares](data_collection/gazette/spiders/mg_governador_valadares.py) |
  | 3127800 | Grão Mogol | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3127909 | Grupiara | |
  | 3128006 | Guanhães | |
  | 3128105 | Guapé | |
  | 3128204 | Guaraciaba | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3128253 | Guaraciama | |
  | 3128303 | Guaranésia | |
  | 3128402 | Guarani | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3128501 | Guarará | |
  | 3128600 | Guarda-Mor | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3128709 | Guaxupé | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3128808 | Guidoval | |
  | 3128907 | Guimarânia | |
  | 3129004 | Guiricema | |
  | 3129103 | Gurinhatã | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3129202 | Heliodora | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3129301 | Iapu | |
  | 3129400 | Ibertioga | |
  | 3129509 | Ibiá | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3129608 | Ibiaí | |
  | 3129657 | Ibiracatu | |
  | 3129707 | Ibiraci | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3129806 | Ibirité | |
  | 3129905 | Ibitiúra de Minas | |
  | 3130002 | Ibituruna | |
  | 3130051 | Icaraí de Minas | |
  | 3130101 | Igarapé | |
  | 3130200 | Igaratinga | |
  | 3130309 | Iguatama | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3130408 | Ijaci | |
  | 3130507 | Ilicínea | |
  | 3130556 | Imbé de Minas | |
  | 3130606 | Inconfidentes | |
  | 3130655 | Indaiabira | |
  | 3130705 | Indianópolis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3130804 | Ingaí | |
  | 3130903 | Inhapim | |
  | 3131000 | Inhaúma | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3131109 | Inimutaba | |
  | 3131158 | Ipaba | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3131208 | Ipanema | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3131307 | Ipatinga | |
  | 3131406 | Ipiaçu | |
  | 3131505 | Ipuiúna | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3131604 | Iraí de Minas | |
  | 3131703 | Itabira | |
  | 3131802 | Itabirinha | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3131901 | Itabirito | |
  | 3132008 | Itacambira | |
  | 3132107 | Itacarambi | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3132206 | Itaguara | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3132305 | Itaipé | |
  | 3132404 | Itajubá | |
  | 3132503 | Itamarandiba | |
  | 3132602 | Itamarati de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3132701 | Itambacuri | |
  | 3132800 | Itambé do Mato Dentro | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3132909 | Itamogi | |
  | 3133006 | Itamonte | |
  | 3133105 | Itanhandu | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3133204 | Itanhomi | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3133303 | Itaobim | |
  | 3133402 | Itapagipe | |
  | 3133501 | Itapecerica | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3133600 | Itapeva | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3133709 | Itatiaiuçu | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3133758 | Itaú de Minas | |
  | 3133808 | Itaúna | [mg_itauna](data_collection/gazette/spiders/mg_itauna.py) |
  | 3133907 | Itaverava | |
  | 3134004 | Itinga | |
  | 3134103 | Itueta | |
  | 3134202 | Ituiutaba | |
  | 3134301 | Itumirim | |
  | 3134400 | Iturama | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3134509 | Itutinga | |
  | 3134608 | Jaboticatubas | |
  | 3134707 | Jacinto | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3134806 | Jacuí | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3134905 | Jacutinga | |
  | 3135001 | Jaguaraçu | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3135050 | Jaíba | |
  | 3135076 | Jampruca | |
  | 3135100 | Janaúba | |
  | 3135209 | Januária | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3135308 | Japaraíba | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3135357 | Japonvar | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3135407 | Jeceaba | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3135456 | Jenipapo de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3135506 | Jequeri | |
  | 3135605 | Jequitaí | |
  | 3135704 | Jequitibá | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3135803 | Jequitinhonha | |
  | 3135902 | Jesuânia | |
  | 3136009 | Joaíma | |
  | 3136108 | Joanésia | |
  | 3136207 | João Monlevade | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3136306 | João Pinheiro | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3136405 | Joaquim Felício | |
  | 3136504 | Jordânia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3136520 | José Gonçalves de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3136553 | José Raydan | |
  | 3136579 | Josenópolis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3136652 | Juatuba | |
  | 3136702 | Juiz de Fora | |
  | 3136801 | Juramento | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3136900 | Juruaia | |
  | 3136959 | Juvenília | |
  | 3137007 | Ladainha | |
  | 3137106 | Lagamar | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3137403 | Lagoa Dourada | |
  | 3137502 | Lagoa Formosa | |
  | 3137536 | Lagoa Grande | |
  | 3137304 | Lagoa dos Patos | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3137205 | Lagoa da Prata | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3137601 | Lagoa Santa | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3137700 | Lajinha | |
  | 3137809 | Lambari | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3137908 | Lamim | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3138005 | Laranjal | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3138104 | Lassance | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3138203 | Lavras | |
  | 3138302 | Leandro Ferreira | |
  | 3138351 | Leme do Prado | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3138401 | Leopoldina | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3138500 | Liberdade | |
  | 3138609 | Lima Duarte | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3138625 | Limeira do Oeste | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3138658 | Lontra | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3138674 | Luisburgo | |
  | 3138682 | Luislândia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3138708 | Luminárias | |
  | 3138807 | Luz | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3138906 | Machacalis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3139003 | Machado | |
  | 3139102 | Madre de Deus de Minas | |
  | 3139201 | Malacacheta | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3139250 | Mamonas | |
  | 3139300 | Manga | |
  | 3139409 | Manhuaçu | |
  | 3139508 | Manhumirim | |
  | 3139607 | Mantena | |
  | 3139805 | Mar de Espanha | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3139706 | Maravilhas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3139904 | Maria da Fé | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3140001 | Mariana | |
  | 3140100 | Marilac | |
  | 3140159 | Mário Campos | |
  | 3140209 | Maripá de Minas | |
  | 3140308 | Marliéria | |
  | 3140407 | Marmelópolis | |
  | 3140506 | Martinho Campos | |
  | 3140530 | Martins Soares | |
  | 3140555 | Mata Verde | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3140605 | Materlândia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3140704 | Mateus Leme | |
  | 3171501 | Mathias Lobato | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3140803 | Matias Barbosa | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3140852 | Matias Cardoso | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3140902 | Matipó | |
  | 3141009 | Mato Verde | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3141108 | Matozinhos | |
  | 3141207 | Matutina | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3141306 | Medeiros | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3141405 | Medina | |
  | 3141504 | Mendes Pimentel | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3141603 | Mercês | |
  | 3141702 | Mesquita | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3141801 | Minas Novas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3141900 | Minduri | |
  | 3142007 | Mirabela | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3142106 | Miradouro | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3142205 | Miraí | |
  | 3142254 | Miravânia | |
  | 3142304 | Moeda | |
  | 3142403 | Moema | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3142502 | Monjolos | |
  | 3142601 | Monsenhor Paulo | |
  | 3142700 | Montalvânia | |
  | 3142809 | Monte Alegre de Minas | |
  | 3142908 | Monte Azul | |
  | 3143005 | Monte Belo | |
  | 3143104 | Monte Carmelo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3143153 | Monte Formoso | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3143203 | Monte Santo de Minas | |
  | 3143401 | Monte Sião | |
  | 3143302 | Montes Claros | |
  | 3143450 | Montezuma | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3143500 | Morada Nova de Minas | |
  | 3143609 | Morro da Garça | |
  | 3143708 | Morro do Pilar | |
  | 3143807 | Munhoz | |
  | 3143906 | Muriaé | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3144003 | Mutum | |
  | 3144102 | Muzambinho | |
  | 3144201 | Nacip Raydan | |
  | 3144300 | Nanuque | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3144359 | Naque | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3144375 | Natalândia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3144409 | Natércia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3144508 | Nazareno | |
  | 3144607 | Nepomuceno | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3144656 | Ninheira | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3144672 | Nova Belém | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3144706 | Nova Era | |
  | 3144805 | Nova Lima | |
  | 3144904 | Nova Módica | |
  | 3145000 | Nova Ponte | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3145059 | Nova Porteirinha | |
  | 3145109 | Nova Resende | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3145208 | Nova Serrana | [mg_nova_serrana](data_collection/gazette/spiders/mg_nova_serrana.py) |
  | 3136603 | Nova União | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3145307 | Novo Cruzeiro | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3145356 | Novo Oriente de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3145372 | Novorizonte | |
  | 3145406 | Olaria | |
  | 3145455 | Olhos d'Água | |
  | 3145505 | Olímpio Noronha | |
  | 3145604 | Oliveira | |
  | 3145703 | Oliveira Fortes | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3145802 | Onça de Pitangui | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3145851 | Oratórios | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3145877 | Orizânia | |
  | 3145901 | Ouro Branco | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3146008 | Ouro Fino | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3146107 | Ouro Preto | |
  | 3146206 | Ouro Verde de Minas | |
  | 3146255 | Padre Carvalho | |
  | 3146305 | Padre Paraíso | |
  | 3146552 | Pai Pedro | |
  | 3146404 | Paineiras | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3146503 | Pains | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3146602 | Paiva | |
  | 3146701 | Palma | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3146750 | Palmópolis | |
  | 3146909 | Papagaios | |
  | 3147105 | Pará de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3147006 | Paracatu | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3147204 | Paraguaçu | |
  | 3147303 | Paraisópolis | |
  | 3147402 | Paraopeba | |
  | 3147600 | Passa Quatro | |
  | 3147709 | Passa Tempo | |
  | 3147808 | Passa-Vinte | |
  | 3147501 | Passabém | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3147907 | Passos | |
  | 3147956 | Patis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3148004 | Patos de Minas | |
  | 3148103 | Patrocínio | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3148202 | Patrocínio do Muriaé | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3148301 | Paula Cândido | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3148400 | Paulistas | |
  | 3148509 | Pavão | |
  | 3148608 | Peçanha | |
  | 3148806 | Pedra do Anta | |
  | 3148707 | Pedra Azul | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3148756 | Pedra Bonita | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3149002 | Pedra Dourada | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3148905 | Pedra do Indaiá | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3149101 | Pedralva | |
  | 3149150 | Pedras de Maria da Cruz | |
  | 3149200 | Pedrinópolis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3149309 | Pedro Leopoldo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3149408 | Pedro Teixeira | |
  | 3149507 | Pequeri | |
  | 3149606 | Pequi | |
  | 3149705 | Perdigão | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3149804 | Perdizes | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3149903 | Perdões | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3149952 | Periquito | |
  | 3150000 | Pescador | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3150109 | Piau | |
  | 3150158 | Piedade de Caratinga | |
  | 3150406 | Piedade dos Gerais | |
  | 3150208 | Piedade de Ponte Nova | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3150307 | Piedade do Rio Grande | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3150505 | Pimenta | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3150539 | Pingo-d'Água | |
  | 3150570 | Pintópolis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3150604 | Piracema | |
  | 3150703 | Pirajuba | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3150802 | Piranga | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3150901 | Piranguçu | |
  | 3151008 | Piranguinho | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py), [mg_piranguinho](data_collection/gazette/spiders/mg_piranguinho.py) |
  | 3151107 | Pirapetinga | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3151206 | Pirapora | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3151305 | Piraúba | |
  | 3151404 | Pitangui | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3151503 | Piumhi | |
  | 3151602 | Planura | |
  | 3151701 | Poço Fundo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3151800 | Poços de Caldas | |
  | 3151909 | Pocrane | |
  | 3152006 | Pompéu | |
  | 3152105 | Ponte Nova | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3152131 | Ponto Chique | |
  | 3152170 | Ponto dos Volantes | |
  | 3152204 | Porteirinha | |
  | 3152303 | Porto Firme | |
  | 3152402 | Poté | |
  | 3152501 | Pouso Alegre | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3152600 | Pouso Alto | |
  | 3152709 | Prados | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3152808 | Prata | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3152907 | Pratápolis | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3153004 | Pratinha | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3153103 | Presidente Bernardes | |
  | 3153202 | Presidente Juscelino | |
  | 3153301 | Presidente Kubitschek | |
  | 3153400 | Presidente Olegário | |
  | 3153608 | Prudente de Morais | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3153707 | Quartel Geral | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3153806 | Queluzito | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3153905 | Raposos | |
  | 3154002 | Raul Soares | |
  | 3154101 | Recreio | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3154150 | Reduto | |
  | 3154200 | Resende Costa | |
  | 3154309 | Resplendor | |
  | 3154408 | Ressaquinha | |
  | 3154457 | Riachinho | |
  | 3154507 | Riacho dos Machados | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3154606 | Ribeirão das Neves | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3154705 | Ribeirão Vermelho | |
  | 3154804 | Rio Acima | |
  | 3154903 | Rio Casca | |
  | 3155009 | Rio Doce | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3155207 | Rio Espera | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3155306 | Rio Manso | |
  | 3155405 | Rio Novo | |
  | 3155504 | Rio Paranaíba | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3155603 | Rio Pardo de Minas | |
  | 3155702 | Rio Piracicaba | |
  | 3155801 | Rio Pomba | |
  | 3155108 | Rio do Prado | |
  | 3155900 | Rio Preto | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3156007 | Rio Vermelho | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3156106 | Ritápolis | |
  | 3156205 | Rochedo de Minas | |
  | 3156304 | Rodeiro | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3156403 | Romaria | |
  | 3156452 | Rosário da Limeira | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3156502 | Rubelita | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3156601 | Rubim | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3156700 | Sabará | |
  | 3156809 | Sabinópolis | |
  | 3156908 | Sacramento | |
  | 3157005 | Salinas | [mg_salinas](data_collection/gazette/spiders/mg_salinas.py) |
  | 3157104 | Salto da Divisa | |
  | 3157203 | Santa Bárbara | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3157252 | Santa Bárbara do Leste | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3157278 | Santa Bárbara do Monte Verde | |
  | 3157302 | Santa Bárbara do Tugúrio | |
  | 3157401 | Santa Cruz do Escalvado | |
  | 3157336 | Santa Cruz de Minas | |
  | 3157377 | Santa Cruz de Salinas | |
  | 3157500 | Santa Efigênia de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3157609 | Santa Fé de Minas | |
  | 3157658 | Santa Helena de Minas | |
  | 3157708 | Santa Juliana | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3157807 | Santa Luzia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3157906 | Santa Margarida | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3158003 | Santa Maria de Itabira | |
  | 3158102 | Santa Maria do Salto | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3158201 | Santa Maria do Suaçuí | |
  | 3159209 | Santa Rita de Caldas | |
  | 3159407 | Santa Rita de Ibitipoca | |
  | 3159506 | Santa Rita do Itueto | |
  | 3159308 | Santa Rita de Jacutinga | |
  | 3159357 | Santa Rita de Minas | |
  | 3159605 | Santa Rita do Sapucaí | |
  | 3159704 | Santa Rosa da Serra | |
  | 3159803 | Santa Vitória | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3158409 | Santana de Cataguases | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3158607 | Santana do Deserto | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3158706 | Santana do Garambéu | |
  | 3158805 | Santana do Jacaré | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3158904 | Santana do Manhuaçu | |
  | 3159100 | Santana dos Montes | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3158953 | Santana do Paraíso | |
  | 3158508 | Santana de Pirapama | |
  | 3159001 | Santana do Riacho | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3158300 | Santana da Vargem | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3159902 | Santo Antônio do Amparo | |
  | 3160009 | Santo Antônio do Aventureiro | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3160108 | Santo Antônio do Grama | |
  | 3160207 | Santo Antônio do Itambé | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3160306 | Santo Antônio do Jacinto | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3160405 | Santo Antônio do Monte | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3160454 | Santo Antônio do Retiro | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3160504 | Santo Antônio do Rio Abaixo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3160603 | Santo Hipólito | |
  | 3160702 | Santos Dumont | |
  | 3160801 | São Bento Abade | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3160900 | São Brás do Suaçuí | |
  | 3160959 | São Domingos das Dores | |
  | 3161007 | São Domingos do Prata | |
  | 3161056 | São Félix de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3161106 | São Francisco | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3161403 | São Francisco do Glória | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3161205 | São Francisco de Paula | |
  | 3161304 | São Francisco de Sales | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3161502 | São Geraldo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3161650 | São Geraldo do Baixio | |
  | 3161601 | São Geraldo da Piedade | |
  | 3161700 | São Gonçalo do Abaeté | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3161809 | São Gonçalo do Pará | |
  | 3161908 | São Gonçalo do Rio Abaixo | |
  | 3125507 | São Gonçalo do Rio Preto | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3162005 | São Gonçalo do Sapucaí | |
  | 3162104 | São Gotardo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3162203 | São João Batista do Glória | |
  | 3162500 | São João del Rei | |
  | 3162807 | São João Evangelista | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3162252 | São João da Lagoa | |
  | 3162559 | São João do Manhuaçu | |
  | 3162575 | São João do Manteninha | |
  | 3162302 | São João da Mata | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3162450 | São João das Missões | |
  | 3162906 | São João Nepomuceno | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3162609 | São João do Oriente | |
  | 3162658 | São João do Pacuí | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3162708 | São João do Paraíso | |
  | 3162401 | São João da Ponte | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3162922 | São Joaquim de Bicas | |
  | 3163201 | São José do Alegre | |
  | 3162948 | São José da Barra | |
  | 3163300 | São José do Divino | |
  | 3163409 | São José do Goiabal | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3163508 | São José do Jacuri | |
  | 3162955 | São José da Lapa | |
  | 3163607 | São José do Mantimento | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3163003 | São José da Safira | |
  | 3163102 | São José da Varginha | |
  | 3163706 | São Lourenço | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3163805 | São Miguel do Anta | |
  | 3164001 | São Pedro dos Ferros | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3164100 | São Pedro do Suaçuí | |
  | 3163904 | São Pedro da União | |
  | 3164209 | São Romão | |
  | 3164308 | São Roque de Minas | |
  | 3164472 | São Sebastião do Anta | |
  | 3164407 | São Sebastião da Bela Vista | |
  | 3164506 | São Sebastião do Maranhão | |
  | 3164605 | São Sebastião do Oeste | |
  | 3164704 | São Sebastião do Paraíso | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3164803 | São Sebastião do Rio Preto | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3164902 | São Sebastião do Rio Verde | |
  | 3164431 | São Sebastião da Vargem Alegre | |
  | 3165206 | São Thomé das Letras | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3165008 | São Tiago | |
  | 3165107 | São Tomás de Aquino | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3165305 | São Vicente de Minas | |
  | 3165404 | Sapucaí-Mirim | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3165503 | Sardoá | |
  | 3165537 | Sarzedo | |
  | 3165560 | Sem-Peixe | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3165578 | Senador Amaral | |
  | 3165602 | Senador Cortes | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3165701 | Senador Firmino | |
  | 3165800 | Senador José Bento | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3165909 | Senador Modestino Gonçalves | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3166006 | Senhora de Oliveira | |
  | 3166105 | Senhora do Porto | |
  | 3166204 | Senhora dos Remédios | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3166303 | Sericita | |
  | 3166402 | Seritinga | |
  | 3166709 | Serra dos Aimorés | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3166501 | Serra Azul de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3166808 | Serra do Salitre | |
  | 3166600 | Serra da Saudade | |
  | 3166907 | Serrania | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3166956 | Serranópolis de Minas | |
  | 3167004 | Serranos | |
  | 3167103 | Serro | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3167202 | Sete Lagoas | |
  | 3165552 | Setubinha | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3167301 | Silveirânia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3167400 | Silvianópolis | |
  | 3167509 | Simão Pereira | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3167608 | Simonésia | |
  | 3167707 | Sobrália | |
  | 3167806 | Soledade de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3167905 | Tabuleiro | |
  | 3168002 | Taiobeiras | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3168051 | Taparuba | |
  | 3168101 | Tapira | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3168200 | Tapiraí | |
  | 3168309 | Taquaraçu de Minas | |
  | 3168408 | Tarumirim | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3168507 | Teixeiras | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3168606 | Teófilo Otoni | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3168705 | Timóteo | |
  | 3168804 | Tiradentes | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3168903 | Tiros | |
  | 3169000 | Tocantins | |
  | 3169059 | Tocos do Moji | |
  | 3169109 | Toledo | |
  | 3169208 | Tombos | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3169307 | Três Corações | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3169356 | Três Marias | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3169406 | Três Pontas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3169505 | Tumiritinga | |
  | 3169604 | Tupaciguara | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3169703 | Turmalina | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3169802 | Turvolândia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3169901 | Ubá | |
  | 3170008 | Ubaí | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3170057 | Ubaporanga | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3170107 | Uberaba | [mg_uberaba](data_collection/gazette/spiders/mg_uberaba.py) |
  | 3170206 | Uberlândia | |
  | 3170305 | Umburatiba | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3170404 | Unaí | |
  | 3170438 | União de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3170479 | Uruana de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3170503 | Urucânia | |
  | 3170529 | Urucuia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3170578 | Vargem Alegre | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3170602 | Vargem Bonita | |
  | 3170651 | Vargem Grande do Rio Pardo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3170701 | Varginha | |
  | 3170750 | Varjão de Minas | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3170800 | Várzea da Palma | |
  | 3170909 | Varzelândia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3171006 | Vazante | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3171030 | Verdelândia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3171071 | Veredinha | |
  | 3171105 | Veríssimo | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3171154 | Vermelho Novo | |
  | 3171204 | Vespasiano | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3171303 | Viçosa | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3171402 | Vieiras | |
  | 3171600 | Virgem da Lapa | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3171709 | Virgínia | |
  | 3171808 | Virginópolis | |
  | 3171907 | Virgolândia | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3172004 | Visconde do Rio Branco | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3172103 | Volta Grande | [mg_associacao_municipios](data_collection/gazette/spiders/mg_associacao_municipios.py) |
  | 3172202 | Wenceslau Braz | |
</details>


### Pará

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 1500107 | Abaetetuba | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1500131 | Abel Figueiredo | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1500206 | Acará | |
  | 1500305 | Afuá | |
  | 1500347 | Água Azul do Norte | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1500404 | Alenquer | |
  | 1500503 | Almeirim | |
  | 1500602 | Altamira | |
  | 1500701 | Anajás | |
  | 1500800 | Ananindeua | [pa_ananindeua](data_collection/gazette/spiders/pa_ananindeua.py) |
  | 1500859 | Anapu | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1500909 | Augusto Corrêa | |
  | 1500958 | Aurora do Pará | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1501006 | Aveiro | |
  | 1501105 | Bagre | |
  | 1501204 | Baião | |
  | 1501253 | Bannach | |
  | 1501303 | Barcarena | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1501402 | Belém | [pa_belem](data_collection/gazette/spiders/pa_belem.py) |
  | 1501451 | Belterra | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1501501 | Benevides | |
  | 1501576 | Bom Jesus do Tocantins | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1501600 | Bonito | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1501709 | Bragança | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1501725 | Brasil Novo | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1501758 | Brejo Grande do Araguaia | |
  | 1501782 | Breu Branco | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1501808 | Breves | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1501907 | Bujaru | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502004 | Cachoeira do Arari | |
  | 1501956 | Cachoeira do Piriá | |
  | 1502103 | Cametá | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502152 | Canaã dos Carajás | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502202 | Capanema | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502301 | Capitão Poço | |
  | 1502400 | Castanhal | |
  | 1502509 | Chaves | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502608 | Colares | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502707 | Conceição do Araguaia | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502756 | Concórdia do Pará | |
  | 1502764 | Cumaru do Norte | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502772 | Curionópolis | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502806 | Curralinho | |
  | 1502855 | Curuá | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502905 | Curuçá | |
  | 1502939 | Dom Eliseu | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1502954 | Eldorado do Carajás | |
  | 1503002 | Faro | |
  | 1503044 | Floresta do Araguaia | |
  | 1503077 | Garrafão do Norte | |
  | 1503093 | Goianésia do Pará | |
  | 1503101 | Gurupá | |
  | 1503200 | Igarapé-Açu | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1503309 | Igarapé-Miri | |
  | 1503408 | Inhangapi | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1503457 | Ipixuna do Pará | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1503507 | Irituia | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1503606 | Itaituba | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1503705 | Itupiranga | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1503754 | Jacareacanga | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1503804 | Jacundá | |
  | 1503903 | Juruti | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1504000 | Limoeiro do Ajuru | |
  | 1504059 | Mãe do Rio | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1504109 | Magalhães Barata | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1504208 | Marabá | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1504307 | Maracanã | |
  | 1504406 | Marapanim | |
  | 1504422 | Marituba | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1504455 | Medicilândia | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1504505 | Melgaço | |
  | 1504604 | Mocajuba | |
  | 1504703 | Moju | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1504752 | Mojuí dos Campos | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1504802 | Monte Alegre | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1504901 | Muaná | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1504950 | Nova Esperança do Piriá | |
  | 1504976 | Nova Ipixuna | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505007 | Nova Timboteua | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505031 | Novo Progresso | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505064 | Novo Repartimento | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505106 | Óbidos | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505205 | Oeiras do Pará | |
  | 1505304 | Oriximiná | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505403 | Ourém | |
  | 1505437 | Ourilândia do Norte | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505486 | Pacajá | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505494 | Palestina do Pará | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505502 | Paragominas | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505536 | Parauapebas | |
  | 1505551 | Pau d'Arco | |
  | 1505601 | Peixe-Boi | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505635 | Piçarra | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505650 | Placas | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505700 | Ponta de Pedras | |
  | 1505809 | Portel | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1505908 | Porto de Moz | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1506005 | Prainha | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1506104 | Primavera | |
  | 1506112 | Quatipuru | |
  | 1506138 | Redenção | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1506161 | Rio Maria | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1506187 | Rondon do Pará | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1506195 | Rurópolis | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1506203 | Salinópolis | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1506302 | Salvaterra | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1506351 | Santa Bárbara do Pará | |
  | 1506401 | Santa Cruz do Arari | |
  | 1506500 | Santa Izabel do Pará | |
  | 1506559 | Santa Luzia do Pará | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1506583 | Santa Maria das Barreiras | |
  | 1506609 | Santa Maria do Pará | |
  | 1506708 | Santana do Araguaia | |
  | 1506807 | Santarém | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1506906 | Santarém Novo | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507003 | Santo Antônio do Tauá | |
  | 1507102 | São Caetano de Odivelas | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507151 | São Domingos do Araguaia | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507201 | São Domingos do Capim | |
  | 1507300 | São Félix do Xingu | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507409 | São Francisco do Pará | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507458 | São Geraldo do Araguaia | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507508 | São João do Araguaia | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507474 | São João de Pirabas | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507466 | São João da Ponta | |
  | 1507607 | São Miguel do Guamá | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507706 | São Sebastião da Boa Vista | |
  | 1507755 | Sapucaia | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507805 | Senador José Porfírio | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507904 | Soure | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1507953 | Tailândia | |
  | 1507961 | Terra Alta | |
  | 1507979 | Terra Santa | |
  | 1508001 | Tomé-Açu | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1508035 | Tracuateua | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1508050 | Trairão | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1508084 | Tucumã | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1508100 | Tucuruí | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1508126 | Ulianópolis | |
  | 1508159 | Uruará | |
  | 1508209 | Vigia | |
  | 1508308 | Viseu | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
  | 1508357 | Vitória do Xingu | |
  | 1508407 | Xinguara | [pa_associacao_municipios](data_collection/gazette/spiders/pa_associacao_municipios.py) |
</details>


### Paraíba

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 2500106 | Água Branca | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2500205 | Aguiar | |
  | 2500304 | Alagoa Grande | |
  | 2500403 | Alagoa Nova | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2500502 | Alagoinha | |
  | 2500536 | Alcantil | |
  | 2500577 | Algodão de Jandaíra | |
  | 2500601 | Alhandra | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2500734 | Amparo | |
  | 2500775 | Aparecida | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2500809 | Araçagi | |
  | 2500908 | Arara | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2501005 | Araruna | |
  | 2501104 | Areia | |
  | 2501153 | Areia de Baraúnas | |
  | 2501203 | Areial | |
  | 2501302 | Aroeiras | |
  | 2501351 | Assunção | |
  | 2501401 | Baía da Traição | |
  | 2501500 | Bananeiras | |
  | 2501534 | Baraúna | |
  | 2501609 | Barra de Santa Rosa | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2501575 | Barra de Santana | |
  | 2501708 | Barra de São Miguel | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2501807 | Bayeux | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2501906 | Belém | |
  | 2502003 | Belém do Brejo do Cruz | |
  | 2502052 | Bernardino Batista | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2502102 | Boa Ventura | |
  | 2502151 | Boa Vista | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2502201 | Bom Jesus | |
  | 2502300 | Bom Sucesso | |
  | 2502409 | Bonito de Santa Fé | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2502508 | Boqueirão | |
  | 2502706 | Borborema | |
  | 2502805 | Brejo do Cruz | |
  | 2502904 | Brejo dos Santos | |
  | 2503001 | Caaporã | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2503100 | Cabaceiras | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2503209 | Cabedelo | |
  | 2503308 | Cachoeira dos Índios | |
  | 2503407 | Cacimba de Areia | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2503506 | Cacimba de Dentro | |
  | 2503555 | Cacimbas | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2503605 | Caiçara | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2503704 | Cajazeiras | |
  | 2503753 | Cajazeirinhas | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2503803 | Caldas Brandão | |
  | 2503902 | Camalaú | |
  | 2504009 | Campina Grande | [pb_campina_grande](data_collection/gazette/spiders/pb_campina_grande.py) |
  | 2504033 | Capim | |
  | 2504074 | Caraúbas | |
  | 2504108 | Carrapateira | |
  | 2504157 | Casserengue | |
  | 2504207 | Catingueira | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2504306 | Catolé do Rocha | |
  | 2504355 | Caturité | |
  | 2504405 | Conceição | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2504504 | Condado | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2504603 | Conde | |
  | 2504702 | Congo | |
  | 2504801 | Coremas | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2504850 | Coxixola | |
  | 2504900 | Cruz do Espírito Santo | |
  | 2505006 | Cubati | |
  | 2505105 | Cuité | |
  | 2505238 | Cuité de Mamanguape | |
  | 2505204 | Cuitegi | |
  | 2505279 | Curral de Cima | |
  | 2505303 | Curral Velho | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2505352 | Damião | |
  | 2505402 | Desterro | |
  | 2505600 | Diamante | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2505709 | Dona Inês | |
  | 2505808 | Duas Estradas | |
  | 2505907 | Emas | |
  | 2506004 | Esperança | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2506103 | Fagundes | |
  | 2506202 | Frei Martinho | |
  | 2506251 | Gado Bravo | |
  | 2506301 | Guarabira | |
  | 2506400 | Gurinhém | |
  | 2506509 | Gurjão | |
  | 2506608 | Ibiara | |
  | 2502607 | Igaracy | |
  | 2506707 | Imaculada | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2506806 | Ingá | |
  | 2506905 | Itabaiana | |
  | 2507002 | Itaporanga | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2507101 | Itapororoca | |
  | 2507200 | Itatuba | |
  | 2507309 | Jacaraú | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2507408 | Jericó | |
  | 2507507 | João Pessoa | [pb_joao_pessoa](data_collection/gazette/spiders/pb_joao_pessoa.py) |
  | 2513653 | Joca Claudino | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2507606 | Juarez Távora | |
  | 2507705 | Juazeirinho | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2507804 | Junco do Seridó | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2507903 | Juripiranga | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2508000 | Juru | |
  | 2508109 | Lagoa | |
  | 2508208 | Lagoa de Dentro | |
  | 2508307 | Lagoa Seca | |
  | 2508406 | Lastro | |
  | 2508505 | Livramento | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2508554 | Logradouro | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2508604 | Lucena | |
  | 2508703 | Mãe d'Água | |
  | 2508802 | Malta | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2508901 | Mamanguape | |
  | 2509008 | Manaíra | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2509057 | Marcação | |
  | 2509107 | Mari | |
  | 2509156 | Marizópolis | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2509206 | Massaranduba | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2509305 | Mataraca | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2509339 | Matinhas | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2509370 | Mato Grosso | |
  | 2509396 | Maturéia | |
  | 2509404 | Mogeiro | |
  | 2509503 | Montadas | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2509602 | Monte Horebe | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2509701 | Monteiro | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2509800 | Mulungu | |
  | 2509909 | Natuba | |
  | 2510006 | Nazarezinho | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2510105 | Nova Floresta | |
  | 2510204 | Nova Olinda | |
  | 2510303 | Nova Palmeira | |
  | 2510402 | Olho d'Água | |
  | 2510501 | Olivedos | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2510600 | Ouro Velho | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2510659 | Parari | |
  | 2510709 | Passagem | |
  | 2510808 | Patos | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2510907 | Paulista | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2511004 | Pedra Branca | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2511103 | Pedra Lavrada | |
  | 2511202 | Pedras de Fogo | |
  | 2512721 | Pedro Régis | |
  | 2511301 | Piancó | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2511400 | Picuí | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2511509 | Pilar | |
  | 2511608 | Pilões | |
  | 2511707 | Pilõezinhos | |
  | 2511806 | Pirpirituba | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2511905 | Pitimbu | |
  | 2512002 | Pocinhos | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2512036 | Poço Dantas | |
  | 2512077 | Poço de José de Moura | |
  | 2512101 | Pombal | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2512200 | Prata | |
  | 2512309 | Princesa Isabel | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2512408 | Puxinanã | |
  | 2512507 | Queimadas | |
  | 2512606 | Quixabá | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2512705 | Remígio | |
  | 2512747 | Riachão | |
  | 2512754 | Riachão do Bacamarte | |
  | 2512762 | Riachão do Poço | |
  | 2512804 | Riacho dos Cavalos | |
  | 2512788 | Riacho de Santo Antônio | |
  | 2512903 | Rio Tinto | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2513000 | Salgadinho | |
  | 2513109 | Salgado de São Félix | |
  | 2513158 | Santa Cecília | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2513208 | Santa Cruz | |
  | 2513307 | Santa Helena | |
  | 2513356 | Santa Inês | |
  | 2513406 | Santa Luzia | |
  | 2513703 | Santa Rita | |
  | 2513802 | Santa Teresinha | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2513604 | Santana dos Garrotes | |
  | 2513505 | Santana de Mangueira | |
  | 2513851 | Santo André | |
  | 2513927 | São Bentinho | |
  | 2513901 | São Bento | |
  | 2513968 | São Domingos | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2513943 | São Domingos do Cariri | |
  | 2513984 | São Francisco | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2514008 | São João do Cariri | |
  | 2500700 | São João do Rio do Peixe | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2514107 | São João do Tigre | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2514602 | São José do Bonfim | |
  | 2514651 | São José do Brejo do Cruz | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2514305 | São José de Caiana | |
  | 2514800 | São José dos Cordeiros | |
  | 2514404 | São José de Espinharas | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2514206 | São José da Lagoa Tapada | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2514503 | São José de Piranhas | |
  | 2514552 | São José de Princesa | |
  | 2514453 | São José dos Ramos | |
  | 2514701 | São José do Sabugi | |
  | 2514909 | São Mamede | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2515005 | São Miguel de Taipu | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2515104 | São Sebastião de Lagoa de Roça | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2515203 | São Sebastião do Umbuzeiro | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2515401 | São Vicente do Seridó | |
  | 2515302 | Sapé | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2515500 | Serra Branca | |
  | 2515708 | Serra Grande | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2515609 | Serra da Raiz | |
  | 2515807 | Serra Redonda | |
  | 2515906 | Serraria | |
  | 2515930 | Sertãozinho | |
  | 2515971 | Sobrado | |
  | 2516003 | Solânea | |
  | 2516102 | Soledade | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2516151 | Sossêgo | |
  | 2516201 | Sousa | |
  | 2516300 | Sumé | |
  | 2516409 | Tacima | |
  | 2516508 | Taperoá | |
  | 2516607 | Tavares | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2516706 | Teixeira | |
  | 2516755 | Tenório | |
  | 2516805 | Triunfo | |
  | 2516904 | Uiraúna | [pb_associacao_municipios](data_collection/gazette/spiders/pb_associacao_municipios.py) |
  | 2517001 | Umbuzeiro | |
  | 2517100 | Várzea | |
  | 2517209 | Vieirópolis | |
  | 2505501 | Vista Serrana | |
  | 2517407 | Zabelê | |
</details>


### Paraná

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 4100103 | Abatiá | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4100202 | Adrianópolis | |
  | 4100301 | Agudos do Sul | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4100400 | Almirante Tamandaré | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4100459 | Altamira do Paraná | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4128625 | Alto Paraíso | |
  | 4100608 | Alto Paraná | |
  | 4100707 | Alto Piquiri | |
  | 4100509 | Altônia | |
  | 4100806 | Alvorada do Sul | |
  | 4100905 | Amaporã | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4101002 | Ampére | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4101051 | Anahy | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4101101 | Andirá | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4101150 | Ângulo | |
  | 4101200 | Antonina | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4101309 | Antônio Olinto | |
  | 4101408 | Apucarana | |
  | 4101507 | Arapongas | |
  | 4101606 | Arapoti | |
  | 4101655 | Arapuã | |
  | 4101705 | Araruna | |
  | 4101804 | Araucária | |
  | 4101853 | Ariranha do Ivaí | |
  | 4101903 | Assaí | |
  | 4102000 | Assis Chateaubriand | |
  | 4102109 | Astorga | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4102208 | Atalaia | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4102307 | Balsa Nova | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4102406 | Bandeirantes | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4102505 | Barbosa Ferraz | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4102703 | Barra do Jacaré | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4102604 | Barracão | |
  | 4102752 | Bela Vista da Caroba | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4102802 | Bela Vista do Paraíso | |
  | 4102901 | Bituruna | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103008 | Boa Esperança | |
  | 4103024 | Boa Esperança do Iguaçu | |
  | 4103040 | Boa Ventura de São Roque | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103057 | Boa Vista da Aparecida | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103107 | Bocaiúva do Sul | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103156 | Bom Jesus do Sul | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103206 | Bom Sucesso | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103222 | Bom Sucesso do Sul | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103305 | Borrazópolis | |
  | 4103354 | Braganey | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103370 | Brasilândia do Sul | |
  | 4103404 | Cafeara | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103453 | Cafelândia | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103479 | Cafezal do Sul | |
  | 4103503 | Califórnia | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103602 | Cambará | |
  | 4103701 | Cambé | |
  | 4103800 | Cambira | |
  | 4104006 | Campina Grande do Sul | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4103909 | Campina da Lagoa | |
  | 4103958 | Campina do Simão | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4104055 | Campo Bonito | |
  | 4104204 | Campo Largo | |
  | 4104253 | Campo Magro | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4104303 | Campo Mourão | |
  | 4104105 | Campo do Tenente | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4104402 | Cândido de Abreu | |
  | 4104428 | Candói | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4104451 | Cantagalo | |
  | 4104501 | Capanema | |
  | 4104600 | Capitão Leônidas Marques | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4104659 | Carambeí | |
  | 4104709 | Carlópolis | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4104808 | Cascavel | [pr_cascavel](data_collection/gazette/spiders/pr_cascavel.py) |
  | 4104907 | Castro | |
  | 4105003 | Catanduvas | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4105102 | Centenário do Sul | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4105201 | Cerro Azul | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4105300 | Céu Azul | |
  | 4105409 | Chopinzinho | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4105508 | Cianorte | |
  | 4105607 | Cidade Gaúcha | |
  | 4105706 | Clevelândia | |
  | 4105805 | Colombo | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4105904 | Colorado | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4106001 | Congonhinhas | |
  | 4106100 | Conselheiro Mairinck | |
  | 4106209 | Contenda | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4106308 | Corbélia | |
  | 4106407 | Cornélio Procópio | |
  | 4106456 | Coronel Domingos Soares | |
  | 4106506 | Coronel Vivida | |
  | 4106555 | Corumbataí do Sul | |
  | 4106803 | Cruz Machado | |
  | 4106571 | Cruzeiro do Iguaçu | |
  | 4106605 | Cruzeiro do Oeste | |
  | 4106704 | Cruzeiro do Sul | |
  | 4106852 | Cruzmaltina | |
  | 4106902 | Curitiba | [pr_curitiba](data_collection/gazette/spiders/pr_curitiba.py) |
  | 4107009 | Curiúva | |
  | 4107108 | Diamante do Norte | |
  | 4107157 | Diamante D'Oeste | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4107124 | Diamante do Sul | |
  | 4107207 | Dois Vizinhos | |
  | 4107256 | Douradina | |
  | 4107306 | Doutor Camargo | |
  | 4128633 | Doutor Ulysses | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4107405 | Enéas Marques | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4107504 | Engenheiro Beltrão | |
  | 4107538 | Entre Rios do Oeste | |
  | 4107520 | Esperança Nova | |
  | 4107546 | Espigão Alto do Iguaçu | |
  | 4107553 | Farol | |
  | 4107603 | Faxinal | |
  | 4107652 | Fazenda Rio Grande | |
  | 4107702 | Fênix | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4107736 | Fernandes Pinheiro | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4107751 | Figueira | |
  | 4107850 | Flor da Serra do Sul | |
  | 4107801 | Floraí | |
  | 4107900 | Floresta | |
  | 4108007 | Florestópolis | |
  | 4108106 | Flórida | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4108205 | Formosa do Oeste | |
  | 4108304 | Foz do Iguaçu | [pr_foz_do_iguacu](data_collection/gazette/spiders/pr_foz_do_iguacu.py) |
  | 4108452 | Foz do Jordão | |
  | 4108320 | Francisco Alves | |
  | 4108403 | Francisco Beltrão | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4108502 | General Carneiro | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4108551 | Godoy Moreira | |
  | 4108601 | Goioerê | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4108650 | Goioxim | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4108700 | Grandes Rios | |
  | 4108809 | Guaíra | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4108908 | Guairaçá | |
  | 4108957 | Guamiranga | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4109005 | Guapirama | |
  | 4109104 | Guaporema | |
  | 4109203 | Guaraci | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4109302 | Guaraniaçu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4109401 | Guarapuava | |
  | 4109500 | Guaraqueçaba | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4109609 | Guaratuba | |
  | 4109658 | Honório Serpa | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4109708 | Ibaiti | |
  | 4109757 | Ibema | |
  | 4109807 | Ibiporã | |
  | 4109906 | Icaraíma | |
  | 4110003 | Iguaraçu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4110052 | Iguatu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4110078 | Imbaú | |
  | 4110102 | Imbituva | |
  | 4110201 | Inácio Martins | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4110300 | Inajá | |
  | 4110409 | Indianópolis | |
  | 4110508 | Ipiranga | |
  | 4110607 | Iporã | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4110656 | Iracema do Oeste | |
  | 4110706 | Irati | |
  | 4110805 | Iretama | |
  | 4110904 | Itaguajé | |
  | 4110953 | Itaipulândia | |
  | 4111001 | Itambaracá | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4111100 | Itambé | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4111209 | Itapejara d'Oeste | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4111258 | Itaperuçu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4111308 | Itaúna do Sul | |
  | 4111407 | Ivaí | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4111506 | Ivaiporã | |
  | 4111555 | Ivaté | |
  | 4111605 | Ivatuba | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4111704 | Jaboti | [pr_jaboti](data_collection/gazette/spiders/sp_jaboti.py) |
  | 4111803 | Jacarezinho | |
  | 4111902 | Jaguapitã | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4112009 | Jaguariaíva | |
  | 4112108 | Jandaia do Sul | |
  | 4112207 | Janiópolis | |
  | 4112306 | Japira | |
  | 4112405 | Japurá | |
  | 4112504 | Jardim Alegre | |
  | 4112603 | Jardim Olinda | |
  | 4112702 | Jataizinho | |
  | 4112751 | Jesuítas | |
  | 4112801 | Joaquim Távora | |
  | 4112900 | Jundiaí do Sul | |
  | 4112959 | Juranda | |
  | 4113007 | Jussara | |
  | 4113106 | Kaloré | |
  | 4113205 | Lapa | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4113254 | Laranjal | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4113304 | Laranjeiras do Sul | |
  | 4113403 | Leópolis | |
  | 4113429 | Lidianópolis | |
  | 4113452 | Lindoeste | |
  | 4113502 | Loanda | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4113601 | Lobato | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4113700 | Londrina | [pr_londrina](data_collection/gazette/spiders/pr_londrina.py) |
  | 4113734 | Luiziana | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4113759 | Lunardelli | |
  | 4113809 | Lupionópolis | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4113908 | Mallet | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4114005 | Mamborê | |
  | 4114104 | Mandaguaçu | |
  | 4114203 | Mandaguari | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4114302 | Mandirituba | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4114351 | Manfrinópolis | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4114401 | Mangueirinha | |
  | 4114500 | Manoel Ribas | |
  | 4114609 | Marechal Cândido Rondon | |
  | 4114708 | Maria Helena | |
  | 4114807 | Marialva | |
  | 4114906 | Marilândia do Sul | |
  | 4115002 | Marilena | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4115101 | Mariluz | |
  | 4115200 | Maringá | [pr_maringa](data_collection/gazette/spiders/pr_maringa.py) |
  | 4115309 | Mariópolis | |
  | 4115358 | Maripá | |
  | 4115408 | Marmeleiro | |
  | 4115457 | Marquinho | |
  | 4115507 | Marumbi | |
  | 4115606 | Matelândia | |
  | 4115705 | Matinhos | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4115739 | Mato Rico | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4115754 | Mauá da Serra | |
  | 4115804 | Medianeira | |
  | 4115853 | Mercedes | |
  | 4115903 | Mirador | |
  | 4116000 | Miraselva | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4116059 | Missal | |
  | 4116109 | Moreira Sales | |
  | 4116208 | Morretes | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4116307 | Munhoz de Melo | |
  | 4116406 | Nossa Senhora das Graças | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4116505 | Nova Aliança do Ivaí | |
  | 4116604 | Nova América da Colina | |
  | 4116703 | Nova Aurora | |
  | 4116802 | Nova Cantu | |
  | 4116901 | Nova Esperança | |
  | 4116950 | Nova Esperança do Sudoeste | |
  | 4117008 | Nova Fátima | |
  | 4117057 | Nova Laranjeiras | |
  | 4117107 | Nova Londrina | |
  | 4117206 | Nova Olímpia | |
  | 4117255 | Nova Prata do Iguaçu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4117214 | Nova Santa Bárbara | |
  | 4117222 | Nova Santa Rosa | |
  | 4117271 | Nova Tebas | |
  | 4117297 | Novo Itacolomi | |
  | 4117305 | Ortigueira | |
  | 4117404 | Ourizona | |
  | 4117453 | Ouro Verde do Oeste | |
  | 4117503 | Paiçandu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4117602 | Palmas | |
  | 4117701 | Palmeira | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4117800 | Palmital | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4117909 | Palotina | |
  | 4118006 | Paraíso do Norte | |
  | 4118105 | Paranacity | |
  | 4118204 | Paranaguá | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4118303 | Paranapoema | |
  | 4118402 | Paranavaí | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4118451 | Pato Bragado | |
  | 4118501 | Pato Branco | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4118600 | Paula Freitas | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4118709 | Paulo Frontin | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4118808 | Peabiru | |
  | 4118857 | Perobal | |
  | 4118907 | Pérola | |
  | 4119004 | Pérola d'Oeste | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4119103 | Piên | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4119152 | Pinhais | |
  | 4119251 | Pinhal de São Bento | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4119202 | Pinhalão | |
  | 4119301 | Pinhão | |
  | 4119400 | Piraí do Sul | |
  | 4119509 | Piraquara | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4119608 | Pitanga | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4119657 | Pitangueiras | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4119707 | Planaltina do Paraná | |
  | 4119806 | Planalto | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4119905 | Ponta Grossa | [pr_ponta_grossa](data_collection/gazette/spiders/pr_ponta_grossa.py) |
  | 4119954 | Pontal do Paraná | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4120002 | Porecatu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4120101 | Porto Amazonas | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4120150 | Porto Barreiro | |
  | 4120200 | Porto Rico | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4120309 | Porto Vitória | |
  | 4120333 | Prado Ferreira | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4120358 | Pranchita | |
  | 4120408 | Presidente Castelo Branco | |
  | 4120507 | Primeiro de Maio | |
  | 4120606 | Prudentópolis | |
  | 4120655 | Quarto Centenário | |
  | 4120705 | Quatiguá | |
  | 4120804 | Quatro Barras | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4120853 | Quatro Pontes | |
  | 4120903 | Quedas do Iguaçu | |
  | 4121000 | Querência do Norte | |
  | 4121109 | Quinta do Sol | |
  | 4121208 | Quitandinha | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4121257 | Ramilândia | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4121307 | Rancho Alegre | |
  | 4121356 | Rancho Alegre D'Oeste | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4121406 | Realeza | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4121505 | Rebouças | |
  | 4121604 | Renascença | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4121703 | Reserva | |
  | 4121752 | Reserva do Iguaçu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4121802 | Ribeirão Claro | |
  | 4121901 | Ribeirão do Pinhal | |
  | 4122008 | Rio Azul | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4122107 | Rio Bom | |
  | 4122156 | Rio Bonito do Iguaçu | |
  | 4122172 | Rio Branco do Ivaí | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4122206 | Rio Branco do Sul | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4122305 | Rio Negro | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4122404 | Rolândia | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4122503 | Roncador | |
  | 4122602 | Rondon | |
  | 4122651 | Rosário do Ivaí | |
  | 4122701 | Sabáudia | |
  | 4122800 | Salgado Filho | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4122909 | Salto do Itararé | |
  | 4123006 | Salto do Lontra | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4123105 | Santa Amélia | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4123204 | Santa Cecília do Pavão | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4123303 | Santa Cruz de Monte Castelo | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4123402 | Santa Fé | |
  | 4123501 | Santa Helena | |
  | 4123600 | Santa Inês | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4123709 | Santa Isabel do Ivaí | |
  | 4123808 | Santa Izabel do Oeste | |
  | 4123824 | Santa Lúcia | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4123857 | Santa Maria do Oeste | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4123907 | Santa Mariana | |
  | 4123956 | Santa Mônica | |
  | 4124020 | Santa Tereza do Oeste | |
  | 4124053 | Santa Terezinha de Itaipu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4124004 | Santana do Itararé | |
  | 4124202 | Santo Antônio do Caiuá | |
  | 4124301 | Santo Antônio do Paraíso | |
  | 4124103 | Santo Antônio da Platina | |
  | 4124400 | Santo Antônio do Sudoeste | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4124509 | Santo Inácio | |
  | 4124608 | São Carlos do Ivaí | |
  | 4124707 | São Jerônimo da Serra | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4124806 | São João | |
  | 4124905 | São João do Caiuá | |
  | 4125001 | São João do Ivaí | |
  | 4125100 | São João do Triunfo | |
  | 4125308 | São Jorge do Ivaí | |
  | 4125209 | São Jorge d'Oeste | |
  | 4125357 | São Jorge do Patrocínio | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4125407 | São José da Boa Vista | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4125456 | São José das Palmeiras | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4125506 | São José dos Pinhais | [pr_sao_jose_pinhais](data_collection/gazette/spiders/pr_sao_jose_pinhais.py) |
  | 4125555 | São Manoel do Paraná | |
  | 4125605 | São Mateus do Sul | [pr_sao_mateus_do_sul](data_collection/gazette/spiders/pr_sao_mateus_do_sul.py) |
  | 4125704 | São Miguel do Iguaçu | |
  | 4125753 | São Pedro do Iguaçu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4125803 | São Pedro do Ivaí | |
  | 4125902 | São Pedro do Paraná | |
  | 4126009 | São Sebastião da Amoreira | |
  | 4126108 | São Tomé | |
  | 4126207 | Sapopema | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4126256 | Sarandi | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4126272 | Saudade do Iguaçu | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4126306 | Sengés | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4126355 | Serranópolis do Iguaçu | |
  | 4126405 | Sertaneja | |
  | 4126504 | Sertanópolis | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4126603 | Siqueira Campos | |
  | 4126652 | Sulina | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4126678 | Tamarana | |
  | 4126702 | Tamboara | |
  | 4126801 | Tapejara | |
  | 4126900 | Tapira | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4127007 | Teixeira Soares | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4127106 | Telêmaco Borba | |
  | 4127205 | Terra Boa | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4127304 | Terra Rica | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4127403 | Terra Roxa | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4127502 | Tibagi | |
  | 4127601 | Tijucas do Sul | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4127700 | Toledo | |
  | 4127809 | Tomazina | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4127858 | Três Barras do Paraná | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4127882 | Tunas do Paraná | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4127908 | Tuneiras do Oeste | |
  | 4127957 | Tupãssi | |
  | 4127965 | Turvo | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4128005 | Ubiratã | |
  | 4128104 | Umuarama | |
  | 4128203 | União da Vitória | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4128302 | Uniflor | |
  | 4128401 | Uraí | |
  | 4128534 | Ventania | |
  | 4128559 | Vera Cruz do Oeste | |
  | 4128609 | Verê | [pr_associacao_municipios](data_collection/gazette/spiders/pr_associacao_municipios.py) |
  | 4128658 | Virmond | |
  | 4128708 | Vitorino | |
  | 4128500 | Wenceslau Braz | |
  | 4128807 | Xambrê | |
</details>


### Pernambuco

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 2600054 | Abreu e Lima | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2600104 | Afogados da Ingazeira | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2600203 | Afrânio | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2600302 | Agrestina | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2600401 | Água Preta | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2600500 | Águas Belas | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2600609 | Alagoinha | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2600708 | Aliança | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2600807 | Altinho | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2600906 | Amaraji | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601003 | Angelim | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601052 | Araçoiaba | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601102 | Araripina | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601201 | Arcoverde | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601300 | Barra de Guabiraba | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601409 | Barreiros | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601508 | Belém de Maria | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601607 | Belém do São Francisco | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601706 | Belo Jardim | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601805 | Betânia | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2601904 | Bezerros | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2602001 | Bodocó | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2602100 | Bom Conselho | |
  | 2602209 | Bom Jardim | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2602308 | Bonito | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2602407 | Brejão | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2602506 | Brejinho | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2602605 | Brejo da Madre de Deus | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2602704 | Buenos Aires | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2602803 | Buíque | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2602902 | Cabo de Santo Agostinho | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603009 | Cabrobó | |
  | 2603108 | Cachoeirinha | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603207 | Caetés | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603306 | Calçado | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603405 | Calumbi | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603454 | Camaragibe | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603504 | Camocim de São Félix | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603603 | Camutanga | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603702 | Canhotinho | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603801 | Capoeiras | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603900 | Carnaíba | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2603926 | Carnaubeira da Penha | |
  | 2604007 | Carpina | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2604106 | Caruaru | |
  | 2604155 | Casinhas | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2604205 | Catende | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2604304 | Cedro | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2604403 | Chã de Alegria | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2604502 | Chã Grande | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2604601 | Condado | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2604700 | Correntes | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2604809 | Cortês | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2604908 | Cumaru | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605004 | Cupira | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605103 | Custódia | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605152 | Dormentes | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605202 | Escada | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605301 | Exu | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605400 | Feira Nova | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605459 | Fernando de Noronha | |
  | 2605509 | Ferreiros | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605608 | Flores | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605707 | Floresta | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605806 | Frei Miguelinho | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2605905 | Gameleira | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2606002 | Garanhuns | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2606101 | Glória do Goitá | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2606200 | Goiana | |
  | 2606309 | Granito | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2606408 | Gravatá | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2606507 | Iati | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2606606 | Ibimirim | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2606705 | Ibirajuba | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2606804 | Igarassu | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2606903 | Iguaracy | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2607604 | Ilha de Itamaracá | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2607000 | Inajá | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2607109 | Ingazeira | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2607208 | Ipojuca | |
  | 2607307 | Ipubi | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2607406 | Itacuruba | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2607505 | Itaíba | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2607653 | Itambé | |
  | 2607703 | Itapetim | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2607752 | Itapissuma | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2607802 | Itaquitinga | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2607901 | Jaboatão dos Guararapes | |
  | 2607950 | Jaqueira | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608008 | Jataúba | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608057 | Jatobá | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608107 | João Alfredo | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608206 | Joaquim Nabuco | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608255 | Jucati | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608305 | Jupi | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608404 | Jurema | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608453 | Lagoa do Carro | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608701 | Lagoa dos Gatos | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608750 | Lagoa Grande | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608503 | Lagoa de Itaenga | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608602 | Lagoa do Ouro | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608800 | Lajedo | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2608909 | Limoeiro | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609006 | Macaparana | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609105 | Machados | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609154 | Manari | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609204 | Maraial | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609303 | Mirandiba | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2614303 | Moreilândia | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609402 | Moreno | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609501 | Nazaré da Mata | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609600 | Olinda | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609709 | Orobó | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609808 | Orocó | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2609907 | Ouricuri | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2610004 | Palmares | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2610103 | Palmeirina | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2610202 | Panelas | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2610301 | Paranatama | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2610400 | Parnamirim | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2610509 | Passira | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2610608 | Paudalho | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2610707 | Paulista | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2610806 | Pedra | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2610905 | Pesqueira | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2611002 | Petrolândia | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2611101 | Petrolina | |
  | 2611200 | Poção | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2611309 | Pombos | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2611408 | Primavera | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2611507 | Quipapá | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2611533 | Quixaba | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2611606 | Recife | [pe_recife](data_collection/gazette/spiders/pe_recife.py) |
  | 2611705 | Riacho das Almas | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2611804 | Ribeirão | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2611903 | Rio Formoso | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2612000 | Sairé | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2612109 | Salgadinho | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2612208 | Salgueiro | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2612307 | Saloá | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2612406 | Sanharó | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2612455 | Santa Cruz | |
  | 2612471 | Santa Cruz da Baixa Verde | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2612505 | Santa Cruz do Capibaribe | |
  | 2612554 | Santa Filomena | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2612604 | Santa Maria da Boa Vista | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2612703 | Santa Maria do Cambucá | |
  | 2612802 | Santa Terezinha | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2612901 | São Benedito do Sul | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2613008 | São Bento do Una | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2613107 | São Caetano | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2613206 | São João | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2613305 | São Joaquim do Monte | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2613503 | São José do Belmonte | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2613404 | São José da Coroa Grande | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2613602 | São José do Egito | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2613701 | São Lourenço da Mata | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2613800 | São Vicente Ferrer | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2613909 | Serra Talhada | |
  | 2614006 | Serrita | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2614105 | Sertânia | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2614204 | Sirinhaém | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2614402 | Solidão | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2614501 | Surubim | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2614600 | Tabira | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2614709 | Tacaimbó | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2614808 | Tacaratu | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2614857 | Tamandaré | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2615003 | Taquaritinga do Norte | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2615102 | Terezinha | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2615201 | Terra Nova | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2615300 | Timbaúba | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2615409 | Toritama | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2615508 | Tracunhaém | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2615607 | Trindade | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2615706 | Triunfo | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2615805 | Tupanatinga | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2615904 | Tuparetama | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2616001 | Venturosa | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2616100 | Verdejante | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2616183 | Vertente do Lério | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2616209 | Vertentes | |
  | 2616308 | Vicência | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2616407 | Vitória de Santo Antão | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
  | 2616506 | Xexéu | [pe_associacao_municipios](data_collection/gazette/spiders/pe_associacao_municipios.py) |
</details>


### Piauí

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 2200053 | Acauã | |
  | 2200103 | Agricolândia | |
  | 2200202 | Água Branca | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2200251 | Alagoinha do Piauí | |
  | 2200277 | Alegrete do Piauí | |
  | 2200301 | Alto Longá | |
  | 2200400 | Altos | |
  | 2200459 | Alvorada do Gurguéia | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2200509 | Amarante | |
  | 2200608 | Angical do Piauí | |
  | 2200707 | Anísio de Abreu | |
  | 2200806 | Antônio Almeida | |
  | 2200905 | Aroazes | |
  | 2200954 | Aroeiras do Itaim | |
  | 2201002 | Arraial | |
  | 2201051 | Assunção do Piauí | |
  | 2201101 | Avelino Lopes | |
  | 2201150 | Baixa Grande do Ribeiro | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2201176 | Barra D'Alcântara | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2201200 | Barras | |
  | 2201309 | Barreiras do Piauí | |
  | 2201408 | Barro Duro | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2201507 | Batalha | |
  | 2201556 | Bela Vista do Piauí | |
  | 2201572 | Belém do Piauí | |
  | 2201606 | Beneditinos | |
  | 2201705 | Bertolínia | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2201739 | Betânia do Piauí | |
  | 2201770 | Boa Hora | |
  | 2201804 | Bocaina | |
  | 2201903 | Bom Jesus | |
  | 2201919 | Bom Princípio do Piauí | |
  | 2201929 | Bonfim do Piauí | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2201945 | Boqueirão do Piauí | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2201960 | Brasileira | |
  | 2201988 | Brejo do Piauí | |
  | 2202000 | Buriti dos Lopes | |
  | 2202026 | Buriti dos Montes | |
  | 2202059 | Cabeceiras do Piauí | |
  | 2202075 | Cajazeiras do Piauí | |
  | 2202083 | Cajueiro da Praia | |
  | 2202091 | Caldeirão Grande do Piauí | |
  | 2202109 | Campinas do Piauí | |
  | 2202117 | Campo Alegre do Fidalgo | |
  | 2202133 | Campo Grande do Piauí | |
  | 2202174 | Campo Largo do Piauí | |
  | 2202208 | Campo Maior | |
  | 2202251 | Canavieira | |
  | 2202307 | Canto do Buriti | |
  | 2202406 | Capitão de Campos | |
  | 2202455 | Capitão Gervásio Oliveira | |
  | 2202505 | Caracol | |
  | 2202539 | Caraúbas do Piauí | |
  | 2202554 | Caridade do Piauí | |
  | 2202604 | Castelo do Piauí | |
  | 2202653 | Caxingó | |
  | 2202703 | Cocal | |
  | 2202729 | Cocal dos Alves | |
  | 2202711 | Cocal de Telha | |
  | 2202737 | Coivaras | |
  | 2202752 | Colônia do Gurguéia | |
  | 2202778 | Colônia do Piauí | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2202802 | Conceição do Canindé | |
  | 2202851 | Coronel José Dias | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2202901 | Corrente | |
  | 2203008 | Cristalândia do Piauí | |
  | 2203107 | Cristino Castro | |
  | 2203206 | Curimatá | |
  | 2203230 | Currais | |
  | 2203271 | Curral Novo do Piauí | |
  | 2203255 | Curralinhos | |
  | 2203305 | Demerval Lobão | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2203354 | Dirceu Arcoverde | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2203404 | Dom Expedito Lopes | |
  | 2203453 | Dom Inocêncio | |
  | 2203420 | Domingos Mourão | |
  | 2203503 | Elesbão Veloso | |
  | 2203602 | Eliseu Martins | |
  | 2203701 | Esperantina | |
  | 2203750 | Fartura do Piauí | |
  | 2203800 | Flores do Piauí | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2203859 | Floresta do Piauí | |
  | 2203909 | Floriano | |
  | 2204006 | Francinópolis | |
  | 2204105 | Francisco Ayres | |
  | 2204154 | Francisco Macedo | |
  | 2204204 | Francisco Santos | |
  | 2204303 | Fronteiras | |
  | 2204352 | Geminiano | |
  | 2204402 | Gilbués | |
  | 2204501 | Guadalupe | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2204550 | Guaribas | |
  | 2204600 | Hugo Napoleão | |
  | 2204659 | Ilha Grande | |
  | 2204709 | Inhuma | |
  | 2204808 | Ipiranga do Piauí | |
  | 2204907 | Isaías Coelho | |
  | 2205003 | Itainópolis | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2205102 | Itaueira | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2205151 | Jacobina do Piauí | |
  | 2205201 | Jaicós | |
  | 2205250 | Jardim do Mulato | |
  | 2205276 | Jatobá do Piauí | |
  | 2205300 | Jerumenha | |
  | 2205359 | João Costa | |
  | 2205409 | Joaquim Pires | |
  | 2205458 | Joca Marques | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2205508 | José de Freitas | |
  | 2205516 | Juazeiro do Piauí | |
  | 2205524 | Júlio Borges | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2205532 | Jurema | |
  | 2205557 | Lagoa Alegre | |
  | 2205565 | Lagoa do Barro do Piauí | |
  | 2205581 | Lagoa do Piauí | |
  | 2205573 | Lagoa de São Francisco | |
  | 2205599 | Lagoa do Sítio | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2205540 | Lagoinha do Piauí | |
  | 2205607 | Landri Sales | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2205706 | Luís Correia | |
  | 2205805 | Luzilândia | |
  | 2205854 | Madeiro | |
  | 2205904 | Manoel Emídio | |
  | 2205953 | Marcolândia | |
  | 2206001 | Marcos Parente | |
  | 2206050 | Massapê do Piauí | |
  | 2206100 | Matias Olímpio | |
  | 2206209 | Miguel Alves | |
  | 2206308 | Miguel Leão | |
  | 2206357 | Milton Brandão | |
  | 2206407 | Monsenhor Gil | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2206506 | Monsenhor Hipólito | |
  | 2206605 | Monte Alegre do Piauí | |
  | 2206654 | Morro Cabeça no Tempo | |
  | 2206670 | Morro do Chapéu do Piauí | |
  | 2206696 | Murici dos Portelas | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2206704 | Nazaré do Piauí | |
  | 2206720 | Nazária | |
  | 2206753 | Nossa Senhora de Nazaré | |
  | 2206803 | Nossa Senhora dos Remédios | |
  | 2207959 | Nova Santa Rita | |
  | 2206902 | Novo Oriente do Piauí | |
  | 2206951 | Novo Santo Antônio | |
  | 2207009 | Oeiras | |
  | 2207108 | Olho D'Água do Piauí | |
  | 2207207 | Padre Marcos | |
  | 2207306 | Paes Landim | |
  | 2207355 | Pajeú do Piauí | |
  | 2207405 | Palmeira do Piauí | |
  | 2207504 | Palmeirais | |
  | 2207553 | Paquetá | |
  | 2207603 | Parnaguá | |
  | 2207702 | Parnaíba | |
  | 2207751 | Passagem Franca do Piauí | |
  | 2207777 | Patos do Piauí | |
  | 2207793 | Pau D'Arco do Piauí | |
  | 2207801 | Paulistana | |
  | 2207850 | Pavussu | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2207900 | Pedro II | |
  | 2207934 | Pedro Laurentino | |
  | 2208007 | Picos | |
  | 2208106 | Pimenteiras | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2208205 | Pio IX | |
  | 2208304 | Piracuruca | |
  | 2208403 | Piripiri | |
  | 2208502 | Porto | |
  | 2208551 | Porto Alegre do Piauí | |
  | 2208601 | Prata do Piauí | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2208650 | Queimada Nova | |
  | 2208700 | Redenção do Gurguéia | |
  | 2208809 | Regeneração | |
  | 2208858 | Riacho Frio | |
  | 2208874 | Ribeira do Piauí | |
  | 2208908 | Ribeiro Gonçalves | |
  | 2209005 | Rio Grande do Piauí | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2209153 | Santa Cruz dos Milagres | |
  | 2209104 | Santa Cruz do Piauí | |
  | 2209203 | Santa Filomena | |
  | 2209302 | Santa Luz | |
  | 2209377 | Santa Rosa do Piauí | |
  | 2209351 | Santana do Piauí | |
  | 2209401 | Santo Antônio de Lisboa | |
  | 2209450 | Santo Antônio dos Milagres | |
  | 2209500 | Santo Inácio do Piauí | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2209559 | São Braz do Piauí | |
  | 2209609 | São Félix do Piauí | |
  | 2209658 | São Francisco de Assis do Piauí | |
  | 2209708 | São Francisco do Piauí | |
  | 2209757 | São Gonçalo do Gurguéia | |
  | 2209807 | São Gonçalo do Piauí | |
  | 2209971 | São João do Arraial | |
  | 2209856 | São João da Canabrava | |
  | 2209872 | São João da Fronteira | |
  | 2210003 | São João do Piauí | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2209906 | São João da Serra | |
  | 2209955 | São João da Varjota | |
  | 2210052 | São José do Divino | |
  | 2210102 | São José do Peixe | |
  | 2210201 | São José do Piauí | |
  | 2210300 | São Julião | |
  | 2210359 | São Lourenço do Piauí | |
  | 2210375 | São Luis do Piauí | |
  | 2210383 | São Miguel da Baixa Grande | |
  | 2210391 | São Miguel do Fidalgo | |
  | 2210409 | São Miguel do Tapuio | |
  | 2210508 | São Pedro do Piauí | |
  | 2210607 | São Raimundo Nonato | |
  | 2210623 | Sebastião Barros | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2210631 | Sebastião Leal | |
  | 2210656 | Sigefredo Pacheco | |
  | 2210706 | Simões | |
  | 2210805 | Simplício Mendes | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2210904 | Socorro do Piauí | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2210938 | Sussuapara | |
  | 2210953 | Tamboril do Piauí | |
  | 2210979 | Tanque do Piauí | |
  | 2211001 | Teresina | [pi_teresina](data_collection/gazette/spiders/pi_teresina.py) |
  | 2211100 | União | |
  | 2211209 | Uruçuí | |
  | 2211308 | Valença do Piauí | |
  | 2211357 | Várzea Branca | |
  | 2211407 | Várzea Grande | |
  | 2211506 | Vera Mendes | |
  | 2211605 | Vila Nova do Piauí | [pi_associacao_municipios](data_collection/gazette/spiders/pi_associacao_municipios.py) |
  | 2211704 | Wall Ferraz | |
</details>


### Rio de Janeiro

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 3300100 | Angra dos Reis | |
  | 3300159 | Aperibé | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3300209 | Araruama | |
  | 3300225 | Areal | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3300233 | Armação dos Búzios | |
  | 3300258 | Arraial do Cabo | [rj_arraial_do_cabo](data_collection/gazette/spiders/rj_arraial_do_cabo.py) |
  | 3300407 | Barra Mansa | |
  | 3300308 | Barra do Piraí | |
  | 3300456 | Belford Roxo | |
  | 3300506 | Bom Jardim | |
  | 3300605 | Bom Jesus do Itabapoana | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3300704 | Cabo Frio | |
  | 3300803 | Cachoeiras de Macacu | |
  | 3300902 | Cambuci | |
  | 3301009 | Campos dos Goytacazes | [rj_campos_goytacazes](data_collection/gazette/spiders/rj_campos_goytacazes.py) |
  | 3301108 | Cantagalo | |
  | 3300936 | Carapebus | |
  | 3301157 | Cardoso Moreira | |
  | 3301207 | Carmo | |
  | 3301306 | Casimiro de Abreu | |
  | 3300951 | Comendador Levy Gasparian | |
  | 3301405 | Conceição de Macabu | |
  | 3301504 | Cordeiro | |
  | 3301603 | Duas Barras | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3301702 | Duque de Caxias | |
  | 3301801 | Engenheiro Paulo de Frontin | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3301850 | Guapimirim | |
  | 3301876 | Iguaba Grande | |
  | 3301900 | Itaboraí | |
  | 3302007 | Itaguaí | |
  | 3302056 | Italva | |
  | 3302106 | Itaocara | |
  | 3302205 | Itaperuna | |
  | 3302254 | Itatiaia | |
  | 3302270 | Japeri | |
  | 3302304 | Laje do Muriaé | |
  | 3302403 | Macaé | |
  | 3302452 | Macuco | |
  | 3302502 | Magé | |
  | 3302601 | Mangaratiba | |
  | 3302700 | Maricá | |
  | 3302809 | Mendes | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3302858 | Mesquita | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3302908 | Miguel Pereira | |
  | 3303005 | Miracema | |
  | 3303104 | Natividade | |
  | 3303203 | Nilópolis | |
  | 3303302 | Niterói | [rj_niteroi](data_collection/gazette/spiders/rj_niteroi.py) |
  | 3303401 | Nova Friburgo | |
  | 3303500 | Nova Iguaçu | [rj_nova_iguacu](data_collection/gazette/spiders/rj_nova_iguacu.py) |
  | 3303609 | Paracambi | |
  | 3303708 | Paraíba do Sul | |
  | 3303807 | Paraty | |
  | 3303856 | Paty do Alferes | |
  | 3303906 | Petrópolis | |
  | 3303955 | Pinheiral | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3304003 | Piraí | |
  | 3304102 | Porciúncula | |
  | 3304110 | Porto Real | |
  | 3304128 | Quatis | |
  | 3304144 | Queimados | |
  | 3304151 | Quissamã | |
  | 3304201 | Resende | |
  | 3304300 | Rio Bonito | |
  | 3304409 | Rio Claro | |
  | 3304508 | Rio das Flores | |
  | 3304557 | Rio de Janeiro | [rj_rio_de_janeiro](data_collection/gazette/spiders/rj_rio_de_janeiro.py) |
  | 3304524 | Rio das Ostras | |
  | 3304607 | Santa Maria Madalena | |
  | 3304706 | Santo Antônio de Pádua | |
  | 3304805 | São Fidélis | |
  | 3304755 | São Francisco de Itabapoana | |
  | 3304904 | São Gonçalo | |
  | 3305000 | São João da Barra | |
  | 3305109 | São João de Meriti | |
  | 3305133 | São José de Ubá | |
  | 3305158 | São José do Vale do Rio Preto | |
  | 3305208 | São Pedro da Aldeia | |
  | 3305307 | São Sebastião do Alto | |
  | 3305406 | Sapucaia | |
  | 3305505 | Saquarema | |
  | 3305554 | Seropédica | |
  | 3305604 | Silva Jardim | |
  | 3305703 | Sumidouro | |
  | 3305752 | Tanguá | |
  | 3305802 | Teresópolis | |
  | 3305901 | Trajano de Moraes | |
  | 3306008 | Três Rios | |
  | 3306107 | Valença | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3306156 | Varre-Sai | |
  | 3306206 | Vassouras | [rj_associacao_municipios](data_collection/gazette/spiders/rj_associacao_municipios.py) |
  | 3306305 | Volta Redonda | |
</details>


### Rio Grande do Norte

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 2400109 | Acari | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2400208 | Açu | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2400307 | Afonso Bezerra | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2400406 | Água Nova | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2400505 | Alexandria | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2400604 | Almino Afonso | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2400703 | Alto do Rodrigues | |
  | 2400802 | Angicos | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2400901 | Antônio Martins | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401008 | Apodi | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401107 | Areia Branca | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401206 | Arês | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401305 | Augusto Severo (Campo Grande) | |
  | 2401404 | Baía Formosa | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401453 | Baraúna | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401503 | Barcelona | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401602 | Bento Fernandes | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401651 | Bodó | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401701 | Bom Jesus | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401800 | Brejinho | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401859 | Caiçara do Norte | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2401909 | Caiçara do Rio do Vento | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2402006 | Caicó | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2402105 | Campo Redondo | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2402204 | Canguaretama | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2402303 | Caraúbas | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2402402 | Carnaúba dos Dantas | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2402501 | Carnaubais | |
  | 2402600 | Ceará-Mirim | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2402709 | Cerro Corá | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2402808 | Coronel Ezequiel | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2402907 | Coronel João Pessoa | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403004 | Cruzeta | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403103 | Currais Novos | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403202 | Doutor Severiano | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403301 | Encanto | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403400 | Equador | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403509 | Espírito Santo | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403608 | Extremoz | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403707 | Felipe Guerra | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403756 | Fernando Pedroza | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403806 | Florânia | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403905 | Francisco Dantas | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404002 | Frutuoso Gomes | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404101 | Galinhos | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404200 | Goianinha | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404309 | Governador Dix-Sept Rosado | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404408 | Grossos | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404507 | Guamaré | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404606 | Ielmo Marinho | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404705 | Ipanguaçu | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404804 | Ipueira | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404853 | Itajá | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2404903 | Itaú | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2405009 | Jaçanã | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2405108 | Jandaíra | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2405207 | Janduís | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2405306 | Januário Cicco (Boa Saúde) | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2405405 | Japi | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2405504 | Jardim de Angicos | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2405603 | Jardim de Piranhas | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2405702 | Jardim do Seridó | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2405801 | João Câmara | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2405900 | João Dias | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406007 | José da Penha | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406106 | Jucurutu | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406155 | Jundiá | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406205 | Lagoa d'Anta | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406502 | Lagoa Nova | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406304 | Lagoa de Pedras | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406601 | Lagoa Salgada | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406403 | Lagoa de Velhos | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406700 | Lajes | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406809 | Lajes Pintadas | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2406908 | Lucrécia | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2407005 | Luís Gomes | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2407104 | Macaíba | |
  | 2407203 | Macau | |
  | 2407252 | Major Sales | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2407302 | Marcelino Vieira | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2407401 | Martins | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2407500 | Maxaranguape | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2407609 | Messias Targino | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2407708 | Montanhas | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2407807 | Monte Alegre | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2407906 | Monte das Gameleiras | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2408003 | Mossoró | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py), [rn_mossoro](data_collection/gazette/spiders/rn_mossoro.py) |
  | 2408102 | Natal | [rn_natal](data_collection/gazette/spiders/rn_natal.py) |
  | 2408201 | Nísia Floresta | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2408300 | Nova Cruz | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2408409 | Olho-d'Água do Borges | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2408508 | Ouro Branco | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2408607 | Paraná | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2408706 | Paraú | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2408805 | Parazinho | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2408904 | Parelhas | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2403251 | Parnamirim | |
  | 2409100 | Passa e Fica | |
  | 2409209 | Passagem | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2409308 | Patu | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2409407 | Pau dos Ferros | |
  | 2409506 | Pedra Grande | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2409605 | Pedra Preta | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2409704 | Pedro Avelino | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2409803 | Pedro Velho | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2409902 | Pendências | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2410009 | Pilões | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2410108 | Poço Branco | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2410207 | Portalegre | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2410256 | Porto do Mangue | |
  | 2410405 | Pureza | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2410504 | Rafael Fernandes | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2410603 | Rafael Godeiro | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2410702 | Riacho da Cruz | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2410801 | Riacho de Santana | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2410900 | Riachuelo | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2408953 | Rio do Fogo | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411007 | Rodolfo Fernandes | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411106 | Ruy Barbosa | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411205 | Santa Cruz | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2409332 | Santa Maria | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411403 | Santana do Matos | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411429 | Santana do Seridó | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411502 | Santo Antônio | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411601 | São Bento do Norte | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411700 | São Bento do Trairí | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411809 | São Fernando | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411908 | São Francisco do Oeste | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2412005 | São Gonçalo do Amarante | [rn_sao_goncalo_do_amarante](data_collection/gazette/spiders/rn_sao_goncalo_do_amarante.py) |
  | 2412104 | São João do Sabugi | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2412302 | São José do Campestre | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2412203 | São José de Mipibu | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2412401 | São José do Seridó | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2412500 | São Miguel | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2412559 | São Miguel do Gostoso | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2412609 | São Paulo do Potengi | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2412708 | São Pedro | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2412807 | São Rafael | |
  | 2412906 | São Tomé | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413003 | São Vicente | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413102 | Senador Elói de Souza | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413201 | Senador Georgino Avelino | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2410306 | Serra Caiada | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413359 | Serra do Mel | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413409 | Serra Negra do Norte | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413300 | Serra de São Bento | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413508 | Serrinha | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413557 | Serrinha dos Pintos | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413607 | Severiano Melo | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413706 | Sítio Novo | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2413805 | Taboleiro Grande | |
  | 2413904 | Taipu | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414001 | Tangará | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414100 | Tenente Ananias | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414159 | Tenente Laurentino Cruz | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2411056 | Tibau | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414209 | Tibau do Sul | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414308 | Timbaúba dos Batistas | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414407 | Touros | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414456 | Triunfo Potiguar | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414506 | Umarizal | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414605 | Upanema | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414704 | Várzea | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414753 | Venha-Ver | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414803 | Vera Cruz | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2414902 | Viçosa | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
  | 2415008 | Vila Flor | [rn_associacao_municipios](data_collection/gazette/spiders/rn_associacao_municipios.py) |
</details>


### Rio Grande do Sul

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 4300034 | Aceguá | |
  | 4300059 | Água Santa | |
  | 4300109 | Agudo | |
  | 4300208 | Ajuricaba | |
  | 4300307 | Alecrim | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4300406 | Alegrete | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4300455 | Alegria | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4300471 | Almirante Tamandaré do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4300505 | Alpestre | |
  | 4300554 | Alto Alegre | |
  | 4300570 | Alto Feliz | |
  | 4300604 | Alvorada | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4300638 | Amaral Ferrador | |
  | 4300646 | Ametista do Sul | |
  | 4300661 | André da Rocha | |
  | 4300703 | Anta Gorda | |
  | 4300802 | Antônio Prado | |
  | 4300851 | Arambaré | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4300877 | Araricá | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4300901 | Aratiba | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4301305 | Arroio Grande | |
  | 4301008 | Arroio do Meio | |
  | 4301073 | Arroio do Padre | |
  | 4301107 | Arroio dos Ratos | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4301057 | Arroio do Sal | |
  | 4301206 | Arroio do Tigre | |
  | 4301404 | Arvorezinha | |
  | 4301503 | Augusto Pestana | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4301552 | Áurea | |
  | 4301602 | Bagé | |
  | 4301636 | Balneário Pinhal | |
  | 4301651 | Barão | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4301701 | Barão de Cotegipe | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4301750 | Barão do Triunfo | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4301958 | Barra Funda | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4301859 | Barra do Guarita | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4301875 | Barra do Quaraí | |
  | 4301909 | Barra do Ribeiro | |
  | 4301925 | Barra do Rio Azul | |
  | 4301800 | Barracão | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4302006 | Barros Cassal | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4302055 | Benjamin Constant do Sul | |
  | 4302105 | Bento Gonçalves | |
  | 4302204 | Boa Vista do Buricá | |
  | 4302220 | Boa Vista do Cadeado | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4302238 | Boa Vista do Incra | |
  | 4302154 | Boa Vista das Missões | |
  | 4302253 | Boa Vista do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4302303 | Bom Jesus | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4302352 | Bom Princípio | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4302378 | Bom Progresso | |
  | 4302402 | Bom Retiro do Sul | |
  | 4302451 | Boqueirão do Leão | |
  | 4302501 | Bossoroca | |
  | 4302584 | Bozano | |
  | 4302600 | Braga | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4302659 | Brochier | |
  | 4302709 | Butiá | |
  | 4302808 | Caçapava do Sul | |
  | 4302907 | Cacequi | |
  | 4303004 | Cachoeira do Sul | |
  | 4303103 | Cachoeirinha | |
  | 4303202 | Cacique Doble | |
  | 4303301 | Caibaté | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4303400 | Caiçara | |
  | 4303509 | Camaquã | [rs_camaqua](data_collection/gazette/spiders/rs_camaqua.py) |
  | 4303558 | Camargo | |
  | 4303608 | Cambará do Sul | |
  | 4303673 | Campestre da Serra | |
  | 4303707 | Campina das Missões | |
  | 4303806 | Campinas do Sul | |
  | 4303905 | Campo Bom | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4304002 | Campo Novo | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4304101 | Campos Borges | |
  | 4304200 | Candelária | |
  | 4304309 | Cândido Godói | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4304358 | Candiota | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4304408 | Canela | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4304507 | Canguçu | |
  | 4304606 | Canoas | [rs_canoas](data_collection/gazette/spiders/rs_canoas.py) |
  | 4304614 | Canudos do Vale | |
  | 4304622 | Capão Bonito do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4304630 | Capão da Canoa | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4304655 | Capão do Cipó | |
  | 4304663 | Capão do Leão | |
  | 4304689 | Capela de Santana | |
  | 4304697 | Capitão | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4304671 | Capivari do Sul | |
  | 4304713 | Caraá | |
  | 4304705 | Carazinho | |
  | 4304804 | Carlos Barbosa | |
  | 4304853 | Carlos Gomes | |
  | 4304903 | Casca | |
  | 4304952 | Caseiros | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4305009 | Catuípe | |
  | 4305108 | Caxias do Sul | [rs_caxias_do_sul](data_collection/gazette/spiders/rs_caxias_do_sul.py) |
  | 4305116 | Centenário | |
  | 4305124 | Cerrito | [rs_cerrito](data_collection/gazette/spiders/rs_cerrito.py) |
  | 4305132 | Cerro Branco | |
  | 4305157 | Cerro Grande | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4305173 | Cerro Grande do Sul | |
  | 4305207 | Cerro Largo | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4305306 | Chapada | |
  | 4305355 | Charqueadas | |
  | 4305371 | Charrua | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4305405 | Chiapetta | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4305439 | Chuí | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4305447 | Chuvisca | |
  | 4305454 | Cidreira | |
  | 4305504 | Ciríaco | |
  | 4305587 | Colinas | |
  | 4305603 | Colorado | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4305702 | Condor | |
  | 4305801 | Constantina | |
  | 4305835 | Coqueiro Baixo | |
  | 4305850 | Coqueiros do Sul | |
  | 4305871 | Coronel Barros | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4305900 | Coronel Bicaco | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4305934 | Coronel Pilar | |
  | 4305959 | Cotiporã | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4305975 | Coxilha | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4306007 | Crissiumal | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4306056 | Cristal | |
  | 4306072 | Cristal do Sul | |
  | 4306106 | Cruz Alta | |
  | 4306130 | Cruzaltense | |
  | 4306205 | Cruzeiro do Sul | |
  | 4306304 | David Canabarro | |
  | 4306320 | Derrubadas | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4306353 | Dezesseis de Novembro | |
  | 4306379 | Dilermando de Aguiar | |
  | 4306403 | Dois Irmãos | |
  | 4306429 | Dois Irmãos das Missões | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4306452 | Dois Lajeados | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4306502 | Dom Feliciano | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4306601 | Dom Pedrito | |
  | 4306551 | Dom Pedro de Alcântara | |
  | 4306700 | Dona Francisca | |
  | 4306734 | Doutor Maurício Cardoso | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4306759 | Doutor Ricardo | |
  | 4306767 | Eldorado do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4306809 | Encantado | |
  | 4306908 | Encruzilhada do Sul | |
  | 4306924 | Engenho Velho | |
  | 4306932 | Entre-Ijuís | |
  | 4306957 | Entre Rios do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4306973 | Erebango | |
  | 4307005 | Erechim | |
  | 4307054 | Ernestina | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4307203 | Erval Grande | |
  | 4307302 | Erval Seco | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4307401 | Esmeralda | |
  | 4307450 | Esperança do Sul | |
  | 4307500 | Espumoso | |
  | 4307559 | Estação | |
  | 4307609 | Estância Velha | |
  | 4307708 | Esteio | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4307807 | Estrela | |
  | 4307815 | Estrela Velha | |
  | 4307831 | Eugênio de Castro | |
  | 4307864 | Fagundes Varela | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4307906 | Farroupilha | |
  | 4308003 | Faxinal do Soturno | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4308052 | Faxinalzinho | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4308078 | Fazenda Vilanova | |
  | 4308102 | Feliz | |
  | 4308201 | Flores da Cunha | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4308250 | Floriano Peixoto | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4308300 | Fontoura Xavier | |
  | 4308409 | Formigueiro | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4308433 | Forquetinha | |
  | 4308458 | Fortaleza dos Valos | |
  | 4308508 | Frederico Westphalen | |
  | 4308607 | Garibaldi | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4308656 | Garruchos | |
  | 4308706 | Gaurama | |
  | 4308805 | General Câmara | |
  | 4308854 | Gentil | |
  | 4308904 | Getúlio Vargas | |
  | 4309001 | Giruá | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4309050 | Glorinha | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4309100 | Gramado | |
  | 4309126 | Gramado dos Loureiros | |
  | 4309159 | Gramado Xavier | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4309209 | Gravataí | [rs_gravatai](data_collection/gazette/spiders/rs_gravatai.py) |
  | 4309258 | Guabiju | |
  | 4309308 | Guaíba | |
  | 4309407 | Guaporé | |
  | 4309506 | Guarani das Missões | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4309555 | Harmonia | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4307104 | Herval | |
  | 4309571 | Herveiras | |
  | 4309605 | Horizontina | |
  | 4309654 | Hulha Negra | |
  | 4309704 | Humaitá | |
  | 4309753 | Ibarama | |
  | 4309803 | Ibiaçá | |
  | 4309902 | Ibiraiaras | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4309951 | Ibirapuitã | |
  | 4310009 | Ibirubá | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310108 | Igrejinha | |
  | 4310207 | Ijuí | |
  | 4310306 | Ilópolis | |
  | 4310330 | Imbé | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310363 | Imigrante | |
  | 4310405 | Independência | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310413 | Inhacorá | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310439 | Ipê | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310462 | Ipiranga do Sul | |
  | 4310504 | Iraí | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310538 | Itaara | |
  | 4310553 | Itacurubi | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310579 | Itapuca | |
  | 4310603 | Itaqui | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310652 | Itati | |
  | 4310702 | Itatiba do Sul | |
  | 4310751 | Ivorá | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310801 | Ivoti | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310850 | Jaboticaba | |
  | 4310876 | Jacuizinho | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4310900 | Jacutinga | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4311007 | Jaguarão | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4311106 | Jaguari | |
  | 4311122 | Jaquirana | |
  | 4311130 | Jari | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4311155 | Jóia | |
  | 4311205 | Júlio de Castilhos | |
  | 4311239 | Lagoa Bonita do Sul | |
  | 4311270 | Lagoa dos Três Cantos | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4311304 | Lagoa Vermelha | |
  | 4311254 | Lagoão | |
  | 4311403 | Lajeado | |
  | 4311429 | Lajeado do Bugre | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4311502 | Lavras do Sul | |
  | 4311601 | Liberato Salzano | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4311627 | Lindolfo Collor | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4311643 | Linha Nova | |
  | 4311718 | Maçambará | |
  | 4311700 | Machadinho | |
  | 4311734 | Mampituba | |
  | 4311759 | Manoel Viana | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4311775 | Maquiné | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4311791 | Maratá | |
  | 4311809 | Marau | |
  | 4311908 | Marcelino Ramos | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4311981 | Mariana Pimentel | |
  | 4312005 | Mariano Moro | |
  | 4312054 | Marques de Souza | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4312104 | Mata | |
  | 4312138 | Mato Castelhano | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4312153 | Mato Leitão | |
  | 4312179 | Mato Queimado | |
  | 4312203 | Maximiliano de Almeida | |
  | 4312252 | Minas do Leão | |
  | 4312302 | Miraguaí | |
  | 4312351 | Montauri | |
  | 4312377 | Monte Alegre dos Campos | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4312385 | Monte Belo do Sul | |
  | 4312401 | Montenegro | |
  | 4312427 | Mormaço | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4312443 | Morrinhos do Sul | |
  | 4312450 | Morro Redondo | |
  | 4312476 | Morro Reuter | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4312500 | Mostardas | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4312609 | Muçum | |
  | 4312617 | Muitos Capões | |
  | 4312625 | Muliterno | |
  | 4312658 | Não-Me-Toque | |
  | 4312674 | Nicolau Vergueiro | |
  | 4312708 | Nonoai | |
  | 4312757 | Nova Alvorada | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4312807 | Nova Araçá | |
  | 4312906 | Nova Bassano | |
  | 4312955 | Nova Boa Vista | |
  | 4313003 | Nova Bréscia | |
  | 4313011 | Nova Candelária | |
  | 4313037 | Nova Esperança do Sul | |
  | 4313060 | Nova Hartz | |
  | 4313086 | Nova Pádua | |
  | 4313102 | Nova Palma | |
  | 4313201 | Nova Petrópolis | |
  | 4313300 | Nova Prata | |
  | 4313334 | Nova Ramada | |
  | 4313359 | Nova Roma do Sul | |
  | 4313375 | Nova Santa Rita | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4313490 | Novo Barreiro | |
  | 4313391 | Novo Cabrais | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4313409 | Novo Hamburgo | |
  | 4313425 | Novo Machado | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4313441 | Novo Tiradentes | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4313466 | Novo Xingu | |
  | 4313508 | Osório | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4313607 | Paim Filho | |
  | 4313656 | Palmares do Sul | |
  | 4313706 | Palmeira das Missões | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4313805 | Palmitinho | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4313904 | Panambi | |
  | 4313953 | Pantano Grande | |
  | 4314001 | Paraí | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4314027 | Paraíso do Sul | |
  | 4314035 | Pareci Novo | |
  | 4314050 | Parobé | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4314068 | Passa Sete | |
  | 4314100 | Passo Fundo | |
  | 4314076 | Passo do Sobrado | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4314134 | Paulo Bento | |
  | 4314159 | Paverama | |
  | 4314175 | Pedras Altas | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4314209 | Pedro Osório | |
  | 4314308 | Pejuçara | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4314407 | Pelotas | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4314423 | Picada Café | |
  | 4314456 | Pinhal | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4314472 | Pinhal Grande | |
  | 4314464 | Pinhal da Serra | |
  | 4314498 | Pinheirinho do Vale | |
  | 4314506 | Pinheiro Machado | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4314548 | Pinto Bandeira | |
  | 4314555 | Pirapó | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4314605 | Piratini | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4314704 | Planalto | |
  | 4314753 | Poço das Antas | |
  | 4314779 | Pontão | |
  | 4314787 | Ponte Preta | |
  | 4314803 | Portão | |
  | 4314902 | Porto Alegre | [rs_porto_alegre](data_collection/gazette/spiders/rs_porto_alegre.py) |
  | 4315008 | Porto Lucena | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4315057 | Porto Mauá | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4315073 | Porto Vera Cruz | |
  | 4315107 | Porto Xavier | |
  | 4315131 | Pouso Novo | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4315149 | Presidente Lucena | |
  | 4315156 | Progresso | |
  | 4315172 | Protásio Alves | |
  | 4315206 | Putinga | |
  | 4315305 | Quaraí | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4315313 | Quatro Irmãos | |
  | 4315321 | Quevedos | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4315354 | Quinze de Novembro | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4315404 | Redentora | |
  | 4315453 | Relvado | |
  | 4315503 | Restinga Sêca | |
  | 4315602 | Rio Grande | |
  | 4315552 | Rio dos Índios | |
  | 4315701 | Rio Pardo | |
  | 4315750 | Riozinho | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4315800 | Roca Sales | |
  | 4315909 | Rodeio Bonito | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4315958 | Rolador | |
  | 4316006 | Rolante | |
  | 4316105 | Ronda Alta | |
  | 4316204 | Rondinha | |
  | 4316303 | Roque Gonzales | |
  | 4316402 | Rosário do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4316428 | Sagrada Família | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4316436 | Saldanha Marinho | |
  | 4316451 | Salto do Jacuí | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4316477 | Salvador das Missões | |
  | 4316501 | Salvador do Sul | |
  | 4316600 | Sananduva | |
  | 4316709 | Santa Bárbara do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4316733 | Santa Cecília do Sul | |
  | 4316758 | Santa Clara do Sul | |
  | 4316808 | Santa Cruz do Sul | |
  | 4316972 | Santa Margarida do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4316907 | Santa Maria | |
  | 4316956 | Santa Maria do Herval | |
  | 4317202 | Santa Rosa | |
  | 4317251 | Santa Tereza | |
  | 4317301 | Santa Vitória do Palmar | |
  | 4317004 | Santana da Boa Vista | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4317103 | Sant'Ana do Livramento | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4317400 | Santiago | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4317509 | Santo Ângelo | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4317707 | Santo Antônio das Missões | |
  | 4317558 | Santo Antônio do Palma | |
  | 4317608 | Santo Antônio da Patrulha | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4317756 | Santo Antônio do Planalto | |
  | 4317806 | Santo Augusto | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4317905 | Santo Cristo | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4317954 | Santo Expedito do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4318002 | São Borja | |
  | 4318051 | São Domingos do Sul | |
  | 4318101 | São Francisco de Assis | |
  | 4318200 | São Francisco de Paula | |
  | 4318309 | São Gabriel | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4318408 | São Jerônimo | |
  | 4318432 | São João do Polêsine | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4318424 | São João da Urtiga | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4318440 | São Jorge | |
  | 4318622 | São José dos Ausentes | |
  | 4318465 | São José do Herval | |
  | 4318481 | São José do Hortêncio | |
  | 4318499 | São José do Inhacorá | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4318457 | São José das Missões | |
  | 4318507 | São José do Norte | |
  | 4318606 | São José do Ouro | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4318614 | São José do Sul | |
  | 4318705 | São Leopoldo | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4318804 | São Lourenço do Sul | |
  | 4318903 | São Luiz Gonzaga | |
  | 4319000 | São Marcos | |
  | 4319109 | São Martinho | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4319125 | São Martinho da Serra | |
  | 4319158 | São Miguel das Missões | |
  | 4319208 | São Nicolau | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4319307 | São Paulo das Missões | |
  | 4319372 | São Pedro do Butiá | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4319364 | São Pedro das Missões | |
  | 4319356 | São Pedro da Serra | |
  | 4319406 | São Pedro do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4319505 | São Sebastião do Caí | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4319604 | São Sepé | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4319703 | São Valentim | |
  | 4319711 | São Valentim do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4319737 | São Valério do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4319752 | São Vendelino | |
  | 4319802 | São Vicente do Sul | |
  | 4319901 | Sapiranga | |
  | 4320008 | Sapucaia do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4320107 | Sarandi | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4320206 | Seberi | |
  | 4320230 | Sede Nova | |
  | 4320263 | Segredo | |
  | 4320305 | Selbach | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4320321 | Senador Salgado Filho | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4320354 | Sentinela do Sul | |
  | 4320404 | Serafina Corrêa | |
  | 4320453 | Sério | |
  | 4320503 | Sertão | |
  | 4320552 | Sertão Santana | |
  | 4320578 | Sete de Setembro | |
  | 4320602 | Severiano de Almeida | |
  | 4320651 | Silveira Martins | |
  | 4320677 | Sinimbu | |
  | 4320701 | Sobradinho | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4320800 | Soledade | |
  | 4320859 | Tabaí | |
  | 4320909 | Tapejara | |
  | 4321006 | Tapera | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321105 | Tapes | |
  | 4321204 | Taquara | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321303 | Taquari | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321329 | Taquaruçu do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321352 | Tavares | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321402 | Tenente Portela | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321436 | Terra de Areia | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321451 | Teutônia | |
  | 4321469 | Tio Hugo | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321477 | Tiradentes do Sul | |
  | 4321493 | Toropi | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321501 | Torres | |
  | 4321600 | Tramandaí | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321626 | Travesseiro | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321634 | Três Arroios | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321667 | Três Cachoeiras | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321709 | Três Coroas | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4321832 | Três Forquilhas | |
  | 4321808 | Três de Maio | |
  | 4321857 | Três Palmeiras | |
  | 4321907 | Três Passos | |
  | 4321956 | Trindade do Sul | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4322004 | Triunfo | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4322103 | Tucunduva | |
  | 4322152 | Tunas | |
  | 4322186 | Tupanci do Sul | |
  | 4322202 | Tupanciretã | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4322251 | Tupandi | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4322301 | Tuparendi | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4322327 | Turuçu | |
  | 4322343 | Ubiretama | |
  | 4322350 | União da Serra | |
  | 4322376 | Unistalda | |
  | 4322400 | Uruguaiana | |
  | 4322509 | Vacaria | |
  | 4322541 | Vale Real | |
  | 4322533 | Vale do Sol | |
  | 4322525 | Vale Verde | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4322558 | Vanini | |
  | 4322608 | Venâncio Aires | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4322707 | Vera Cruz | [rs_vera_cruz](data_collection/gazette/spiders/rs_vera_cruz.py) |
  | 4322806 | Veranópolis | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4322855 | Vespasiano Corrêa | |
  | 4322905 | Viadutos | |
  | 4323002 | Viamão | |
  | 4323101 | Vicente Dutra | |
  | 4323200 | Victor Graeff | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
  | 4323309 | Vila Flores | |
  | 4323358 | Vila Lângaro | |
  | 4323408 | Vila Maria | |
  | 4323457 | Vila Nova do Sul | |
  | 4323507 | Vista Alegre | |
  | 4323606 | Vista Alegre do Prata | |
  | 4323705 | Vista Gaúcha | |
  | 4323754 | Vitória das Missões | |
  | 4323770 | Westfália | |
  | 4323804 | Xangri-lá | [rs_associacao_municipios](data_collection/gazette/spiders/rs_associacao_municipios.py) |
</details>


### Rondônia

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 1100015 | Alta Floresta D'Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100379 | Alto Alegre dos Parecis | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100403 | Alto Paraíso | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100346 | Alvorada D'Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100023 | Ariquemes | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100452 | Buritis | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100031 | Cabixi | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100601 | Cacaulândia | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100049 | Cacoal | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100700 | Campo Novo de Rondônia | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100809 | Candeias do Jamari | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100908 | Castanheiras | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100056 | Cerejeiras | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100924 | Chupinguaia | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100064 | Colorado do Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100072 | Corumbiara | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100080 | Costa Marques | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100940 | Cujubim | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100098 | Espigão D'Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101005 | Governador Jorge Teixeira | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100106 | Guajará-Mirim | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101104 | Itapuã do Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100114 | Jaru | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100122 | Ji-Paraná | |
  | 1100130 | Machadinho D'Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101203 | Ministro Andreazza | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101302 | Mirante da Serra | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101401 | Monte Negro | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100148 | Nova Brasilândia D'Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100338 | Nova Mamoré | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101435 | Nova União | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100502 | Novo Horizonte do Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100155 | Ouro Preto do Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101450 | Parecis | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100189 | Pimenta Bueno | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101468 | Pimenteiras do Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100205 | Porto Velho | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py), [ro_porto_velho](data_collection/gazette/spiders/ro_porto_velho.py) |
  | 1100254 | Presidente Médici | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101476 | Primavera de Rondônia | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100262 | Rio Crespo | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100288 | Rolim de Moura | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100296 | Santa Luzia D'Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101484 | São Felipe D'Oeste | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101492 | São Francisco do Guaporé | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100320 | São Miguel do Guaporé | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101500 | Seringueiras | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101559 | Teixeirópolis | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101609 | Theobroma | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101708 | Urupá | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101757 | Vale do Anari | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1101807 | Vale do Paraíso | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
  | 1100304 | Vilhena | [ro_associacao_municipios](data_collection/gazette/spiders/ro_associacao_municipios.py) |
</details>


### Roraima

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 1400050 | Alto Alegre | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400027 | Amajari | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400100 | Boa Vista | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py), [rr_boa_vista](data_collection/gazette/spiders/rr_boa_vista.py) |
  | 1400159 | Bonfim | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400175 | Cantá | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400209 | Caracaraí | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400233 | Caroebe | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400282 | Iracema | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400308 | Mucajaí | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400407 | Normandia | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400456 | Pacaraima | |
  | 1400472 | Rorainópolis | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400506 | São João da Baliza | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400605 | São Luiz | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
  | 1400704 | Uiramutã | [rr_associacao_municipios](data_collection/gazette/spiders/rr_associacao_municipios.py) |
</details>


### Santa Catarina

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 4200051 | Abdon Batista | [sc_abdon_batista](data_collection/gazette/spiders/sc_abdon_batista.py) |
  | 4200101 | Abelardo Luz | |
  | 4200200 | Agrolândia | [sc_agrolandia](data_collection/gazette/spiders/sc_agrolandia.py) |
  | 4200309 | Agronômica | [sc_agronomica](data_collection/gazette/spiders/sc_agronomica.py) |
  | 4200408 | Água Doce | [sc_agua_doce](data_collection/gazette/spiders/sc_agua_doce.py) |
  | 4200507 | Águas de Chapecó | [sc_aguas_de_chapeco](data_collection/gazette/spiders/sc_aguas_de_chapeco.py) |
  | 4200556 | Águas Frias | [sc_aguas_frias](data_collection/gazette/spiders/sc_aguas_frias.py) |
  | 4200606 | Águas Mornas | [sc_aguas_mornas](data_collection/gazette/spiders/sc_aguas_mornas.py) |
  | 4200705 | Alfredo Wagner | [sc_alfredo_wagner](data_collection/gazette/spiders/sc_alfredo_wagner.py) |
  | 4200754 | Alto Bela Vista | [sc_alto_bela_vista](data_collection/gazette/spiders/sc_alto_bela_vista.py) |
  | 4200804 | Anchieta | [sc_anchieta](data_collection/gazette/spiders/sc_anchieta.py) |
  | 4200903 | Angelina | [sc_angelina](data_collection/gazette/spiders/sc_angelina.py) |
  | 4201000 | Anita Garibaldi | [sc_anita_garibaldi](data_collection/gazette/spiders/sc_anita_garibaldi.py) |
  | 4201109 | Anitápolis | [sc_anitapolis](data_collection/gazette/spiders/sc_anitapolis.py) |
  | 4201208 | Antônio Carlos | [sc_antonio_carlos](data_collection/gazette/spiders/sc_antonio_carlos.py) |
  | 4201257 | Apiúna | [sc_apiuna](data_collection/gazette/spiders/sc_apiuna.py) |
  | 4201273 | Arabutã | [sc_arabuta](data_collection/gazette/spiders/sc_arabuta.py) |
  | 4201307 | Araquari | |
  | 4201406 | Araranguá | |
  | 4201505 | Armazém | |
  | 4201604 | Arroio Trinta | [sc_arroio_trinta](data_collection/gazette/spiders/sc_arroio_trinta.py) |
  | 4201653 | Arvoredo | [sc_arvoredo](data_collection/gazette/spiders/sc_arvoredo.py) |
  | 4201703 | Ascurra | [sc_ascurra](data_collection/gazette/spiders/sc_ascurra.py) |
  | 4201802 | Atalanta | [sc_atalanta](data_collection/gazette/spiders/sc_atalanta.py) |
  | 4201901 | Aurora | [sc_aurora](data_collection/gazette/spiders/sc_aurora.py) |
  | 4201950 | Balneário Arroio do Silva | [sc_balneario_arroio_do_silva](data_collection/gazette/spiders/sc_balneario_arroio_do_silva.py) |
  | 4202057 | Balneário Barra do Sul | |
  | 4202008 | Balneário Camboriú | [sc_balneario_camboriu](data_collection/gazette/spiders/sc_balneario_camboriu.py) |
  | 4202073 | Balneário Gaivota | [sc_balneario_gaivota](data_collection/gazette/spiders/sc_balneario_gaivota.py) |
  | 4212809 | Balneário Piçarras | [sc_balneario_picarras](data_collection/gazette/spiders/sc_balneario_picarras.py) |
  | 4220000 | Balneário Rincão | [sc_balneario_rincao](data_collection/gazette/spiders/sc_balneario_rincao.py) |
  | 4202081 | Bandeirante | [sc_bandeirante](data_collection/gazette/spiders/sc_bandeirante.py) |
  | 4202099 | Barra Bonita | [sc_barra_bonita](data_collection/gazette/spiders/sc_barra_bonita.py) |
  | 4202107 | Barra Velha | [sc_barra_velha](data_collection/gazette/spiders/sc_barra_velha.py) |
  | 4202131 | Bela Vista do Toldo | [sc_bela_vista_do_toldo](data_collection/gazette/spiders/sc_bela_vista_do_toldo.py) |
  | 4202156 | Belmonte | [sc_belmonte](data_collection/gazette/spiders/sc_belmonte.py) |
  | 4202206 | Benedito Novo | [sc_benedito_novo](data_collection/gazette/spiders/sc_benedito_novo.py) |
  | 4202305 | Biguaçu | [sc_biguacu](data_collection/gazette/spiders/sc_biguacu.py) |
  | 4202404 | Blumenau | [sc_blumenau](data_collection/gazette/spiders/sc_blumenau.py) |
  | 4202438 | Bocaina do Sul | |
  | 4202503 | Bom Jardim da Serra | [sc_bom_jardim_da_serra](data_collection/gazette/spiders/sc_bom_jardim_da_serra.py) |
  | 4202537 | Bom Jesus | [sc_bom_jesus](data_collection/gazette/spiders/sc_bom_jesus.py) |
  | 4202578 | Bom Jesus do Oeste | [sc_bom_jesus_do_oeste](data_collection/gazette/spiders/sc_bom_jesus_do_oeste.py) |
  | 4202602 | Bom Retiro | [sc_bom_retiro](data_collection/gazette/spiders/sc_bom_retiro.py) |
  | 4202453 | Bombinhas | |
  | 4202701 | Botuverá | [sc_botuvera](data_collection/gazette/spiders/sc_botuvera.py) |
  | 4202800 | Braço do Norte | [sc_braco_do_norte](data_collection/gazette/spiders/sc_braco_do_norte.py) |
  | 4202859 | Braço do Trombudo | [sc_braco_do_trombudo](data_collection/gazette/spiders/sc_braco_do_trombudo.py) |
  | 4202875 | Brunópolis | [sc_brunopolis](data_collection/gazette/spiders/sc_brunopolis.py) |
  | 4202909 | Brusque | [sc_brusque](data_collection/gazette/spiders/sc_brusque.py) |
  | 4203006 | Caçador | [sc_cacador](data_collection/gazette/spiders/sc_cacador.py) |
  | 4203105 | Caibi | [sc_caibi](data_collection/gazette/spiders/sc_caibi.py) |
  | 4203154 | Calmon | |
  | 4203204 | Camboriú | [sc_camboriu](data_collection/gazette/spiders/sc_camboriu.py) |
  | 4203303 | Campo Alegre | [sc_campo_alegre](data_collection/gazette/spiders/sc_campo_alegre.py) |
  | 4203402 | Campo Belo do Sul | |
  | 4203501 | Campo Erê | [sc_campo_ere](data_collection/gazette/spiders/sc_campo_ere.py) |
  | 4203600 | Campos Novos | [sc_campos_novos](data_collection/gazette/spiders/sc_campos_novos.py) |
  | 4203709 | Canelinha | [sc_canelinha](data_collection/gazette/spiders/sc_canelinha.py) |
  | 4203808 | Canoinhas | [sc_canoinhas](data_collection/gazette/spiders/sc_canoinhas.py) |
  | 4203253 | Capão Alto | [sc_capao_alto](data_collection/gazette/spiders/sc_capao_alto.py) |
  | 4203907 | Capinzal | [sc_capinzal](data_collection/gazette/spiders/sc_capinzal.py) |
  | 4203956 | Capivari de Baixo | |
  | 4204004 | Catanduvas | [sc_catanduvas](data_collection/gazette/spiders/sc_catanduvas.py) |
  | 4204103 | Caxambu do Sul | [sc_caxambu_do_sul](data_collection/gazette/spiders/sc_caxambu_do_sul.py) |
  | 4204152 | Celso Ramos | [sc_celso_ramos](data_collection/gazette/spiders/sc_celso_ramos.py) |
  | 4204178 | Cerro Negro | [sc_cerro_negro](data_collection/gazette/spiders/sc_cerro_negro.py) |
  | 4204194 | Chapadão do Lageado | [sc_chapadao_do_lageado](data_collection/gazette/spiders/sc_chapadao_do_lageado.py) |
  | 4204202 | Chapecó | [sc_chapeco](data_collection/gazette/spiders/sc_chapeco.py) |
  | 4204251 | Cocal do Sul | [sc_cocal_do_sul](data_collection/gazette/spiders/sc_cocal_do_sul.py) |
  | 4204301 | Concórdia | [sc_concordia](data_collection/gazette/spiders/sc_concordia.py) |
  | 4204350 | Cordilheira Alta | [sc_cordilheira_alta](data_collection/gazette/spiders/sc_cordilheira_alta.py) |
  | 4204400 | Coronel Freitas | [sc_coronel_freitas](data_collection/gazette/spiders/sc_coronel_freitas.py) |
  | 4204459 | Coronel Martins | [sc_coronel_martins](data_collection/gazette/spiders/sc_coronel_martins.py) |
  | 4204558 | Correia Pinto | [sc_correia_pinto](data_collection/gazette/spiders/sc_correia_pinto.py) |
  | 4204509 | Corupá | [sc_corupa](data_collection/gazette/spiders/sc_corupa.py) |
  | 4204608 | Criciúma | [sc_criciuma](data_collection/gazette/spiders/sc_criciuma.py) |
  | 4204707 | Cunha Porã | [sc_cunha_pora](data_collection/gazette/spiders/sc_cunha_pora.py) |
  | 4204756 | Cunhataí | [sc_cunhatai](data_collection/gazette/spiders/sc_cunhatai.py) |
  | 4204806 | Curitibanos | [sc_curitibanos](data_collection/gazette/spiders/sc_curitibanos.py) |
  | 4204905 | Descanso | [sc_descanso](data_collection/gazette/spiders/sc_descanso.py) |
  | 4205001 | Dionísio Cerqueira | [sc_dionisio_cerqueira](data_collection/gazette/spiders/sc_dionisio_cerqueira.py) |
  | 4205100 | Dona Emma | [sc_dona_emma](data_collection/gazette/spiders/sc_dona_emma.py) |
  | 4205159 | Doutor Pedrinho | [sc_doutor_pedrinho](data_collection/gazette/spiders/sc_doutor_pedrinho.py) |
  | 4205175 | Entre Rios | [sc_entre_rios](data_collection/gazette/spiders/sc_entre_rios.py) |
  | 4205191 | Ermo | [sc_ermo](data_collection/gazette/spiders/sc_ermo.py) |
  | 4205209 | Erval Velho | [sc_erval_velho](data_collection/gazette/spiders/sc_erval_velho.py) |
  | 4205308 | Faxinal dos Guedes | [sc_faxinal_dos_guedes](data_collection/gazette/spiders/sc_faxinal_dos_guedes.py) |
  | 4205357 | Flor do Sertão | [sc_flor_do_sertao](data_collection/gazette/spiders/sc_flor_do_sertao.py) |
  | 4205407 | Florianópolis | [sc_florianopolis](data_collection/gazette/spiders/sc_florianopolis.py) |
  | 4205431 | Formosa do Sul | [sc_formosa_do_sul](data_collection/gazette/spiders/sc_formosa_do_sul.py) |
  | 4205456 | Forquilhinha | [sc_forquilhinha](data_collection/gazette/spiders/sc_forquilhinha.py) |
  | 4205506 | Fraiburgo | [sc_fraiburgo](data_collection/gazette/spiders/sc_fraiburgo.py) |
  | 4205555 | Frei Rogério | [sc_frei_rogerio](data_collection/gazette/spiders/sc_frei_rogerio.py) |
  | 4205605 | Galvão | [sc_galvao](data_collection/gazette/spiders/sc_galvao.py) |
  | 4205704 | Garopaba | [sc_garopaba](data_collection/gazette/spiders/sc_garopaba.py) |
  | 4205803 | Garuva | [sc_garuva](data_collection/gazette/spiders/sc_garuva.py) |
  | 4205902 | Gaspar | [sc_gaspar](data_collection/gazette/spiders/sc_gaspar.py) |
  | 4206009 | Governador Celso Ramos | [sc_governador_celso_ramos](data_collection/gazette/spiders/sc_governador_celso_ramos.py) |
  | 4206108 | Grão Pará | [sc_grao_para](data_collection/gazette/spiders/sc_grao_para.py) |
  | 4206207 | Gravatal | [sc_gravatal](data_collection/gazette/spiders/sc_gravatal.py) |
  | 4206306 | Guabiruba | [sc_guabiruba](data_collection/gazette/spiders/sc_guabiruba.py) |
  | 4206405 | Guaraciaba | [sc_guaraciaba](data_collection/gazette/spiders/sc_guaraciaba.py) |
  | 4206504 | Guaramirim | [sc_guaramirim](data_collection/gazette/spiders/sc_guaramirim.py) |
  | 4206603 | Guarujá do Sul | [sc_guaruja_do_sul](data_collection/gazette/spiders/sc_guaruja_do_sul.py) |
  | 4206652 | Guatambú | [sc_guatambu](data_collection/gazette/spiders/sc_guatambu.py) |
  | 4206702 | Herval d'Oeste | [sc_herval_doeste](data_collection/gazette/spiders/sc_herval_doeste.py) |
  | 4206751 | Ibiam | [sc_ibiam](data_collection/gazette/spiders/sc_ibiam.py) |
  | 4206801 | Ibicaré | [sc_ibicare](data_collection/gazette/spiders/sc_ibicare.py) |
  | 4206900 | Ibirama | [sc_ibirama](data_collection/gazette/spiders/sc_ibirama.py) |
  | 4207007 | Içara | |
  | 4207106 | Ilhota | [sc_ilhota](data_collection/gazette/spiders/sc_ilhota.py) |
  | 4207205 | Imaruí | [sc_imarui](data_collection/gazette/spiders/sc_imarui.py) |
  | 4207304 | Imbituba | [sc_imbituba](data_collection/gazette/spiders/sc_imbituba.py) |
  | 4207403 | Imbuia | [sc_imbuia](data_collection/gazette/spiders/sc_imbuia.py) |
  | 4207502 | Indaial | [sc_indaial](data_collection/gazette/spiders/sc_indaial.py) |
  | 4207577 | Iomerê | [sc_iomere](data_collection/gazette/spiders/sc_iomere.py) |
  | 4207601 | Ipira | [sc_ipira](data_collection/gazette/spiders/sc_ipira.py) |
  | 4207650 | Iporã do Oeste | [sc_ipora_do_oeste](data_collection/gazette/spiders/sc_ipora_do_oeste.py) |
  | 4207684 | Ipuaçu | [sc_ipuacu](data_collection/gazette/spiders/sc_ipuacu.py) |
  | 4207700 | Ipumirim | [sc_ipumirim](data_collection/gazette/spiders/sc_ipumirim.py) |
  | 4207759 | Iraceminha | [sc_iraceminha](data_collection/gazette/spiders/sc_iraceminha.py) |
  | 4207809 | Irani | [sc_irani](data_collection/gazette/spiders/sc_irani.py) |
  | 4207858 | Irati | [sc_irati](data_collection/gazette/spiders/sc_irati.py) |
  | 4207908 | Irineópolis | [sc_irineopolis](data_collection/gazette/spiders/sc_irineopolis.py) |
  | 4208005 | Itá | [sc_ita](data_collection/gazette/spiders/sc_ita.py) |
  | 4208104 | Itaiópolis | [sc_itaiopolis](data_collection/gazette/spiders/sc_itaiopolis.py) |
  | 4208203 | Itajaí | [sc_itajai](data_collection/gazette/spiders/sc_itajai.py) |
  | 4208302 | Itapema | [sc_itapema](data_collection/gazette/spiders/sc_itapema.py) |
  | 4208401 | Itapiranga | [sc_itapiranga](data_collection/gazette/spiders/sc_itapiranga.py) |
  | 4208450 | Itapoá | [sc_itapoa](data_collection/gazette/spiders/sc_itapoa.py) |
  | 4208500 | Ituporanga | [sc_ituporanga](data_collection/gazette/spiders/sc_ituporanga.py) |
  | 4208609 | Jaborá | [sc_jabora](data_collection/gazette/spiders/sc_jabora.py) |
  | 4208708 | Jacinto Machado | [sc_jacinto_machado](data_collection/gazette/spiders/sc_jacinto_machado.py) |
  | 4208807 | Jaguaruna | [sc_jaguaruna](data_collection/gazette/spiders/sc_jaguaruna.py) |
  | 4208906 | Jaraguá do Sul | [sc_jaragua_do_sul](data_collection/gazette/spiders/sc_jaragua_do_sul.py) |
  | 4208955 | Jardinópolis | [sc_jardinopolis](data_collection/gazette/spiders/sc_jardinopolis.py) |
  | 4209003 | Joaçaba | [sc_joacaba](data_collection/gazette/spiders/sc_joacaba.py) |
  | 4209102 | Joinville | [sc_joinville](data_collection/gazette/spiders/sc_joinville.py) |
  | 4209151 | José Boiteux | [sc_jose_boiteux](data_collection/gazette/spiders/sc_jose_boiteux.py) |
  | 4209177 | Jupiá | [sc_jupia](data_collection/gazette/spiders/sc_jupia.py) |
  | 4209201 | Lacerdópolis | [sc_lacerdopolis](data_collection/gazette/spiders/sc_lacerdopolis.py) |
  | 4209300 | Lages | [sc_lages](data_collection/gazette/spiders/sc_lages.py) |
  | 4209409 | Laguna | [sc_laguna](data_collection/gazette/spiders/sc_laguna.py) |
  | 4209458 | Lajeado Grande | [sc_lajeado_grande](data_collection/gazette/spiders/sc_lajeado_grande.py) |
  | 4209508 | Laurentino | |
  | 4209607 | Lauro Muller | [sc_lauro_muller](data_collection/gazette/spiders/sc_lauro_muller.py) |
  | 4209706 | Lebon Régis | [sc_lebon_regis](data_collection/gazette/spiders/sc_lebon_regis.py) |
  | 4209805 | Leoberto Leal | [sc_leoberto_leal](data_collection/gazette/spiders/sc_leoberto_leal.py) |
  | 4209854 | Lindóia do Sul | [sc_lindoia_do_sul](data_collection/gazette/spiders/sc_lindoia_do_sul.py) |
  | 4209904 | Lontras | [sc_lontras](data_collection/gazette/spiders/sc_lontras.py) |
  | 4210001 | Luiz Alves | [sc_luiz_alves](data_collection/gazette/spiders/sc_luiz_alves.py) |
  | 4210035 | Luzerna | [sc_luzerna](data_collection/gazette/spiders/sc_luzerna.py) |
  | 4210050 | Macieira | [sc_macieira](data_collection/gazette/spiders/sc_macieira.py) |
  | 4210100 | Mafra | [sc_mafra](data_collection/gazette/spiders/sc_mafra.py) |
  | 4210209 | Major Gercino | |
  | 4210308 | Major Vieira | [sc_major_vieira](data_collection/gazette/spiders/sc_major_vieira.py) |
  | 4210407 | Maracajá | [sc_maracaja](data_collection/gazette/spiders/sc_maracaja.py) |
  | 4210506 | Maravilha | [sc_maravilha](data_collection/gazette/spiders/sc_maravilha.py) |
  | 4210555 | Marema | [sc_marema](data_collection/gazette/spiders/sc_marema.py) |
  | 4210605 | Massaranduba | [sc_massaranduba](data_collection/gazette/spiders/sc_massaranduba.py) |
  | 4210704 | Matos Costa | [sc_matos_costa](data_collection/gazette/spiders/sc_matos_costa.py) |
  | 4210803 | Meleiro | [sc_meleiro](data_collection/gazette/spiders/sc_meleiro.py) |
  | 4210852 | Mirim Doce | [sc_mirim_doce](data_collection/gazette/spiders/sc_mirim_doce.py) |
  | 4210902 | Modelo | [sc_modelo](data_collection/gazette/spiders/sc_modelo.py) |
  | 4211009 | Mondaí | [sc_mondai](data_collection/gazette/spiders/sc_mondai.py) |
  | 4211058 | Monte Carlo | [sc_monte_carlo](data_collection/gazette/spiders/sc_monte_carlo.py) |
  | 4211108 | Monte Castelo | [sc_monte_castelo](data_collection/gazette/spiders/sc_monte_castelo.py) |
  | 4211207 | Morro da Fumaça | [sc_morro_da_fumaca](data_collection/gazette/spiders/sc_morro_da_fumaca.py) |
  | 4211256 | Morro Grande | [sc_morro_grande](data_collection/gazette/spiders/sc_morro_grande.py) |
  | 4211306 | Navegantes | [sc_navegantes](data_collection/gazette/spiders/sc_navegantes.py) |
  | 4211405 | Nova Erechim | [sc_nova_erechim](data_collection/gazette/spiders/sc_nova_erechim.py) |
  | 4211454 | Nova Itaberaba | [sc_nova_itaberaba](data_collection/gazette/spiders/sc_nova_itaberaba.py) |
  | 4211504 | Nova Trento | [sc_nova_trento](data_collection/gazette/spiders/sc_nova_trento.py) |
  | 4211603 | Nova Veneza | [sc_nova_veneza](data_collection/gazette/spiders/sc_nova_veneza.py) |
  | 4211652 | Novo Horizonte | [sc_novo_horizonte](data_collection/gazette/spiders/sc_novo_horizonte.py) |
  | 4211702 | Orleans | [sc_orleans](data_collection/gazette/spiders/sc_orleans.py) |
  | 4211751 | Otacílio Costa | [sc_otacilio_costa](data_collection/gazette/spiders/sc_otacilio_costa.py) |
  | 4211801 | Ouro | [sc_ouro](data_collection/gazette/spiders/sc_ouro.py) |
  | 4211850 | Ouro Verde | [sc_ouro_verde](data_collection/gazette/spiders/sc_ouro_verde.py) |
  | 4211876 | Paial | [sc_paial](data_collection/gazette/spiders/sc_paial.py) |
  | 4211892 | Painel | |
  | 4211900 | Palhoça | [sc_palhoca](data_collection/gazette/spiders/sc_palhoca.py) |
  | 4212007 | Palma Sola | [sc_palma_sola](data_collection/gazette/spiders/sc_palma_sola.py) |
  | 4212056 | Palmeira | [sc_palmeira](data_collection/gazette/spiders/sc_palmeira.py) |
  | 4212106 | Palmitos | [sc_palmitos](data_collection/gazette/spiders/sc_palmitos.py) |
  | 4212205 | Papanduva | [sc_papanduva](data_collection/gazette/spiders/sc_papanduva.py) |
  | 4212239 | Paraíso | [sc_paraiso](data_collection/gazette/spiders/sc_paraiso.py) |
  | 4212254 | Passo de Torres | [sc_passo_de_torres](data_collection/gazette/spiders/sc_passo_de_torres.py) |
  | 4212270 | Passos Maia | [sc_passos_maia](data_collection/gazette/spiders/sc_passos_maia.py) |
  | 4212304 | Paulo Lopes | [sc_paulo_lopes](data_collection/gazette/spiders/sc_paulo_lopes.py) |
  | 4212403 | Pedras Grandes | [sc_pedras_grandes](data_collection/gazette/spiders/sc_pedras_grandes.py) |
  | 4212502 | Penha | [sc_penha](data_collection/gazette/spiders/sc_penha.py) |
  | 4212601 | Peritiba | [sc_peritiba](data_collection/gazette/spiders/sc_peritiba.py) |
  | 4212650 | Pescaria Brava | [sc_pescaria_brava](data_collection/gazette/spiders/sc_pescaria_brava.py) |
  | 4212700 | Petrolândia | [sc_petrolandia](data_collection/gazette/spiders/sc_petrolandia.py) |
  | 4212908 | Pinhalzinho | [sc_pinhalzinho](data_collection/gazette/spiders/sc_pinhalzinho.py) |
  | 4213005 | Pinheiro Preto | [sc_pinheiro_preto](data_collection/gazette/spiders/sc_pinheiro_preto.py) |
  | 4213104 | Piratuba | [sc_piratuba](data_collection/gazette/spiders/sc_piratuba.py) |
  | 4213153 | Planalto Alegre | [sc_planalto_alegre](data_collection/gazette/spiders/sc_planalto_alegre.py) |
  | 4213203 | Pomerode | [sc_pomerode](data_collection/gazette/spiders/sc_pomerode.py) |
  | 4213302 | Ponte Alta | |
  | 4213351 | Ponte Alta do Norte | [sc_ponte_alta_do_norte](data_collection/gazette/spiders/sc_ponte_alta_do_norte.py) |
  | 4213401 | Ponte Serrada | [sc_ponte_serrada](data_collection/gazette/spiders/sc_ponte_serrada.py) |
  | 4213500 | Porto Belo | [sc_porto_belo](data_collection/gazette/spiders/sc_porto_belo.py) |
  | 4213609 | Porto União | [sc_porto_uniao](data_collection/gazette/spiders/sc_porto_uniao.py) |
  | 4213708 | Pouso Redondo | [sc_pouso_redondo](data_collection/gazette/spiders/sc_pouso_redondo.py) |
  | 4213807 | Praia Grande | [sc_praia_grande](data_collection/gazette/spiders/sc_praia_grande.py) |
  | 4213906 | Presidente Castello Branco | [sc_presidente_castello_branco](data_collection/gazette/spiders/sc_presidente_castello_branco.py) |
  | 4214003 | Presidente Getúlio | [sc_presidente_getulio](data_collection/gazette/spiders/sc_presidente_getulio.py) |
  | 4214102 | Presidente Nereu | [sc_presidente_nereu](data_collection/gazette/spiders/sc_presidente_nereu.py) |
  | 4214151 | Princesa | [sc_princesa](data_collection/gazette/spiders/sc_princesa.py) |
  | 4214201 | Quilombo | [sc_quilombo](data_collection/gazette/spiders/sc_quilombo.py) |
  | 4214300 | Rancho Queimado | [sc_rancho_queimado](data_collection/gazette/spiders/sc_rancho_queimado.py) |
  | 4214409 | Rio das Antas | [sc_rio_das_antas](data_collection/gazette/spiders/sc_rio_das_antas.py) |
  | 4214508 | Rio do Campo | [sc_rio_do_campo](data_collection/gazette/spiders/sc_rio_do_campo.py) |
  | 4214706 | Rio dos Cedros | [sc_rio_dos_cedros](data_collection/gazette/spiders/sc_rio_dos_cedros.py) |
  | 4214904 | Rio Fortuna | [sc_rio_fortuna](data_collection/gazette/spiders/sc_rio_fortuna.py) |
  | 4215000 | Rio Negrinho | [sc_rio_negrinho](data_collection/gazette/spiders/sc_rio_negrinho.py) |
  | 4214607 | Rio do Oeste | [sc_rio_do_oeste](data_collection/gazette/spiders/sc_rio_do_oeste.py) |
  | 4215059 | Rio Rufino | [sc_rio_rufino](data_collection/gazette/spiders/sc_rio_rufino.py) |
  | 4214805 | Rio do Sul | [sc_rio_do_sul](data_collection/gazette/spiders/sc_rio_do_sul.py) |
  | 4215075 | Riqueza | |
  | 4215109 | Rodeio | [sc_rodeio](data_collection/gazette/spiders/sc_rodeio.py) |
  | 4215208 | Romelândia | [sc_romelandia](data_collection/gazette/spiders/sc_romelandia.py) |
  | 4215307 | Salete | |
  | 4215356 | Saltinho | [sc_saltinho](data_collection/gazette/spiders/sc_saltinho.py) |
  | 4215406 | Salto Veloso | [sc_salto_veloso](data_collection/gazette/spiders/sc_salto_veloso.py) |
  | 4215455 | Sangão | |
  | 4215505 | Santa Cecília | [sc_santa_cecilia](data_collection/gazette/spiders/sc_santa_cecilia.py) |
  | 4215554 | Santa Helena | [sc_santa_helena](data_collection/gazette/spiders/sc_santa_helena.py) |
  | 4215604 | Santa Rosa de Lima | [sc_santa_rosa_de_lima](data_collection/gazette/spiders/sc_santa_rosa_de_lima.py) |
  | 4215653 | Santa Rosa do Sul | [sc_santa_rosa_do_sul](data_collection/gazette/spiders/sc_santa_rosa_do_sul.py) |
  | 4215679 | Santa Terezinha | |
  | 4215695 | Santa Terezinha do Progresso | [sc_santiago_do_sul](data_collection/gazette/spiders/sc_santiago_do_sul.py) |
  | 4215687 | Santiago do Sul | [sc_santa_terezinha_do_progresso](data_collection/gazette/spiders/sc_santa_terezinha_do_progresso.py) |
  | 4215703 | Santo Amaro da Imperatriz | [sc_santo_amaro_da_imperatriz](data_collection/gazette/spiders/sc_santo_amaro_da_imperatriz.py) |
  | 4215802 | São Bento do Sul | [sc_sao_bento_do_sul](data_collection/gazette/spiders/sc_sao_bento_do_sul.py) |
  | 4215752 | São Bernardino | [sc_sao_bernardino](data_collection/gazette/spiders/sc_sao_bernardino.py) |
  | 4215901 | São Bonifácio | [sc_sao_bonifacio](data_collection/gazette/spiders/sc_sao_bonifacio.py) |
  | 4216008 | São Carlos | [sc_sao_carlos](data_collection/gazette/spiders/sc_sao_carlos.py) |
  | 4216057 | São Cristovão do Sul | [sc_sao_cristovao_do_sul](data_collection/gazette/spiders/sc_sao_cristovao_do_sul.py) |
  | 4216107 | São Domingos | [sc_sao_domingos](data_collection/gazette/spiders/sc_sao_domingos.py) |
  | 4216206 | São Francisco do Sul | [sc_sao_francisco_do_sul](data_collection/gazette/spiders/sc_sao_francisco_do_sul.py) |
  | 4216305 | São João Batista | [sc_sao_joao_batista](data_collection/gazette/spiders/sc_sao_joao_batista.py) |
  | 4216354 | São João do Itaperiú | |
  | 4216255 | São João do Oeste | [sc_sao_joao_do_oeste](data_collection/gazette/spiders/sc_sao_joao_do_oeste.py) |
  | 4216404 | São João do Sul | [sc_sao_joao_do_sul](data_collection/gazette/spiders/sc_sao_joao_do_sul.py) |
  | 4216503 | São Joaquim | [sc_sao_joaquim](data_collection/gazette/spiders/sc_sao_joaquim.py) |
  | 4216602 | São José | [sc_sao_jose](data_collection/gazette/spiders/sc_sao_jose.py) |
  | 4216701 | São José do Cedro | [sc_sao_jose_do_cedro](data_collection/gazette/spiders/sc_sao_jose_do_cedro.py) |
  | 4216800 | São José do Cerrito | [sc_sao_jose_do_cerrito](data_collection/gazette/spiders/sc_sao_jose_do_cerrito.py) |
  | 4216909 | São Lourenço do Oeste | [sc_sao_lourenco_do_oeste](data_collection/gazette/spiders/sc_sao_lourenco_do_oeste.py) |
  | 4217006 | São Ludgero | |
  | 4217105 | São Martinho | |
  | 4217154 | São Miguel da Boa Vista | [sc_sao_miguel_da_boa_vista](data_collection/gazette/spiders/sc_sao_miguel_da_boa_vista.py) |
  | 4217204 | São Miguel do Oeste | [sc_sao_miguel_do_oeste](data_collection/gazette/spiders/sc_sao_miguel_do_oeste.py) |
  | 4217253 | São Pedro de Alcântara | [sc_sao_pedro_de_alcantara](data_collection/gazette/spiders/sc_sao_pedro_de_alcantara.py) |
  | 4217303 | Saudades | [sc_saudades](data_collection/gazette/spiders/sc_saudades.py) |
  | 4217402 | Schroeder | [sc_schroeder](data_collection/gazette/spiders/sc_schroeder.py) |
  | 4217501 | Seara | [sc_seara](data_collection/gazette/spiders/sc_seara.py) |
  | 4217550 | Serra Alta | [sc_serra_alta](data_collection/gazette/spiders/sc_serra_alta.py) |
  | 4217600 | Siderópolis | [sc_sideropolis](data_collection/gazette/spiders/sc_sideropolis.py) |
  | 4217709 | Sombrio | [sc_sombrio](data_collection/gazette/spiders/sc_sombrio.py) |
  | 4217758 | Sul Brasil | [sc_sul_brasil](data_collection/gazette/spiders/sc_sul_brasil.py) |
  | 4217808 | Taió | |
  | 4217907 | Tangará | [sc_tangara](data_collection/gazette/spiders/sc_tangara.py) |
  | 4217956 | Tigrinhos | [sc_tigrinhos](data_collection/gazette/spiders/sc_tigrinhos.py) |
  | 4218004 | Tijucas | [sc_tijucas](data_collection/gazette/spiders/sc_tijucas.py) |
  | 4218103 | Timbé do Sul | [sc_timbe_do_sul](data_collection/gazette/spiders/sc_timbe_do_sul.py) |
  | 4218202 | Timbó | [sc_timbo](data_collection/gazette/spiders/sc_timbo.py) |
  | 4218251 | Timbó Grande | [sc_timbo_grande](data_collection/gazette/spiders/sc_timbo_grande.py) |
  | 4218301 | Três Barras | [sc_tres_barras](data_collection/gazette/spiders/sc_tres_barras.py) |
  | 4218350 | Treviso | [sc_treviso](data_collection/gazette/spiders/sc_treviso.py) |
  | 4218400 | Treze de Maio | [sc_treze_de_maio](data_collection/gazette/spiders/sc_treze_de_maio.py) |
  | 4218509 | Treze Tílias | [sc_treze_tilias](data_collection/gazette/spiders/sc_treze_tilias.py) |
  | 4218608 | Trombudo Central | [sc_trombudo_central](data_collection/gazette/spiders/sc_trombudo_central.py) |
  | 4218707 | Tubarão | [sc_tubarao](data_collection/gazette/spiders/sc_tubarao.py) |
  | 4218756 | Tunápolis | [sc_tunapolis](data_collection/gazette/spiders/sc_tunapolis.py) |
  | 4218806 | Turvo | [sc_turvo](data_collection/gazette/spiders/sc_turvo.py) |
  | 4218855 | União do Oeste | [sc_uniao_do_oeste](data_collection/gazette/spiders/sc_uniao_do_oeste.py) |
  | 4218905 | Urubici | [sc_urubici](data_collection/gazette/spiders/sc_urubici.py) |
  | 4218954 | Urupema | [sc_urupema](data_collection/gazette/spiders/sc_urupema.py) |
  | 4219002 | Urussanga | [sc_urussanga](data_collection/gazette/spiders/sc_urussanga.py) |
  | 4219101 | Vargeão | [sc_vargeao](data_collection/gazette/spiders/sc_vargeao.py) |
  | 4219150 | Vargem | [sc_vargem](data_collection/gazette/spiders/sc_vargem.py) |
  | 4219176 | Vargem Bonita | [sc_vargem_bonita](data_collection/gazette/spiders/sc_vargem_bonita.py) |
  | 4219200 | Vidal Ramos | [sc_vidal_ramos](data_collection/gazette/spiders/sc_vidal_ramos.py) |
  | 4219309 | Videira | [sc_videira](data_collection/gazette/spiders/sc_videira.py) |
  | 4219358 | Vitor Meireles | [sc_vitor_meireles](data_collection/gazette/spiders/sc_vitor_meireles.py) |
  | 4219408 | Witmarsum | [sc_witmarsum](data_collection/gazette/spiders/sc_witmarsum.py) |
  | 4219507 | Xanxerê | [sc_xanxere](data_collection/gazette/spiders/sc_xanxere.py) |
  | 4219606 | Xavantina | [sc_xavantina](data_collection/gazette/spiders/sc_xavantina.py) |
  | 4219705 | Xaxim | [sc_xaxim](data_collection/gazette/spiders/sc_xaxim.py) |
  | 4219853 | Zortéa | [sc_zortea](data_collection/gazette/spiders/sc_zortea.py) |
</details>


### São Paulo

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 3500105 | Adamantina | |
  | 3500204 | Adolfo | |
  | 3500303 | Aguaí | |
  | 3500501 | Águas de Lindóia | |
  | 3500402 | Águas da Prata | |
  | 3500550 | Águas de Santa Bárbara | |
  | 3500600 | Águas de São Pedro | |
  | 3500709 | Agudos | |
  | 3500758 | Alambari | |
  | 3500808 | Alfredo Marcondes | |
  | 3500907 | Altair | |
  | 3501004 | Altinópolis | |
  | 3501103 | Alto Alegre | [sp_alto_alegre](data_collection/gazette/spiders/sp_alto_alegre.py) |
  | 3501152 | Alumínio | |
  | 3501202 | Álvares Florence | |
  | 3501301 | Álvares Machado | |
  | 3501400 | Álvaro de Carvalho | |
  | 3501509 | Alvinlândia | |
  | 3501608 | Americana | |
  | 3501707 | Américo Brasiliense | |
  | 3501806 | Américo de Campos | |
  | 3501905 | Amparo | |
  | 3502002 | Analândia | |
  | 3502101 | Andradina | |
  | 3502200 | Angatuba | |
  | 3502309 | Anhembi | |
  | 3502408 | Anhumas | |
  | 3502507 | Aparecida | |
  | 3502606 | Aparecida d'Oeste | |
  | 3502705 | Apiaí | |
  | 3502754 | Araçariguama | [sp_aracariguama](data_collection/gazette/spiders/sp_aracariguama.py) |
  | 3502804 | Araçatuba | |
  | 3502903 | Araçoiaba da Serra | |
  | 3503000 | Aramina | |
  | 3503109 | Arandu | |
  | 3503158 | Arapeí | |
  | 3503208 | Araraquara | |
  | 3503307 | Araras | |
  | 3503356 | Arco-Íris | |
  | 3503406 | Arealva | |
  | 3503505 | Areias | |
  | 3503604 | Areiópolis | |
  | 3503703 | Ariranha | |
  | 3503802 | Artur Nogueira | |
  | 3503901 | Arujá | |
  | 3503950 | Aspásia | |
  | 3504008 | Assis | |
  | 3504107 | Atibaia | |
  | 3504206 | Auriflama | |
  | 3504305 | Avaí | |
  | 3504404 | Avanhandava | |
  | 3504503 | Avaré | |
  | 3504602 | Bady Bassitt | |
  | 3504701 | Balbinos | |
  | 3504800 | Bálsamo | |
  | 3504909 | Bananal | |
  | 3505005 | Barão de Antonina | [sp_barao_de_antonina](data_collection/gazette/spiders/sp_barao_de_antonina.py) |
  | 3505104 | Barbosa | |
  | 3505203 | Bariri | |
  | 3505302 | Barra Bonita | |
  | 3505351 | Barra do Chapéu | |
  | 3505401 | Barra do Turvo | [sp_associacao_municipios](data_collection/gazette/spiders/sp_associacao_municipios.py) |
  | 3505500 | Barretos | |
  | 3505609 | Barrinha | |
  | 3505708 | Barueri | |
  | 3505807 | Bastos | |
  | 3505906 | Batatais | |
  | 3506003 | Bauru | [sp_bauru](data_collection/gazette/spiders/sp_bauru.py) |
  | 3506102 | Bebedouro | |
  | 3506201 | Bento de Abreu | |
  | 3506300 | Bernardino de Campos | |
  | 3506359 | Bertioga | |
  | 3506409 | Bilac | |
  | 3506508 | Birigui | |
  | 3506607 | Biritiba-Mirim | |
  | 3506706 | Boa Esperança do Sul | |
  | 3506805 | Bocaina | [sp_associacao_municipios](data_collection/gazette/spiders/sp_associacao_municipios.py) |
  | 3506904 | Bofete | |
  | 3507001 | Boituva | |
  | 3507100 | Bom Jesus dos Perdões | |
  | 3507159 | Bom Sucesso de Itararé | |
  | 3507209 | Borá | |
  | 3507308 | Boracéia | |
  | 3507407 | Borborema | |
  | 3507456 | Borebi | |
  | 3507506 | Botucatu | |
  | 3507605 | Bragança Paulista | |
  | 3507704 | Braúna | |
  | 3507753 | Brejo Alegre | |
  | 3507803 | Brodowski | |
  | 3507902 | Brotas | |
  | 3508009 | Buri | |
  | 3508108 | Buritama | |
  | 3508207 | Buritizal | |
  | 3508306 | Cabrália Paulista | |
  | 3508405 | Cabreúva | |
  | 3508504 | Caçapava | |
  | 3508603 | Cachoeira Paulista | |
  | 3508702 | Caconde | |
  | 3508801 | Cafelândia | |
  | 3508900 | Caiabu | |
  | 3509007 | Caieiras | |
  | 3509106 | Caiuá | |
  | 3509205 | Cajamar | |
  | 3509254 | Cajati | |
  | 3509304 | Cajobi | |
  | 3509403 | Cajuru | |
  | 3509452 | Campina do Monte Alegre | |
  | 3509502 | Campinas | [sp_campinas](data_collection/gazette/spiders/sp_campinas.py) |
  | 3509601 | Campo Limpo Paulista | |
  | 3509700 | Campos do Jordão | |
  | 3509809 | Campos Novos Paulista | |
  | 3509908 | Cananéia | |
  | 3509957 | Canas | |
  | 3510005 | Cândido Mota | |
  | 3510104 | Cândido Rodrigues | |
  | 3510153 | Canitar | |
  | 3510203 | Capão Bonito | |
  | 3510302 | Capela do Alto | |
  | 3510401 | Capivari | |
  | 3510500 | Caraguatatuba | |
  | 3510609 | Carapicuíba | |
  | 3510708 | Cardoso | |
  | 3510807 | Casa Branca | |
  | 3510906 | Cássia dos Coqueiros | |
  | 3511003 | Castilho | |
  | 3511102 | Catanduva | |
  | 3511201 | Catiguá | |
  | 3511300 | Cedral | |
  | 3511409 | Cerqueira César | |
  | 3511508 | Cerquilho | |
  | 3511607 | Cesário Lange | |
  | 3511706 | Charqueada | |
  | 3557204 | Chavantes | |
  | 3511904 | Clementina | |
  | 3512001 | Colina | |
  | 3512100 | Colômbia | |
  | 3512209 | Conchal | |
  | 3512308 | Conchas | |
  | 3512407 | Cordeirópolis | |
  | 3512506 | Coroados | |
  | 3512605 | Coronel Macedo | [sp_coronel_macedo](data_collection/gazette/spiders/sp_coronel_macedo.py) |
  | 3512704 | Corumbataí | |
  | 3512803 | Cosmópolis | |
  | 3512902 | Cosmorama | |
  | 3513009 | Cotia | |
  | 3513108 | Cravinhos | |
  | 3513207 | Cristais Paulista | |
  | 3513306 | Cruzália | |
  | 3513405 | Cruzeiro | |
  | 3513504 | Cubatão | |
  | 3513603 | Cunha | |
  | 3513702 | Descalvado | |
  | 3513801 | Diadema | |
  | 3513850 | Dirce Reis | |
  | 3513900 | Divinolândia | |
  | 3514007 | Dobrada | |
  | 3514106 | Dois Córregos | |
  | 3514205 | Dolcinópolis | |
  | 3514304 | Dourado | |
  | 3514403 | Dracena | |
  | 3514502 | Duartina | |
  | 3514601 | Dumont | |
  | 3514700 | Echaporã | |
  | 3514809 | Eldorado | |
  | 3514908 | Elias Fausto | |
  | 3514924 | Elisiário | |
  | 3514957 | Embaúba | |
  | 3515004 | Embu das Artes | |
  | 3515103 | Embu-Guaçu | |
  | 3515129 | Emilianópolis | |
  | 3515152 | Engenheiro Coelho | |
  | 3515186 | Espírito Santo do Pinhal | |
  | 3515194 | Espírito Santo do Turvo | |
  | 3557303 | Estiva Gerbi | |
  | 3515301 | Estrela do Norte | |
  | 3515202 | Estrela d'Oeste | |
  | 3515350 | Euclides da Cunha Paulista | |
  | 3515400 | Fartura | |
  | 3515608 | Fernando Prestes | |
  | 3515509 | Fernandópolis | [sp_fernandopolis](data_collection/gazette/spiders/sp_fernandopolis.py) |
  | 3515657 | Fernão | |
  | 3515707 | Ferraz de Vasconcelos | |
  | 3515806 | Flora Rica | |
  | 3515905 | Floreal | |
  | 3516002 | Flórida Paulista | |
  | 3516101 | Florínia | |
  | 3516200 | Franca | [sp_franca](data_collection/gazette/spiders/sp_franca.py) |
  | 3516309 | Francisco Morato | |
  | 3516408 | Franco da Rocha | |
  | 3516507 | Gabriel Monteiro | |
  | 3516606 | Gália | |
  | 3516705 | Garça | |
  | 3516804 | Gastão Vidigal | |
  | 3516853 | Gavião Peixoto | |
  | 3516903 | General Salgado | |
  | 3517000 | Getulina | |
  | 3517109 | Glicério | [sp_glicerio](data_collection/gazette/spiders/sp_glicerio.py) |
  | 3517208 | Guaiçara | |
  | 3517307 | Guaimbê | |
  | 3517406 | Guaíra | |
  | 3517505 | Guapiaçu | |
  | 3517604 | Guapiara | |
  | 3517703 | Guará | |
  | 3517802 | Guaraçaí | |
  | 3517901 | Guaraci | |
  | 3518008 | Guarani d'Oeste | |
  | 3518107 | Guarantã | |
  | 3518206 | Guararapes | |
  | 3518305 | Guararema | |
  | 3518404 | Guaratinguetá | |
  | 3518503 | Guareí | |
  | 3518602 | Guariba | |
  | 3518701 | Guarujá | [sp_guaruja](data_collection/gazette/spiders/sp_guaruja.py) |
  | 3518800 | Guarulhos | [sp_guarulhos](data_collection/gazette/spiders/sp_guarulhos.py) |
  | 3518859 | Guatapará | |
  | 3518909 | Guzolândia | |
  | 3519006 | Herculândia | |
  | 3519055 | Holambra | |
  | 3519071 | Hortolândia | |
  | 3519105 | Iacanga | |
  | 3519204 | Iacri | |
  | 3519253 | Iaras | |
  | 3519303 | Ibaté | |
  | 3519402 | Ibirá | |
  | 3519501 | Ibirarema | |
  | 3519600 | Ibitinga | [sp_ibitinga](data_collection/gazette/spiders/sp_ibitinga.py) |
  | 3519709 | Ibiúna | |
  | 3519808 | Icém | |
  | 3519907 | Iepê | |
  | 3520004 | Igaraçu do Tietê | |
  | 3520103 | Igarapava | |
  | 3520202 | Igaratá | |
  | 3520301 | Iguape | |
  | 3520426 | Ilha Comprida | |
  | 3520442 | Ilha Solteira | |
  | 3520400 | Ilhabela | |
  | 3520509 | Indaiatuba | |
  | 3520608 | Indiana | |
  | 3520707 | Indiaporã | |
  | 3520806 | Inúbia Paulista | |
  | 3520905 | Ipaussu | |
  | 3521002 | Iperó | |
  | 3521101 | Ipeúna | |
  | 3521150 | Ipiguá | |
  | 3521200 | Iporanga | |
  | 3521309 | Ipuã | |
  | 3521408 | Iracemápolis | |
  | 3521507 | Irapuã | [sp_associacao_municipios](data_collection/gazette/spiders/sp_associacao_municipios.py) |
  | 3521606 | Irapuru | |
  | 3521705 | Itaberá | |
  | 3521804 | Itaí | |
  | 3521903 | Itajobi | |
  | 3522000 | Itaju | |
  | 3522109 | Itanhaém | |
  | 3522158 | Itaóca | |
  | 3522208 | Itapecerica da Serra | |
  | 3522307 | Itapetininga | |
  | 3522406 | Itapeva | |
  | 3522505 | Itapevi | |
  | 3522604 | Itapira | |
  | 3522653 | Itapirapuã Paulista | [sp_itapirapua_paulista](data_collection/gazette/spiders/sp_itapirapua_paulista.py) |
  | 3522703 | Itápolis | |
  | 3522802 | Itaporanga | |
  | 3522901 | Itapuí | |
  | 3523008 | Itapura | |
  | 3523107 | Itaquaquecetuba | |
  | 3523206 | Itararé | |
  | 3523305 | Itariri | |
  | 3523404 | Itatiba | |
  | 3523503 | Itatinga | |
  | 3523602 | Itirapina | |
  | 3523701 | Itirapuã | |
  | 3523800 | Itobi | |
  | 3523909 | Itu | [sp_associacao_municipios](data_collection/gazette/spiders/sp_associacao_municipios.py), [sp_itu](data_collection/gazette/spiders/sp_itu.py) |
  | 3524006 | Itupeva | [sp_associacao_municipios](data_collection/gazette/spiders/sp_associacao_municipios.py) |
  | 3524105 | Ituverava | |
  | 3524204 | Jaborandi | |
  | 3524303 | Jaboticabal | |
  | 3524402 | Jacareí | |
  | 3524501 | Jaci | |
  | 3524600 | Jacupiranga | |
  | 3524709 | Jaguariúna | |
  | 3524808 | Jales | |
  | 3524907 | Jambeiro | |
  | 3525003 | Jandira | |
  | 3525102 | Jardinópolis | |
  | 3525201 | Jarinu | |
  | 3525300 | Jaú | [sp_jau](data_collection/gazette/spiders/sp_jau.py) |
  | 3525409 | Jeriquara | |
  | 3525508 | Joanópolis | |
  | 3525607 | João Ramalho | |
  | 3525706 | José Bonifácio | |
  | 3525805 | Júlio Mesquita | |
  | 3525854 | Jumirim | |
  | 3525904 | Jundiaí | [sp_jundiai](data_collection/gazette/spiders/sp_jundiai.py) |
  | 3526001 | Junqueirópolis | |
  | 3526100 | Juquiá | |
  | 3526209 | Juquitiba | |
  | 3526308 | Lagoinha | |
  | 3526407 | Laranjal Paulista | |
  | 3526506 | Lavínia | [sp_lavinia](data_collection/gazette/spiders/sp_lavinia.py) |
  | 3526605 | Lavrinhas | |
  | 3526704 | Leme | |
  | 3526803 | Lençóis Paulista | |
  | 3526902 | Limeira | |
  | 3527009 | Lindóia | |
  | 3527108 | Lins | |
  | 3527207 | Lorena | |
  | 3527256 | Lourdes | |
  | 3527306 | Louveira | |
  | 3527405 | Lucélia | |
  | 3527504 | Lucianópolis | |
  | 3527603 | Luís Antônio | |
  | 3527702 | Luiziânia | |
  | 3527801 | Lupércio | |
  | 3527900 | Lutécia | |
  | 3528007 | Macatuba | [sp_macatuba](data_collection/gazette/spiders/sp_macatuba.py) |
  | 3528106 | Macaubal | |
  | 3528205 | Macedônia | |
  | 3528304 | Magda | |
  | 3528403 | Mairinque | |
  | 3528502 | Mairiporã | |
  | 3528601 | Manduri | |
  | 3528700 | Marabá Paulista | |
  | 3528809 | Maracaí | |
  | 3528858 | Marapoama | |
  | 3528908 | Mariápolis | |
  | 3529005 | Marília | [sp_marilia](data_collection/gazette/spiders/sp_marilia.py) |
  | 3529104 | Marinópolis | |
  | 3529203 | Martinópolis | |
  | 3529302 | Matão | |
  | 3529401 | Mauá | |
  | 3529500 | Mendonça | |
  | 3529609 | Meridiano | |
  | 3529658 | Mesópolis | |
  | 3529708 | Miguelópolis | |
  | 3529807 | Mineiros do Tietê | |
  | 3530003 | Mira Estrela | |
  | 3529906 | Miracatu | |
  | 3530102 | Mirandópolis | |
  | 3530201 | Mirante do Paranapanema | |
  | 3530300 | Mirassol | |
  | 3530409 | Mirassolândia | |
  | 3530508 | Mococa | [sp_associacao_municipios](data_collection/gazette/spiders/sp_associacao_municipios.py) |
  | 3530607 | Mogi das Cruzes | |
  | 3530706 | Mogi Guaçu | |
  | 3530805 | Mogi Mirim | |
  | 3530904 | Mombuca | |
  | 3531001 | Monções | |
  | 3531100 | Mongaguá | |
  | 3531209 | Monte Alegre do Sul | |
  | 3531308 | Monte Alto | [sp_monte_alto](data_collection/gazette/spiders/sp_monte_alto.py), [sp_monte_alto_sigpub](data_collection/gazette/spiders/sp_monte_alto.py) |
  | 3531407 | Monte Aprazível | |
  | 3531506 | Monte Azul Paulista | |
  | 3531605 | Monte Castelo | |
  | 3531803 | Monte Mor | |
  | 3531704 | Monteiro Lobato | |
  | 3531902 | Morro Agudo | |
  | 3532009 | Morungaba | |
  | 3532058 | Motuca | |
  | 3532108 | Murutinga do Sul | |
  | 3532157 | Nantes | |
  | 3532207 | Narandiba | |
  | 3532306 | Natividade da Serra | |
  | 3532405 | Nazaré Paulista | |
  | 3532504 | Neves Paulista | |
  | 3532603 | Nhandeara | |
  | 3532702 | Nipoã | |
  | 3532801 | Nova Aliança | |
  | 3532827 | Nova Campina | |
  | 3532843 | Nova Canaã Paulista | |
  | 3532868 | Nova Castilho | |
  | 3532900 | Nova Europa | |
  | 3533007 | Nova Granada | |
  | 3533106 | Nova Guataporanga | |
  | 3533205 | Nova Independência | |
  | 3533304 | Nova Luzitânia | |
  | 3533403 | Nova Odessa | |
  | 3533254 | Novais | |
  | 3533502 | Novo Horizonte | |
  | 3533601 | Nuporanga | |
  | 3533700 | Ocauçu | |
  | 3533809 | Óleo | |
  | 3533908 | Olímpia | |
  | 3534005 | Onda Verde | |
  | 3534104 | Oriente | |
  | 3534203 | Orindiúva | |
  | 3534302 | Orlândia | |
  | 3534401 | Osasco | |
  | 3534500 | Oscar Bressane | |
  | 3534609 | Osvaldo Cruz | |
  | 3534708 | Ourinhos | |
  | 3534807 | Ouro Verde | |
  | 3534757 | Ouroeste | |
  | 3534906 | Pacaembu | |
  | 3535002 | Palestina | |
  | 3535101 | Palmares Paulista | |
  | 3535200 | Palmeira d'Oeste | |
  | 3535309 | Palmital | |
  | 3535408 | Panorama | |
  | 3535507 | Paraguaçu Paulista | |
  | 3535606 | Paraibuna | |
  | 3535705 | Paraíso | |
  | 3535804 | Paranapanema | |
  | 3535903 | Paranapuã | |
  | 3536000 | Parapuã | |
  | 3536109 | Pardinho | |
  | 3536208 | Pariquera-Açu | |
  | 3536257 | Parisi | [sp_parisi](data_collection/gazette/spiders/sp_parisi.py) |
  | 3536307 | Patrocínio Paulista | [sp_patrocinio_paulista](data_collection/gazette/spiders/sp_patrocinio_paulista.py) |
  | 3536406 | Paulicéia | |
  | 3536505 | Paulínia | |
  | 3536570 | Paulistânia | |
  | 3536604 | Paulo de Faria | |
  | 3536703 | Pederneiras | |
  | 3536802 | Pedra Bela | |
  | 3536901 | Pedranópolis | |
  | 3537008 | Pedregulho | |
  | 3537107 | Pedreira | |
  | 3537156 | Pedrinhas Paulista | |
  | 3537206 | Pedro de Toledo | |
  | 3537305 | Penápolis | [sp_penapolis](data_collection/gazette/spiders/sp_penapolis.py) |
  | 3537404 | Pereira Barreto | |
  | 3537503 | Pereiras | |
  | 3537602 | Peruíbe | |
  | 3537701 | Piacatu | |
  | 3537800 | Piedade | [sp_piedade](data_collection/gazette/spiders/sp_piedade.py) |
  | 3537909 | Pilar do Sul | |
  | 3538006 | Pindamonhangaba | |
  | 3538105 | Pindorama | |
  | 3538204 | Pinhalzinho | |
  | 3538303 | Piquerobi | |
  | 3538501 | Piquete | |
  | 3538600 | Piracaia | |
  | 3538709 | Piracicaba | [sp_piracicaba](data_collection/gazette/spiders/sp_piracicaba.py) |
  | 3538808 | Piraju | |
  | 3538907 | Pirajuí | |
  | 3539004 | Pirangi | |
  | 3539103 | Pirapora do Bom Jesus | |
  | 3539202 | Pirapozinho | |
  | 3539301 | Pirassununga | |
  | 3539400 | Piratininga | |
  | 3539509 | Pitangueiras | |
  | 3539608 | Planalto | |
  | 3539707 | Platina | |
  | 3539806 | Poá | |
  | 3539905 | Poloni | |
  | 3540002 | Pompéia | |
  | 3540101 | Pongaí | |
  | 3540200 | Pontal | |
  | 3540259 | Pontalinda | |
  | 3540309 | Pontes Gestal | |
  | 3540408 | Populina | |
  | 3540507 | Porangaba | |
  | 3540606 | Porto Feliz | |
  | 3540705 | Porto Ferreira | |
  | 3540754 | Potim | |
  | 3540804 | Potirendaba | |
  | 3540853 | Pracinha | |
  | 3540903 | Pradópolis | |
  | 3541000 | Praia Grande | |
  | 3541059 | Pratânia | [sp_pratania](data_collection/gazette/spiders/sp_pratania.py) |
  | 3541109 | Presidente Alves | |
  | 3541208 | Presidente Bernardes | |
  | 3541307 | Presidente Epitácio | |
  | 3541406 | Presidente Prudente | [sp_presidente_prudente](data_collection/gazette/spiders/sp_presidente_prudente.py) |
  | 3541505 | Presidente Venceslau | |
  | 3541604 | Promissão | |
  | 3541653 | Quadra | |
  | 3541703 | Quatá | |
  | 3541802 | Queiroz | |
  | 3541901 | Queluz | |
  | 3542008 | Quintana | |
  | 3542107 | Rafard | |
  | 3542206 | Rancharia | |
  | 3542305 | Redenção da Serra | |
  | 3542404 | Regente Feijó | |
  | 3542503 | Reginópolis | |
  | 3542602 | Registro | |
  | 3542701 | Restinga | |
  | 3542800 | Ribeira | |
  | 3542909 | Ribeirão Bonito | |
  | 3543006 | Ribeirão Branco | |
  | 3543105 | Ribeirão Corrente | |
  | 3543253 | Ribeirão Grande | |
  | 3543238 | Ribeirão dos Índios | |
  | 3543303 | Ribeirão Pires | |
  | 3543402 | Ribeirão Preto | |
  | 3543204 | Ribeirão do Sul | |
  | 3543600 | Rifaina | |
  | 3543709 | Rincão | |
  | 3543808 | Rinópolis | |
  | 3543907 | Rio Claro | |
  | 3544103 | Rio Grande da Serra | |
  | 3544004 | Rio das Pedras | |
  | 3544202 | Riolândia | |
  | 3543501 | Riversul | |
  | 3544251 | Rosana | |
  | 3544301 | Roseira | |
  | 3544400 | Rubiácea | |
  | 3544509 | Rubinéia | |
  | 3544608 | Sabino | |
  | 3544707 | Sagres | |
  | 3544806 | Sales | |
  | 3544905 | Sales Oliveira | |
  | 3545001 | Salesópolis | |
  | 3545100 | Salmourão | |
  | 3545159 | Saltinho | |
  | 3545209 | Salto | |
  | 3545407 | Salto Grande | |
  | 3545308 | Salto de Pirapora | |
  | 3545506 | Sandovalina | |
  | 3545605 | Santa Adélia | |
  | 3545704 | Santa Albertina | |
  | 3545803 | Santa Bárbara d'Oeste | |
  | 3546009 | Santa Branca | |
  | 3546108 | Santa Clara d'Oeste | |
  | 3546207 | Santa Cruz da Conceição | |
  | 3546256 | Santa Cruz da Esperança | |
  | 3546306 | Santa Cruz das Palmeiras | |
  | 3546405 | Santa Cruz do Rio Pardo | |
  | 3546504 | Santa Ernestina | [sp_santa_ernestina](data_collection/gazette/spiders/sp_santa_ernestina.py) |
  | 3546603 | Santa Fé do Sul | |
  | 3546702 | Santa Gertrudes | |
  | 3546801 | Santa Isabel | |
  | 3546900 | Santa Lúcia | |
  | 3547007 | Santa Maria da Serra | |
  | 3547106 | Santa Mercedes | |
  | 3547403 | Santa Rita d'Oeste | |
  | 3547502 | Santa Rita do Passa Quatro | |
  | 3547601 | Santa Rosa de Viterbo | |
  | 3547650 | Santa Salete | |
  | 3547304 | Santana de Parnaíba | |
  | 3547205 | Santana da Ponte Pensa | |
  | 3547700 | Santo Anastácio | |
  | 3547809 | Santo André | |
  | 3547908 | Santo Antônio da Alegria | |
  | 3548054 | Santo Antônio do Aracanguá | |
  | 3548104 | Santo Antônio do Jardim | |
  | 3548203 | Santo Antônio do Pinhal | |
  | 3548005 | Santo Antônio de Posse | |
  | 3548302 | Santo Expedito | |
  | 3548401 | Santópolis do Aguapeí | |
  | 3548500 | Santos | [sp_santos](data_collection/gazette/spiders/sp_santos.py) |
  | 3548609 | São Bento do Sapucaí | |
  | 3548708 | São Bernardo do Campo | |
  | 3548807 | São Caetano do Sul | |
  | 3548906 | São Carlos | |
  | 3549003 | São Francisco | |
  | 3549102 | São João da Boa Vista | |
  | 3549201 | São João das Duas Pontes | |
  | 3549250 | São João de Iracema | |
  | 3549300 | São João do Pau d'Alho | |
  | 3549409 | São Joaquim da Barra | |
  | 3549607 | São José do Barreiro | |
  | 3549508 | São José da Bela Vista | |
  | 3549904 | São José dos Campos | [sp_sao_jose_dos_campos](data_collection/gazette/spiders/sp_sao_jose_dos_campos.py) |
  | 3549706 | São José do Rio Pardo | |
  | 3549805 | São José do Rio Preto | |
  | 3549953 | São Lourenço da Serra | |
  | 3550001 | São Luiz do Paraitinga | |
  | 3550100 | São Manuel | [sp_sao_manuel](data_collection/gazette/spiders/sp_sao_manuel.py) |
  | 3550209 | São Miguel Arcanjo | |
  | 3550308 | São Paulo | [sp_sao_paulo](data_collection/gazette/spiders/sp_sao_paulo.py) |
  | 3550407 | São Pedro | |
  | 3550506 | São Pedro do Turvo | |
  | 3550605 | São Roque | [sp_sao_roque](data_collection/gazette/spiders/sp_sao_roque.py) |
  | 3550704 | São Sebastião | |
  | 3550803 | São Sebastião da Grama | |
  | 3550902 | São Simão | |
  | 3551009 | São Vicente | |
  | 3551108 | Sarapuí | |
  | 3551207 | Sarutaiá | [sp_sarutaia](data_collection/gazette/spiders/sp_sarutaia.py) |
  | 3551306 | Sebastianópolis do Sul | |
  | 3551405 | Serra Azul | |
  | 3551603 | Serra Negra | |
  | 3551504 | Serrana | |
  | 3551702 | Sertãozinho | |
  | 3551801 | Sete Barras | |
  | 3551900 | Severínia | |
  | 3552007 | Silveiras | |
  | 3552106 | Socorro | |
  | 3552205 | Sorocaba | |
  | 3552304 | Sud Mennucci | |
  | 3552403 | Sumaré | |
  | 3552551 | Suzanápolis | |
  | 3552502 | Suzano | |
  | 3552601 | Tabapuã | |
  | 3552700 | Tabatinga | |
  | 3552809 | Taboão da Serra | |
  | 3552908 | Taciba | |
  | 3553005 | Taguaí | |
  | 3553104 | Taiaçu | |
  | 3553203 | Taiúva | |
  | 3553302 | Tambaú | |
  | 3553401 | Tanabi | |
  | 3553500 | Tapiraí | |
  | 3553609 | Tapiratiba | |
  | 3553658 | Taquaral | |
  | 3553708 | Taquaritinga | |
  | 3553807 | Taquarituba | [sp_associacao_municipios](data_collection/gazette/spiders/sp_associacao_municipios.py) |
  | 3553856 | Taquarivaí | |
  | 3553906 | Tarabai | |
  | 3553955 | Tarumã | |
  | 3554003 | Tatuí | |
  | 3554102 | Taubaté | |
  | 3554201 | Tejupá | |
  | 3554300 | Teodoro Sampaio | |
  | 3554409 | Terra Roxa | |
  | 3554508 | Tietê | |
  | 3554607 | Timburi | |
  | 3554656 | Torre de Pedra | |
  | 3554706 | Torrinha | |
  | 3554755 | Trabiju | |
  | 3554805 | Tremembé | |
  | 3554904 | Três Fronteiras | |
  | 3554953 | Tuiuti | |
  | 3555000 | Tupã | |
  | 3555109 | Tupi Paulista | |
  | 3555208 | Turiúba | |
  | 3555307 | Turmalina | |
  | 3555356 | Ubarana | |
  | 3555406 | Ubatuba | |
  | 3555505 | Ubirajara | |
  | 3555604 | Uchoa | |
  | 3555703 | União Paulista | |
  | 3555802 | Urânia | |
  | 3555901 | Uru | |
  | 3556008 | Urupês | |
  | 3556107 | Valentim Gentil | |
  | 3556206 | Valinhos | |
  | 3556305 | Valparaíso | |
  | 3556354 | Vargem | |
  | 3556453 | Vargem Grande Paulista | |
  | 3556404 | Vargem Grande do Sul | |
  | 3556503 | Várzea Paulista | |
  | 3556602 | Vera Cruz | [sp_vera_cruz](data_collection/gazette/spiders/sp_vera_cruz.py) |
  | 3556701 | Vinhedo | |
  | 3556800 | Viradouro | |
  | 3556909 | Vista Alegre do Alto | |
  | 3556958 | Vitória Brasil | |
  | 3557006 | Votorantim | [sp_votorantim](data_collection/gazette/spiders/sp_votorantim.py) |
  | 3557105 | Votuporanga | |
  | 3557154 | Zacarias | |
</details>


### Sergipe

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 2800100 | Amparo de São Francisco | |
  | 2800209 | Aquidabã | |
  | 2800308 | Aracaju | |
  | 2800407 | Arauá | |
  | 2800506 | Areia Branca | |
  | 2800605 | Barra dos Coqueiros | |
  | 2800670 | Boquim | |
  | 2800704 | Brejo Grande | |
  | 2801009 | Campo do Brito | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2801108 | Canhoba | |
  | 2801207 | Canindé de São Francisco | |
  | 2801306 | Capela | |
  | 2801405 | Carira | |
  | 2801504 | Carmópolis | |
  | 2801603 | Cedro de São João | |
  | 2801702 | Cristinápolis | |
  | 2801900 | Cumbe | |
  | 2802007 | Divina Pastora | |
  | 2802106 | Estância | |
  | 2802205 | Feira Nova | |
  | 2802304 | Frei Paulo | |
  | 2802403 | Gararu | |
  | 2802502 | General Maynard | |
  | 2802601 | Gracho Cardoso | |
  | 2802700 | Ilha das Flores | |
  | 2802809 | Indiaroba | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2802908 | Itabaiana | |
  | 2803005 | Itabaianinha | |
  | 2803104 | Itabi | |
  | 2803203 | Itaporanga d'Ajuda | |
  | 2803302 | Japaratuba | |
  | 2803401 | Japoatã | |
  | 2803500 | Lagarto | |
  | 2803609 | Laranjeiras | |
  | 2803708 | Macambira | |
  | 2803807 | Malhada dos Bois | |
  | 2803906 | Malhador | |
  | 2804003 | Maruim | |
  | 2804102 | Moita Bonita | |
  | 2804201 | Monte Alegre de Sergipe | |
  | 2804300 | Muribeca | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2804409 | Neópolis | |
  | 2804458 | Nossa Senhora Aparecida | |
  | 2804607 | Nossa Senhora das Dores | |
  | 2804508 | Nossa Senhora da Glória | |
  | 2804706 | Nossa Senhora de Lourdes | |
  | 2804805 | Nossa Senhora do Socorro | |
  | 2804904 | Pacatuba | |
  | 2805000 | Pedra Mole | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2805109 | Pedrinhas | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2805208 | Pinhão | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2805307 | Pirambu | |
  | 2805406 | Poço Redondo | |
  | 2805505 | Poço Verde | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2805604 | Porto da Folha | |
  | 2805703 | Propriá | |
  | 2805802 | Riachão do Dantas | |
  | 2805901 | Riachuelo | |
  | 2806008 | Ribeirópolis | |
  | 2806107 | Rosário do Catete | |
  | 2806206 | Salgado | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2806305 | Santa Luzia do Itanhy | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2806503 | Santa Rosa de Lima | |
  | 2806404 | Santana do São Francisco | |
  | 2806602 | Santo Amaro das Brotas | |
  | 2806701 | São Cristóvão | |
  | 2806800 | São Domingos | |
  | 2806909 | São Francisco | |
  | 2807006 | São Miguel do Aleixo | |
  | 2807105 | Simão Dias | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2807204 | Siriri | |
  | 2807303 | Telha | |
  | 2807402 | Tobias Barreto | [se_associacao_municipios](data_collection/gazette/spiders/se_associacao_municipios.py) |
  | 2807501 | Tomar do Geru | |
  | 2807600 | Umbaúba | |
</details>


### Tocantins

<details>
  <summary>Click to expand</summary>

  | IBGE code | City name | Implemented spiders |
  | :-------: | :-------- | :------------------ |
  | 1700251 | Abreulândia | |
  | 1700301 | Aguiarnópolis | |
  | 1700350 | Aliança do Tocantins | |
  | 1700400 | Almas | |
  | 1700707 | Alvorada | |
  | 1701002 | Ananás | |
  | 1701051 | Angico | |
  | 1701101 | Aparecida do Rio Negro | |
  | 1701309 | Aragominas | |
  | 1701903 | Araguacema | |
  | 1702000 | Araguaçu | |
  | 1702109 | Araguaína | [to_araguaina](data_collection/gazette/spiders/to_araguaina.py) |
  | 1702158 | Araguanã | |
  | 1702208 | Araguatins | |
  | 1702307 | Arapoema | |
  | 1702406 | Arraias | |
  | 1702554 | Augustinópolis | |
  | 1702703 | Aurora do Tocantins | |
  | 1702901 | Axixá do Tocantins | |
  | 1703008 | Babaçulândia | |
  | 1703057 | Bandeirantes do Tocantins | |
  | 1703073 | Barra do Ouro | |
  | 1703107 | Barrolândia | |
  | 1703206 | Bernardo Sayão | |
  | 1703305 | Bom Jesus do Tocantins | |
  | 1703602 | Brasilândia do Tocantins | |
  | 1703701 | Brejinho de Nazaré | |
  | 1703800 | Buriti do Tocantins | |
  | 1703826 | Cachoeirinha | |
  | 1703842 | Campos Lindos | |
  | 1703867 | Cariri do Tocantins | |
  | 1703883 | Carmolândia | |
  | 1703891 | Carrasco Bonito | |
  | 1703909 | Caseara | |
  | 1704105 | Centenário | |
  | 1704600 | Chapada de Areia | |
  | 1705102 | Chapada da Natividade | |
  | 1705508 | Colinas do Tocantins | |
  | 1716703 | Colméia | |
  | 1705557 | Combinado | |
  | 1705607 | Conceição do Tocantins | |
  | 1706001 | Couto Magalhães | |
  | 1706100 | Cristalândia | |
  | 1706258 | Crixás do Tocantins | |
  | 1706506 | Darcinópolis | |
  | 1707009 | Dianópolis | |
  | 1707108 | Divinópolis do Tocantins | |
  | 1707207 | Dois Irmãos do Tocantins | |
  | 1707306 | Dueré | |
  | 1707405 | Esperantina | |
  | 1707553 | Fátima | |
  | 1707652 | Figueirópolis | |
  | 1707702 | Filadélfia | |
  | 1708205 | Formoso do Araguaia | |
  | 1708254 | Fortaleza do Tabocão | |
  | 1708304 | Goianorte | |
  | 1709005 | Goiatins | |
  | 1709302 | Guaraí | |
  | 1709500 | Gurupi | |
  | 1709807 | Ipueiras | |
  | 1710508 | Itacajá | |
  | 1710706 | Itaguatins | |
  | 1710904 | Itapiratins | |
  | 1711100 | Itaporã do Tocantins | |
  | 1711506 | Jaú do Tocantins | |
  | 1711803 | Juarina | |
  | 1711902 | Lagoa da Confusão | |
  | 1711951 | Lagoa do Tocantins | |
  | 1712009 | Lajeado | |
  | 1712157 | Lavandeira | |
  | 1712405 | Lizarda | |
  | 1712454 | Luzinópolis | |
  | 1712504 | Marianópolis do Tocantins | |
  | 1712702 | Mateiros | |
  | 1712801 | Maurilândia do Tocantins | |
  | 1713205 | Miracema do Tocantins | |
  | 1713304 | Miranorte | |
  | 1713601 | Monte do Carmo | |
  | 1713700 | Monte Santo do Tocantins | |
  | 1713957 | Muricilândia | |
  | 1714203 | Natividade | |
  | 1714302 | Nazaré | |
  | 1714880 | Nova Olinda | |
  | 1715002 | Nova Rosalândia | |
  | 1715101 | Novo Acordo | |
  | 1715150 | Novo Alegre | |
  | 1715259 | Novo Jardim | |
  | 1715507 | Oliveira de Fátima | |
  | 1721000 | Palmas | [to_palmas](data_collection/gazette/spiders/to_palmas.py) |
  | 1715705 | Palmeirante | |
  | 1713809 | Palmeiras do Tocantins | |
  | 1715754 | Palmeirópolis | |
  | 1716109 | Paraíso do Tocantins | |
  | 1716208 | Paranã | |
  | 1716307 | Pau D'Arco | |
  | 1716505 | Pedro Afonso | |
  | 1716604 | Peixe | |
  | 1716653 | Pequizeiro | |
  | 1717008 | Pindorama do Tocantins | |
  | 1717206 | Piraquê | |
  | 1717503 | Pium | |
  | 1717800 | Ponte Alta do Bom Jesus | |
  | 1717909 | Ponte Alta do Tocantins | |
  | 1718006 | Porto Alegre do Tocantins | |
  | 1718204 | Porto Nacional | |
  | 1718303 | Praia Norte | |
  | 1718402 | Presidente Kennedy | |
  | 1718451 | Pugmil | |
  | 1718501 | Recursolândia | |
  | 1718550 | Riachinho | |
  | 1718709 | Rio dos Bois | |
  | 1718659 | Rio da Conceição | |
  | 1718758 | Rio Sono | |
  | 1718808 | Sampaio | |
  | 1718840 | Sandolândia | |
  | 1718865 | Santa Fé do Araguaia | |
  | 1718881 | Santa Maria do Tocantins | |
  | 1718899 | Santa Rita do Tocantins | |
  | 1718907 | Santa Rosa do Tocantins | |
  | 1719004 | Santa Tereza do Tocantins | |
  | 1720002 | Santa Terezinha do Tocantins | |
  | 1720101 | São Bento do Tocantins | |
  | 1720150 | São Félix do Tocantins | |
  | 1720200 | São Miguel do Tocantins | |
  | 1720259 | São Salvador do Tocantins | |
  | 1720309 | São Sebastião do Tocantins | |
  | 1720499 | São Valério | |
  | 1720655 | Silvanópolis | |
  | 1720804 | Sítio Novo do Tocantins | |
  | 1720853 | Sucupira | |
  | 1720903 | Taguatinga | |
  | 1720937 | Taipas do Tocantins | |
  | 1720978 | Talismã | |
  | 1721109 | Tocantínia | |
  | 1721208 | Tocantinópolis | |
  | 1721257 | Tupirama | |
  | 1721307 | Tupiratins | |
  | 1722081 | Wanderlândia | |
  | 1722107 | Xambioá | |
</details>
