import re
from typing import List, Dict, Optional
import pandas as pd

RAW_TEXT = r"""
Home Page Foodstuff info Buyers and Distributors Our Services
BUYERS AND DISTRIBUTORS OF
AFRICAN FOODSTUFF
Mama Calabar - Nigerian Restaurant
2-4 Empire Way Wembley, London HA9 0EF
http://www.mamacalabar.co.uk/
Telephone: +44(0)87 1704 0719
EKO RESTRAURANT
160 Homerton High Road
London. E9 6JA
Tel: 0208 985 7345
Mob: 07946 796 230
07946 796 156
Email: info@ekorestaurant.co.uk
Presidential Suya162-164 Old kent road
London SE1 5TY
Tel: 020 7708 4491
E-mail: info@presidentialsuya.com
Abuja Connection Restaurant
112-114 Anerley Road, London SE19 2AN
Telephone. 020 8778 5522
Aso Rock Restaurant
7 Bradbury Street, London N16 8JN
Telephone. -020 7923 7068
Alayo Kitchen
18 Peckham Park Road, London SE15 6TW
Telephone. 020 7639 0055Faaji
299 Finchley Road, London NW3 6DT
Telephone. 020 7794 6004
805
Address: 805 Old Kent Road, London, SE15 1NX
Phone: +44 (0) 20 7639 0808
Akiwa Restaurant
Address: 42 Brixton Hill, London, SW2 2AB
Phone: +44 (0) 20 7582 8258
Angie's African Cuisine
Nigerian and African cuisine
Address: 381 Harrow Road, Maida Vale, London, W9 3NDPhone: +44 (0) 20 8962 8761
Cornerstone Restaurant
Indoor open kitchen Nigerian suya grill.
Address: 72 High Road, South Tottenham, London N15 6JU
Phone: +44 (0) 20 8880 1222
D' Den Exotic African Cuisine
Address: 47 Cricklewood Broadway, London, NW2 3JX
Phone: +44 (0) 20 8830 5000
Eko Restaurant
Nigerian cuisine. Suya, Dodo, Ewa, Iyan, Amala, Eba, Gira,
Semo, Asaro as well as stew like Egusi, Eforiro, Ewedu, Egusi,
Ogbona, Edikaikong, Afang, Nkwobi, meat stew.
Address: 160 Homerton High Road, London, E9 6JA
Phone: +44 (0) 208 985 7345, 07946 796 230, 07946 796 156
E-mail: info@ekorestaurant.co.ukWebsite: http://www.ekorestaurant.co.uk
Je-African Grill
Traditional Nigerian dishes specializing in grills prepared on an
open flame char grill.
Address: 304 Kilburn High Road, London. NW6 2DB
Phone: +44 (0) 20 7372 8884
Mama Calabar
Address: 3rd Floor, Dexion House, 2-4 Empire Way, Wembley,
London, HA9 0XA
Phone: +44 (0) 20 8902 2277
Obalende Suya Express
Indoor open kitchen Nigerian suya grill.
Address: 43 Peckham High Street, London, SE15 5EB
Phone: +44 (0) 20 7703 7033Website: http://www.suyaexpress.com
Ovation Restaurant & Bar
Address: 166B Tower Bridge Road, London, SE1 3LS
Phone: +44 (0) 20 7378 7989
Q Bar and Grill
Address: 7 - 9 Kilburn High Road, London, NW6 5SD
Phone: +44 (0) 20 7624 2525
Taris
Address: 332-336 Barking Road, Canning Town, London, E13
8HL
Phone: +44 (0) 20 7476 0207Tomis Kitchen
Nigerian restaurant.
Address: 126 Deptford High Street, London SE8 4NS
Phone: +44 (0) 20 8694 9352
Angie's African Cuisine Ltd
Contact name: Isaac Namabiri
Address: 381 Harrow Road, London W9 3NA
Phone: 44 20 89628761
E-Mail: info@angies-restaurant.co.uk
Website: www.angies-restaurant.co.uk
Description: Angie's brings the unique and undiscovered
flavours of Africa to West London. Our fantastic new Fully
Licensed restaurant has seating capacity for 100. The
environment is also fully conditioned for the maximum comfort
of our guests
OBALENDE SUYA
Contact name: TOKUNBO ODEBUNMI
Address: 43, PECKHAM HIGH STREET London SE15
Phone: 44 20 7703 7033E-Mail: soulfood@obalendesuya.com
Website: www.obalendesuya.com
Description: THE WORLD'S FIRST INDOOR OPEN KITCHEN
SUYA GRILL CONCEPT.A DEDICATED T/AWAY SERVICE.
APPIAH MARKT Import-Export
Manager: E. K. Appiah
Fuhlsbüttler str. 460
22309 Hamburg, Germany
Tel +4940-18 07 84 20
Mobile: 0160-38 98 10 1
E-mail: kusiemma@yahoo.com
Direction: From U/ S Bahnhof Barmbek Bus 172 & 7; Bus stop
Eliigersweg.
Speciality: African Foodstuffs, African Flags, Body creams and
Traditional African wears from Ghana.
Grace Foods Packaging and Services
Ghana, Ltd.
100 Tettegu McCarthy Hill South WestAccra, Ghana
Phone +233,289544349, Mobil +233,249112184,
+233,248947612
usglobal70@yahoo.com
We package and export West African foods. We want importers
of African foods in all parts of the world to buy from us. We help
our customers source what ever food products they need in
West Africa. We offer very chipper prices. We have in stock
gari, palm oil, fresh yams, vegetables, brown beans, egusi,
ogbolo, achi,and many more.
Leemex Foods
Address: P. O. Box 16810
Accra North
Tel: +233-(0)244-376-747
leemexfoods@yahoo.com
We are producers and exporters of the following African
gourmet foods: yam flour, plantain fufu flour, banku mix, hausa
koko, edible palm oil, corn flour, corn starch, maize
(white/yellow). These products are prepared under strict
hygienic conditions to meet the most stringent international
standards in food processing and Certified by the Ghana
Standards Board and Food and Drugs Board. We are looking
for Distributors and Agents throughout the world especially in
UK and America. All inquiries will be addressed. We thank you
in anticipation.Makroyals Company Limited
P.O. Box ML 367
Hno. 48 1st Makunta Street Mallam
Accra, Ghana
makroyals@yahoo.com
We are exporters of peanuts, tigernuts, palmnut kernels, yam,
raw cashew nuts, pineapples, sesame seeds, annato seeds and
other kinds of farm produce. We also export African gourmet
flours like, plantain fufu flour, yam flour, banku flour, hausa koko
flour, gari, and red oil. With an efficient quality management and
cost control system, we can offer products with different prices
according to your various quality requirements. We insist on
implementing contracts efficiently, delivering goods on time,
providing high quality products with the most competitive prices.
We cherish every chance of cooperation, and have built stable
relationship with our customers based on mutual trust and
benefit. We are hoping to cooperate and establish a long lasting
relationship with you. And we are confident that we can turn to
be your stable, reliable, and powerful supplier of agricultural
products.
Mensah Alimentari and Farms
Kofi Dei Mensah (owner)
PO Box MC 2660, M / Circle
Takoradi, Ghana
West AfricaMOB.+ 233 277 480 810
FAX. + 233 31 22385
Exporters of smoked tuna and swordfish, tilapia, vac pack and
dried and frozen snail meat, a variety of tropical fruits and
vegetables such as palm products, yam, and more! Based in
Takoradi, Ghana.
Queen Lart Company Limited
PO Box AH 177
Achimota, Accra
Ghana, West Africa
223-021-403748
dodzious@yahoo.com
This company manufactures gari on a small scale and is looking
for an export partner.
, Distributors and Manufacturers
Nigeria
Balanced Development Limited
9b Old Refinery Road, ElelenwoP.O.Box 8568, Port Harcourt
Email: nemetu@yahoo.com
This is a registered Nigerian wholesaler that specializes in
packaging and exportation of African food products with
singular objective of making sure that African food is
hygienically processed and packaged to everybody all over the
world. Always available are fresh and dried Bitter-leaf, Ogbono,
Egusi, Achi, Cray-fish, Ukazi dried leaf, Oporo (smoked
shrimps), Bitter Kola nuts, Dadawa cubes, etc. They are
capable of exporting any quantity of product you may require
and at moderate prices. They also offer personal sales.
Cassava Marketers Association of
Nigeria
2 Export House 213
Kumba Street Wuse Zone 2
Abuja, Nigeria
3234-08036177493
simonoch@usa.com
This association in Nigeria is capable of supplying all African
food items from Africa at competitive prices. They also carry
Nigeria Home CDs, and both new and old films. They can
supply African cosmetics, cassava leaves, and any other
agricultural products.Cejin Nigeria Limited
Zone D34
Farm Centre
Minna
Niger State
Corporate Office
Suite 20
Melita Plaza
Area 11
Garki
Abuja
chiihej@gmail.com
We are exporters of palmnut kernels, yam, raw cashew nuts,
sesame seeds, and other kinds of farm produce. We also export
African yam flour, cassava and red oil. With an efficient quality
management and cost control system, we can offer products
with different prices according to your various quality
requirements. We insist on implementing contracts efficiently,
delivering goods on time, providing high quality products with
the most competitive prices. We cherish every chance of
cooperation, and have built stable relationship with our
customers based on mutual trust and benefit. We are hoping to
cooperate and establish a long lasting relationship with you.
And we are confident that we can turn to be your stable,reliable, and powerful supplier of agricultural products.
Fayolam Farms
Shop 06 Ayoola Shopping Plaza
Asero Abeokua
Ogun State
Nigeria
08033502883
iyalodefadillah@yahoo.com
The farm is located at Ijeun Akoni Village, Via Osiele in
Abeokuta, Ogun State. Fayolam Farms is a registered farm with
the Nigera Corporate Affairs Commission Abuja in 2009. Main
activities are cultivation of crops that include cassava, maize,
watermelon, and yam. They process cassava into very fine garri
known as garri ijebu or garri wenkun or olowonyo. Processing is
based on Standard Organisation of Nigeria standard. Farms
Mission: To be a foremost exporter of garri product to European
and American countries.
Grace Bee Ventures Ltd
26 Alhaji Bashiru Street, Ojodu
P.O. Box 9483, Ikeja. LagosNIGERIA
Specializing in production, processing and packaging of
hygienically-processed African foods, including gaari, raw
plantain, raw yam tubers and many different types of flour.
Importers Co-operative, Ltd
P.O.Box 1862
Surulere 33, Ogunmefun Street, Pedro, Gbagada
Lagos, Nigeria
Tel: 134-1-8139377
Cell: 2348033215157
Email: importers_ng@yahoo.com
Worldwide wholesale suppliers for African foods. Items include
soup ingredients such as achi, bitter leaf, crayfish, egusi,
ogbono, ukazi, smoked shrimp, palm oil, African spices and
seasonings. They also carry stock fish, garri, yams and yam
flour, nuts (kola, bitter kola, coco nuts, etc), beverages such as
Milo and Bournvita, African video films, African weekly and
monthly news magazines, newspapers, and native clothing.
Kenni700 International Fisheries
Benin City, Edo StateNigeria
+2348027265392
kenni700@yahoo.co.uk
Kenni700 International Fisheries is a major distributor of dried
crayfish, catfishes,tilapia and basa fish fillets to other
businesses. They also have a local fish market, and distribute
their own manuactured products to hotels, food houses and
restaurants. They are looking for expansion of their business to
more distributors and outlets in other states.
Lashbol, Nigeria Limited
Lashbol Road, off Ayedun Junction, Ajegunle bus stop,Sango
Otta
phone: 2348084914626
otabolaji@yahoo.com
Lashbol Nig Ltd is a manufacturing company sub divided into 3
sections of commercial farming of smoked catfish, fillet,
fingerlings, local fish feed and Coppens fish feed. Arable
farming of palm trees, bananas, sesame seeds, sunflower
seeds, palm oil extract on a 30 acre land in Oluke, Ogun State,
and an educational institution in Lagos State. The company is
looking to export smoked catfish, fillets, palm oil, sesame
seeds, water melons and processed birds to other African
countries, Europe and the United States.
MamaCookWellLocated in Lagos, Nigeria
Phone: 07068779370
chikasprivateinformation@yahoo.com
We specialize in supplying natural African ground food,
especially Nigerian food, such as: cocoyam for soup, plantain
for fufu, local nutmeg for pepper soup (Ehuru Egbe in Igbo
language), green dried vegetable, green dried okazi, green
dried oha, kolanut, bitter kola, dried bitter leaf, grounded egusi,
cent pepper from Ghana, grounded achi and more at your
request.
Pystol (Nig) Limited
11 Olabisi Street
Ikotun, Lagos
234-803-308-6151, 234-748-2235
pystol_ng@yahoo.com
pystolng@gmail.com
We export well packaged African Foods, especially Nigerian
foodstuffs garri, afang, ugwu, yam flour, snails (with permit) etc,
to EU Countries and the USA. Our goods and services are
cheap and affordable. We also package goods based on your
specification, these can include already processed beverages,
tomato paste, semovita, etc. With a continued business of 1
year (12 months) credit facility can be considered for reliable
and trust worthy partners, we look forward to doing business
with you.Walvin Global Res. Ltd
No 20 Deco Road Warri
Delta State, Nigeria
Phone: +2348037068000
walvinglobal@yahoo.com
Walvin Global Res. Ltd is a Nigerian based company. They
export well packaged African foods, especially Nigerian
foodstuffs. Items include soup ingredients such as achi, bitter
leaf, crayfish, egusi, ogbono, ukazi, smoked fish, palm oil,
African spices and seasonings. They also carry garri, yams and
yam flour, nuts (kola, bitter kola, coco nuts, etc), beverages
such as Milo and Bournvita, black cosmetics and beauty care.
Zion Ventures
Zone 4, PO Box 15020
Wuse, Abuja, Nigeria
Telephone: 234-803-3307645
zionbiz3@yahoo.com or dailymarketingservices@yahoo.com
Our main aim is to get quality yam and other African food stuffs
to living houses of any interested buyers and we ship in small
and large quantities on request.Distributors and Manufacturers in
South Africa
African Pride International
Shop Number 7
47 West Street, Kempton Park
South Africa
Phone number:00 27 83 949 22 88
africanfoodvendor@gmail.com
We specialise in African traditional delicacies such as fresh and
dry fishes, potatoes, variety of vegetables, oils (palm), yams,
peanuts, white rice, baobab juices, spices, etc. We supply
chambo -tilapia fish to the wholesale butcheries and catering
industry across South Africa. Contact Siraj.
Chukstracy Import and Export CC
No. 31 Pretoria Street Hillbrow
J.H.B South Africa
Phone: +27,11,4845118 Mobil: +27,731260532,
+27,732195263
chuks.tracycc@yahoo.comWe import West African foods into South Africa. Our imports
include gari, fresh yams, palm oil, egusi, ogbolo, achi, and
more.
Circle Seven Trading
PO Box 1885
Musina
South Africa
0900
Tel / Fax +27 15 530 0219
Cell: +27 82 877 8517 / +27 82 852 5225
This is a South African based company trading in sustainable
resources. They are suppliers of Baobab pods, seeds, and pulp
and are looking for markets for Southern and East African
produce. The collection of the product is done with the local
community in an effort to give the rural people some access to
income from those things that grow around them.
Matlabopi Foods
Electron Road No5
Uraniaville
KlerksdorpNorth West Province
South Africa
Phone No:+27184693904/2
Fax No: +27184693903
This manufacturer is a maize milling plant and they produce
maize meal, the staple food of Africa.
Mpilende Foods (PTY) Ltd
P O Box 5909
Durban, South Africa, 4000
Phone: +27 31 201 6923 Fax : +27 31 201 6929 Mobile :
+27 72 010 5566
info@mpilendefroods.co.za
Mpilende Foods (Pty) Ltd, is a South African based company
that is professionally managed, and specialises in the
manufacturing of nutritional and basic food commodities
(general grocery), using its state of the art manufacturing facility
based in Glen Anil- Durban. Our company has been certified to
be compliant with most of the international quality management
and food production systems including : ISO9001: 2008, FDA,
ISO22000: 2005 (in process) among others. The food products
that we manufacture include, but are not limited to : instant
cereals (pre-cooked maize based and sorghum based), milk
powders (full cream, creamer and lactose free), high energy
drinks, maize meal, parboiled rice, soya mince, flavoured soup
powders. Mpilende is also a member of the South African
Alliance Against Malnutrition (South African Health Department
/ GAIN and Private Sector initiative).Niod Trading Services
P.O. Box 2702
Primrose, Johannesburg
Gauteng South Africa 1416
dionva@telkomsa.net
Niod Trading Services is a South African trading house that is
involved with the trading of goods and services internationally,
exporting and importing into Africa and the rest of the global
market. We represent the local manufacturing industry within
the following industrial sectors i.e. agricultural products,
perishables, foodstuff, consumables, mining equipment and
parts etc.
WP Exports & Sales
103 Gie Road
Tableview, Cape Town,South Africa
Tel:+27 215575665 Mobile:+27 786100590
wpexportct@gmail.com
We are an exporting company of well known South-African
FMCG products like Mrs.Balls chutney, Niknaks, etc. We mainly
export dry groceries, but also products of multi-national
companies like Reckitts-Benckiser and Colgate-Palmolive. We
are looking for new business and we have contactable
references.
Distributors and Manufacturers Zi
mbabwe
Alpha Betting Private Limited (trading as
Bon Fruit)
REGG 12 Waterfalls Avenue
Ardbennie, Harare, Zimbabwe
Tel: +263 733894138, or +263 912368795
bon_fruit@ymail.com
Bon Fruit is the trade name for Alpha Betting Private Limited
which was incorporated in February 2008 and started
operations in April 2010. Our vision is to be the leading dried
beef manufacturer in Zimbabwe and to create lasting
relationships with our local and international clients. We
manufacture preservative free dried beef from Zimbabwe using
high quality hindquarter beef steak. We package our dried beef
products in 50g and 100g packets and they cost US$1.45 and
US$2.80 per packet respectively. All interested buyers can
order a free sample but will be required to pay for
shipping/courier costs.Australian Wholesalers and Distributors
DF Hunny
Cnr Punchbowl & Benaroon Roads
Belfield, NSW, Australia
sales@dfhunny.com
DF Hunny is the distributor of choice for African food products.
Our Ola-Ola brand of products are exclusively processed and
manufactured in the United States of America. The Ola-Ola
brand are available in a wide selection of African gourmet flour
such as: plantain fufu flour, potato starch, cassava starch, bean
flour, ground rice, rice flour, cassava flour, akpu-fufu,
elubo/amala and yam flour. Our other brand products are the
Ola-Ola Carotino cooking oil and the Ola-Ola cholesterol-free
red palm oil. We also distribute other products such as: Titus
sardines, Geisha, white gari, yellow gari, ijebu gari, egusi,
ogbonno, Derica tomato paste, hot red chilli, Ata suya, Maggi
crayfish, etc.
Solarben International Foods
PO Box 1067
Armadale WA 6112
Phone: 61893905240
Mobile: +61438993631
Fax: +61893905240solarbenfoods@aol.com
solarbenfoods@yahoo.com.au
Solarben International Foods was established in Perth, Western
Australia in May, 2005. We are the sole importer and distributor
of "Ayoola brand" of West African food products. We specialise
in wholesale, manufacture and distribution of afro-caribbean
foods, spices and drinks. Our goal is to make ethnic foods and
drinks available to all Africans and Carribeans throughout
Australia.
Solarben ....... Bringing You Your Home Foods!!!
Canadian Wholesalers
North Atlantic Stockfish
Nova Scotia
Phone (508) 496-2443
Gudni Bjornsson is the owner of this supplier of stockfish bits.
Freshly caught cod fish are dried in the open air, then cut into
convenient serving pieces. This highly nutritious concentrated
food can be stored for a long period of time. Stockfish is
commonly used in West African soups and stews. For more
information send an email to the owner at
stockfish@stockfish.ws
TwinStar Overseas Trading8367 Copeland Road
Ottawa, Ontario KOA 1BO
Canada
Tel: 1-613-838-5603
Fax: 1-613-838-5603
queenstarfufu@gmail.com
TwinStar OT manufactures and distributes Queenstar Plantain
Fufu made from 100% natural source ingredients. Unlike most
other brands of plantain fufu, Queenstar Plantain Fufu does not
contain Yellow No. 5 food colour. Please follow this link to
understand why Yellow No. 5 food colour is not used in
Queenstar Plantain Fufu. We are currently looking for reliable
Importers/ Distributors in the US, Europe, Australia and Africa.
View an ad flyer for Queenstar Fufu
European Wholesalers
Ezeani Import and Export
Reideburger St.51
Halle Saale 06116
Germany
ezeaniimport@yahoo.com
We are importer of nigeria food stuffs and we sell in wholesale
to our customer, We also have nigerian drinks such as fanta
35cl, schweppes bitter lemon, star, gulder, malitina, guinness
stout, malta guinness, and palmwine, all at a reasonable price.Fiji Islands
Balthan (Western) Ltd
P.O.Box 1228
SUVA, Fiji
(679) 398 912 913 Fax: (679) 3398 916
gst@connect.com.fj
This company is a long established and leading Fiji Islands
grower, processor and exporter to the International market.
They carry a range of premium frozen, Afro type products, such
as cassava, taro (dasheen), breadfruit, sweet potatoes, and
others. They currently export to Australia, New Zealand, West
Coast USA, Europe, Japan, and the Sth Pacific Islands. They
are looking for a reliable Importer/ Distributor on the US East
Coast and Canada.
South American Wholesalers
Surimaribo Products
Isserdeistr. 63
Paramaribo
Suriname, SA
TEL/FAX: 00597 33 82 00MBL: 00597 86 56 008
surimariboproducts@hotmail.com
A fish company specializing in processing seafood the
traditional African and Carribean way. They follow the HACCP
processing standards. They can ship fish in reefer containers or
twice a week by air through Miami. From there by truck to any
destination in US or Canada. Products include smoked fish as
catfish chunk, whiskered fish fillet, scale fish fillet, barracuda
and tai rings, splitted catfish, akwebi, kutafish, perch, whitefish,
akau, pitrie, tiko, carp. Also salted cobi (tilapia). Frozen
vegetables include poundu (zaka zaka), matembele leaf, bitter
leaf, hot red and yellow pepper and sweet cassava chunks.
Email them for a complete product list.
United Kingdom Wholesalers
Akoma Foods
Unit 16 Brian Clough Business Centre
200-222 Cotton Lane
Derby
DE24 8GJ
United Kingdom
Tel:+44 (0)1332 268 626
Fax:+44 (0)1332 268 627
info@akomafoods.com
Importer, Wholesaler and distributor of African foods based in
the East Midlands. We specialise in Ghanaian and Nigerian
Foods but also carry foods from other African countries. Akoma
foods is a division of Akoma International (UK) Limited.
Divine Tropical Food
184 Marsh Road Leagrave, Luton
Bedfordshire. LU3 2QL
info@divinefoodonline.com
Wholesale /retailer of all African foods and special pre-packed
soups such as Stew, Egbono, Okaze, p-soup, Efo etc and
more.
MA Quality Foods
23 New Mount Street
Manchester M4 4DE
United Kingdom
Phone: +44[0]1619534015 Mobile: +44[0] 7782260849
enquiry@maqualityfoods.co.uk
We are manufacturers and distributors of African food in United
Kingdom. Our brands include Sankofa fufu powder and Lagos
agbe pounded yam powder, and more!
Odiega House
Odeiga House Limited
Unit 46 Cariocca Business Park
Helidon Close
Ardwick
Manchester
M12 4AH
+44 (0)161 2736665
Email: odeigahouse@btconnect.com
Odeiga House is a young bustling business with an insatiable
appetite for producing full-bodied African and Caribbean
cooking sauces and marinades brimming with bold, unflinching
flavours.
United States Wholesalers
4Biltong.com
5320 Gulfton St, Suite 12
Houston, TX 77081
(713) 417-3780
info@4biltong.com
Offering the finest South African Biltong and Boerewors in theUSA. We are located in Houston, Texas & will ship anywhere in
the US.
AA Biltong
11229 E. Independence Blvd.
Matthews, NC 28105
(704) 849-2660
Wholesalers of South African Beef Biltong and Droewors in the
USA
African Goods Traders And Imports
11 Gibbs Street
Worcestor, MA 01769
phone: 001-(484) 318-3344
africangamenart@gmail.com
Importers and suppliers of african food, art, clothing and raw
materials like sheabutter.
African Tropical Importer
Kansas City, KS, 66101
Phone: (913) 371-0061email
Wholesalers of all kinds of African, Central American and
Carribean foods and merchandise.
African Pacific Imports and Exports
P.O. Box 8104
Mesa, Arizona
(480) 981-0999
This company imports African products to the US, and exports
North American products to Africa.
All United Imports, Inc.
9225 S. Blue Island Ave. Unit#107
Chicago, Illinois 60633
(866) 319-4645 Fax: (773) 831-4725
Email:sales@allunitedimports.com
All United Imports, Inc. brings you the very best imported
products for delicious tasting Caribbean, Haitian, African, and
Mexican foods. Experience real cooking with our imported
authentic food ingredients - hundreds of products ready for your
table. Our products are supplied by reputable vendors, so you
can be assured that you are always getting great quality, price,
and service. We carry all of the popular brands such as Ocho
Rios, Blue Mountain, Walkerswoods, JCS, Grace. Whether it's
from Africa, Jamaica, or from any other country in the
Caribbean, you can find it here.
Big River Fish Corp.
14310 State Hwy 100
Pearl, IL 62361
Phone: (217) 829-4004 Fax: (217) 829-4004
fishmart@hughes.net
Products include smoked/dried catfish chunks, catfish rings,
Kuta, Azu Asa, Perch, Pike rings, White fish, and Tilipia
Wholesale and retail sales. Visa and Mastercard accepted.
Careco LLC, Red Palm Oil Wholesaler
23352 Madero Road #K
Mission Viejo CA 92691
(888) 877-4746 fax: (949) 380-3753
info@goldencoastfoods.com
Golden Coast Foods sells 100% natural and unrefined red palm
oil, imported directly from Ghana.
Fountains Food: African/CaribbeanFoods
Retail, Wholesale and Distribution Center
19 King Court
New Castle, DE 19720
(302) 690-4881
Fountains Food is a tropical food processing, packaging and
distribution center of Delaware. We process oats foo foo,and
package African honey, peeled beans, hot pepper, ehiri-
wedeaba spicy. We distribute Titus sardine, Ghana Fresh palm
butter, frozen bitter leaves, Ugu (pumpkin leaves), ukazi leaves,
sour-sour leaves, palm oil, etc. We seek distributors to cover
West, South and Midwestern States for our oats foo foo.
Global Marketing Ent. Inc.
1801 S. Canal St.
Chicago, IL 60616
This company is a direct importer and distributor.
Golden Country Oriental Food
2355 S. Blue Island Avenue
Chicago, IL 60608
Phone: (773) 847-2442, (773) 847-1700 ext. 139
Fax: (773) 847-1717
Importer, Wholesaler and Distributor of African and Caribbean
food products in the United States.
Email: gift@goldencountry.com
Islar International
P.O Box 2662
Woodbridge, Virginia 22195
(888) 204-1998
sales@islarinternational.com
Exporters, Wholesalers and Distributors of African style dried
smoked fish, meat and other authentic ethnic products.
Experience the traditional aroma and taste of back home with
our range of wild catch smoked fish and free range smoked
meat. Our products are supplied by reputable HACCP, USDA
and FDA registered vendors, so you can be assured that you
will always get quality and price.
Manaco Liquid Pepper Inc
P.O.Box 1707
Sugar Land, TX 77487 USA
Phone : (800) 353-1382
Fax: 281-491-2533
We are maker and producer of a Liquid Pepper from Houston
TX. This Original and Unique product is homogeneous and
Extremely Hot. This is not a sauce or a puree with salt or other
preservatives. This is Habanero Pepper Extract and vegetable
oil only.
M'Bambi and M'Bambi Tropical Produce
Growers Inc.
1142 Crooked Creek Road
Lithonia, GA 30058
mbambi@netscape.com
This company is a wholesaler of frozen ground cassava leaf,
amaranthus, roselle, bitter leaf, and african hot pepper. All
seeds and planting material are directly from Africa.
Nina International
PO Box 6566
Hyatsville, MD 20789
Novelty Food Wholesale
20 W. Streamwood Blvd
Streamwood, IL 60107
(630) 372-7704 Fax (630) 372-7705
Email: info@iwunzeholdings.com ; sales@iwunzeholdings.com
Novelty Food Wholesale is a specialist and cheapest source of
variety and hard to find African food and other products.
Oja Village Market and Travel Int.
3114 Summit Ave.
Greensboro, NC 27405
phone: (336) 358-8260
Prince and Brothers
(413) 739-7214 fax:(413) 739-9368
Quality African Foods, Inc.
73-75 Joseph St.
Newark NJ 07105 (warehouse/office)
(973) 522-1552 FAX:(973) 522-1553
Raymond Hadley Corp.
89 Tompkins St.
Spencer, New York, 14883
(607) 589-4415 (800) 252-5220 fax:(607) 589-6442
This manufacturer/distributer contracts packaging for private
labels. They might have packaged up that favorite brand of gari
you've been buying! They furnish foods to ethnic groups,
institutions, bakeries, distributors and wholesalers. West African
foods include fufu mix, bean flour, plantain flour and gari. They
also carry Peruvian, Colombian, Salvadorian, Haitian, East
Indian, Portugese and other specialty items. Email to
info@raymondhadley.com
Regal Brands Fried Plantains
Manufacturers of delicious, juicy, fried plantains, vacuum
packed and frozen, ready to microwave and serve in minutes.
Generous discounts on your first wholesale order.
Email: fmgi@hotmail.com
404-438-2077
SA Import Company
27601 forbes Rd #19
Laguna Niguel
CA, 92677
(949) 582-9546
sales@saimportcompany.com
Importer and distributer of wholesale South African groceries in
the US.
Sandies Deliz
2871 Brandl Cove Ct
Marietta, GA 30067
(770) 402-7077
antiley@yahoo.com
Wholesaler and retailer of African foods, including okazi (eru),
bitterleaf, njangsa, egusi, red colanuts, bitter colanuts, ogu
(okongobong), crayfish, njanja moto, bobolo, miyondo, baked
peanuts, roast dry corn, kalaba chalk, and natural african black
soap. Other products are available at request.
Spicy World of USA, Inc
10421 SW Plaza Drive
Houston, TX 77074
(713) 661-2972
ashish62@gmail.com
We are a wholesale distributor of Indian/British/African
products. Our product line includes, but is not limited to: Peak
milk, Birds Custard, Heinz products, Cerelac from Europe,
Farina, Semolina, Parboiled rice, Dettol, Ribena, Lucozade,
Milo, Ovaltine, etc.
Other locations:
Spicy World II, LLC 735 Park North Blvd #120, Clarkston, GA
30021....Ph: 404-294-7440
Spicy World III, LLC 3500 Oakton St, Unit 102, Skokie, IL
60076......Ph: 847-410-1045
Tyal International
203 Calypso Lane
League City, TX 77573
phone and fax: (281) 334-0718
email
This import company brings in small consignments of Southern
African foods, mainly ingredients to compliment South African
recipes. The small consignments ensure freshness. Web site
under construction. They have been making their own biltong,
an air dried meat delicacy for the past 4 years. They use
imported ingredients from South Africa. They make the biltong
slightly soft, suitable for further air drying (for a day or three) to
get it to the exact preferred dryness. The biltong is frozen after
coming out of the drying machine, and is shipped in a frozen
state; hence shipping must be 2 days max. (If it thaws out it can
be refrozen). Shipping is done at cost. Contact Allen or Heather
Botha.
Urban Logistics
4807 Colley Ave
Norfolk, VA 23508
mgt@urbanlogistics.net
Urban Logistics provides shipping, warehousing, distribution
and custom brokerage services. They have customs brokerage
operations in Conakry, Guinea; Mombasa, Kenya; Monrovia,
Liberia; and Tema, Ghana. They offer air cargo service to most
African countries. See their web site for more information.
White Dove Farm
15821 West Santa Paula St.
Santa Paula, CA 93060
(805) 933-1889
White Dove Farm sells Passion Fruit wholesale direct to
residential and business alike.
Winner Group LLC (formerly ETS
Legrand LLC)
1489 Newton Street NW #35
Washington, D.C. 20010
Phone: 202-341-4775 fax: 202-280-6550
Alternate: 202-483-0036
winnerlegand@verizon.net
Importers of African foods, including gari, shea butter, palm oil,
several types of smoked fish, jute, cassava and sweet potato
leaves, and more. Food can be sold by container, bulk or retail.
Zuka Trading and Distribution Company,
Inc.
1780H Old Bayshore Hwy
San Jose, CA 95112
(408) 392-0128 Fax: (408) 392-0129
email: zukao@yahoo.com
Distributors of African foods and beauty care products.
Kumusha African Food and Gifts
2100 Logan Road, Upper Mount Gravatt
Brisbane, Australia, 4114
Phone: 07 3420 3422
Our goal is to bring all the popular foods from Kumusha to
Australia and provide a friendly, family based store with great
pricing and a central location.
Poland
Yem Africa
Ul.Polna 1-13,00-633
Warsaw, Poland
Tel/Fax:+48-22-3310892
Wholesale and retail market of African and Caribbean foods.
Their products include yam, plantain, egusi, drinks and alcohol
from Nigeria such as palm wine, Star, and herbal teas.
British Markets
Friends
22 Plumstead Road
Woolwich
London
SE18 7BZ
Telephone: 0208 309 8202
Fax: 0208 854 7279
Mobile: 07943 47456
This is a family run shop which sells all kinds of West African
food, especially Nigerian, Ghanian and Cameroonian. Some of
their products are Ugo, scented leaf, bitter leaf and other
vegetables, with a choice of fresh, frozen or dried. They also
sell Nigerian and Ghanaian Milo, Nido, Peak, Indomie noodles,
akam, custard, bournvita, and tolly boy rice.
Linal Food Store
Unit 2, 8 Roumelia Lane
Boscome, Bournemouth
Dorset, England
phone: 07920405275
dakoru2002@yahoo.com
We are a family business, newly started in the South of
England. We provide both wholesale and retail of African and
Caribbean foodstuffs. Our products include pounded yam flour,
smoked fish, egusi, ogbono, ogi, ukazi leaves, ugwu, utazi,
ackee, saltfish, callaloo, hot pepper sauces, jerk sauces and
more.
D4 FOODS
Woolwich Market
Beresford Square
London SE18
or...
69 Austen Close
Thamesmead
London
SE28 8AY
E-mail:d4foods@hotmail.com
Specialises in wholesale and retail african raw foods, like gari,
ijebu, elubo, palm oil, snails, agbo for different ailments, obi,
orogbo, ogi and others.
Savannah-African Food Stores Ltd.
17 Church Road
Lawrence Hill, Redfield, Bristol
BS5 9JJ
07776324388 / 07950584569
A new African foods retail shop, the first in Bristol, selling all
West, East and South African foods.
Zambezi Foods
Birmingham Store: Limpopo Foods, Birmingham, Great Britain
Phone: 0121 434 5253
Luton Store: Zambezi Foods, 76 Hightown Road, Luton, LU2
0BW, Great Britain
Phone: 01528 419 284
email
Zambezi Foods is Britains leading household name for
Southern African soul food, beverages and memorilibia.
Through consistently valuing our customers needs and
demands we are now online delivering Africa`s finest foods
straight to your doorstep.
Canadian Markets
Eat-Sum-More, Inc
7700 Bathurst Street, Unit #6
Thornhill, Ontario
L4J 7Y3
eatsummore@bellnet.ca
Located in Toronto, Canada, we are ex South Africans who help
other ex South Africans who have a craving for their favourite
South African foods fulfill their cravings.
Arizona
Ako International Market
1400 S. McClintock Dr. Ste.14
Tempe, AZ, USA
(480) 317-9000
We sell lots of african groceries, authentic clothing, arts + crafts,
black cosmetics and beauty care, pre-paid phone cards,african
movies on vhs, dvd and vcd,african music cd's. Including the
following; kenkey(dokono), yams, fufu flour, rice flour,
corndough, cassava dough, stockfish, fried fish, smoked fish,
semolina, farina, maggi cube, spices, shito(black pepper
sauce), plantains, palmoil, egusi, ogbono, ukazi, plantain chips,
frozen snails, gari, dry shrimp, crayflish, ginger beer, malta,
shea butter, dermovate, lemovate, black soap, mercy cream,
wigs and Auntie Lizzie hair extensions.
California
African Hut
27601 Forbes Rd. Suite 20
Laguna Niguel, CA 92677
(949)582-9546 Fax (949)582-5616
email
African Hut sells Southern African foods including beers,
beverages, cereals, samosas, jams, wines and sweets. You can
order online.
Brookside Grocery (Afrimart)
2085 23rd Street
San Pablo California 94606
(510)776-1916
This is an ethnic shop selling African and Caribbean foods.
Motherland African Foods Market
80 West Grand Ave. Suite 124
Corona, CA 92882
(951) 280-0222
This market is recommended by a patron. They sell all sorts of
African foods including yams, palm oil, chin-chin, egusi and
more. The owner's wife also has a hair and makeup business
and does African styles and head-wraps (gele).
Tropical Foods African Market
4511 Orange Ave.
Long Beach, CA 90807
(562) 492-1129
tropicalfoods@yahoo.com
A wholesale and retail store of all African food items, imported
from Africa. The items include Ukazi, bitterleaf, egusi, colanuts
(goro & Igbo), bitter cola, Ugu (okongobong), crayfish, roasted
peanuts, smoked fish, nzu (kalaba chalk), natural african black
soap, Snails, stock fish, and various other products are
available. We also carry Nigeria, Ghana, etc Movie & Music
CDs.
We Yone Foods Convenience Market
251 E. Baseline Road
Rialto, Ca 92376
(909) 879-0242
Specialize in all African, Caribbean and Central American
foods. Come find us-we'll find whatever you are looking for.
Yinkus African and Caribbean Market
869 E. Washington Blvd
Pasadena, CA 91107
(626) 798-5212
This market run by a Liberian woman offers many selections of
African foods.
Connecticut
Kristodia Market
818 First Avenue
West Haven, CT 06516
kristodia@live.com
This beautiful, well organised, well stocked African/Caribbean
Market comes recommended by a patron.
Florida
Africa On The Bay
1908 W. Dr. Martin Luther King Jr. Blvd.
Tampa, FL 33607
(813) 374-9614
africaonthebay@yahoo.com
We are a wholesome African marketplace, providing a variety of
products and services to the African and Caribbean
communities in the Tampa Bay area of Florida. Products
include African and Caribbean food and grocery items such as
meat, seafood and poultry, fresh produce from the farmer's
market, latest African movies and music, health and beauty
products, African attire and materials, African arts, and services
such as money transfer, airline tickets and shipping services.
Find us on Facebook
Meal in a Pie - South African Groceries and Food
4440 NE 20th Ave
Fort Lauderdale, FL, 33308
(954) 202-9178
Georgia
Find us on Facebook
Chez Nou Market
4015 Holcomb Bridge Road #640
Norcross, Georgia 30092
(770) 449-4114
manager@cheznousmarket.com
We are certified C.A.M and UNI-Transfer wire agents. We add
minutes to cell phones in the Caribbean by the carrier 'Viola'.
We sell West African food, beauty products and cooked food in
a separate section in the store. Chelie (the owner) is from the
Island of Haiti, her husband is from Mali and all our friends are a
mixture of Ghanaians, Senegalese to Gambian. We enjoy every
minute of serving the African community.
Sheba Foods
3420D East Ponce De Leon Ave.
(770) 982-1000
Sheba Foods is the first and only company with ready to eat
African cuisine in major supermarkets, for example, Wal Mart
and Whole Foods Market. Visit their gourmet store at the
Georgia location listed above.
Illinois
Aboasa International Market
221 South Green Bay Road
Waukegan, IL 60085
Phone: (888)205-4868 OR (847)596-2032
Fax: (847)599-1632
accentafrica@aol.com
Aboasa International Market is an authentic African store
dealing in various African and Caribbean groceries, clothing &
crafts. We also sell various electronics products including GMS
phones for Africa and Europe at competitive prices. Visit our
web site for more information. We ship throughout continental
United States at reasonable prices.
Anu's Store Co.
231 East 79th Street
Chicago IL 60619
anusstore@gmail.com
This is a Chicago-based company that sells African and
Carribean products to the general public, both at our site
located at 231 East 79th Street and online through our website.
If you want quality products at a cheap price, come and visit us
today!
Chika International Food Market
522 E Boughton Rd
Bolingbrook, IL 60440
Phone: 630-739-7799
The store is well stocked with a variety of African food products
and hard to find African Cosmetics. It has the largest line of
Ghana products in Chicago. Also does money transfer to most
African countries including Nigeria, Ghana, Ivory coast and
Sierra Leone.
Hours:
Monday: 5pm-8pm, Tuesday to Friday: 10am to 8pm,
Saturday: 10am to 7pm, Sunday: 11am to 5pm
Devine Food market, Inc.
4445 N. Broadway
Chicago, IL 600640
(773) 334-7906 Fax: (773) 334-7917
anike.anthony@yahoo.com
We carry all African, Caribbean, Mexican and Jamaican food
products. We are the source of hard-to-find African food
products such as fresh kola nuts, bitter kola, alligator pepper,
etc. We sell retail and wholesale.
Flo Tropical Foods
1652 Sibley Blvd.
Calumet City, IL 60409
708-730-1070
flotropical@aol.com
La Fruteria, Inc.
8909 S. Commercial Avenue
Chicago, Illinois 60617
(773) 768-4969 Fax: (773) 768-0734
Email: sales@lafruteria.net
La Fruteria brings you the very best imported products for
-delicious tasting Caribbean, African, and Mexican foods.
Experience real cooking with our imported authentic food
ingredients-hundreds of products ready for your table.
Old World Market
5129 N. Broadway
Chicago, IL 60640
(773) 989-4440
Specializing in fresh, frozen, canned and dry West African and
Carribean foods.
Riteprice African Food Market
2227 West Schaumburg road
Schaumburg, IL. 60194
Phone: (847)352-4951
riteprice@talkamerica.net
Serving African descendants in the heart of the northwest
suburb of Chicago. They offer all types of African foods, both in
retail and wholesales prices.
Kansas
African Tropical Market
901 N 7th Street
Kansas City, KS 66101
913-371-0061
This market is owned by Paul Abanishe, a Nigerian. Mr.
Abanishe carries a large selection of East, Central and West
African foods. He is fluent in Spanish and carries many Central
and South American and Caribbean products. Mail orders
shipped within 48 hours. Mr. Abanishe has been serving the
Kansas City area since 1998.
Kentucky
ValuMarket Iroquois
5301 Mitscher Ave
Louisville, Kentucky 40214
phone:(502)361-9285
fax:(502)367-8552
email
This is an international grocery store with over 200 authentic
West African products.
Massachusetts
Albino Fruit Market
92 Belmont St.
Worcester, MA 01605
(508) 753-9280
Albino's sells all sorts of African foods from palm oil to agbono,
kenkey to sweet bread. Their selection is always different
depending on the stock.
Tropical Foods
2101 Washington St.
Roxbury, MA 02119
(617) 442-7439
This large market in Boston sells Caribbean, Spanish, West
Indian and a number of African products. Here you can get your
gari and egusi and do the rest of your weekly shopping as well.
They carry palm oil, meats, fresh tropical produce, cosmetics
and more. They plan to do online sales in their upcoming web
site.
We Can Stores, Inc.
700 Suite 2, North Street
Pittsfield, MA 01201
(413) 464-8124 fax: (413) 464-8125
They specialize in african food, cosmetics, movies, fedex
express and ground services, copy, fax, internet cafe, bill
payment, and money transfer.
Mississippi
Ijaw Smoke Fish and Meats
51 Sunrise Lane
Silver City, MS 39166
ijawsmokefish@hotmail.com
(662)247-0881
We provide smoked fish to all of the African Stores around the
United States. We sell all kinds of meats and fish, smoked just
the way you want it. You set the smoke quality and we deliver
great taste. All product are smoked slowly with the finest oak
wood available. Call to order.
Phamega African Caribbean Market
4253 Robinson Road, Suite 102
Jackson, MS 39209
(601) 923-8787
We specialize in African and Caribbean groceries, international
money transfer, African clothing, calling cards, beauty supplies,
current African movies.
Missouri
African Depot
9944 West Florissant Ave (near the corner of Chambers Rd and
W. Florissant)
St Louis MO 63136-1432
phone: (314) 868-9555 fax: (314) 867-2330
cell (314) 249-3176
Best source for African food items, art and clothing
African Market
3701 Main Street
Kansas City, MO 64111
(816) 753-2520 Fax: (816) 753-1096
Imported foods from Africa and the Carribean.
Global Foods Market
Fine Imported Products from Around the World
421 N. Kirkwood Rd.
Kirkwood, MO 63122
Phone: (314) 835-1112 Fax: (314) 835-1113
This shop is open 7 days a week. It offers a good variety of
international foods organized by country, with each section
marked by that country's flag. Reports say this store is
superclean and an exciting place to shop. It includes an
American section.
Jay International Food Co.
3172 S. Grand Ave.
St. Louis, MO 63118
Retail: (314)772-2552 Wholesale: (314)772-9393
This market is an excellent source of several kinds of West
African and other exotic foods.
New Hampshire
Tropical Markets
58 Chestnut Street
Nashua, New Hampshire 03060
(603) 880-0270
This Spanish grocery carries many tropical foods such as yams,
plantains, fruits, all sorts of dried peppers, dried shrimp, frozen
tropical fruit purees, frozen yams (peeled and cut in chunks),
banana leaves, and more.
Spanish and American Grocery Store
50 Whitney Street
Nashua, NH 03064
(603) 881-9531
Some of the tropical foods you'll find in this Spanish store are
yams, plantains, chorizo, guava paste wrapped in banana
leaves, and canned whole guavas in syrup.
New Jersey
3J's African Convenience Food Mart
1400 Asbury Avenue
Asbury Park, NJ 07712
(732) 807-4750
3JYinka@gmail.com
We specialize in african, and tropical food grocery products at
affordable prices, all under one roof. The food we sell includes
pounded yam, fresh yam, parboiled & basmati rice, garri, white
& brown beans, smoked chicken, dry fish, fresh fish, blue fish,
bitter leaves, melon seed (egunsi), Nido, Milo, British Heinz
Baked Beans, original African & Christian DVDs, Tura Soap &
Cream and MoneyGram Money Transfer.
Ade International African Market
590 Central Ave
East Orange, NJ 07018
(973)674-3031 Fax: (973)674-2653
Herbs, medicine, food products, clothes, jewelry, shea butter,
black soap, haitian products, religious articles and outfits,
catering. They have some great Nigerian palm juice!
Calabash
45 Edison Place
Newark, NJ 07102
(973) 643-7828 You can get just about any West African foods
from this shop, including daddawa!
Makola African Market Imports
375 Lyons Ave. (Exeter Plaza)
Newark, NJ 07112
(973)926-3919 fax:(973)926-2520
U Save International foods, The African
Market
266 George Street
New Brunswick, NJ
You can buy your egusi, stockfish and bitter leaves here, for a
propa African meal that will make you remember your Mma's
cooking.
New York
African Heritage Foods
D.B.A. Country Cottage Savories
PO Box 497
Jefferson Valley, NY 10535
(914) 228-1584
African Market and Resto
International Exotic Products Inc.
172-20 Jamaica Ave.
Jamaica, NY 11432
Phone: (718) 523-1057
email
Juliette is a whole saler and retailer of Africa Food products,
European cosmetics, African cloths, cassettes, Nigeria and
Togo movies and comedies, and finger licking African Cuisine,
where you can eat any African food.
Almacenes Shango
661 Madison Avenue
New York, NY 10029
(212) 722-4275
Osa Adolor African Market
774 Lenox Road
Brooklyn, NY 11203
(718) 363-2148
Osa Adolor sells authentic African food supplies and
ingredients, such as stock fish, cray fish, gari, ogbono, yam,
kola nuts, bitter leaves, palm oil and more. They also sell
African artwork, materal and clothing.
North Carolina
Eki African and Caribbean Market
1705 Ramsey St
Fayetteville, NC 28301
(910) 484-4278
Health and beauty products, Nigerian movies and music and an
outstanding selection of African food.
chin-chin Motherland Cuisine & Market
6024A The Plaza
Charlotte, N.C 28215
(704) 532-4279 cell (704) 236-5999
dollywey2000@yahoo.com
This combination market/restaurant is newly opened by the
previous owners of Flapper International Market in Charlotte.
They carry mostly African groceries and serve authentic African
(West African) and continental dishes. They also claim to make
the best CHIN-CHIN in U.S.A.! I think they might be right about
this. I have had their chin-chin, and it's delicious. See the photo
of their chin-chin to the right, and a description on my blog.
Sankofa International Market, Inc.
3209 Yanceyville Street
Greensboro, NC 27405
(336) 375-4111 Fax: (336) 375-6699
Email: Mariagbie@aol.com
This local market carries African and Caribbean food, arts and
crafts.
The South African Food Shop
11229 East Independence Blvd.
Matthews, NC 28105, USA
(704) 849-2660
Retailers of traditional South African foods and grocery products
in the USA.
North Dakota
African Market
1230 23rd St.
Fargo, ND 58103
(701) 298-7909
e-mail: noahkpena@yahoo.com
Products include bottled red palm oil, powdered yams, and
REAL fresh yams from Ghana.
Oklahoma
R.K. Supermarket, Inc.
2328 N. MacArthur
Oklahoma City, OK 73127
Phone: (405) 946-1996 Fax: (405) 942-6916
This African market sells wholesale and retail products.
Oregon
African Food Market
1910 N Killingsworth St
Portland, OR 97217-4437
(503) 283-8585
Pennsylvania
ACI Market
79 North Progress Avenue
Harrisburg, PA 17109
(717)540-1449 Fax: (717)540-1688
This market sells african foods and meats, clothings and
treasures. They also help convert video to either ntsc or pal,
and sell african movies.
The African Market
121 ½ E. Beaver Ave
State College PA 16801
(814) 238-1938
Newly opened in November 2007, this market carries african
-groceries, fair trade art & decor, fabrics and movie rentals.
International Market
328 S. Allen Street
State College, PA 16801
(814)238-7679
This Chinese market run by Clara Wang has a little African
corner where you can find foods such as dried fish, palm oil,
egusi or ground pepper.
Royal International Food Market
1132 N George street
York, PA 17404
(717) 848-1764
This African and Caribean food market sells african foods and
meats, clothing and treasures. We also rent and sell african
movies.
South Carolina
FHG International Food And Spices
Trader Marc's Flea Market Mall
2200 Carolina Place
Fort Mill, SC, 29715
(803)810-0505 or (803)389-8940
This store sells a wide variety of West African foods. See a list
of products on their Facebook page. Great tasting food starts
here!
Tennessee
Tropical Foods & Convenience Store
467 Bell Road
Nashville, TN 37013
(615) 366-3978
We provide the best services in town, with products ranging
from bitter kola to dried fish/stockfish. We take pride in our
cosmetic products, luggages, and movies straight from Nigeria.
Please come by during our hours from Mon- Sat 10-7pm , Sun
11-5pm.
Texas
African Palms
1104 East Beltline Road #106
Carrollton, TX 75006
manager@africanpalms.biz
African Palms is home to a large selection of authentic African
foods and spices. We bring you the very best imported
Caribbean & African food products. It is a delightful experience
when you cook with our imported authentic food ingredients.
Products include meats, breads spices, grains, and other
African foods, money transfer, calling cards, fax, notary public,
beer and wine, cosmetics and African movies.
"""


def is_section_header(line: str) -> Optional[str]:
    headers = [
        'Nigeria', 'South Africa', 'Zimbabwe', 'Australian Wholesalers and Distributors',
        'Canadian Wholesalers', 'European Wholesalers', 'Fiji Islands',
        'South American Wholesalers', 'United Kingdom Wholesalers', 'United States Wholesalers',
        'British Markets', 'Canadian Markets', 'Arizona', 'California', 'Connecticut', 'Florida',
        'Georgia', 'Illinois', 'Kansas', 'Kentucky', 'Massachusetts', 'Mississippi', 'Missouri',
        'New Hampshire', 'New Jersey', 'New York', 'North Carolina', 'North Dakota', 'Oklahoma',
        'Oregon', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Poland'
    ]
    clean = line.strip()
    for h in headers:
        if clean.lower() == h.lower():
            return h
    # Also handle broken word wrap like "Distributors and Manufacturers in" lines
    if re.fullmatch(r",?\s*Distributors and Manufacturers( in)?", clean, flags=re.I):
        return 'Distributors and Manufacturers'
    if re.fullmatch(r"Distributors and Manufacturers Zi\s*mbabwe", clean, flags=re.I):
        return 'Zimbabwe'
    return None


def extract_emails(text: str) -> List[str]:
    return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)


def extract_urls(text: str) -> List[str]:
    urls = re.findall(r"(https?://\S+)", text)
    urls += re.findall(r"\bwww\.[\w.-]+\.[A-Za-z]{2,}\b", text)
    return list(dict.fromkeys([u.strip().rstrip(').,') for u in urls]))


def extract_phones(text: str) -> Dict[str, List[str]]:
    phones = {
        'phone': [], 'mobile': [], 'fax': []
    }
    # Normalize label variants
    for line in text.splitlines():
        low = line.lower()
        nums = re.findall(r"[+]?\d[\d()\-.,\s]{5,}\d", line)
        nums = [n.replace('....', '').strip() for n in nums]
        if 'fax' in low:
            phones['fax'].extend(nums)
        elif 'mob' in low or 'cell' in low or 'mobile' in low:
            phones['mobile'].extend(nums)
        elif 'tel' in low or 'phone' in low or 'telephone' in low:
            phones['phone'].extend(nums)
    # Fallback: any bare numbers on their own line
    for line in text.splitlines():
        if re.fullmatch(r"\s*[+]?\d[\d()\-.,\s]{5,}\d\s*", line):
            if line.strip() not in phones['phone']:
                phones['phone'].append(line.strip())
    # Deduplicate
    for k in phones:
        dedup = []
        seen = set()
        for n in phones[k]:
            n_clean = re.sub(r"[^0-9+]+", " ", n).strip()
            if n_clean not in seen:
                seen.add(n_clean)
                dedup.append(n.strip())
        phones[k] = dedup
    return phones


def guess_name(first_line: str) -> str:
    return first_line.strip()


def parse_blocks(raw: str) -> List[Dict[str, str]]:
    records = []
    current_category = ''
    current_region = ''
    current_country = ''
    current_state = ''

    # Pre-split into lines and iterate, creating entries when a likely name is found
    lines = [l.rstrip() for l in raw.splitlines()]

    buffer_lines: List[str] = []
    buffer_name: Optional[str] = None

    def flush_buffer():
        nonlocal buffer_lines, buffer_name
        if buffer_name and buffer_lines:
            block_text = "\n".join(buffer_lines).strip()
            emails = extract_emails(block_text)
            urls = extract_urls(block_text)
            phones = extract_phones(block_text)

            # Address extraction: prefer lines starting with 'Address:' else lines that look like address
            address_lines = []
            for bl in buffer_lines:
                if bl.strip().lower().startswith('address:'):
                    address_lines.append(bl.split(':', 1)[1].strip())
                elif re.match(r"^\d+\s+.+", bl):
                    address_lines.append(bl.strip())
                elif re.match(r".*\b(road|rd\.|street|st\.|ave\.|avenue|lane|close|drive|dr\.|high road|broadway|park|blvd\.|boulevard|way|place)\b.*", bl, flags=re.I):
                    address_lines.append(bl.strip())
            full_address = "; ".join(dict.fromkeys(address_lines))

            # Description: leftover text excluding lines that are obvious labels
            description_lines = []
            for bl in buffer_lines:
                low = bl.lower()
                if (low.startswith('address:') or 'email' in low or 'e-mail' in low or 'tel' in low or 'phone' in low or 'fax' in low
                        or 'website' in low or re.findall(r"https?://", bl) or re.findall(r"\bwww\.", bl)):
                    continue
                # skip direct phone-only lines
                if re.fullmatch(r"\s*[+]?\d[\d()\-.,\s]{5,}\d\s*", bl):
                    continue
                description_lines.append(bl)
            description = " ".join([d.strip() for d in description_lines if d.strip()])

            record = {
                'category_group': current_category,
                'region_or_section': current_region,
                'country': current_country,
                'state_or_province': current_state,
                'name': buffer_name.strip(),
                'contact_name': '',
                'manager': '',
                'address': full_address,
                'city': '',
                'postal_code': '',
                'phones': ", ".join(phones.get('phone', [])),
                'mobiles': ", ".join(phones.get('mobile', [])),
                'fax': ", ".join(phones.get('fax', [])),
                'emails': ", ".join(emails),
                'websites': ", ".join(urls),
                'description': description,
            }

            # Contact/Manager specific
            for bl in buffer_lines:
                m = re.search(r"Contact name\s*:\s*(.+)", bl, flags=re.I)
                if m:
                    record['contact_name'] = m.group(1).strip()
                m2 = re.search(r"Manager\s*:\s*(.+)", bl, flags=re.I)
                if m2:
                    record['manager'] = m2.group(1).strip()

            # Try to pull city/postal from address line patterns
            m_city_post = re.search(r"([A-Za-z .']+),\s*([A-Z]{2,}|[A-Za-z .']+)\s*(\d{3,6}|[A-Z]\d[ A-Z]?\d[ A-Z]?\d)?$", record['address'])
            if m_city_post and not record['city']:
                record['city'] = m_city_post.group(1).strip()
                if m_city_post.group(2):
                    # Could be state or second part of city
                    if re.fullmatch(r"[A-Z]{2}", m_city_post.group(2)):
                        record['state_or_province'] = record['state_or_province'] or m_city_post.group(2)
                    else:
                        # maybe country
                        pass
                if m_city_post.group(3):
                    record['postal_code'] = m_city_post.group(3)

            records.append(record)
        # reset
        buffer_lines = []
        buffer_name = None

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            # blank line -> potential boundary
            continue

        # Update section headers
        hdr = is_section_header(line)
        if hdr:
            # Flush any current entry when moving to a new header
            flush_buffer()
            # Update hierarchy
            if hdr in {'Nigeria', 'South Africa', 'Zimbabwe', 'Poland', 'Fiji Islands'}:
                current_country = hdr
                current_region = hdr
                current_category = 'Distributors/Manufacturers'
                current_state = ''
            elif hdr in {'United Kingdom Wholesalers'}:
                current_country = 'United Kingdom'
                current_region = hdr
                current_category = 'Wholesalers'
                current_state = ''
            elif hdr in {'United States Wholesalers'}:
                current_country = 'United States'
                current_region = hdr
                current_category = 'Wholesalers'
                current_state = ''
            elif hdr in {'Canadian Wholesalers'}:
                current_country = 'Canada'
                current_region = hdr
                current_category = 'Wholesalers'
                current_state = ''
            elif hdr in {'European Wholesalers'}:
                current_country = ''
                current_region = hdr
                current_category = 'Wholesalers'
                current_state = ''
            elif hdr in {'South American Wholesalers'}:
                current_country = ''
                current_region = hdr
                current_category = 'Wholesalers'
                current_state = ''
            elif hdr in {'Australian Wholesalers and Distributors'}:
                current_country = 'Australia'
                current_region = hdr
                current_category = 'Wholesalers/Distributors'
                current_state = ''
            elif hdr in {'British Markets'}:
                current_country = 'United Kingdom'
                current_region = hdr
                current_category = 'Markets'
                current_state = ''
            elif hdr in {'Canadian Markets'}:
                current_country = 'Canada'
                current_region = hdr
                current_category = 'Markets'
                current_state = ''
            elif hdr in {'Arizona', 'California', 'Connecticut', 'Florida', 'Georgia', 'Illinois', 'Kansas', 'Kentucky', 'Massachusetts', 'Mississippi', 'Missouri', 'New Hampshire', 'New Jersey', 'New York', 'North Carolina', 'North Dakota', 'Oklahoma', 'Oregon', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas'}:
                current_country = 'United States'
                current_state = hdr
                current_region = 'United States Markets'
                current_category = 'Markets'
            else:
                current_region = hdr
            continue

        # Detect the very initial section (UK restaurants). After the initial banner, assume UK restaurants until another header appears
        if not current_region:
            current_country = 'United Kingdom'
            current_region = 'Buyers and Distributors of African Foodstuff - UK'
            current_category = 'Restaurants/Buyers'

        # Detect entry start: heuristics - a line with letters and not a label
        is_label = bool(re.match(r"(?i)^(address:|phone|tel|telephone|fax|email|e-mail|website|web site|manager:|contact name:)", line))
        looks_like_name = (not is_label) and (bool(re.search(r"[A-Za-z]", line))) and (len(line) <= 80)

        # If we have an active buffer name and encounter a new likely name, flush
        if buffer_name and looks_like_name:
            # Avoid lines that are clearly continuation of description (sentences ending with period)
            if not line.endswith('.') and not line.endswith(':'):
                flush_buffer()

        # Start a new record name if none set and this looks like a name
        if not buffer_name and looks_like_name:
            buffer_name = guess_name(line)
            continue

        # Otherwise, collect into buffer
        if buffer_name:
            buffer_lines.append(line)

    # Flush at end
    flush_buffer()

    return records


def main():
    records = parse_blocks(RAW_TEXT)
    # Create DataFrame with consistent columns
    columns = [
        'category_group', 'region_or_section', 'country', 'state_or_province', 'name', 'contact_name', 'manager',
        'address', 'city', 'postal_code', 'phones', 'mobiles', 'fax', 'emails', 'websites', 'description'
    ]
    df = pd.DataFrame(records, columns=columns)

    # Write to Excel
    output_path = "/workspace/african_food_contacts.xlsx"
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='contacts')
        # Also include a raw text sheet for traceability
        pd.DataFrame({'raw_text': RAW_TEXT.splitlines()}).to_excel(writer, index=False, sheet_name='raw_text')

    print(f"Wrote {len(df)} records to {output_path}")


if __name__ == '__main__':
    main()