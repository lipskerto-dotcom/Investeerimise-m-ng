📈 Investeerimise Mäng
Lihtsas Pythonis kirjutatud investeerimissimulaator, kus katsetad oma õnne aktsiate, krüpto ja optsioonidega — ilma päris raha kaotamata.

🎮 Mängu kirjeldus
Alustad $10 000-ga ja teed 5 päeva jooksul investeerimisotsuseid. Iga päev toob kaasa juhusliku turuevent, mis mõjutab tootlusi. Mängu lõpus saad hinnangu oma tulemuse põhjal.

🚀 Käivitamine
Nõuded: Python 3.x (lisateeke pole vaja)
bashgit clone https://github.com/sinu-kasutajanimi/investeerimise-mang.git
cd investeerimise-mang
python mang.py

💼 Investeerimisvõimalused
ValikVahemikKirjeldusNVDA-10% kuni +20%TehnoloogiaaktsiaKuld-5% kuni +8%Stabiilne väärtmetallKrüpto-30% kuni +30%Kõrge riskiga, kõrge tootlusNVDA 3x-30% kuni +60%Võimendatud NVDANVDA CALL 100xkuni +1500% / -60–90%Opsioon: võidad kui NVDA tõusebNVDA PUT 100xkuni +1500% / -60–90%Opsioon: võidad kui NVDA langebKuld CALL 100xkuni +800% / -60–90%Opsioon: võidad kui Kuld tõusebKuld PUT 100xkuni +800% / -60–90%Opsioon: võidad kui Kuld langeb

📰 Päeva sündmused
Iga päev ilmub juhuslik turuevent, mis mõjutab kõikide investeeringute tootlust:
SündmusKordajaGlobaalne majanduskriis×0.5Börsid kukuvad paanika tõttu×0.6Tavaline päev turul×1.0Investorite optimism kasvab×1.3Turud plahvatavad positiivselt×1.6
Tavaline päev on 3× tõenäolisem kui kriis või boom.

📊 Lõpphinded
LõpprahaHinne$20 000+LEGEND 🏆$15 000+Investor 📈$10 000+Stabiilne 😊$7 000+McDonalds kutsub tööle 🍟alla $7 000See kuu süüa ei saa 💸

⚙️ Kuidas optsioonid töötavad
CALL — panustad et hind tõuseb:

Hind tõusis → võit korrutatakse 100×
Hind langes → kaotad 60–90% juhuslikult

PUT — panustad et hind langeb:

Hind langes → võit korrutatakse 100×
Hind tõusis → kaotad 60–90% juhuslikult


📁 Struktuur
investeerimise-mang/
└── mang.py       # kogu mäng ühes failis
└── README.md

🛠️ Võimalikud edasiarendused

 Mitu mängijat korraga
 Portfelli jagamine mitme investeeringu vahel
 Pikem mäng (10–30 päeva)
 Tulemuste salvestamine faili
 Graafiline liides (tkinter / pygame)


📄 Litsents
MIT — kasuta vabalt, muuda kui tahad.
