## Author: Luka Mesarić

## Generira "PopulateTableCity.sql" file. Overwrita postojeći,
## ali se slobodno može pokretat ponovno i ponovno jer se generirani
## sql ne smije mijenjat. Tj. ako treba, radimo to preko ovog generatora.
## LONGER i SHORTER su kopirani s weba, ova skripta ih
## samo mergea i konvertira u SQL.
## Tko se hoće žalit da je loše napisano, slobodno može,
## ali ovo dovoljno brzo radi :P


LONGER = """10000	Sljeme	Zagreb	ZAGREBAČKA
10000	Zagreb-dio	Zagreb	ZAGREBAČKA
10010	Buzin	Zagreb-Sloboština	ZAGREBAČKA
10010	Veliko Polje	Zagreb-Sloboština	ZAGREBAČKA
10010	Zagreb-dio	Zagreb-Sloboština	ZAGREBAČKA
10020	Zagreb-dio	Zagreb-Novi Zagreb	ZAGREBAČKA
10020	Strmec	Zagreb-Novi Zagreb	ZAGREBAČKA
10020	Odranski Obrež	Zagreb-Novi Zagreb	ZAGREBAČKA
10020	Odra	Zagreb-Novi Zagreb	ZAGREBAČKA
10020	Mala Mlaka	Zagreb-Novi Zagreb	ZAGREBAČKA
10020	Hrašće Turopoljsko	Zagreb-Novi Zagreb	ZAGREBAČKA
10020	Gornji Čehi	Zagreb-Novi Zagreb	ZAGREBAČKA
10020	Donji Čehi	Zagreb-Novi Zagreb	ZAGREBAČKA
10020	Botinec	Zagreb-Novi Zagreb	ZAGREBAČKA
10040	Zagreb-dio	Zagreb-Dubrava	ZAGREBAČKA
10090	Zagreb-dio	Zagreb-Susedgrad	ZAGREBAČKA
10250	Ježdovec	Lučko	ZAGREBAČKA
10250	Lučko	Lučko	ZAGREBAČKA
10251	Hrvatski Leskovac	Hrvatski Leskovac	ZAGREBAČKA
10251	Demerje	Hrvatski Leskovac	ZAGREBAČKA
10253	Markuševec Turopoljski	Donji Dragonožec	ZAGREBAČKA
10253	Lipnica	Donji Dragonožec	ZAGREBAČKA
10253	Havidić Selo	Donji Dragonožec	ZAGREBAČKA
10253	Gudci	Donji Dragonožec	ZAGREBAČKA
10253	Gornji Trupci	Donji Dragonožec	ZAGREBAČKA
10253	Gornji Dragonožec	Donji Dragonožec	ZAGREBAČKA
10253	Donji Trupci	Donji Dragonožec	ZAGREBAČKA
10253	Donji Dragonožec	Donji Dragonožec	ZAGREBAČKA
10253	Bukovčak	Donji Dragonožec	ZAGREBAČKA
10255	Obrež Stupnički	Gornji Stupnik	ZAGREBAČKA
10255	Gornji Stupnik	Gornji Stupnik	ZAGREBAČKA
10255	Donji Stupnik	Gornji Stupnik	ZAGREBAČKA
10257	Zadvorsko	Brezovica	ZAGREBAČKA
10257	Stavjak	Brezovica	ZAGREBAČKA
10257	Kupinečki Kraljevec	Brezovica	ZAGREBAČKA
10257	Hudi Bitek	Brezovica	ZAGREBAČKA
10257	Graničari	Brezovica	ZAGREBAČKA
10257	Goli Breg	Brezovica	ZAGREBAČKA
10257	Drežnik Brezovički	Brezovica	ZAGREBAČKA
10257	Desprim	Brezovica	ZAGREBAČKA
10257	Brebernica	Brezovica	ZAGREBAČKA
10257	Brezovica	Brezovica	ZAGREBAČKA
10290	Zaprešić	Zaprešić	ZAGREBAČKA
10290	Šibice	Zaprešić	ZAGREBAČKA
10290	Lužnica	Zaprešić	ZAGREBAČKA
10290	Ivanec Bistranski	Zaprešić	ZAGREBAČKA
10291	Zdenci Brdovečki	Prigorje Brdovečko	ZAGREBAČKA
10291	Trstenik Pušćanski	Prigorje Brdovečko	ZAGREBAČKA
10291	Savski Marof	Prigorje Brdovečko	ZAGREBAČKA
10291	Prudnice	Prigorje Brdovečko	ZAGREBAČKA
10291	Prigorje Brdovečko	Prigorje Brdovečko	ZAGREBAČKA
10291	Javorje	Prigorje Brdovečko	ZAGREBAČKA
10291	Drenje Brdovečko	Prigorje Brdovečko	ZAGREBAČKA
10291	Brdovec	Prigorje Brdovečko	ZAGREBAČKA
10292	Vukovo Selo	Šenkovec	ZAGREBAČKA
10292	Šenkovec	Šenkovec	ZAGREBAČKA
10292	Ključ Brdovečki	Šenkovec	ZAGREBAČKA
10292	Harmica	Šenkovec	ZAGREBAČKA
10292	Gornji Laduč	Šenkovec	ZAGREBAČKA
10292	Donji Laduč	Šenkovec	ZAGREBAČKA
10293	Vučilčevo	Dubravica	ZAGREBAČKA
10293	Rozga	Dubravica	ZAGREBAČKA
10293	Prosinec	Dubravica	ZAGREBAČKA
10293	Pologi	Dubravica	ZAGREBAČKA
10293	Lukavec Sutlanski	Dubravica	ZAGREBAČKA
10293	Lugarski Breg	Dubravica	ZAGREBAČKA
10293	Kraj Gornji -sjeverni dio	Dubravica	ZAGREBAČKA
10293	Bela Gorica	Dubravica	ZAGREBAČKA
10293	Bobovec Rozganski	Dubravica	ZAGREBAČKA
10293	Donji Čemehovec	Dubravica	ZAGREBAČKA
10293	Dubravica	Dubravica	ZAGREBAČKA
10293	Kraj Gornji -južni dio	Dubravica	ZAGREBAČKA
10294	Žlebec Pušćanski	Donja Pušća	ZAGREBAČKA
10294	Žlebec Gorički	Donja Pušća	ZAGREBAČKA
10294	Pojatno	Donja Pušća	ZAGREBAČKA
10294	Marija Magdalena	Donja Pušća	ZAGREBAČKA
10294	Hruševec Pušćanski	Donja Pušća	ZAGREBAČKA
10294	Hrebine	Donja Pušća	ZAGREBAČKA
10294	Gornja Pušća	Donja Pušća	ZAGREBAČKA
10294	Dubrava Pušćanska	Donja Pušća	ZAGREBAČKA
10294	Donja Pušća	Donja Pušća	ZAGREBAČKA
10294	Celine Pušćanske	Donja Pušća	ZAGREBAČKA
10294	Bregovljana	Donja Pušća	ZAGREBAČKA
10295	Merenje	Kupljenovo	ZAGREBAČKA
10295	Kupljenovo	Kupljenovo	ZAGREBAČKA
10295	Hruševec Kupljenski	Kupljenovo	ZAGREBAČKA
10296	Žejinci	Luka	ZAGREBAČKA
10296	Vadina	Luka	ZAGREBAČKA
10296	Pluska	Luka	ZAGREBAČKA
10296	Luka	Luka	ZAGREBAČKA
10296	Krajska Vas	Luka	ZAGREBAČKA
10297	Igrišće	Jakovlje	ZAGREBAČKA
10297	Jakovlje	Jakovlje	ZAGREBAČKA
10297	Kraljev Vrh	Jakovlje	ZAGREBAČKA
10298	Poljanica Bistranska	Donja Bistra	ZAGREBAČKA
10298	Oborovo Bistransko	Donja Bistra	ZAGREBAČKA
10298	Novaki Bistranski	Donja Bistra	ZAGREBAČKA
10298	Jablanovec	Donja Bistra	ZAGREBAČKA
10298	Gornja Bistra	Donja Bistra	ZAGREBAČKA
10298	Donja Bistra	Donja Bistra	ZAGREBAČKA
10298	Bukovje Bistransko	Donja Bistra	ZAGREBAČKA
10299	Oplaznik	Marija Gorica	ZAGREBAČKA
10299	Marija Gorica	Marija Gorica	ZAGREBAČKA
10299	Križ Brdovečki	Marija Gorica	ZAGREBAČKA
10299	Kraj Donji	Marija Gorica	ZAGREBAČKA
10299	Hrastina Brdovečka	Marija Gorica	ZAGREBAČKA
10310	Tarno	Ivanić-Grad	ZAGREBAČKA
10310	Opatinec	Ivanić-Grad	ZAGREBAČKA
10310	Lepšić	Ivanić-Grad	ZAGREBAČKA
10310	Jalševec Breški	Ivanić-Grad	ZAGREBAČKA
10310	Ivanić Grad	Ivanić-Grad	ZAGREBAČKA
10310	Donji Šarampov	Ivanić-Grad	ZAGREBAČKA
10311	Zelina Breška	Posavski Bregi	ZAGREBAČKA
10311	Zaklepica	Posavski Bregi	ZAGREBAČKA
10311	Trebovec	Posavski Bregi	ZAGREBAČKA
10311	Topolje	Posavski Bregi	ZAGREBAČKA
10311	Šemovec Breški	Posavski Bregi	ZAGREBAČKA
10311	Posavski Bregi	Posavski Bregi	ZAGREBAČKA
10311	Greda Breška	Posavski Bregi	ZAGREBAČKA
10312	Šćapovec	Kloštar Ivanić	ZAGREBAČKA
10312	Stara Marča	Kloštar Ivanić	ZAGREBAČKA
10312	Sobočani	Kloštar Ivanić	ZAGREBAČKA
10312	Predavec	Kloštar Ivanić	ZAGREBAČKA
10312	Lipovec Lonjski	Kloštar Ivanić	ZAGREBAČKA
10312	Križci	Kloštar Ivanić	ZAGREBAČKA
10312	Kloštar Ivanić	Kloštar Ivanić	ZAGREBAČKA
10312	Gornja Obreška	Kloštar Ivanić	ZAGREBAČKA
10312	Donja Obreška	Kloštar Ivanić	ZAGREBAČKA
10312	Čemernica Lonjska	Kloštar Ivanić	ZAGREBAČKA
10312	Bešlinec	Kloštar Ivanić	ZAGREBAČKA
10313	Šumećani	Graberje Ivaničko	ZAGREBAČKA
10313	Prkos Ivanićki	Graberje Ivaničko	ZAGREBAČKA
10313	Graberje Ivanićko	Graberje Ivaničko	ZAGREBAČKA
10313	Derežani	Graberje Ivaničko	ZAGREBAČKA
10313	Deanovec	Graberje Ivaničko	ZAGREBAČKA
10313	Caginec	Graberje Ivaničko	ZAGREBAČKA
10314	Velika Hrastilnica	Križ	ZAGREBAČKA
10314	Šušnjari	Križ	ZAGREBAČKA
10314	Širinec	Križ	ZAGREBAČKA
10314	Mala Hrastilnica	Križ	ZAGREBAČKA
10314	Križ	Križ	ZAGREBAČKA
10314	Johovec	Križ	ZAGREBAČKA
10314	Gornji Prnjarovec	Križ	ZAGREBAČKA
10314	Donji Prnjarovec	Križ	ZAGREBAČKA
10314	Bunjani	Križ	ZAGREBAČKA
10315	Vezišće	Novoselec	ZAGREBAČKA
10315	Rečica Kriška	Novoselec	ZAGREBAČKA
10315	Razljev	Novoselec	ZAGREBAČKA
10315	Okešinec	Novoselec	ZAGREBAČKA
10315	Obedišće	Novoselec	ZAGREBAČKA
10315	Novoselec	Novoselec	ZAGREBAČKA
10315	Konšćani	Novoselec	ZAGREBAČKA
10316	Lijevi Dubrovčak	Lijevi Dubrovčak	ZAGREBAČKA
10316	Prerovec	Lijevi Dubrovčak	ZAGREBAČKA
10340	Novo Selo	Vrbovec	ZAGREBAČKA
10340	Naselje Stjepana Radića	Vrbovec	ZAGREBAČKA
10340	Martinska Ves	Vrbovec	ZAGREBAČKA
10340	Marenić	Vrbovec	ZAGREBAČKA
10340	Lukovo	Vrbovec	ZAGREBAČKA
10340	Luka	Vrbovec	ZAGREBAČKA
10340	Podolec	Vrbovec	ZAGREBAČKA
10340	Poljana	Vrbovec	ZAGREBAČKA
10340	Poljanski Lug	Vrbovec	ZAGREBAČKA
10340	Prilesje	Vrbovec	ZAGREBAČKA
10340	Savska Cesta	Vrbovec	ZAGREBAČKA
10340	Topolovec	Vrbovec	ZAGREBAČKA
10340	Vrbovec	Vrbovec	ZAGREBAČKA
10340	Vrbovečki Pavlovec	Vrbovec	ZAGREBAČKA
10340	Lovrečka Velika	Vrbovec	ZAGREBAČKA
10340	Lovrečka Varoš	Vrbovec	ZAGREBAČKA
10340	Lazarevac	Vrbovec	ZAGREBAČKA
10340	Banovo	Vrbovec	ZAGREBAČKA
10340	Brčevec	Vrbovec	ZAGREBAČKA
10340	Celine	Vrbovec	ZAGREBAČKA
10340	Cerik	Vrbovec	ZAGREBAČKA
10340	Cerje	Vrbovec	ZAGREBAČKA
10340	Dijaneš	Vrbovec	ZAGREBAČKA
10340	Đivan	Vrbovec	ZAGREBAČKA
10340	Gaj	Vrbovec	ZAGREBAČKA
10340	Kućari	Vrbovec	ZAGREBAČKA
10340	Krkač	Vrbovec	ZAGREBAČKA
10340	Konak	Vrbovec	ZAGREBAČKA
10340	Hruškovica	Vrbovec	ZAGREBAČKA
10340	Graberanec	Vrbovec	ZAGREBAČKA
10340	Gostović	Vrbovec	ZAGREBAČKA
10341	Pirakovec	Lonjica	ZAGREBAČKA
10341	Peskovec	Lonjica	ZAGREBAČKA
10341	Negovec	Lonjica	ZAGREBAČKA
10341	Lonjica	Lonjica	ZAGREBAČKA
10341	Greda	Lonjica	ZAGREBAČKA
10341	Dulepska	Lonjica	ZAGREBAČKA
10342	Novaki	Dubrava	ZAGREBAČKA
10342	Paruževac	Dubrava	ZAGREBAČKA
10342	Pehardovac	Dubrava	ZAGREBAČKA
10342	Podlužan	Dubrava	ZAGREBAČKA
10342	Radulec	Dubrava	ZAGREBAČKA
10342	Svinjarec	Dubrava	ZAGREBAČKA
10342	Zetkan	Dubrava	ZAGREBAČKA
10342	Zgališće	Dubrava	ZAGREBAČKA
10342	Zvekovac	Dubrava	ZAGREBAČKA
10342	Žukovec	Dubrava	ZAGREBAČKA
10342	Mostari	Dubrava	ZAGREBAČKA
10342	Ladina	Dubrava	ZAGREBAČKA
10342	Kostanj	Dubrava	ZAGREBAČKA
10342	Bađinec	Dubrava	ZAGREBAČKA
10342	Brezje	Dubrava	ZAGREBAČKA
10342	Donji Marinkovac	Dubrava	ZAGREBAČKA
10342	Donji Vukašinac	Dubrava	ZAGREBAČKA
10342	Dubrava	Dubrava	ZAGREBAČKA
10342	Dubravski Markovac	Dubrava	ZAGREBAČKA
10342	Gornji Marinkovac	Dubrava	ZAGREBAČKA
10342	Gornji Vukašinac	Dubrava	ZAGREBAČKA
10342	Graberec	Dubrava	ZAGREBAČKA
10342	Koritna	Dubrava	ZAGREBAČKA
10343	Žabnica	Nova Kapela	ZAGREBAČKA
10343	Stari Glog	Nova Kapela	ZAGREBAČKA
10343	Stara Kapela	Nova Kapela	ZAGREBAČKA
10343	Nova Kapela	Nova Kapela	ZAGREBAČKA
10343	Haganj	Nova Kapela	ZAGREBAČKA
10343	Habjanovac	Nova Kapela	ZAGREBAČKA
10343	Fuka	Nova Kapela	ZAGREBAČKA
10344	Zvonik	Farkaševac	ZAGREBAČKA
10344	Prašćevac	Farkaševac	ZAGREBAČKA
10344	Majur	Farkaševac	ZAGREBAČKA
10344	Mački	Farkaševac	ZAGREBAČKA
10344	Kabal	Farkaševac	ZAGREBAČKA
10344	Ivančani	Farkaševac	ZAGREBAČKA
10344	Farkaševac	Farkaševac	ZAGREBAČKA
10344	Donji Markovac	Farkaševac	ZAGREBAČKA
10344	Brezine	Farkaševac	ZAGREBAČKA
10344	Bolč	Farkaševac	ZAGREBAČKA
10345	Potočec	Gradec	ZAGREBAČKA
10345	Remetinec	Gradec	ZAGREBAČKA
10345	Repinec	Gradec	ZAGREBAČKA
10345	Salajci	Gradec	ZAGREBAČKA
10345	Tučenik	Gradec	ZAGREBAČKA
10345	Veliki Brezovec	Gradec	ZAGREBAČKA
10345	Zabrđe	Gradec	ZAGREBAČKA
10345	Pokasin	Gradec	ZAGREBAČKA
10345	Podjales	Gradec	ZAGREBAČKA
10345	Mali Brezovec	Gradec	ZAGREBAČKA
10345	Buzadovac	Gradec	ZAGREBAČKA
10345	Cugovec	Gradec	ZAGREBAČKA
10345	Festinec	Gradec	ZAGREBAČKA
10345	Grabrić	Gradec	ZAGREBAČKA
10345	Gradec	Gradec	ZAGREBAČKA
10345	Gradečki Pavlovec	Gradec	ZAGREBAČKA
10345	Lubena	Gradec	ZAGREBAČKA
10346	Žunci	Preseka	ZAGREBAČKA
10346	Žabnjak	Preseka	ZAGREBAČKA
10346	Vinkovec /dio/	Preseka	ZAGREBAČKA
10346	Strmec	Preseka	ZAGREBAČKA
10346	Slatina	Preseka	ZAGREBAČKA
10346	Preseka	Preseka	ZAGREBAČKA
10346	Pogančec	Preseka	ZAGREBAČKA
10346	Ledina	Preseka	ZAGREBAČKA
10346	Krušljevac	Preseka	ZAGREBAČKA
10346	Kraljev Vrh	Preseka	ZAGREBAČKA
10346	Kamenica	Preseka	ZAGREBAČKA
10346	Gornjaki	Preseka	ZAGREBAČKA
10347	Mlaka	Rakovec	ZAGREBAČKA
10347	Rakovec	Rakovec	ZAGREBAČKA
10347	Samoborec	Rakovec	ZAGREBAČKA
10347	Šelovec	Rakovec	ZAGREBAČKA
10347	Valetić	Rakovec	ZAGREBAČKA
10347	Vrhovec	Rakovec	ZAGREBAČKA
10347	Lipnica	Rakovec	ZAGREBAČKA
10347	Kolenica	Rakovec	ZAGREBAČKA
10347	Hudovo	Rakovec	ZAGREBAČKA
10347	Baničevec	Rakovec	ZAGREBAČKA
10347	Brezani	Rakovec	ZAGREBAČKA
10347	Dropčevec	Rakovec	ZAGREBAČKA
10347	Dvorišće	Rakovec	ZAGREBAČKA
10347	Goli Vrh	Rakovec	ZAGREBAČKA
10347	Hruškovec	Rakovec	ZAGREBAČKA
10360	Šašinovec	Sesvete	ZAGREBAČKA
10360	Šimunčevec	Sesvete	ZAGREBAČKA
10360	Vuger Selo	Sesvete	ZAGREBAČKA
10360	Vugrovec Donji	Sesvete	ZAGREBAČKA
10360	Vugrovec Gornji	Sesvete	ZAGREBAČKA
10360	Žerjavinec	Sesvete	ZAGREBAČKA
10360	Soblinec	Sesvete	ZAGREBAČKA
10360	Sesvete	Sesvete	ZAGREBAČKA
10360	Budenec	Sesvete	ZAGREBAČKA
10360	Dobrodol	Sesvete	ZAGREBAČKA
10360	Goranec	Sesvete	ZAGREBAČKA
10360	Kućanec	Sesvete	ZAGREBAČKA
10360	Markovo Polje	Sesvete	ZAGREBAČKA
10360	Popovec	Sesvete	ZAGREBAČKA
10361	Trstenik Nartski	Sesvete-Kraljevec	ZAGREBAČKA
10361	Svibje	Sesvete-Kraljevec	ZAGREBAČKA
10361	Struga Nartska	Sesvete-Kraljevec	ZAGREBAČKA
10361	Sop	Sesvete-Kraljevec	ZAGREBAČKA
10361	Otok Svibovski	Sesvete-Kraljevec	ZAGREBAČKA
10361	Otok Nartski	Sesvete-Kraljevec	ZAGREBAČKA
10361	Novaki Nartski	Sesvete-Kraljevec	ZAGREBAČKA
10361	Glavničica	Sesvete-Kraljevec	ZAGREBAČKA
10361	Dumovec	Sesvete-Kraljevec	ZAGREBAČKA
10361	Drenčec	Sesvete-Kraljevec	ZAGREBAČKA
10361	Čista Mlaka	Sesvete-Kraljevec	ZAGREBAČKA
10361	Cerje	Sesvete-Kraljevec	ZAGREBAČKA
10362	Planina Donja	Kašina	ZAGREBAČKA
10362	Planina Gornja	Kašina	ZAGREBAČKA
10362	Prekvršje	Kašina	ZAGREBAČKA
10362	Prepuštovec	Kašina	ZAGREBAČKA
10362	Vurnovec	Kašina	ZAGREBAČKA
10362	Paruževina	Kašina	ZAGREBAČKA
10362	Kučilovina	Kašina	ZAGREBAČKA
10362	Kašinska Sopnica	Kašina	ZAGREBAČKA
10362	Kašina	Kašina	ZAGREBAČKA
10362	Gajec	Kašina	ZAGREBAČKA
10362	Đurđekovec	Kašina	ZAGREBAČKA
10362	Blaguša	Kašina	ZAGREBAČKA
10363	Moravče	Belovar	ZAGREBAČKA
10363	Lužan	Belovar	ZAGREBAČKA
10363	Jasenovec	Belovar	ZAGREBAČKA
10363	Glavnica Gornja	Belovar	ZAGREBAČKA
10363	Glavnica Donja	Belovar	ZAGREBAČKA
10363	Belovar	Belovar	ZAGREBAČKA
10363	Adamovec	Belovar	ZAGREBAČKA
10370	Okunšćak	Dugo Selo	ZAGREBAČKA
10370	Obedišće Ježevsko	Dugo Selo	ZAGREBAČKA
10370	Nart Savski	Dugo Selo	ZAGREBAČKA
10370	Mala Ostrna	Dugo Selo	ZAGREBAČKA
10370	Lupoglav	Dugo Selo	ZAGREBAČKA
10370	Lukarišće	Dugo Selo	ZAGREBAČKA
10370	Leprovica	Dugo Selo	ZAGREBAČKA
10370	Prečec	Dugo Selo	ZAGREBAČKA
10370	Prikraj	Dugo Selo	ZAGREBAČKA
10370	Prozorje	Dugo Selo	ZAGREBAČKA
10370	Puhovo	Dugo Selo	ZAGREBAČKA
10370	Rugvica	Dugo Selo	ZAGREBAČKA
10370	Stančić	Dugo Selo	ZAGREBAČKA
10370	Štakorovec	Dugo Selo	ZAGREBAČKA
10370	Tedrovec	Dugo Selo	ZAGREBAČKA
10370	Velika Ostrna	Dugo Selo	ZAGREBAČKA
10370	Kusanovec	Dugo Selo	ZAGREBAČKA
10370	Kozinščak	Dugo Selo	ZAGREBAČKA
10370	Andrilovec	Dugo Selo	ZAGREBAČKA
10370	Božjakovina	Dugo Selo	ZAGREBAČKA
10370	Brckovljani	Dugo Selo	ZAGREBAČKA
10370	Črnec Dugoselski	Dugo Selo	ZAGREBAČKA
10370	Črnec Rugvički	Dugo Selo	ZAGREBAČKA
10370	Donja Greda	Dugo Selo	ZAGREBAČKA
10370	Donje Dvorišće	Dugo Selo	ZAGREBAČKA
10370	Dragošička	Dugo Selo	ZAGREBAČKA
10370	Dugo Selo	Dugo Selo	ZAGREBAČKA
10370	Kopčevec	Dugo Selo	ZAGREBAČKA
10370	Ježevo	Dugo Selo	ZAGREBAČKA
10370	Jalševec Nartski	Dugo Selo	ZAGREBAČKA
10370	Hrebinec	Dugo Selo	ZAGREBAČKA
10370	Gračec	Dugo Selo	ZAGREBAČKA
10370	Gornje Dvorišće	Dugo Selo	ZAGREBAČKA
10370	Gornja Greda	Dugo Selo	ZAGREBAČKA
10372	Prevlaka	Oborovo	ZAGREBAČKA
10372	Preseka Oborovska	Oborovo	ZAGREBAČKA
10372	Prečno	Oborovo	ZAGREBAČKA
10372	Oborovo	Oborovo	ZAGREBAČKA
10372	Novaki Oborovski	Oborovo	ZAGREBAČKA
10373	Hruščica	Ivanja Reka	ZAGREBAČKA
10373	Ivanja Reka	Ivanja Reka	ZAGREBAČKA
10380	Obrež Zelinski	Sveti Ivan Zelina	ZAGREBAČKA
10380	Novo Mjesto	Sveti Ivan Zelina	ZAGREBAČKA
10380	Novakovec Bisački	Sveti Ivan Zelina	ZAGREBAČKA
10380	Marinovec Zelinski	Sveti Ivan Zelina	ZAGREBAČKA
10380	Kreča Ves	Sveti Ivan Zelina	ZAGREBAČKA
10380	Prepolno	Sveti Ivan Zelina	ZAGREBAČKA
10380	Pretoki	Sveti Ivan Zelina	ZAGREBAČKA
10380	Selnica Psarjevačka	Sveti Ivan Zelina	ZAGREBAČKA
10380	Sveti Ivan Zelina	Sveti Ivan Zelina	ZAGREBAČKA
10380	Šalovec	Sveti Ivan Zelina	ZAGREBAČKA
10380	Šulinec	Sveti Ivan Zelina	ZAGREBAČKA
10380	Velika Gora	Sveti Ivan Zelina	ZAGREBAČKA
10380	Žitomir	Sveti Ivan Zelina	ZAGREBAČKA
10380	Kladešćica	Sveti Ivan Zelina	ZAGREBAČKA
10380	Kalinje	Sveti Ivan Zelina	ZAGREBAČKA
10380	Hrastje	Sveti Ivan Zelina	ZAGREBAČKA
10380	Berislavec	Sveti Ivan Zelina	ZAGREBAČKA
10380	Biškupec Zelinski	Sveti Ivan Zelina	ZAGREBAČKA
10380	Blaževdol	Sveti Ivan Zelina	ZAGREBAČKA
10380	Breg Mokrički	Sveti Ivan Zelina	ZAGREBAČKA
10380	Bukevje	Sveti Ivan Zelina	ZAGREBAČKA
10380	Bukovec Zelinski	Sveti Ivan Zelina	ZAGREBAČKA
10380	Črečan	Sveti Ivan Zelina	ZAGREBAČKA
10380	Donja Topličica	Sveti Ivan Zelina	ZAGREBAČKA
10380	Gornje Psarjevo	Sveti Ivan Zelina	ZAGREBAČKA
10380	Gornje Orešje	Sveti Ivan Zelina	ZAGREBAČKA
10380	Gornja Topličica	Sveti Ivan Zelina	ZAGREBAČKA
10380	Donje Psarjevo	Sveti Ivan Zelina	ZAGREBAČKA
10380	Donje Orešje	Sveti Ivan Zelina	ZAGREBAČKA
10381	Zadrkovec	Bedenica	ZAGREBAČKA
10381	Turkovčina	Bedenica	ZAGREBAČKA
10381	Šurdovec	Bedenica	ZAGREBAČKA
10381	Otrčkovec	Bedenica	ZAGREBAČKA
10381	Omamno	Bedenica	ZAGREBAČKA
10381	Bosna	Bedenica	ZAGREBAČKA
10381	Beloslavec	Bedenica	ZAGREBAČKA
10381	Bedenica	Bedenica	ZAGREBAČKA
10382	Hrnjanec	Donja Zelina	ZAGREBAČKA
10382	Križevčec	Donja Zelina	ZAGREBAČKA
10382	Laktec	Donja Zelina	ZAGREBAČKA
10382	Majkovec	Donja Zelina	ZAGREBAČKA
10382	Nespeš	Donja Zelina	ZAGREBAČKA
10382	Paukovec	Donja Zelina	ZAGREBAČKA
10382	Suhodol Zelinski	Donja Zelina	ZAGREBAČKA
10382	Sveta Helena	Donja Zelina	ZAGREBAČKA
10382	Vukovje Zelinsko	Donja Zelina	ZAGREBAČKA
10382	Gornja Drenova	Donja Zelina	ZAGREBAČKA
10382	Goričica	Donja Zelina	ZAGREBAČKA
10382	Goričanec	Donja Zelina	ZAGREBAČKA
10382	Banje Selo	Donja Zelina	ZAGREBAČKA
10382	Blaškovec	Donja Zelina	ZAGREBAČKA
10382	Brezovec Zelinski	Donja Zelina	ZAGREBAČKA
10382	Bukevje	Donja Zelina	ZAGREBAČKA
10382	Bukovec Zelinski	Donja Zelina	ZAGREBAČKA
10382	Bunjak	Donja Zelina	ZAGREBAČKA
10382	Curkovec	Donja Zelina	ZAGREBAČKA
10382	Donja Drenova	Donja Zelina	ZAGREBAČKA
10382	Donja Zelina	Donja Zelina	ZAGREBAČKA
10383	Radoišće	Komin	ZAGREBAČKA
10383	Salnik	Komin	ZAGREBAČKA
10383	Tomaševec	Komin	ZAGREBAČKA
10383	Vinkovec /dio/	Komin	ZAGREBAČKA
10383	Zrinšćina	Komin	ZAGREBAČKA
10383	Polonje Tomaševečko	Komin	ZAGREBAČKA
10383	Polonje	Komin	ZAGREBAČKA
10383	Mokrica Tomaševečka	Komin	ZAGREBAČKA
10383	Komin	Komin	ZAGREBAČKA
10383	Keleminovec	Komin	ZAGREBAČKA
10383	Gornji Vinkovec	Komin	ZAGREBAČKA
10383	Filipovići	Komin	ZAGREBAČKA
10383	Dubovec Bisaški	Komin	ZAGREBAČKA
10408	Velika Mlaka	Velika Mlaka	ZAGREBAČKA
10410	Petina	Velika Gorica	ZAGREBAČKA
10410	Petrovina Turopoljska	Velika Gorica	ZAGREBAČKA
10410	Sasi	Velika Gorica	ZAGREBAČKA
10410	Selnica	Velika Gorica	ZAGREBAČKA
10410	Strmec Bukevski	Velika Gorica	ZAGREBAČKA
10410	Šćitarjevo	Velika Gorica	ZAGREBAČKA
10410	Trnje	Velika Gorica	ZAGREBAČKA
10410	Velika Gorica	Velika Gorica	ZAGREBAČKA
10410	Velika Kosnica	Velika Gorica	ZAGREBAČKA
10410	Zablatje Posavsko	Velika Gorica	ZAGREBAČKA
10410	Okuje	Velika Gorica	ZAGREBAČKA
10410	Obrezina	Velika Gorica	ZAGREBAČKA
10410	Novaki Šćitarjevski	Velika Gorica	ZAGREBAČKA
10410	Bapče	Velika Gorica	ZAGREBAČKA
10410	Črnkovec	Velika Gorica	ZAGREBAČKA
10410	Drenje Šćitarjevsko	Velika Gorica	ZAGREBAČKA
10410	Gradići	Velika Gorica	ZAGREBAČKA
10410	Kobilić	Velika Gorica	ZAGREBAČKA
10410	Lazi Turopoljski	Velika Gorica	ZAGREBAČKA
10410	Lekneno	Velika Gorica	ZAGREBAČKA
10410	Mala Kosnica	Velika Gorica	ZAGREBAČKA
10410	Mičevec	Velika Gorica	ZAGREBAČKA
10410	Mraclin	Velika Gorica	ZAGREBAČKA
10411	Stružec Posavski	Orle	ZAGREBAČKA
10411	Suša	Orle	ZAGREBAČKA
10411	Veleševec	Orle	ZAGREBAČKA
10411	Vrbovo Posavsko	Orle	ZAGREBAČKA
10411	Sop Bukevski	Orle	ZAGREBAČKA
10411	Ruča	Orle	ZAGREBAČKA
10411	Orle	Orle	ZAGREBAČKA
10411	Obed	Orle	ZAGREBAČKA
10411	Drnek	Orle	ZAGREBAČKA
10411	Čret Posavski	Orle	ZAGREBAČKA
10411	Bukevje	Orle	ZAGREBAČKA
10412	Lukavec	Donja Lomnica	ZAGREBAČKA
10412	Gornja Lomnica	Donja Lomnica	ZAGREBAČKA
10412	Donja Lomnica	Donja Lomnica	ZAGREBAČKA
10413	Novo Brdo	Kravarsko	ZAGREBAČKA
10413	Opatija	Kravarsko	ZAGREBAČKA
10413	Podvornica	Kravarsko	ZAGREBAČKA
10413	Pustike	Kravarsko	ZAGREBAČKA
10413	Šiljakovina	Kravarsko	ZAGREBAČKA
10413	Velika Buna	Kravarsko	ZAGREBAČKA
10413	Žitkovčica	Kravarsko	ZAGREBAČKA
10413	Mala Buna	Kravarsko	ZAGREBAČKA
10413	Kravarsko	Kravarsko	ZAGREBAČKA
10413	Barbarići Kravarski	Kravarsko	ZAGREBAČKA
10413	Čakanec	Kravarsko	ZAGREBAČKA
10413	Donji Hruševec	Kravarsko	ZAGREBAČKA
10413	Gladovec Kravarski	Kravarsko	ZAGREBAČKA
10413	Gornji Hruševec	Kravarsko	ZAGREBAČKA
10413	Ključić Brdo	Kravarsko	ZAGREBAČKA
10413	Kozjača	Kravarsko	ZAGREBAČKA
10414	Opatija	Pokupsko	ZAGREBAČKA
10414	Pokupsko	Pokupsko	ZAGREBAČKA
10414	Roženica	Pokupsko	ZAGREBAČKA
10414	Strezojevo	Pokupsko	ZAGREBAČKA
10414	Šestak Brdo	Pokupsko	ZAGREBAČKA
10414	Zgurić Brdo	Pokupsko	ZAGREBAČKA
10414	Lukinić Brdo	Pokupsko	ZAGREBAČKA
10414	Lijevi Štefanki	Pokupsko	ZAGREBAČKA
10414	Lijevi Degoj	Pokupsko	ZAGREBAČKA
10414	Auguštanovec	Pokupsko	ZAGREBAČKA
10414	Brkiševina	Pokupsko	ZAGREBAČKA
10414	Cerje Pokupsko	Pokupsko	ZAGREBAČKA
10414	Cvetnić Brdo	Pokupsko	ZAGREBAČKA
10414	Gladovec Pokupski	Pokupsko	ZAGREBAČKA
10414	Hotnja	Pokupsko	ZAGREBAČKA
10415	Ribnica	Novo Čiče	ZAGREBAČKA
10415	Poljana Čička	Novo Čiče	ZAGREBAČKA
10415	Novo Čiče	Novo Čiče	ZAGREBAČKA
10415	Lazina Čička	Novo Čiče	ZAGREBAČKA
10415	Jagodno	Novo Čiče	ZAGREBAČKA
10415	Donje Podotočje	Novo Čiče	ZAGREBAČKA
10417	Turopolje	Buševec	ZAGREBAČKA
10417	Ogulinac	Buševec	ZAGREBAČKA
10417	Novo Selo Lekeničko	Buševec	ZAGREBAČKA
10417	Buševec	Buševec	ZAGREBAČKA
10418	Vukomerić	Dubranec	ZAGREBAČKA
10418	Prvonožina	Dubranec	ZAGREBAČKA
10418	Petrovec	Dubranec	ZAGREBAČKA
10418	Jerebić	Dubranec	ZAGREBAČKA
10418	Gustelnica	Dubranec	ZAGREBAČKA
10418	Dubranec	Dubranec	ZAGREBAČKA
10418	Cvetković Brdo	Dubranec	ZAGREBAČKA
10418	Cerovski Vrh	Dubranec	ZAGREBAČKA
10419	Vukovina	Vukovina	ZAGREBAČKA
10419	Staro Čiče	Vukovina	ZAGREBAČKA
10419	Rakitovec	Vukovina	ZAGREBAČKA
10419	Kuče	Vukovina	ZAGREBAČKA
10419	Gornje Podotočje	Vukovina	ZAGREBAČKA
10430	Slani Dol	Samobor	ZAGREBAČKA
10430	Savršćak	Samobor	ZAGREBAČKA
10430	Samoborski Otok	Samobor	ZAGREBAČKA
10430	Samobor	Samobor	ZAGREBAČKA
10430	Rude	Samobor	ZAGREBAČKA
10430	Prekrižje Plešivičko	Samobor	ZAGREBAČKA
10430	Molvice	Samobor	ZAGREBAČKA
10430	Slapnica	Samobor	ZAGREBAČKA
10430	Slavagora	Samobor	ZAGREBAČKA
10430	Smerovišće	Samobor	ZAGREBAČKA
10430	Šipački Breg	Samobor	ZAGREBAČKA
10430	Velika Rakovica	Samobor	ZAGREBAČKA
10430	Veliki Lipovec	Samobor	ZAGREBAČKA
10430	Vratnik Samoborski	Samobor	ZAGREBAČKA
10430	Vrbovec Samoborski	Samobor	ZAGREBAČKA
10430	Vrhovčak	Samobor	ZAGREBAČKA
10430	Medsave	Samobor	ZAGREBAČKA
10430	Manja Vas	Samobor	ZAGREBAČKA
10430	Mali Lipovec	Samobor	ZAGREBAČKA
10430	Bobovica	Samobor	ZAGREBAČKA
10430	Braslovje	Samobor	ZAGREBAČKA
10430	Bukovje Podvrško	Samobor	ZAGREBAČKA
10430	Celine Samoborske	Samobor	ZAGREBAČKA
10430	Cerje Samoborsko	Samobor	ZAGREBAČKA
10430	Domaslovec	Samobor	ZAGREBAČKA
10430	Draganje Selo	Samobor	ZAGREBAČKA
10430	Dragonoš	Samobor	ZAGREBAČKA
10430	Dubrava Samoborska	Samobor	ZAGREBAČKA
10430	Mala Rakovica	Samobor	ZAGREBAČKA
10430	Kotari	Samobor	ZAGREBAČKA
10430	Kladje	Samobor	ZAGREBAČKA
10430	Hrastina Samoborska	Samobor	ZAGREBAČKA
10430	Gregurić Breg	Samobor	ZAGREBAČKA
10430	Gradna	Samobor	ZAGREBAČKA
10430	Farkaševec Samoborski	Samobor	ZAGREBAČKA
10431	Svetonedjeljski Breg	Sveta Nedjelja	ZAGREBAČKA
10431	Sveta Nedjelja	Sveta Nedjelja	ZAGREBAČKA
10431	Srebrenjak	Sveta Nedjelja	ZAGREBAČKA
10431	Novaki Samoborski	Sveta Nedjelja	ZAGREBAČKA
10431	Mala Gorica	Sveta Nedjelja	ZAGREBAČKA
10431	Kerestinec	Sveta Nedjelja	ZAGREBAČKA
10431	Jagnjić Dol	Sveta Nedjelja	ZAGREBAČKA
10431	Brezje Samoborsko	Sveta Nedjelja	ZAGREBAČKA
10432	Noršić Selo	Bregana	ZAGREBAČKA
10432	Otruševec	Bregana	ZAGREBAČKA
10432	Podvrh	Bregana	ZAGREBAČKA
10432	Poklek	Bregana	ZAGREBAČKA
10432	Selce Žumberačko	Bregana	ZAGREBAČKA
10432	Stojdraga	Bregana	ZAGREBAČKA
10432	Velika Jazbina	Bregana	ZAGREBAČKA
10432	Višnjevac Podvrški	Bregana	ZAGREBAČKA
10432	Mala Jazbina	Bregana	ZAGREBAČKA
10432	Lug Samoborski	Bregana	ZAGREBAČKA
10432	Kravljak	Bregana	ZAGREBAČKA
10432	Beder	Bregana	ZAGREBAČKA
10432	Bregana	Bregana	ZAGREBAČKA
10432	Breganica	Bregana	ZAGREBAČKA
10432	Grdanjci	Bregana	ZAGREBAČKA
10432	Jarušje	Bregana	ZAGREBAČKA
10432	Javorek	Bregana	ZAGREBAČKA
10432	Klokočevac Samoborski	Bregana	ZAGREBAČKA
10432	Kostanjevec Podvrški	Bregana	ZAGREBAČKA
10434	Strmec Samoborski	Strmec Samoborski	ZAGREBAČKA
10434	Orešje	Strmec Samoborski	ZAGREBAČKA
10435	Sveti Martin pod Okićem	Sveti Martin pod Okićem	ZAGREBAČKA
10435	Podgrađe Podokićko	Sveti Martin pod Okićem	ZAGREBAČKA
10435	Konšćica	Sveti Martin pod Okićem	ZAGREBAČKA
10435	Klake	Sveti Martin pod Okićem	ZAGREBAČKA
10435	Galgovo	Sveti Martin pod Okićem	ZAGREBAČKA
10435	Falašćak	Sveti Martin pod Okićem	ZAGREBAČKA
10435	Drežnik Podokićki	Sveti Martin pod Okićem	ZAGREBAČKA
10435	Dolec Podokićki	Sveti Martin pod Okićem	ZAGREBAČKA
10436	Žitarka	Rakov Potok	ZAGREBAČKA
10436	Rakov Potok	Rakov Potok	ZAGREBAČKA
10436	Kalinovica	Rakov Potok	ZAGREBAČKA
10436	Horvati	Rakov Potok	ZAGREBAČKA
10437	Bestovje	Bestovje	ZAGREBAČKA
10437	Rakitje	Bestovje	ZAGREBAČKA
10450	Novo Selo Okićko	Jastrebarsko	ZAGREBAČKA
10450	Orešje Okićko	Jastrebarsko	ZAGREBAČKA
10450	Pavlovčani	Jastrebarsko	ZAGREBAČKA
10450	Pavučnjak	Jastrebarsko	ZAGREBAČKA
10450	Petkov Breg	Jastrebarsko	ZAGREBAČKA
10450	Novaki Petrovinski	Jastrebarsko	ZAGREBAČKA
10450	Malunje	Jastrebarsko	ZAGREBAČKA
10450	Lokošin Dol	Jastrebarsko	ZAGREBAČKA
10450	Kupinec	Jastrebarsko	ZAGREBAČKA
10450	Kozlikovo	Jastrebarsko	ZAGREBAČKA
10450	Klinča Sela	Jastrebarsko	ZAGREBAČKA
10450	Jurjevčani	Jastrebarsko	ZAGREBAČKA
10450	Petrovina	Jastrebarsko	ZAGREBAČKA
10450	Plešivica	Jastrebarsko	ZAGREBAČKA
10450	Vranov Dol	Jastrebarsko	ZAGREBAČKA
10450	Volavje	Jastrebarsko	ZAGREBAČKA
10450	Vlaškovec	Jastrebarsko	ZAGREBAČKA
10450	Tržić	Jastrebarsko	ZAGREBAČKA
10450	Stankovo	Jastrebarsko	ZAGREBAČKA
10450	Slavetić	Jastrebarsko	ZAGREBAČKA
10450	Repišće	Jastrebarsko	ZAGREBAČKA
10450	Rastoki	Jastrebarsko	ZAGREBAČKA
10450	Prilipje	Jastrebarsko	ZAGREBAČKA
10450	Prhoć	Jastrebarsko	ZAGREBAČKA
10450	Poljanica Okićka	Jastrebarsko	ZAGREBAČKA
10450	Zdihovo	Jastrebarsko	ZAGREBAČKA
10450	Jastrebarsko	Jastrebarsko	ZAGREBAČKA
10450	Beter	Jastrebarsko	ZAGREBAČKA
10450	Donja Reka	Jastrebarsko	ZAGREBAČKA
10450	Donja Purgarija	Jastrebarsko	ZAGREBAČKA
10450	Domagović	Jastrebarsko	ZAGREBAČKA
10450	Črnilovec	Jastrebarsko	ZAGREBAČKA
10450	Čeglje	Jastrebarsko	ZAGREBAČKA
10450	Čabdin	Jastrebarsko	ZAGREBAČKA
10450	Cvetković	Jastrebarsko	ZAGREBAČKA
10450	Crna Mlaka	Jastrebarsko	ZAGREBAČKA
10450	Breznik Plešivički	Jastrebarsko	ZAGREBAČKA
10450	Brezari	Jastrebarsko	ZAGREBAČKA
10450	Brebrovac	Jastrebarsko	ZAGREBAČKA
10450	Donja Zdenčina	Jastrebarsko	ZAGREBAČKA
10450	Donji Desinec	Jastrebarsko	ZAGREBAČKA
10450	Izimje	Jastrebarsko	ZAGREBAČKA
10450	Hrašća	Jastrebarsko	ZAGREBAČKA
10450	Hrastje Plešivičko	Jastrebarsko	ZAGREBAČKA
10450	Guci Draganički	Jastrebarsko	ZAGREBAČKA
10450	Gornji Desinec	Jastrebarsko	ZAGREBAČKA
10450	Gornja Zdenčina	Jastrebarsko	ZAGREBAČKA
10450	Gornja Reka	Jastrebarsko	ZAGREBAČKA
10450	Gornja Purgarija	Jastrebarsko	ZAGREBAČKA
10450	Gonjeva	Jastrebarsko	ZAGREBAČKA
10450	Goljak	Jastrebarsko	ZAGREBAČKA
10450	Goli Vrh	Jastrebarsko	ZAGREBAČKA
10450	Dragovanščak	Jastrebarsko	ZAGREBAČKA
10451	Lučelnica	Pisarovina	ZAGREBAČKA
10451	Pisarovina	Pisarovina	ZAGREBAČKA
10451	Podgorje Jamničko	Pisarovina	ZAGREBAČKA
10451	Selsko Brdo	Pisarovina	ZAGREBAČKA
10451	Topolovec Pisarovinski	Pisarovina	ZAGREBAČKA
10451	Velika Jamnička	Pisarovina	ZAGREBAČKA
10451	Lijevo Sredičko	Pisarovina	ZAGREBAČKA
10451	Jamnica Pisarovinska	Pisarovina	ZAGREBAČKA
10451	Bratina	Pisarovina	ZAGREBAČKA
10451	Bregana Pisarovinska	Pisarovina	ZAGREBAČKA
10451	Donja Kupčina	Pisarovina	ZAGREBAČKA
10451	Dvoranci	Pisarovina	ZAGREBAČKA
10451	Gorica Jamnička	Pisarovina	ZAGREBAČKA
10451	Gradec Pokupski	Pisarovina	ZAGREBAČKA
10453	Miladini	Gorica Svetojanska	ZAGREBAČKA
10453	Paljugi	Gorica Svetojanska	ZAGREBAČKA
10453	Prodin Dol	Gorica Svetojanska	ZAGREBAČKA
10453	Redovje	Gorica Svetojanska	ZAGREBAČKA
10453	Srednjak	Gorica Svetojanska	ZAGREBAČKA
10453	Špigelski Breg	Gorica Svetojanska	ZAGREBAČKA
10453	Tihočaj	Gorica Svetojanska	ZAGREBAČKA
10453	Toplice	Gorica Svetojanska	ZAGREBAČKA
10453	Lanišće	Gorica Svetojanska	ZAGREBAČKA
10453	Kupeć Dol	Gorica Svetojanska	ZAGREBAČKA
10453	Ivančići	Gorica Svetojanska	ZAGREBAČKA
10453	Belčići	Gorica Svetojanska	ZAGREBAČKA
10453	Brezovac Žumberački	Gorica Svetojanska	ZAGREBAČKA
10453	Bukovac Svetojanski	Gorica Svetojanska	ZAGREBAČKA
10453	Celine	Gorica Svetojanska	ZAGREBAČKA
10453	Dolanjski Jarak	Gorica Svetojanska	ZAGREBAČKA
10453	Draga Svetojanska	Gorica Svetojanska	ZAGREBAČKA
10453	Gorica Svetojanska	Gorica Svetojanska	ZAGREBAČKA
10453	Grabarak	Gorica Svetojanska	ZAGREBAČKA
10454	Pesak	Krašić	ZAGREBAČKA
10454	Mirkopolje	Krašić	ZAGREBAČKA
10454	Kurpezova Gorica	Krašić	ZAGREBAČKA
10454	Kučer	Krašić	ZAGREBAČKA
10454	Krupače	Krašić	ZAGREBAČKA
10454	Pribić	Krašić	ZAGREBAČKA
10454	Pribić Crkveni	Krašić	ZAGREBAČKA
10454	Radina Gorica	Krašić	ZAGREBAČKA
10454	Rude Pribićke	Krašić	ZAGREBAČKA
10454	Strmec Pribićki	Krašić	ZAGREBAČKA
10454	Svrževo	Krašić	ZAGREBAČKA
10454	Vranjak Žumberački	Krašić	ZAGREBAČKA
10454	Vukšin Šipak	Krašić	ZAGREBAČKA
10454	Krnežići	Krašić	ZAGREBAČKA
10454	Krašić	Krašić	ZAGREBAČKA
10454	Brezarić	Krašić	ZAGREBAČKA
10454	Brlenić	Krašić	ZAGREBAČKA
10454	Bukovica Prekriška	Krašić	ZAGREBAČKA
10454	Careva Draga	Krašić	ZAGREBAČKA
10454	Dol	Krašić	ZAGREBAČKA
10454	Donje Prekrižje	Krašić	ZAGREBAČKA
10454	Gornja Kupčina	Krašić	ZAGREBAČKA
10454	Gornje Prekrižje	Krašić	ZAGREBAČKA
10454	Kostel Pribićki	Krašić	ZAGREBAČKA
10454	Jezerine	Krašić	ZAGREBAČKA
10454	Hutin	Krašić	ZAGREBAČKA
10454	Hrženik	Krašić	ZAGREBAČKA
10454	Gračac Slavetički	Krašić	ZAGREBAČKA
10455	Prvinci	Kostanjevac	ZAGREBAČKA
10455	Radinovo Brdo	Kostanjevac	ZAGREBAČKA
10455	Stupe	Kostanjevac	ZAGREBAČKA
10455	Tupčina	Kostanjevac	ZAGREBAČKA
10455	Veliki Vrh	Kostanjevac	ZAGREBAČKA
10455	Vlašić Brdo	Kostanjevac	ZAGREBAČKA
10455	Vukovo Brdo	Kostanjevac	ZAGREBAČKA
10455	Žamarija	Kostanjevac	ZAGREBAČKA
10455	Željezno Žumberačko	Kostanjevac	ZAGREBAČKA
10455	Žumberak	Kostanjevac	ZAGREBAČKA
10455	Medven Draga	Kostanjevac	ZAGREBAČKA
10455	Markušići	Kostanjevac	ZAGREBAČKA
10455	Kupčina Žumberačka	Kostanjevac	ZAGREBAČKA
10455	Barovka	Kostanjevac	ZAGREBAČKA
10455	Begovo Brdo Žumberačko	Kostanjevac	ZAGREBAČKA
10455	Čunkova Draga	Kostanjevac	ZAGREBAČKA
10455	Donji Oštrc	Kostanjevac	ZAGREBAČKA
10455	Drašći Vrh	Kostanjevac	ZAGREBAČKA
10455	Gornji Oštrc	Kostanjevac	ZAGREBAČKA
10455	Grgetići	Kostanjevac	ZAGREBAČKA
10455	Jurkovo Selo	Kostanjevac	ZAGREBAČKA
10455	Konjarić Vrh	Kostanjevac	ZAGREBAČKA
10455	Kostanjevac	Kostanjevac	ZAGREBAČKA
10456	Pećno	Kalje	ZAGREBAČKA
10456	Osunja	Kalje	ZAGREBAČKA
10456	Osredek Žumberački	Kalje	ZAGREBAČKA
10456	Novo Selo Žumberačko	Kalje	ZAGREBAČKA
10456	Petričko Selo	Kalje	ZAGREBAČKA
10456	Sječevac	Kalje	ZAGREBAČKA
10456	Staničići Žumberački	Kalje	ZAGREBAČKA
10456	Šimraki	Kalje	ZAGREBAČKA
10456	Tisovac Žumberački	Kalje	ZAGREBAČKA
10456	Tomaševci	Kalje	ZAGREBAČKA
10456	Višći Vrh	Kalje	ZAGREBAČKA
10456	Mrzlo Polje Žumberačko	Kalje	ZAGREBAČKA
10456	Kalje	Kalje	ZAGREBAČKA
10456	Javor	Kalje	ZAGREBAČKA
10456	Bratelji	Kalje	ZAGREBAČKA
10456	Budinjak	Kalje	ZAGREBAČKA
10456	Cerovica	Kalje	ZAGREBAČKA
10456	Čučići	Kalje	ZAGREBAČKA
10456	Dane	Kalje	ZAGREBAČKA
10456	Glušinja	Kalje	ZAGREBAČKA
10456	Golubići	Kalje	ZAGREBAČKA
10456	Gornja Vas	Kalje	ZAGREBAČKA
10456	Grgetići	Kalje	ZAGREBAČKA
10456	Grič	Kalje	ZAGREBAČKA
10456	Hartje	Kalje	ZAGREBAČKA
10457	Visoće	Sošice	ZAGREBAČKA
10457	Stari Grad Žumberački	Sošice	ZAGREBAČKA
10457	Sošice	Sošice	ZAGREBAČKA
10457	Sopote	Sošice	ZAGREBAČKA
10457	Reštovo Žumberačko	Sošice	ZAGREBAČKA
10457	Plavci	Sošice	ZAGREBAČKA
10457	Kordići Žumberački	Sošice	ZAGREBAČKA
10457	Jezernice	Sošice	ZAGREBAČKA
10457	Cernik	Sošice	ZAGREBAČKA
20000	Dubrovnik	Dubrovnik	DUBROVAČKO-NERETVANSKA
20205	Topolo	Topolo	DUBROVAČKO-NERETVANSKA
20205	Štedrica	Topolo	DUBROVAČKO-NERETVANSKA
20205	Stupa	Topolo	DUBROVAČKO-NERETVANSKA
20205	Ošlje	Topolo	DUBROVAČKO-NERETVANSKA
20205	Imotica	Topolo	DUBROVAČKO-NERETVANSKA
20207	Martinovići	Mlini	DUBROVAČKO-NERETVANSKA
20207	Mlini	Mlini	DUBROVAČKO-NERETVANSKA
20207	Petrača	Mlini	DUBROVAČKO-NERETVANSKA
20207	Plat	Mlini	DUBROVAČKO-NERETVANSKA
20207	Soline	Mlini	DUBROVAČKO-NERETVANSKA
20207	Srebreno	Mlini	DUBROVAČKO-NERETVANSKA
20207	Zavrelje	Mlini	DUBROVAČKO-NERETVANSKA
20207	Makoše	Mlini	DUBROVAČKO-NERETVANSKA
20207	Kupari	Mlini	DUBROVAČKO-NERETVANSKA
20207	Grbavac	Mlini	DUBROVAČKO-NERETVANSKA
20207	Bosanka	Mlini	DUBROVAČKO-NERETVANSKA
20207	Brašina	Mlini	DUBROVAČKO-NERETVANSKA
20207	Brgat Donji	Mlini	DUBROVAČKO-NERETVANSKA
20207	Brgat Gornji	Mlini	DUBROVAČKO-NERETVANSKA
20207	Buići	Mlini	DUBROVAČKO-NERETVANSKA
20207	Čelopeci	Mlini	DUBROVAČKO-NERETVANSKA
20207	Čibača	Mlini	DUBROVAČKO-NERETVANSKA
20210	Zvekovica	Cavtat	DUBROVAČKO-NERETVANSKA
20210	Uskoplje	Cavtat	DUBROVAČKO-NERETVANSKA
20210	Šilješki	Cavtat	DUBROVAČKO-NERETVANSKA
20210	Stravča	Cavtat	DUBROVAČKO-NERETVANSKA
20210	Jasenice	Cavtat	DUBROVAČKO-NERETVANSKA
20210	Duba Konavoska	Cavtat	DUBROVAČKO-NERETVANSKA
20210	Cavtat	Cavtat	DUBROVAČKO-NERETVANSKA
20210	Brotnice	Cavtat	DUBROVAČKO-NERETVANSKA
20213	Močići	Čilipi	DUBROVAČKO-NERETVANSKA
20213	Komaji	Čilipi	DUBROVAČKO-NERETVANSKA
20213	Gabrili	Čilipi	DUBROVAČKO-NERETVANSKA
20213	Čilipi	Čilipi	DUBROVAČKO-NERETVANSKA
20215	Radovčići	Gruda	DUBROVAČKO-NERETVANSKA
20215	Popovići	Gruda	DUBROVAČKO-NERETVANSKA
20215	Poljice	Gruda	DUBROVAČKO-NERETVANSKA
20215	Gruda	Gruda	DUBROVAČKO-NERETVANSKA
20216	Dubravka	Dubravka	DUBROVAČKO-NERETVANSKA
20216	Dunave	Dubravka	DUBROVAČKO-NERETVANSKA
20216	Vodovađa	Dubravka	DUBROVAČKO-NERETVANSKA
20216	Zastolje	Dubravka	DUBROVAČKO-NERETVANSKA
20217	Pridvorje	Pridvorje	DUBROVAČKO-NERETVANSKA
20217	Mihanići	Pridvorje	DUBROVAČKO-NERETVANSKA
20217	Ljuta	Pridvorje	DUBROVAČKO-NERETVANSKA
20217	Lovorno	Pridvorje	DUBROVAČKO-NERETVANSKA
20217	Kuna Konavoska	Pridvorje	DUBROVAČKO-NERETVANSKA
20217	Drvenik	Pridvorje	DUBROVAČKO-NERETVANSKA
20218	Vitaljina	Pločice	DUBROVAČKO-NERETVANSKA
20218	Pločice	Pločice	DUBROVAČKO-NERETVANSKA
20218	Palje Brdo	Pločice	DUBROVAČKO-NERETVANSKA
20218	Molunat	Pločice	DUBROVAČKO-NERETVANSKA
20218	Mikulići	Pločice	DUBROVAČKO-NERETVANSKA
20218	Đurinići	Pločice	DUBROVAČKO-NERETVANSKA
20221	Koločep	Koločep	DUBROVAČKO-NERETVANSKA
20222	Lopud	Lopud	DUBROVAČKO-NERETVANSKA
20223	Suđurađ	Šipanjska Luka	DUBROVAČKO-NERETVANSKA
20223	Šipanjska Luka	Šipanjska Luka	DUBROVAČKO-NERETVANSKA
20224	Saplunara	Maranovići	DUBROVAČKO-NERETVANSKA
20224	Prožurska Luka	Maranovići	DUBROVAČKO-NERETVANSKA
20224	Prožura	Maranovići	DUBROVAČKO-NERETVANSKA
20224	Okuklje	Maranovići	DUBROVAČKO-NERETVANSKA
20224	Maranovići	Maranovići	DUBROVAČKO-NERETVANSKA
20224	Korita	Maranovići	DUBROVAČKO-NERETVANSKA
20225	Sobra	Babino Polje	DUBROVAČKO-NERETVANSKA
20225	Ropa	Babino Polje	DUBROVAČKO-NERETVANSKA
20225	Kozarica	Babino Polje	DUBROVAČKO-NERETVANSKA
20225	Blato	Babino Polje	DUBROVAČKO-NERETVANSKA
20225	Babino Polje	Babino Polje	DUBROVAČKO-NERETVANSKA
20226	Velika Loza	Goveđari	DUBROVAČKO-NERETVANSKA
20226	Tatinica	Goveđari	DUBROVAČKO-NERETVANSKA
20226	Soline	Goveđari	DUBROVAČKO-NERETVANSKA
20226	Pristanište	Goveđari	DUBROVAČKO-NERETVANSKA
20226	Pomena	Goveđari	DUBROVAČKO-NERETVANSKA
20226	Polače	Goveđari	DUBROVAČKO-NERETVANSKA
20226	Njivice	Goveđari	DUBROVAČKO-NERETVANSKA
20226	Goveđari	Goveđari	DUBROVAČKO-NERETVANSKA
20226	Babine Kuće	Goveđari	DUBROVAČKO-NERETVANSKA
20230	Zabrđe	Ston	DUBROVAČKO-NERETVANSKA
20230	Ston	Ston	DUBROVAČKO-NERETVANSKA
20230	Sparagovići	Ston	DUBROVAČKO-NERETVANSKA
20230	Metohija	Ston	DUBROVAČKO-NERETVANSKA
20230	Mali Ston	Ston	DUBROVAČKO-NERETVANSKA
20230	Luka	Ston	DUBROVAČKO-NERETVANSKA
20230	Hodilje	Ston	DUBROVAČKO-NERETVANSKA
20230	Duba Stonska	Ston	DUBROVAČKO-NERETVANSKA
20230	Česvinica	Ston	DUBROVAČKO-NERETVANSKA
20230	Broce	Ston	DUBROVAČKO-NERETVANSKA
20230	Boljenovići	Ston	DUBROVAČKO-NERETVANSKA
20231	Zaton Doli	Doli	DUBROVAČKO-NERETVANSKA
20231	Visočani	Doli	DUBROVAČKO-NERETVANSKA
20231	Trnovica	Doli	DUBROVAČKO-NERETVANSKA
20231	Točionik	Doli	DUBROVAČKO-NERETVANSKA
20231	Smokovljani	Doli	DUBROVAČKO-NERETVANSKA
20231	Podimoć	Doli	DUBROVAČKO-NERETVANSKA
20231	Lisac	Doli	DUBROVAČKO-NERETVANSKA
20231	Doli	Doli	DUBROVAČKO-NERETVANSKA
20231	Čepikuće	Doli	DUBROVAČKO-NERETVANSKA
20232	Trnova	Slano	DUBROVAČKO-NERETVANSKA
20232	Slano	Slano	DUBROVAČKO-NERETVANSKA
20232	Podgora	Slano	DUBROVAČKO-NERETVANSKA
20232	Mravnica	Slano	DUBROVAČKO-NERETVANSKA
20232	Majkovi	Slano	DUBROVAČKO-NERETVANSKA
20232	Banići	Slano	DUBROVAČKO-NERETVANSKA
20233	Trsteno	Trsteno	DUBROVAČKO-NERETVANSKA
20234	Orašac	Orašac	DUBROVAČKO-NERETVANSKA
20234	Mrčevo	Orašac	DUBROVAČKO-NERETVANSKA
20234	Mravinjac	Orašac	DUBROVAČKO-NERETVANSKA
20234	Ljubač	Orašac	DUBROVAČKO-NERETVANSKA
20234	Kliševo	Orašac	DUBROVAČKO-NERETVANSKA
20234	Gromača	Orašac	DUBROVAČKO-NERETVANSKA
20234	Dubravica	Orašac	DUBROVAČKO-NERETVANSKA
20234	Brsećine	Orašac	DUBROVAČKO-NERETVANSKA
20235	Zaton	Zaton Veliki	DUBROVAČKO-NERETVANSKA
20236	Petrovo Selo	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Pobrežje	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Prijevor	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Rožat	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Sustjepan	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Šumet	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Osojnik	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Nova Mokošica	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Mokošica	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Komolac	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Knežica	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Gornje Obuljeno	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Donje Obuljeno	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Čajkovići	Mokošica	DUBROVAČKO-NERETVANSKA
20236	Čajkovica	Mokošica	DUBROVAČKO-NERETVANSKA
20240	Trpanj	Trpanj	DUBROVAČKO-NERETVANSKA
20240	Gornja Vrućica	Trpanj	DUBROVAČKO-NERETVANSKA
20240	Duba Pelješka	Trpanj	DUBROVAČKO-NERETVANSKA
20240	Donja Vrućica	Trpanj	DUBROVAČKO-NERETVANSKA
20242	Donja Banda	Oskorušno	DUBROVAČKO-NERETVANSKA
20242	Oskorušno	Oskorušno	DUBROVAČKO-NERETVANSKA
20243	Kuna Pelješka	Kuna	DUBROVAČKO-NERETVANSKA
20243	Pijavičino	Kuna	DUBROVAČKO-NERETVANSKA
20244	Potomje	Potomje	DUBROVAČKO-NERETVANSKA
20244	Podobuče	Potomje	DUBROVAČKO-NERETVANSKA
20245	Trstenik	Trstenik	DUBROVAČKO-NERETVANSKA
20246	Sreser	Janjina	DUBROVAČKO-NERETVANSKA
20246	Popova Luka	Janjina	DUBROVAČKO-NERETVANSKA
20246	Osobljava	Janjina	DUBROVAČKO-NERETVANSKA
20246	Janjina	Janjina	DUBROVAČKO-NERETVANSKA
20246	Drače	Janjina	DUBROVAČKO-NERETVANSKA
20247	Žuljana	Žuljana	DUBROVAČKO-NERETVANSKA
20248	Tomislavovac	Putniković	DUBROVAČKO-NERETVANSKA
20248	Putniković	Putniković	DUBROVAČKO-NERETVANSKA
20248	Dubrava	Putniković	DUBROVAČKO-NERETVANSKA
20248	Dančanje	Putniković	DUBROVAČKO-NERETVANSKA
20248	Brijesta	Putniković	DUBROVAČKO-NERETVANSKA
20250	Orebić	Orebić	DUBROVAČKO-NERETVANSKA
20250	Podgorje	Orebić	DUBROVAČKO-NERETVANSKA
20250	Stanković	Orebić	DUBROVAČKO-NERETVANSKA
20260	Korčula	Korčula	DUBROVAČKO-NERETVANSKA
20263	Lumbarda	Lumbarda	DUBROVAČKO-NERETVANSKA
20264	Račišće	Račišće	DUBROVAČKO-NERETVANSKA
20267	Kućište	Kućište	DUBROVAČKO-NERETVANSKA
20267	Nakovanj	Kućište	DUBROVAČKO-NERETVANSKA
20267	Viganj	Kućište	DUBROVAČKO-NERETVANSKA
20269	Lovište	Lovište	DUBROVAČKO-NERETVANSKA
20270	Potirna	Vela Luka	DUBROVAČKO-NERETVANSKA
20270	Vela Luka	Vela Luka	DUBROVAČKO-NERETVANSKA
20271	Blato	Blato	DUBROVAČKO-NERETVANSKA
20272	Smokvica	Smokvica	DUBROVAČKO-NERETVANSKA
20273	Čara	Čara	DUBROVAČKO-NERETVANSKA
20274	Pupnat	Pupnat	DUBROVAČKO-NERETVANSKA
20275	Žrnovo	Žrnovo	DUBROVAČKO-NERETVANSKA
20278	Pozla Gora	Nova Sela	DUBROVAČKO-NERETVANSKA
20278	Nova Sela	Nova Sela	DUBROVAČKO-NERETVANSKA
20278	Mali Prolog	Nova Sela	DUBROVAČKO-NERETVANSKA
20278	Kobiljača	Nova Sela	DUBROVAČKO-NERETVANSKA
20278	Dubrave	Nova Sela	DUBROVAČKO-NERETVANSKA
20278	Brečići	Nova Sela	DUBROVAČKO-NERETVANSKA
20278	Borovci	Nova Sela	DUBROVAČKO-NERETVANSKA
20290	Uble	Lastovo	DUBROVAČKO-NERETVANSKA
20290	Zaklopatica	Lastovo	DUBROVAČKO-NERETVANSKA
20290	Sušac	Lastovo	DUBROVAČKO-NERETVANSKA
20290	Skrivena Luka	Lastovo	DUBROVAČKO-NERETVANSKA
20290	Pasadur	Lastovo	DUBROVAČKO-NERETVANSKA
20290	Lastovo	Lastovo	DUBROVAČKO-NERETVANSKA
20290	Glavat	Lastovo	DUBROVAČKO-NERETVANSKA
20340	Baćina	Ploče	DUBROVAČKO-NERETVANSKA
20340	Peračko Blato	Ploče	DUBROVAČKO-NERETVANSKA
20340	Plina Jezero	Ploče	DUBROVAČKO-NERETVANSKA
20340	Ploče	Ploče	DUBROVAČKO-NERETVANSKA
20341	Podrujnica	Kula Norinska	DUBROVAČKO-NERETVANSKA
20341	Momići	Kula Norinska	DUBROVAČKO-NERETVANSKA
20341	Kula Norinska	Kula Norinska	DUBROVAČKO-NERETVANSKA
20341	Krvavac I	Kula Norinska	DUBROVAČKO-NERETVANSKA
20342	Otrić Seoci	Otrić Seoci	DUBROVAČKO-NERETVANSKA
20343	Rogotin	Rogotin	DUBROVAČKO-NERETVANSKA
20343	Šarić Struga	Rogotin	DUBROVAČKO-NERETVANSKA
20344	Komin	Komin (Dalmacija)	DUBROVAČKO-NERETVANSKA
20344	Desne	Komin (Dalmacija)	DUBROVAČKO-NERETVANSKA
20344	Banja	Komin (Dalmacija)	DUBROVAČKO-NERETVANSKA
20345	Staševica	Staševica	DUBROVAČKO-NERETVANSKA
20350	Vidonje	Metković	DUBROVAČKO-NERETVANSKA
20350	Metković	Metković	DUBROVAČKO-NERETVANSKA
20350	Krvavac II	Metković	DUBROVAČKO-NERETVANSKA
20350	Glušci	Metković	DUBROVAČKO-NERETVANSKA
20350	Dubravica	Metković	DUBROVAČKO-NERETVANSKA
20352	Prud	Vid	DUBROVAČKO-NERETVANSKA
20352	Vid	Vid	DUBROVAČKO-NERETVANSKA
20353	Mlinište	Mlinište	DUBROVAČKO-NERETVANSKA
20353	Mislina	Mlinište	DUBROVAČKO-NERETVANSKA
20353	Dobranje	Mlinište	DUBROVAČKO-NERETVANSKA
20353	Bijeli Vir	Mlinište	DUBROVAČKO-NERETVANSKA
20353	Badžula	Mlinište	DUBROVAČKO-NERETVANSKA
20355	Buk Vlaka	Opuzen	DUBROVAČKO-NERETVANSKA
20355	Opuzen	Opuzen	DUBROVAČKO-NERETVANSKA
20355	Podgradina	Opuzen	DUBROVAČKO-NERETVANSKA
20355	Vlaka/lij.ob.Male Neretve/	Opuzen	DUBROVAČKO-NERETVANSKA
20356	Slivno Ravno	Klek	DUBROVAČKO-NERETVANSKA
20356	Raba	Klek	DUBROVAČKO-NERETVANSKA
20356	Komarna	Klek	DUBROVAČKO-NERETVANSKA
20356	Klek	Klek	DUBROVAČKO-NERETVANSKA
20356	Duboka	Klek	DUBROVAČKO-NERETVANSKA
20357	Tuštevac	Blace	DUBROVAČKO-NERETVANSKA
20357	Trn	Blace	DUBROVAČKO-NERETVANSKA
20357	Otok Duba	Blace	DUBROVAČKO-NERETVANSKA
20357	Mihalj	Blace	DUBROVAČKO-NERETVANSKA
20357	Lovorje	Blace	DUBROVAČKO-NERETVANSKA
20357	Blace	Blace	DUBROVAČKO-NERETVANSKA
21000	Kamen	Split	SPLITSKO-DALMATINSKA
21000	Split	Split	SPLITSKO-DALMATINSKA
21201	Trolokve	Prgomet	SPLITSKO-DALMATINSKA
21201	Prgomet	Prgomet	SPLITSKO-DALMATINSKA
21201	Prapatnica	Prgomet	SPLITSKO-DALMATINSKA
21201	Ljubitovica	Prgomet	SPLITSKO-DALMATINSKA
21201	Labin	Prgomet	SPLITSKO-DALMATINSKA
21202	Vučevica	Lećevica	SPLITSKO-DALMATINSKA
21202	Radošić	Lećevica	SPLITSKO-DALMATINSKA
21202	Nisko	Lećevica	SPLITSKO-DALMATINSKA
21202	Lećevica	Lećevica	SPLITSKO-DALMATINSKA
21202	Korušce	Lećevica	SPLITSKO-DALMATINSKA
21202	Kladnjice	Lećevica	SPLITSKO-DALMATINSKA
21202	Dugobabe	Lećevica	SPLITSKO-DALMATINSKA
21202	Divojevići	Lećevica	SPLITSKO-DALMATINSKA
21202	Brštanovo	Lećevica	SPLITSKO-DALMATINSKA
21203	Ramljane	Donji Muć	SPLITSKO-DALMATINSKA
21203	Gornji Muć	Donji Muć	SPLITSKO-DALMATINSKA
21203	Gornje Postinje	Donji Muć	SPLITSKO-DALMATINSKA
21203	Donji Muć	Donji Muć	SPLITSKO-DALMATINSKA
21203	Donje Pustinje	Donji Muć	SPLITSKO-DALMATINSKA
21203	Bračević	Donji Muć	SPLITSKO-DALMATINSKA
21204	Dugopolje	Dugopolje	SPLITSKO-DALMATINSKA
21204	Kotlenice	Dugopolje	SPLITSKO-DALMATINSKA
21205	Srijane	Donji Dolac	SPLITSKO-DALMATINSKA
21205	Putišići	Donji Dolac	SPLITSKO-DALMATINSKA
21205	Gornji Dolac	Donji Dolac	SPLITSKO-DALMATINSKA
21205	Donji Dolac	Donji Dolac	SPLITSKO-DALMATINSKA
21206	Velika Milešina	Donje Ogorje	SPLITSKO-DALMATINSKA
21206	Radunić	Donje Ogorje	SPLITSKO-DALMATINSKA
21206	Pribude	Donje Ogorje	SPLITSKO-DALMATINSKA
21206	Mala Milešina	Donje Ogorje	SPLITSKO-DALMATINSKA
21206	Gornje Ogorje	Donje Ogorje	SPLITSKO-DALMATINSKA
21206	Donje Ogorje	Donje Ogorje	SPLITSKO-DALMATINSKA
21207	Kostanje	Kostanje	SPLITSKO-DALMATINSKA
21207	Podgrađe	Kostanje	SPLITSKO-DALMATINSKA
21208	Kučiće	Kučiće	SPLITSKO-DALMATINSKA
21208	Podašpilje	Kučiće	SPLITSKO-DALMATINSKA
21208	Svinišće	Kučiće	SPLITSKO-DALMATINSKA
21209	Mravince	Mravince	SPLITSKO-DALMATINSKA
21209	Kučine	Mravince	SPLITSKO-DALMATINSKA
21210	Blaca	Solin	SPLITSKO-DALMATINSKA
21210	Vranjic	Solin	SPLITSKO-DALMATINSKA
21210	Solin	Solin	SPLITSKO-DALMATINSKA
21212	Kaštel Sućurac	Kaštel Sućurac	SPLITSKO-DALMATINSKA
21213	Kaštel Gomilica	Kaštel Gomilica	SPLITSKO-DALMATINSKA
21214	Kaštel Kambelovac	Kaštel Kambelovac	SPLITSKO-DALMATINSKA
21215	Kaštel Lukšić	Kaštel Lukšić	SPLITSKO-DALMATINSKA
21216	Kaštel Štafilić	Kaštel Stari	SPLITSKO-DALMATINSKA
21216	Kaštel Stari	Kaštel Stari	SPLITSKO-DALMATINSKA
21216	Kaštel Novi	Kaštel Stari	SPLITSKO-DALMATINSKA
21218	Seget Donji	Seget Donji	SPLITSKO-DALMATINSKA
21218	Seget Gornji	Seget Donji	SPLITSKO-DALMATINSKA
21220	Žedno	Trogir	SPLITSKO-DALMATINSKA
21220	Trogir	Trogir	SPLITSKO-DALMATINSKA
21220	Seget Vranjica	Trogir	SPLITSKO-DALMATINSKA
21220	Plano	Trogir	SPLITSKO-DALMATINSKA
21220	Divulje	Trogir	SPLITSKO-DALMATINSKA
21222	Vrsine	Marina	SPLITSKO-DALMATINSKA
21222	Svinca	Marina	SPLITSKO-DALMATINSKA
21222	Sevid	Marina	SPLITSKO-DALMATINSKA
21222	Pozorac	Marina	SPLITSKO-DALMATINSKA
21222	Poljica	Marina	SPLITSKO-DALMATINSKA
21222	Najevi	Marina	SPLITSKO-DALMATINSKA
21222	Marina	Marina	SPLITSKO-DALMATINSKA
21222	Gustirna	Marina	SPLITSKO-DALMATINSKA
21222	Dograde	Marina	SPLITSKO-DALMATINSKA
21223	Okrug Gornji	Okrug Gornji	SPLITSKO-DALMATINSKA
21223	Okrug Donji	Okrug Gornji	SPLITSKO-DALMATINSKA
21224	Arbanija	Slatine	SPLITSKO-DALMATINSKA
21224	Slatine	Slatine	SPLITSKO-DALMATINSKA
21225	Drvenik Mali	Drvenik Veliki	SPLITSKO-DALMATINSKA
21225	Drvenik Veliki	Drvenik Veliki	SPLITSKO-DALMATINSKA
21226	Vinišće	Vinišće	SPLITSKO-DALMATINSKA
21227	Bogdanovići	Primorski Dolac	SPLITSKO-DALMATINSKA
21227	Primorski Dolac	Primorski Dolac	SPLITSKO-DALMATINSKA
21228	Vinovac	Blizna Donja	SPLITSKO-DALMATINSKA
21228	Rastovac	Blizna Donja	SPLITSKO-DALMATINSKA
21228	Mitlo	Blizna Donja	SPLITSKO-DALMATINSKA
21228	Bristivica	Blizna Donja	SPLITSKO-DALMATINSKA
21228	Blizna Gornja	Blizna Donja	SPLITSKO-DALMATINSKA
21228	Blizna Donja	Blizna Donja	SPLITSKO-DALMATINSKA
21229	Crivac	Crivac	SPLITSKO-DALMATINSKA
21230	Turjaci	Sinj	SPLITSKO-DALMATINSKA
21230	Suhač	Sinj	SPLITSKO-DALMATINSKA
21230	Sinj	Sinj	SPLITSKO-DALMATINSKA
21230	Radošić	Sinj	SPLITSKO-DALMATINSKA
21230	Lučane	Sinj	SPLITSKO-DALMATINSKA
21230	Karakašica	Sinj	SPLITSKO-DALMATINSKA
21230	Jasensko	Sinj	SPLITSKO-DALMATINSKA
21230	Glavice	Sinj	SPLITSKO-DALMATINSKA
21230	Čitluk	Sinj	SPLITSKO-DALMATINSKA
21230	Brnaze	Sinj	SPLITSKO-DALMATINSKA
21231	Veliki Bročanac	Klis	SPLITSKO-DALMATINSKA
21231	Prugovo	Klis	SPLITSKO-DALMATINSKA
21231	Koprivno	Klis	SPLITSKO-DALMATINSKA
21231	Konjsko	Klis	SPLITSKO-DALMATINSKA
21231	Klis	Klis	SPLITSKO-DALMATINSKA
21232	Sušci	Dicmo	SPLITSKO-DALMATINSKA
21232	Sičane	Dicmo	SPLITSKO-DALMATINSKA
21232	Prisoje	Dicmo	SPLITSKO-DALMATINSKA
21232	Osoje	Dicmo	SPLITSKO-DALMATINSKA
21232	Liska	Dicmo	SPLITSKO-DALMATINSKA
21232	Krušvar	Dicmo	SPLITSKO-DALMATINSKA
21232	Kraj	Dicmo	SPLITSKO-DALMATINSKA
21232	Ercegovci	Dicmo	SPLITSKO-DALMATINSKA
21232	Dicmo	Dicmo	SPLITSKO-DALMATINSKA
21232	Bisko	Dicmo	SPLITSKO-DALMATINSKA
21233	Rumin	Hrvace	SPLITSKO-DALMATINSKA
21233	Satrić	Hrvace	SPLITSKO-DALMATINSKA
21233	Vučipolje	Hrvace	SPLITSKO-DALMATINSKA
21233	Zasiok	Hrvace	SPLITSKO-DALMATINSKA
21233	Zelovo	Hrvace	SPLITSKO-DALMATINSKA
21233	Potravlje	Hrvace	SPLITSKO-DALMATINSKA
21233	Maljkovo	Hrvace	SPLITSKO-DALMATINSKA
21233	Laktac	Hrvace	SPLITSKO-DALMATINSKA
21233	Hrvace	Hrvace	SPLITSKO-DALMATINSKA
21233	Gornji Bitelić	Hrvace	SPLITSKO-DALMATINSKA
21233	Donji Bitelić	Hrvace	SPLITSKO-DALMATINSKA
21233	Dabar	Hrvace	SPLITSKO-DALMATINSKA
21235	Otišić	Otišić	SPLITSKO-DALMATINSKA
21235	Maovice	Otišić	SPLITSKO-DALMATINSKA
21236	Vrlika	Vrlika	SPLITSKO-DALMATINSKA
21236	Vinalić	Vrlika	SPLITSKO-DALMATINSKA
21236	Podosoje	Vrlika	SPLITSKO-DALMATINSKA
21236	Otišić	Vrlika	SPLITSKO-DALMATINSKA
21236	Maovice	Vrlika	SPLITSKO-DALMATINSKA
21236	Kosore	Vrlika	SPLITSKO-DALMATINSKA
21236	Koljane	Vrlika	SPLITSKO-DALMATINSKA
21236	Ježević	Vrlika	SPLITSKO-DALMATINSKA
21236	Garjak	Vrlika	SPLITSKO-DALMATINSKA
21238	Ovrlja	Otok (Dalmacija)	SPLITSKO-DALMATINSKA
21238	Otok	Otok (Dalmacija)	SPLITSKO-DALMATINSKA
21238	Korita	Otok (Dalmacija)	SPLITSKO-DALMATINSKA
21240	Vojnić Sinjski	Trilj	SPLITSKO-DALMATINSKA
21240	Velić	Trilj	SPLITSKO-DALMATINSKA
21240	Vedrine	Trilj	SPLITSKO-DALMATINSKA
21240	Trilj	Trilj	SPLITSKO-DALMATINSKA
21240	Strmendolac	Trilj	SPLITSKO-DALMATINSKA
21240	Košute	Trilj	SPLITSKO-DALMATINSKA
21240	Jabuka	Trilj	SPLITSKO-DALMATINSKA
21240	Gardun	Trilj	SPLITSKO-DALMATINSKA
21240	Čaporice	Trilj	SPLITSKO-DALMATINSKA
21240	Čačvina	Trilj	SPLITSKO-DALMATINSKA
21241	Obrovac Sinjski	Obrovac Sinjski	SPLITSKO-DALMATINSKA
21241	Gljev	Obrovac Sinjski	SPLITSKO-DALMATINSKA
21241	Gala	Obrovac Sinjski	SPLITSKO-DALMATINSKA
21241	Bajagić	Obrovac Sinjski	SPLITSKO-DALMATINSKA
21242	Vrabač	Grab	SPLITSKO-DALMATINSKA
21242	Udovičić	Grab	SPLITSKO-DALMATINSKA
21242	Ruda	Grab	SPLITSKO-DALMATINSKA
21242	Podi	Grab	SPLITSKO-DALMATINSKA
21242	Krivodol	Grab	SPLITSKO-DALMATINSKA
21242	Grab	Grab	SPLITSKO-DALMATINSKA
21243	Vinine	Ugljane	SPLITSKO-DALMATINSKA
21243	Ugljane	Ugljane	SPLITSKO-DALMATINSKA
21243	Nova Sela	Ugljane	SPLITSKO-DALMATINSKA
21243	Budimiri	Ugljane	SPLITSKO-DALMATINSKA
21244	Biorine	Cista Velika	SPLITSKO-DALMATINSKA
21244	Dobranje	Cista Velika	SPLITSKO-DALMATINSKA
21244	Cista Velika	Cista Velika	SPLITSKO-DALMATINSKA
21245	Vrpolje	Tijarica	SPLITSKO-DALMATINSKA
21245	Voštane	Tijarica	SPLITSKO-DALMATINSKA
21245	Tijarica	Tijarica	SPLITSKO-DALMATINSKA
21245	Strizirep	Tijarica	SPLITSKO-DALMATINSKA
21245	Rože	Tijarica	SPLITSKO-DALMATINSKA
21245	Ljut	Tijarica	SPLITSKO-DALMATINSKA
21246	Aržano	Aržano	SPLITSKO-DALMATINSKA
21246	Kamensko	Aržano	SPLITSKO-DALMATINSKA
21247	Zelovo Sutinsko	Neorić	SPLITSKO-DALMATINSKA
21247	Sutina	Neorić	SPLITSKO-DALMATINSKA
21247	Neorić	Neorić	SPLITSKO-DALMATINSKA
21247	Gizdavac	Neorić	SPLITSKO-DALMATINSKA
21250	Žeževica	Šestanovac	SPLITSKO-DALMATINSKA
21250	Šestanovac	Šestanovac	SPLITSKO-DALMATINSKA
21250	Kreševo	Šestanovac	SPLITSKO-DALMATINSKA
21250	Katuni	Šestanovac	SPLITSKO-DALMATINSKA
21251	Donje Sitno	Žrnovnica	SPLITSKO-DALMATINSKA
21251	Gornje Sitno	Žrnovnica	SPLITSKO-DALMATINSKA
21251	Žrnovnica	Žrnovnica	SPLITSKO-DALMATINSKA
21252	Tugare	Tugare	SPLITSKO-DALMATINSKA
21252	Naklice	Tugare	SPLITSKO-DALMATINSKA
21252	Dubrava	Tugare	SPLITSKO-DALMATINSKA
21253	Čisla	Gata	SPLITSKO-DALMATINSKA
21253	Gata	Gata	SPLITSKO-DALMATINSKA
21253	Ostrovica	Gata	SPLITSKO-DALMATINSKA
21253	Smolonje	Gata	SPLITSKO-DALMATINSKA
21253	Zvečanje	Gata	SPLITSKO-DALMATINSKA
21254	Trnbusi	Blato na Cetini	SPLITSKO-DALMATINSKA
21254	Seoca	Blato na Cetini	SPLITSKO-DALMATINSKA
21254	Nova Sela	Blato na Cetini	SPLITSKO-DALMATINSKA
21254	Blato na Cetini	Blato na Cetini	SPLITSKO-DALMATINSKA
21255	Zadvarje	Zadvarje	SPLITSKO-DALMATINSKA
21255	Slime	Zadvarje	SPLITSKO-DALMATINSKA
21255	Santrići	Zadvarje	SPLITSKO-DALMATINSKA
21255	Potpoletnica	Zadvarje	SPLITSKO-DALMATINSKA
21255	Pejkovići	Zadvarje	SPLITSKO-DALMATINSKA
21255	Krželji	Zadvarje	SPLITSKO-DALMATINSKA
21255	Krnići	Zadvarje	SPLITSKO-DALMATINSKA
21255	Kraljevac	Zadvarje	SPLITSKO-DALMATINSKA
21255	Gornja Brela	Zadvarje	SPLITSKO-DALMATINSKA
21255	Dupci	Zadvarje	SPLITSKO-DALMATINSKA
21256	Cista Provo	Cista Provo	SPLITSKO-DALMATINSKA
21256	Svib	Cista Provo	SPLITSKO-DALMATINSKA
21257	Opanci	Lovreć	SPLITSKO-DALMATINSKA
21257	Lovreć	Lovreć	SPLITSKO-DALMATINSKA
21260	Medvidovića Draga	Imotski	SPLITSKO-DALMATINSKA
21260	Imotski	Imotski	SPLITSKO-DALMATINSKA
21260	Gornji Vinjani	Imotski	SPLITSKO-DALMATINSKA
21260	Glavina Gornja	Imotski	SPLITSKO-DALMATINSKA
21260	Glavina Donja	Imotski	SPLITSKO-DALMATINSKA
21260	Donji Vinjani	Imotski	SPLITSKO-DALMATINSKA
21261	Podosoje	Runović	SPLITSKO-DALMATINSKA
21261	Runović	Runović	SPLITSKO-DALMATINSKA
21262	Podbablje Gornje	Kamenmost	SPLITSKO-DALMATINSKA
21262	Kamenmost	Kamenmost	SPLITSKO-DALMATINSKA
21262	Ivanbegovina	Kamenmost	SPLITSKO-DALMATINSKA
21262	Hrščevani	Kamenmost	SPLITSKO-DALMATINSKA
21262	Grubine	Kamenmost	SPLITSKO-DALMATINSKA
21262	Drum	Kamenmost	SPLITSKO-DALMATINSKA
21263	Šumet	Krivodol	SPLITSKO-DALMATINSKA
21263	Poljica	Krivodol	SPLITSKO-DALMATINSKA
21263	Lokvičići	Krivodol	SPLITSKO-DALMATINSKA
21263	Krivodol	Krivodol	SPLITSKO-DALMATINSKA
21263	Dolića Draga	Krivodol	SPLITSKO-DALMATINSKA
21263	Dobrinče	Krivodol	SPLITSKO-DALMATINSKA
21264	Donji Proložac	Donji Proložac	SPLITSKO-DALMATINSKA
21264	Gornji Proložac	Donji Proložac	SPLITSKO-DALMATINSKA
21264	Postranje	Donji Proložac	SPLITSKO-DALMATINSKA
21265	Studenci	Studenci	SPLITSKO-DALMATINSKA
21266	Zmijavci	Zmijavci	SPLITSKO-DALMATINSKA
21267	Ričice	Ričice	SPLITSKO-DALMATINSKA
21270	Biokovsko Selo	Zagvozd	SPLITSKO-DALMATINSKA
21270	Rastovac	Zagvozd	SPLITSKO-DALMATINSKA
21270	Zagvozd	Zagvozd	SPLITSKO-DALMATINSKA
21271	Grabovac	Grabovac	SPLITSKO-DALMATINSKA
21271	Medov Dolac	Grabovac	SPLITSKO-DALMATINSKA
21272	Slivno	Slivno	SPLITSKO-DALMATINSKA
21272	Mijaca	Slivno	SPLITSKO-DALMATINSKA
21272	Krstatice	Slivno	SPLITSKO-DALMATINSKA
21273	Raščane	Župa	SPLITSKO-DALMATINSKA
21273	Raščane Gornje	Župa	SPLITSKO-DALMATINSKA
21273	Župa	Župa	SPLITSKO-DALMATINSKA
21273	Župa Srednja	Župa	SPLITSKO-DALMATINSKA
21275	Zavojane	Dragljane	SPLITSKO-DALMATINSKA
21275	Vlaka	Dragljane	SPLITSKO-DALMATINSKA
21275	Poljica Kozička	Dragljane	SPLITSKO-DALMATINSKA
21275	Kozica	Dragljane	SPLITSKO-DALMATINSKA
21275	Duge Njive	Dragljane	SPLITSKO-DALMATINSKA
21275	Dragljane	Dragljane	SPLITSKO-DALMATINSKA
21276	Vrgorac	Vrgorac	SPLITSKO-DALMATINSKA
21276	Višnjica	Vrgorac	SPLITSKO-DALMATINSKA
21276	Vina	Vrgorac	SPLITSKO-DALMATINSKA
21276	Stilja	Vrgorac	SPLITSKO-DALMATINSKA
21276	Ravča	Vrgorac	SPLITSKO-DALMATINSKA
21276	Prapatnica	Vrgorac	SPLITSKO-DALMATINSKA
21276	Orah	Vrgorac	SPLITSKO-DALMATINSKA
21276	Kotezi	Vrgorac	SPLITSKO-DALMATINSKA
21276	Kokorić	Vrgorac	SPLITSKO-DALMATINSKA
21276	Kljenak	Vrgorac	SPLITSKO-DALMATINSKA
21276	Banja	Vrgorac	SPLITSKO-DALMATINSKA
21277	Umčani	Veliki Prolog	SPLITSKO-DALMATINSKA
21277	Podprolog	Veliki Prolog	SPLITSKO-DALMATINSKA
21277	Dusina	Veliki Prolog	SPLITSKO-DALMATINSKA
21277	Draževitići	Veliki Prolog	SPLITSKO-DALMATINSKA
21277	Veliki Prolog	Veliki Prolog	SPLITSKO-DALMATINSKA
21292	Srinjine	Srinjine	SPLITSKO-DALMATINSKA
21300	Makarska	Makarska	SPLITSKO-DALMATINSKA
21310	Borak	Omiš	SPLITSKO-DALMATINSKA
21310	Omiš	Omiš	SPLITSKO-DALMATINSKA
21310	Stanići	Omiš	SPLITSKO-DALMATINSKA
21310	Zakučac	Omiš	SPLITSKO-DALMATINSKA
21311	Stobreč	Stobreč	SPLITSKO-DALMATINSKA
21312	Sveti Martin	Podstrana	SPLITSKO-DALMATINSKA
21312	Podstrana	Podstrana	SPLITSKO-DALMATINSKA
21312	Mutogras	Podstrana	SPLITSKO-DALMATINSKA
21312	Miljevac	Podstrana	SPLITSKO-DALMATINSKA
21312	Grljevac	Podstrana	SPLITSKO-DALMATINSKA
21312	Grbavac	Podstrana	SPLITSKO-DALMATINSKA
21312	Gornja Podstrana	Podstrana	SPLITSKO-DALMATINSKA
21314	Jesenice	Jesenice	SPLITSKO-DALMATINSKA
21315	Duće	Dugi Rat	SPLITSKO-DALMATINSKA
21315	Dugi Rat	Dugi Rat	SPLITSKO-DALMATINSKA
21317	Lokva Rogoznica	Lokva Rogoznica	SPLITSKO-DALMATINSKA
21317	Čelina	Lokva Rogoznica	SPLITSKO-DALMATINSKA
21318	Marušići	Mimice	SPLITSKO-DALMATINSKA
21318	Mimice	Mimice	SPLITSKO-DALMATINSKA
21318	Pisak	Mimice	SPLITSKO-DALMATINSKA
21320	Promajna	Baška Voda	SPLITSKO-DALMATINSKA
21320	Krvavica	Baška Voda	SPLITSKO-DALMATINSKA
21320	Bratuš	Baška Voda	SPLITSKO-DALMATINSKA
21320	Baška Voda	Baška Voda	SPLITSKO-DALMATINSKA
21320	Bast	Baška Voda	SPLITSKO-DALMATINSKA
21322	Brela	Brela	SPLITSKO-DALMATINSKA
21325	Tučepi	Tučepi	SPLITSKO-DALMATINSKA
21325	Veliko Brdo	Tučepi	SPLITSKO-DALMATINSKA
21327	Gornje Igrane	Podgora	SPLITSKO-DALMATINSKA
21327	Podgora	Podgora	SPLITSKO-DALMATINSKA
21328	Drašnice	Drašnice	SPLITSKO-DALMATINSKA
21329	Živogošće	Igrane	SPLITSKO-DALMATINSKA
21329	Igrane	Igrane	SPLITSKO-DALMATINSKA
21330	Gradac	Gradac	SPLITSKO-DALMATINSKA
21333	Drvenik	Drvenik	SPLITSKO-DALMATINSKA
21334	Zaostrog	Zaostrog	SPLITSKO-DALMATINSKA
21335	Brist	Podaca	SPLITSKO-DALMATINSKA
21335	Podaca	Podaca	SPLITSKO-DALMATINSKA
21400	Supetar	Supetar	SPLITSKO-DALMATINSKA
21400	Mirca	Supetar	SPLITSKO-DALMATINSKA
21403	Sutivan	Sutivan	SPLITSKO-DALMATINSKA
21404	Bobovišća	Ložišća	SPLITSKO-DALMATINSKA
21404	Ložišća	Ložišća	SPLITSKO-DALMATINSKA
21405	Milna	Milna	SPLITSKO-DALMATINSKA
21405	Podhumlje	Milna	SPLITSKO-DALMATINSKA
21410	Škrip	Postira	SPLITSKO-DALMATINSKA
21410	Splitska	Postira	SPLITSKO-DALMATINSKA
21410	Postira	Postira	SPLITSKO-DALMATINSKA
21410	Dol	Postira	SPLITSKO-DALMATINSKA
21412	Pučišća	Pučišća	SPLITSKO-DALMATINSKA
21413	Povlja	Povlja	SPLITSKO-DALMATINSKA
21420	Murvica	Bol	SPLITSKO-DALMATINSKA
21420	Bol	Bol	SPLITSKO-DALMATINSKA
21423	Donji Humac	Nerežišća	SPLITSKO-DALMATINSKA
21423	Dračevica	Nerežišća	SPLITSKO-DALMATINSKA
21423	Nerežišća	Nerežišća	SPLITSKO-DALMATINSKA
21424	Pražnica	Pražnica	SPLITSKO-DALMATINSKA
21424	Gornji Humac	Pražnica	SPLITSKO-DALMATINSKA
21425	Novo Selo	Selca	SPLITSKO-DALMATINSKA
21425	Selca	Selca	SPLITSKO-DALMATINSKA
21426	Sumartin	Sumartin	SPLITSKO-DALMATINSKA
21430	Srednje Selo	Grohote	SPLITSKO-DALMATINSKA
21430	Nečujam	Grohote	SPLITSKO-DALMATINSKA
21430	Maslinica	Grohote	SPLITSKO-DALMATINSKA
21430	Grohote	Grohote	SPLITSKO-DALMATINSKA
21430	Donje Selo	Grohote	SPLITSKO-DALMATINSKA
21432	Gornje Selo	Stomorska	SPLITSKO-DALMATINSKA
21432	Stomorska	Stomorska	SPLITSKO-DALMATINSKA
21450	Hvar	Hvar	SPLITSKO-DALMATINSKA
21450	Malo Grablje	Hvar	SPLITSKO-DALMATINSKA
21450	Milna	Hvar	SPLITSKO-DALMATINSKA
21450	Velo Grablje	Hvar	SPLITSKO-DALMATINSKA
21450	Zaraće	Hvar	SPLITSKO-DALMATINSKA
21454	Brusje	Brusje	SPLITSKO-DALMATINSKA
21460	Dol	Stari Grad	SPLITSKO-DALMATINSKA
21460	Rudina	Stari Grad	SPLITSKO-DALMATINSKA
21460	Selca kod Starog Grada	Stari Grad	SPLITSKO-DALMATINSKA
21460	Stari Grad	Stari Grad	SPLITSKO-DALMATINSKA
21462	Vrbanj	Vrbanj	SPLITSKO-DALMATINSKA
21462	Svirče	Vrbanj	SPLITSKO-DALMATINSKA
21463	Vrboska	Vrboska	SPLITSKO-DALMATINSKA
21465	Zavala	Jelsa	SPLITSKO-DALMATINSKA
21465	Vrisnik	Jelsa	SPLITSKO-DALMATINSKA
21465	Sveta Nedjelja	Jelsa	SPLITSKO-DALMATINSKA
21465	Pitve	Jelsa	SPLITSKO-DALMATINSKA
21465	Jelsa	Jelsa	SPLITSKO-DALMATINSKA
21465	Ivan Dolac	Jelsa	SPLITSKO-DALMATINSKA
21465	Humac	Jelsa	SPLITSKO-DALMATINSKA
21465	Gromin Dolac	Jelsa	SPLITSKO-DALMATINSKA
21466	Poljica	Zastražišće	SPLITSKO-DALMATINSKA
21466	Zastražišće	Zastražišće	SPLITSKO-DALMATINSKA
21467	Gdinj	Gdinj	SPLITSKO-DALMATINSKA
21468	Bogomolje	Bogomolje	SPLITSKO-DALMATINSKA
21468	Selca kod Bogomolja	Bogomolje	SPLITSKO-DALMATINSKA
21469	Sućuraj	Sućuraj	SPLITSKO-DALMATINSKA
21480	Vis	Vis	SPLITSKO-DALMATINSKA
21480	Stončica	Vis	SPLITSKO-DALMATINSKA
21480	Rukavac	Vis	SPLITSKO-DALMATINSKA
21480	Rogačić	Vis	SPLITSKO-DALMATINSKA
21480	Podstražje	Vis	SPLITSKO-DALMATINSKA
21480	Podselje	Vis	SPLITSKO-DALMATINSKA
21480	Plisko Polje	Vis	SPLITSKO-DALMATINSKA
21480	Milna	Vis	SPLITSKO-DALMATINSKA
21480	Marine Zemlje	Vis	SPLITSKO-DALMATINSKA
21480	Brgujac	Vis	SPLITSKO-DALMATINSKA
21483	Žena Glava	Podšpilje	SPLITSKO-DALMATINSKA
21483	Podšpilje	Podšpilje	SPLITSKO-DALMATINSKA
21483	Podhumlje	Podšpilje	SPLITSKO-DALMATINSKA
21483	Duboka	Podšpilje	SPLITSKO-DALMATINSKA
21483	Dračevo Polje	Podšpilje	SPLITSKO-DALMATINSKA
21483	Borovik	Podšpilje	SPLITSKO-DALMATINSKA
21485	Sveti Andrija	Komiža	SPLITSKO-DALMATINSKA
21485	Palagruža	Komiža	SPLITSKO-DALMATINSKA
21485	Oključna	Komiža	SPLITSKO-DALMATINSKA
21485	Komiža	Komiža	SPLITSKO-DALMATINSKA
21485	Jabuka	Komiža	SPLITSKO-DALMATINSKA
21485	Biševo	Komiža	SPLITSKO-DALMATINSKA
22000	Bilice	Šibenik	ŠIBENSKO-KNINSKA
22000	Danilo Biranj	Šibenik	ŠIBENSKO-KNINSKA
22000	Dubrava kod Šibenika	Šibenik	ŠIBENSKO-KNINSKA
22000	Šibenik-dio	Šibenik	ŠIBENSKO-KNINSKA
22010	Krapanj	Šibenik-Brodarica	ŠIBENSKO-KNINSKA
22010	Šibenik/dio-Brodarica/	Šibenik-Brodarica	ŠIBENSKO-KNINSKA
22010	Jadrtovac	Šibenik-Brodarica	ŠIBENSKO-KNINSKA
22010	Grebaštica	Šibenik-Brodarica	ŠIBENSKO-KNINSKA
22020	Donje Polje	Šibenik-Ražine	ŠIBENSKO-KNINSKA
22020	Šibenik/dio-Ražine/	Šibenik-Ražine	ŠIBENSKO-KNINSKA
22030	Šibenik/dio-Zablaće/	Šibenik-Zablaće	ŠIBENSKO-KNINSKA
22202	Tribežić	Primošten	ŠIBENSKO-KNINSKA
22202	Primošten Burnji/dio/	Primošten	ŠIBENSKO-KNINSKA
22202	Primošten	Primošten	ŠIBENSKO-KNINSKA
22202	Pišćet	Primošten	ŠIBENSKO-KNINSKA
22202	Kotelja	Primošten	ŠIBENSKO-KNINSKA
22202	Kalina	Primošten	ŠIBENSKO-KNINSKA
22202	Draga	Primošten	ŠIBENSKO-KNINSKA
22203	Zečevo Rogozničko	Rogoznica	ŠIBENSKO-KNINSKA
22203	Široka Glavica	Rogoznica	ŠIBENSKO-KNINSKA
22203	Sapina Doca	Rogoznica	ŠIBENSKO-KNINSKA
22203	Rogoznica	Rogoznica	ŠIBENSKO-KNINSKA
22203	Ražanj	Rogoznica	ŠIBENSKO-KNINSKA
22203	Podorljak	Rogoznica	ŠIBENSKO-KNINSKA
22203	Podglavica	Rogoznica	ŠIBENSKO-KNINSKA
22203	Pazdelj	Rogoznica	ŠIBENSKO-KNINSKA
22203	Oglavci	Rogoznica	ŠIBENSKO-KNINSKA
22203	Jarebinjak	Rogoznica	ŠIBENSKO-KNINSKA
22203	Dvornica	Rogoznica	ŠIBENSKO-KNINSKA
22204	Vezac	Široke	ŠIBENSKO-KNINSKA
22204	Vadalj	Široke	ŠIBENSKO-KNINSKA
22204	Široke	Široke	ŠIBENSKO-KNINSKA
22204	Ložnice	Široke	ŠIBENSKO-KNINSKA
22204	Kruševo	Široke	ŠIBENSKO-KNINSKA
22205	Vrpolje	Perković	ŠIBENSKO-KNINSKA
22205	Slivno	Perković	ŠIBENSKO-KNINSKA
22205	Sitno Donje	Perković	ŠIBENSKO-KNINSKA
22205	Perković	Perković	ŠIBENSKO-KNINSKA
22205	Mravnica	Perković	ŠIBENSKO-KNINSKA
22205	Danilo Kraljice	Perković	ŠIBENSKO-KNINSKA
22205	Danilo Gornje	Perković	ŠIBENSKO-KNINSKA
22206	Vrsno	Boraja	ŠIBENSKO-KNINSKA
22206	Podine	Boraja	ŠIBENSKO-KNINSKA
22206	Lepenica	Boraja	ŠIBENSKO-KNINSKA
22206	Boraja	Boraja	ŠIBENSKO-KNINSKA
22211	Srima	Vodice	ŠIBENSKO-KNINSKA
22211	Vodice	Vodice	ŠIBENSKO-KNINSKA
22212	Tribunj	Tribunj	ŠIBENSKO-KNINSKA
22213	Kašić	Pirovac	ŠIBENSKO-KNINSKA
22213	Pirovac	Pirovac	ŠIBENSKO-KNINSKA
22213	Prosika	Pirovac	ŠIBENSKO-KNINSKA
22213	Putičanje	Pirovac	ŠIBENSKO-KNINSKA
22214	Čista Velika	Čista Velika	ŠIBENSKO-KNINSKA
22215	Gaćelezi	Zaton	ŠIBENSKO-KNINSKA
22215	Grabovci	Zaton	ŠIBENSKO-KNINSKA
22215	Raslina	Zaton	ŠIBENSKO-KNINSKA
22215	Zaton	Zaton	ŠIBENSKO-KNINSKA
22221	Radonić	Lozovac	ŠIBENSKO-KNINSKA
22221	Pokrovnik	Lozovac	ŠIBENSKO-KNINSKA
22221	Lozovac	Lozovac	ŠIBENSKO-KNINSKA
22221	Konjevrate	Lozovac	ŠIBENSKO-KNINSKA
22221	Gradina	Lozovac	ŠIBENSKO-KNINSKA
22221	Goriš	Lozovac	ŠIBENSKO-KNINSKA
22221	Čvrljevo	Lozovac	ŠIBENSKO-KNINSKA
22221	Brnjica	Lozovac	ŠIBENSKO-KNINSKA
22222	Skradin	Skradin	ŠIBENSKO-KNINSKA
22222	Skradinsko Polje	Skradin	ŠIBENSKO-KNINSKA
22222	Sonković	Skradin	ŠIBENSKO-KNINSKA
22222	Vačani	Skradin	ŠIBENSKO-KNINSKA
22222	Velika Glava	Skradin	ŠIBENSKO-KNINSKA
22222	Ždrapanj	Skradin	ŠIBENSKO-KNINSKA
22222	Rupe	Skradin	ŠIBENSKO-KNINSKA
22222	Plastovo	Skradin	ŠIBENSKO-KNINSKA
22222	Bičine	Skradin	ŠIBENSKO-KNINSKA
22222	Bratiškovci	Skradin	ŠIBENSKO-KNINSKA
22222	Dubravice	Skradin	ŠIBENSKO-KNINSKA
22222	Gorice	Skradin	ŠIBENSKO-KNINSKA
22222	Gračac	Skradin	ŠIBENSKO-KNINSKA
22222	Ićevo	Skradin	ŠIBENSKO-KNINSKA
22223	Žažvić	Bribir(kod Skradina)	ŠIBENSKO-KNINSKA
22223	Piramatovci	Bribir(kod Skradina)	ŠIBENSKO-KNINSKA
22223	Međare	Bribir(kod Skradina)	ŠIBENSKO-KNINSKA
22223	Lađevci	Bribir(kod Skradina)	ŠIBENSKO-KNINSKA
22223	Krković	Bribir(kod Skradina)	ŠIBENSKO-KNINSKA
22223	Čista Mala	Bribir(kod Skradina)	ŠIBENSKO-KNINSKA
22223	Cicvare	Bribir(kod Skradina)	ŠIBENSKO-KNINSKA
22223	Bribir	Bribir(kod Skradina)	ŠIBENSKO-KNINSKA
22232	Zlarin	Zlarin	ŠIBENSKO-KNINSKA
22233	Prvić Luka	Prvić Luka	ŠIBENSKO-KNINSKA
22234	Prvić Šepurine	Prvić Šepurine	ŠIBENSKO-KNINSKA
22235	Kaprije	Kaprije	ŠIBENSKO-KNINSKA
22236	Žirje	Žirje	ŠIBENSKO-KNINSKA
22240	Tisno	Tisno	ŠIBENSKO-KNINSKA
22240	Dubrava kod Tisnoga	Tisno	ŠIBENSKO-KNINSKA
22240	Dazlina	Tisno	ŠIBENSKO-KNINSKA
22242	Jezera	Jezera	ŠIBENSKO-KNINSKA
22243	Kornati	Murter	ŠIBENSKO-KNINSKA
22243	Murter	Murter	ŠIBENSKO-KNINSKA
22244	Betina	Betina	ŠIBENSKO-KNINSKA
22300	Žagrović	Knin	ŠIBENSKO-KNINSKA
22300	Vrpolje	Knin	ŠIBENSKO-KNINSKA
22300	Vrbnik	Knin	ŠIBENSKO-KNINSKA
22300	Potkonje	Knin	ŠIBENSKO-KNINSKA
22300	Ljubač	Knin	ŠIBENSKO-KNINSKA
22300	Kovačić	Knin	ŠIBENSKO-KNINSKA
22300	Kninsko Polje	Knin	ŠIBENSKO-KNINSKA
22300	Knin	Knin	ŠIBENSKO-KNINSKA
22300	Biskupija	Knin	ŠIBENSKO-KNINSKA
22301	Golubić	Golubić	ŠIBENSKO-KNINSKA
22302	Polača	Polača/kod Knina/	ŠIBENSKO-KNINSKA
22303	Bargatić	Oklaj	ŠIBENSKO-KNINSKA
22303	Suknovci	Oklaj	ŠIBENSKO-KNINSKA
22303	Razvođe	Oklaj	ŠIBENSKO-KNINSKA
22303	Puljane	Oklaj	ŠIBENSKO-KNINSKA
22303	Oklaj	Oklaj	ŠIBENSKO-KNINSKA
22303	Mratovo	Oklaj	ŠIBENSKO-KNINSKA
22303	Matase	Oklaj	ŠIBENSKO-KNINSKA
22303	Ljubotić	Oklaj	ŠIBENSKO-KNINSKA
22303	Lukar	Oklaj	ŠIBENSKO-KNINSKA
22303	Čitluk	Oklaj	ŠIBENSKO-KNINSKA
22303	Bobodol	Oklaj	ŠIBENSKO-KNINSKA
22304	Radučić	Radučić	ŠIBENSKO-KNINSKA
22305	Parčić	Kistanje	ŠIBENSKO-KNINSKA
22305	Nunić	Kistanje	ŠIBENSKO-KNINSKA
22305	Modrino Selo	Kistanje	ŠIBENSKO-KNINSKA
22305	Kolašac	Kistanje	ŠIBENSKO-KNINSKA
22305	Kistanje	Kistanje	ŠIBENSKO-KNINSKA
22305	Ivoševci	Kistanje	ŠIBENSKO-KNINSKA
22305	Biovičino Selo	Kistanje	ŠIBENSKO-KNINSKA
22306	Ervenik	Ervenik	ŠIBENSKO-KNINSKA
22307	Mokro Polje	Mokro Polje	ŠIBENSKO-KNINSKA
22310	Cetina	Kijevo	ŠIBENSKO-KNINSKA
22310	Civljane	Kijevo	ŠIBENSKO-KNINSKA
22310	Kijevo	Kijevo	ŠIBENSKO-KNINSKA
22311	Strmica	Strmica	ŠIBENSKO-KNINSKA
22312	Markovac	Kosovo/Zvjerinac/	ŠIBENSKO-KNINSKA
22312	Orlić	Kosovo/Zvjerinac/	ŠIBENSKO-KNINSKA
22312	Ramljane	Kosovo/Zvjerinac/	ŠIBENSKO-KNINSKA
22312	Riđane	Kosovo/Zvjerinac/	ŠIBENSKO-KNINSKA
22312	Uzdolje	Kosovo/Zvjerinac/	ŠIBENSKO-KNINSKA
22312	Zvjerinac	Kosovo/Zvjerinac/	ŠIBENSKO-KNINSKA
22317	Radljevac	Plavno	ŠIBENSKO-KNINSKA
22317	Plavno	Plavno	ŠIBENSKO-KNINSKA
22318	Oćestovo	Pađene	ŠIBENSKO-KNINSKA
22318	Oton	Pađene	ŠIBENSKO-KNINSKA
22318	Pađene	Pađene	ŠIBENSKO-KNINSKA
22319	Zečevo	Đevrske	ŠIBENSKO-KNINSKA
22319	Varivode	Đevrske	ŠIBENSKO-KNINSKA
22319	Smrdelje	Đevrske	ŠIBENSKO-KNINSKA
22319	Krnjeuve	Đevrske	ŠIBENSKO-KNINSKA
22319	Kakanj	Đevrske	ŠIBENSKO-KNINSKA
22319	Gošić	Đevrske	ŠIBENSKO-KNINSKA
22319	Đevrske	Đevrske	ŠIBENSKO-KNINSKA
22320	Žitnić	Drniš	ŠIBENSKO-KNINSKA
22320	Velušić	Drniš	ŠIBENSKO-KNINSKA
22320	Trbounje	Drniš	ŠIBENSKO-KNINSKA
22320	Pakovo Selo	Drniš	ŠIBENSKO-KNINSKA
22320	Moseć	Drniš	ŠIBENSKO-KNINSKA
22320	Lišnjak	Drniš	ŠIBENSKO-KNINSKA
22320	Kričke	Drniš	ŠIBENSKO-KNINSKA
22320	Drniš	Drniš	ŠIBENSKO-KNINSKA
22320	Badanj	Drniš	ŠIBENSKO-KNINSKA
22321	Tepljuh	Siverić	ŠIBENSKO-KNINSKA
22321	Štikovo	Siverić	ŠIBENSKO-KNINSKA
22321	Siverić	Siverić	ŠIBENSKO-KNINSKA
22321	Parčić	Siverić	ŠIBENSKO-KNINSKA
22321	Miočić	Siverić	ŠIBENSKO-KNINSKA
22321	Kanjane	Siverić	ŠIBENSKO-KNINSKA
22321	Kadina Glavica	Siverić	ŠIBENSKO-KNINSKA
22321	Biočić	Siverić	ŠIBENSKO-KNINSKA
22322	Umljanovići	Ružić	ŠIBENSKO-KNINSKA
22322	Ružić	Ružić	ŠIBENSKO-KNINSKA
22322	Otavice	Ružić	ŠIBENSKO-KNINSKA
22322	Mirlović Polje	Ružić	ŠIBENSKO-KNINSKA
22322	Kljake	Ružić	ŠIBENSKO-KNINSKA
22322	Gradac	Ružić	ŠIBENSKO-KNINSKA
22322	Čavoglave	Ružić	ŠIBENSKO-KNINSKA
22322	Baljci	Ružić	ŠIBENSKO-KNINSKA
22323	Mirlović Zagora	Unešić	ŠIBENSKO-KNINSKA
22323	Nevest	Unešić	ŠIBENSKO-KNINSKA
22323	Ostrogašica	Unešić	ŠIBENSKO-KNINSKA
22323	Podumci	Unešić	ŠIBENSKO-KNINSKA
22323	Sedramić	Unešić	ŠIBENSKO-KNINSKA
22323	Unešić	Unešić	ŠIBENSKO-KNINSKA
22323	Visoka	Unešić	ŠIBENSKO-KNINSKA
22323	Ljubostinje	Unešić	ŠIBENSKO-KNINSKA
22323	Koprno	Unešić	ŠIBENSKO-KNINSKA
22323	Gornje Vinovo	Unešić	ŠIBENSKO-KNINSKA
22323	Cera	Unešić	ŠIBENSKO-KNINSKA
22323	Čvrljevo	Unešić	ŠIBENSKO-KNINSKA
22323	Donje Planjane	Unešić	ŠIBENSKO-KNINSKA
22323	Donje Utore	Unešić	ŠIBENSKO-KNINSKA
22323	Donje Vinovo	Unešić	ŠIBENSKO-KNINSKA
22323	Gornje Planjane	Unešić	ŠIBENSKO-KNINSKA
22323	Gornje Utore	Unešić	ŠIBENSKO-KNINSKA
22324	Širitovci	Drinovci	ŠIBENSKO-KNINSKA
22324	Nos Kalik	Drinovci	ŠIBENSKO-KNINSKA
22324	Ključ	Drinovci	ŠIBENSKO-KNINSKA
22324	Karalić	Drinovci	ŠIBENSKO-KNINSKA
22324	Kaočine	Drinovci	ŠIBENSKO-KNINSKA
22324	Drinovci	Drinovci	ŠIBENSKO-KNINSKA
22324	Brištane	Drinovci	ŠIBENSKO-KNINSKA
22324	Bogatić	Drinovci	ŠIBENSKO-KNINSKA
23000	Zadar	Zadar	ZADARSKA
23000	Murvica	Zadar	ZADARSKA
23000	Crno	Zadar	ZADARSKA
23000	Briševo	Zadar	ZADARSKA
23000	Babindub	Zadar	ZADARSKA
23205	Bibinje	Bibinje	ZADARSKA
23206	Debeljak	Sukošan	ZADARSKA
23206	Podvršje	Sukošan	ZADARSKA
23206	Sukošan	Sukošan	ZADARSKA
23207	Turanj	Sveti Filip i Jakov	ZADARSKA
23207	Sv. Filip i Jakov	Sveti Filip i Jakov	ZADARSKA
23207	Sikovo	Sveti Filip i Jakov	ZADARSKA
23207	Gornje Raštane	Sveti Filip i Jakov	ZADARSKA
23207	Donje Raštane	Sveti Filip i Jakov	ZADARSKA
23210	Biograd na moru	Biograd na moru	ZADARSKA
23210	Vrana	Biograd na moru	ZADARSKA
23210	Vrgada	Biograd na moru	ZADARSKA
23211	Pakoštane	Pakoštane	ZADARSKA
23211	Drage	Pakoštane	ZADARSKA
23212	Kraj	Tkon	ZADARSKA
23212	Tkon	Tkon	ZADARSKA
23222	Zemunik Gornji	Zemunik	ZADARSKA
23222	Zemunik	Zemunik	ZADARSKA
23222	Smoković	Zemunik	ZADARSKA
23222	Gorica	Zemunik	ZADARSKA
23222	Galovac	Zemunik	ZADARSKA
23223	Prkos	Škabrnja	ZADARSKA
23223	Škabrnja	Škabrnja	ZADARSKA
23226	Pridraga	Pridraga	ZADARSKA
23231	Kožino	Petrčane	ZADARSKA
23231	Petrčane	Petrčane	ZADARSKA
23232	Zaton	Nin	ZADARSKA
23232	Ninski Stanovi	Nin	ZADARSKA
23232	Nin	Nin	ZADARSKA
23233	Privlaka	Privlaka (Dalmacija)	ZADARSKA
23234	Lozice	Vir	ZADARSKA
23234	Torovi	Vir	ZADARSKA
23234	Vir	Vir	ZADARSKA
23235	Žerava	Vrsi	ZADARSKA
23235	Vrsi	Vrsi	ZADARSKA
23235	Poljica-Brig	Vrsi	ZADARSKA
23235	Poljica	Vrsi	ZADARSKA
23235	Grbe	Vrsi	ZADARSKA
23241	Dračevac Ninski	Poličnik	ZADARSKA
23241	Islam Latinski/dio Rupalj/	Poličnik	ZADARSKA
23241	Lovinac	Poličnik	ZADARSKA
23241	Poličnik	Poličnik	ZADARSKA
23241	Suhovare	Poličnik	ZADARSKA
23241	Visočane	Poličnik	ZADARSKA
23242	Posedarje	Posedarje	ZADARSKA
23242	Islam Latinski/dio Podgradina/	Posedarje	ZADARSKA
23244	Seline	Starigrad Paklenica	ZADARSKA
23244	Starigrad	Starigrad Paklenica	ZADARSKA
23245	Tribanj	Tribanj	ZADARSKA
23247	Vinjerac	Vinjerac	ZADARSKA
23247	Slivnica	Vinjerac	ZADARSKA
23248	Rtina	Ražanac	ZADARSKA
23248	Ražanac	Ražanac	ZADARSKA
23248	Radovin	Ražanac	ZADARSKA
23248	Podvršje	Ražanac	ZADARSKA
23248	Ljubački Stanovi	Ražanac	ZADARSKA
23248	Ljubač	Ražanac	ZADARSKA
23248	Krneza	Ražanac	ZADARSKA
23248	Jovići	Ražanac	ZADARSKA
23249	Vrčići	Povljana	ZADARSKA
23249	Vlašići	Povljana	ZADARSKA
23249	Stara Vas	Povljana	ZADARSKA
23249	Smokvica	Povljana	ZADARSKA
23249	Povljana	Povljana	ZADARSKA
23249	Miškovići	Povljana	ZADARSKA
23249	Gorica	Povljana	ZADARSKA
23249	Dinjiška	Povljana	ZADARSKA
23250	Bašana	Pag	ZADARSKA
23250	Košljun	Pag	ZADARSKA
23250	Pag	Pag	ZADARSKA
23251	Šimuni	Kolan	ZADARSKA
23251	Mandre	Kolan	ZADARSKA
23251	Kolan	Kolan	ZADARSKA
23251	Gajac-dio	Kolan	ZADARSKA
23262	Barotul	Pašman	ZADARSKA
23262	Pašman	Pašman	ZADARSKA
23263	Ždrelac	Ždrelac	ZADARSKA
23263	Dobropoljana	Ždrelac	ZADARSKA
23263	Banj	Ždrelac	ZADARSKA
23264	Mrljane	Neviđane	ZADARSKA
23264	Neviđane	Neviđane	ZADARSKA
23271	Kukljica	Kukljica	ZADARSKA
23272	Kali	Kali	ZADARSKA
23273	Ošljak	Preko	ZADARSKA
23273	Poljana	Preko	ZADARSKA
23273	Preko	Preko	ZADARSKA
23273	Sutomišćica	Preko	ZADARSKA
23274	Lukoran	Lukoran	ZADARSKA
23275	Ugljan	Ugljan	ZADARSKA
23281	Sali	Sali	ZADARSKA
23281	Zaglav	Sali	ZADARSKA
23282	Žman	Žman	ZADARSKA
23282	Luka	Žman	ZADARSKA
23283	Rava	Rava	ZADARSKA
23284	Mali Iž	Veli Iž	ZADARSKA
23284	Veli Iž	Veli Iž	ZADARSKA
23285	Brbinj	Brbinj	ZADARSKA
23285	Savar	Brbinj	ZADARSKA
23286	Zverinac	Božava	ZADARSKA
23286	Dragove	Božava	ZADARSKA
23286	Božava	Božava	ZADARSKA
23287	Soline	Veli Rat	ZADARSKA
23287	Veli Rat	Veli Rat	ZADARSKA
23291	Rivanj	Sestrunj	ZADARSKA
23291	Sestrunj	Sestrunj	ZADARSKA
23292	Brgulje	Molat	ZADARSKA
23292	Molat	Molat	ZADARSKA
23292	Zapuntel	Molat	ZADARSKA
23293	Ist	Ist	ZADARSKA
23294	Premuda	Premuda	ZADARSKA
23295	Silba	Silba	ZADARSKA
23296	Olib	Olib	ZADARSKA
23312	Novigrad	Novigrad (Dalmacija)	ZADARSKA
23312	Paljuv	Novigrad (Dalmacija)	ZADARSKA
23420	Podgrađe	Benkovac	ZADARSKA
23420	Perušić Benkovački	Benkovac	ZADARSKA
23420	Ostrovica	Benkovac	ZADARSKA
23420	Nadin	Benkovac	ZADARSKA
23420	Miranje	Benkovac	ZADARSKA
23420	Podlug	Benkovac	ZADARSKA
23420	Popovići	Benkovac	ZADARSKA
23420	Pristeg	Benkovac	ZADARSKA
23420	Raštević	Benkovac	ZADARSKA
23420	Šopot	Benkovac	ZADARSKA
23420	Zagrad	Benkovac	ZADARSKA
23420	Zapužane	Benkovac	ZADARSKA
23420	Lišane Ostrovičke	Benkovac	ZADARSKA
23420	Lisičić	Benkovac	ZADARSKA
23420	Benkovac	Benkovac	ZADARSKA
23420	Benkovačko Selo	Benkovac	ZADARSKA
23420	Brgud	Benkovac	ZADARSKA
23420	Buković	Benkovac	ZADARSKA
23420	Bulić	Benkovac	ZADARSKA
23420	Donje Ceranje	Benkovac	ZADARSKA
23420	Gornje Ceranje	Benkovac	ZADARSKA
23420	Kolarina	Benkovac	ZADARSKA
23420	Korlat	Benkovac	ZADARSKA
23420	Kožlovac	Benkovac	ZADARSKA
23420	Kula Atlagić	Benkovac	ZADARSKA
23420	Lepuri	Benkovac	ZADARSKA
23421	Rodaljice	Bjelina	ZADARSKA
23421	Dobropoljci	Bjelina	ZADARSKA
23421	Bruška	Bjelina	ZADARSKA
23421	Bjelina	Bjelina	ZADARSKA
23422	Vukšić	Stankovci	ZADARSKA
23422	Velim	Stankovci	ZADARSKA
23422	Stankovci	Stankovci	ZADARSKA
23422	Radošinovci	Stankovci	ZADARSKA
23422	Prović	Stankovci	ZADARSKA
23422	Morpolača	Stankovci	ZADARSKA
23422	Dobra Voda	Stankovci	ZADARSKA
23422	Crljenik	Stankovci	ZADARSKA
23422	Budak	Stankovci	ZADARSKA
23422	Bila Vlaka	Stankovci	ZADARSKA
23422	Banjevci	Stankovci	ZADARSKA
23423	Tinj	Polača	ZADARSKA
23423	Polača	Polača	ZADARSKA
23423	Lišane Tinjske	Polača	ZADARSKA
23423	Kakma	Polača	ZADARSKA
23423	Gornja Jagodnja	Polača	ZADARSKA
23423	Donja Jagodnja	Polača	ZADARSKA
23424	Smilčić	Smilčić	ZADARSKA
23424	Islam Grčki	Smilčić	ZADARSKA
23424	Gornje Biljane	Smilčić	ZADARSKA
23424	Donji Kašić	Smilčić	ZADARSKA
23424	Donje Biljane	Smilčić	ZADARSKA
23440	Vučipolje	Gračac	ZADARSKA
23440	Tomingaj	Gračac	ZADARSKA
23440	Omsica	Gračac	ZADARSKA
23440	Kijani	Gračac	ZADARSKA
23440	Gubavčevo Polje	Gračac	ZADARSKA
23440	Gračac	Gračac	ZADARSKA
23440	Grab	Gračac	ZADARSKA
23440	Glogovo	Gračac	ZADARSKA
23440	Duboki Dol	Gračac	ZADARSKA
23440	Deringaj	Gračac	ZADARSKA
23440	Cerovac	Gračac	ZADARSKA
23441	Rudopolje Bruvanjsko	Bruvno	ZADARSKA
23441	Mazin	Bruvno	ZADARSKA
23441	Bruvno	Bruvno	ZADARSKA
23442	Velika Popina	Otrić	ZADARSKA
23442	Rastičevo	Otrić	ZADARSKA
23442	Otrić	Otrić	ZADARSKA
23442	Nadvrelo	Otrić	ZADARSKA
23443	Zrmanja Vrelo	Zrmanja	ZADARSKA
23443	Zrmanja	Zrmanja	ZADARSKA
23443	Prljevo	Zrmanja	ZADARSKA
23443	Pribudić	Zrmanja	ZADARSKA
23443	Palanka	Zrmanja	ZADARSKA
23443	Kom	Zrmanja	ZADARSKA
23445	Zaklopac	Srb	ZADARSKA
23445	Suvaja	Srb	ZADARSKA
23445	Srb (Gornji i Donji)	Srb	ZADARSKA
23445	Neteka	Srb	ZADARSKA
23445	Kupirovo	Srb	ZADARSKA
23445	Kunovac Kupirovački	Srb	ZADARSKA
23445	Dabašnica	Srb	ZADARSKA
23445	Brotnja	Srb	ZADARSKA
23445	Begluci	Srb	ZADARSKA
23446	Tiškovac Lički	Kaldrma	ZADARSKA
23446	Osredci	Kaldrma	ZADARSKA
23446	Kaldrma	Kaldrma	ZADARSKA
23446	Dugopolje	Kaldrma	ZADARSKA
23446	Drenovac Osredački	Kaldrma	ZADARSKA
23450	Zelengrad	Obrovac	ZADARSKA
23450	Zaton Obrovački	Obrovac	ZADARSKA
23450	Rovanjska	Obrovac	ZADARSKA
23450	Obrovac	Obrovac	ZADARSKA
23450	Muškovci	Obrovac	ZADARSKA
23450	Medviđa	Obrovac	ZADARSKA
23450	Kruševo	Obrovac	ZADARSKA
23450	Jasenice	Obrovac	ZADARSKA
23450	Bilišane	Obrovac	ZADARSKA
23451	Žegar	Žegar	ZADARSKA
23451	Nadvoda	Žegar	ZADARSKA
23451	Krupa	Žegar	ZADARSKA
23451	Komazeci	Žegar	ZADARSKA
23451	Kaštel Žegarski	Žegar	ZADARSKA
23451	Golubić	Žegar	ZADARSKA
23451	Bogatnik	Žegar	ZADARSKA
23452	Gornji Karin	Karin	ZADARSKA
23452	Donji Karin	Karin	ZADARSKA
31000	Sarvaš	Osijek	OSJEČKO-BARANJSKA
31000	Podravlje	Osijek	OSJEČKO-BARANJSKA
31000	Osijek	Osijek	OSJEČKO-BARANJSKA
31000	Nemetin	Osijek	OSJEČKO-BARANJSKA
31000	Briješće	Osijek	OSJEČKO-BARANJSKA
31000	Brijest	Osijek	OSJEČKO-BARANJSKA
31000	Tvrđavica	Osijek	OSJEČKO-BARANJSKA
31204	Bijelo Brdo	Bijelo Brdo	OSJEČKO-BARANJSKA
31205	Aljmaš	Aljmaš	OSJEČKO-BARANJSKA
31206	Erdut	Erdut	OSJEČKO-BARANJSKA
31207	Tenja	Tenja	OSJEČKO-BARANJSKA
31207	Klisa	Tenja	OSJEČKO-BARANJSKA
31208	Petrijevci	Petrijevci	OSJEČKO-BARANJSKA
31214	Silaš	Laslovo	OSJEČKO-BARANJSKA
31214	Palača	Laslovo	OSJEČKO-BARANJSKA
31214	Laslovo	Laslovo	OSJEČKO-BARANJSKA
31214	Korog	Laslovo	OSJEČKO-BARANJSKA
31214	Ada	Laslovo	OSJEČKO-BARANJSKA
31215	Divoš	Ernestinovo	OSJEČKO-BARANJSKA
31215	Ernestinovo	Ernestinovo	OSJEČKO-BARANJSKA
31215	Koprivna	Ernestinovo	OSJEČKO-BARANJSKA
31215	Paulin Dvor	Ernestinovo	OSJEČKO-BARANJSKA
31215	Petrova Slatina	Ernestinovo	OSJEČKO-BARANJSKA
31215	Šodolovci	Ernestinovo	OSJEČKO-BARANJSKA
31216	Ivanovac	Antunovac	OSJEČKO-BARANJSKA
31216	Antunovac	Antunovac	OSJEČKO-BARANJSKA
31220	Višnjevac	Višnjevac	OSJEČKO-BARANJSKA
31221	Josipovac	Josipovac	OSJEČKO-BARANJSKA
31222	Selci	Bizovac	OSJEČKO-BARANJSKA
31222	Satnica	Bizovac	OSJEČKO-BARANJSKA
31222	Samatovci	Bizovac	OSJEČKO-BARANJSKA
31222	Cret Bizovački	Bizovac	OSJEČKO-BARANJSKA
31222	Cerovac	Bizovac	OSJEČKO-BARANJSKA
31222	Bizovac	Bizovac	OSJEČKO-BARANJSKA
31223	Novaki Bizovački	Brođanci	OSJEČKO-BARANJSKA
31223	Habjanovci	Brođanci	OSJEČKO-BARANJSKA
31223	Brođanci	Brođanci	OSJEČKO-BARANJSKA
31224	Topoline	Koška	OSJEČKO-BARANJSKA
31224	Ordanja	Koška	OSJEČKO-BARANJSKA
31224	Normanci	Koška	OSJEČKO-BARANJSKA
31224	Niza	Koška	OSJEČKO-BARANJSKA
31224	Lug Subotički	Koška	OSJEČKO-BARANJSKA
31224	Ledenik	Koška	OSJEČKO-BARANJSKA
31224	Koška	Koška	OSJEČKO-BARANJSKA
31224	Branimirovac	Koška	OSJEČKO-BARANJSKA
31224	Andrijevac	Koška	OSJEČKO-BARANJSKA
31225	Breznica Našička	Breznica Našička	OSJEČKO-BARANJSKA
31225	Jelisavac	Breznica Našička	OSJEČKO-BARANJSKA
31225	Lađanska	Breznica Našička	OSJEČKO-BARANJSKA
31225	Ribnjak	Breznica Našička	OSJEČKO-BARANJSKA
31226	Dalj	Dalj	OSJEČKO-BARANJSKA
31227	Harkanovci	Zelčin	OSJEČKO-BARANJSKA
31227	Ivanovci	Zelčin	OSJEČKO-BARANJSKA
31227	Marjančanci	Zelčin	OSJEČKO-BARANJSKA
31227	Zelčin	Zelčin	OSJEČKO-BARANJSKA
31300	Šumarina	Beli Manastir	OSJEČKO-BARANJSKA
31300	Širine	Beli Manastir	OSJEČKO-BARANJSKA
31300	Šećerana	Beli Manastir	OSJEČKO-BARANJSKA
31300	Sudaraž	Beli Manastir	OSJEČKO-BARANJSKA
31300	Luč	Beli Manastir	OSJEČKO-BARANJSKA
31300	Beli Manastir	Beli Manastir	OSJEČKO-BARANJSKA
31301	Branjin Vrh	Branjin Vrh	OSJEČKO-BARANJSKA
31302	Kneževo	Kneževo	OSJEČKO-BARANJSKA
31303	Popovac	Popovac	OSJEČKO-BARANJSKA
31303	Podolje	Popovac	OSJEČKO-BARANJSKA
31303	Branjina	Popovac	OSJEČKO-BARANJSKA
31304	Duboševica	Duboševica	OSJEČKO-BARANJSKA
31304	Topolje	Duboševica	OSJEČKO-BARANJSKA
31305	Gajić	Draž	OSJEČKO-BARANJSKA
31305	Draž	Draž	OSJEČKO-BARANJSKA
31306	Batina	Batina	OSJEČKO-BARANJSKA
31307	Zmajevac	Zmajevac	OSJEČKO-BARANJSKA
31308	Suza	Suza	OSJEČKO-BARANJSKA
31309	Zlatna Greda	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31309	Tikveš	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31309	Sokolovac	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31309	Mitrovac	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31309	Mirkovac	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31309	Kozjak	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31309	Kotlina	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31309	Kneževi Vinogradi	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31309	Kamenac	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31309	Jasenovac	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31309	Grabovac	Kneževi Vinogradi	OSJEČKO-BARANJSKA
31315	Karanac	Karanac	OSJEČKO-BARANJSKA
31321	Zeleno Polje	Petlovac	OSJEČKO-BARANJSKA
31321	Petlovac	Petlovac	OSJEČKO-BARANJSKA
31322	Baranjsko Petrovo Selo	Baranjsko Petrovo Selo	OSJEČKO-BARANJSKA
31322	Novi Bezdan	Baranjsko Petrovo Selo	OSJEČKO-BARANJSKA
31322	Novo Nevesinje	Baranjsko Petrovo Selo	OSJEČKO-BARANJSKA
31322	Torjanci	Baranjsko Petrovo Selo	OSJEČKO-BARANJSKA
31323	Bolman	Bolman	OSJEČKO-BARANJSKA
31323	Majiške Međe	Bolman	OSJEČKO-BARANJSKA
31323	Novi Bolman	Bolman	OSJEČKO-BARANJSKA
31324	Jagodnjak	Jagodnjak	OSJEČKO-BARANJSKA
31325	Čeminac	Čeminac	OSJEČKO-BARANJSKA
31325	Kozarac	Čeminac	OSJEČKO-BARANJSKA
31325	Novi Čeminac	Čeminac	OSJEČKO-BARANJSKA
31326	Darda	Darda	OSJEČKO-BARANJSKA
31326	Mece	Darda	OSJEČKO-BARANJSKA
31326	Švajcarnica	Darda	OSJEČKO-BARANJSKA
31326	Uglješ	Darda	OSJEČKO-BARANJSKA
31327	Vardarac	Bilje	OSJEČKO-BARANJSKA
31327	Podunavlje	Bilje	OSJEČKO-BARANJSKA
31327	Kopačevo	Bilje	OSJEČKO-BARANJSKA
31327	Bilje	Bilje	OSJEČKO-BARANJSKA
31328	Lug	Lug	OSJEČKO-BARANJSKA
31400	Kuševac	Đakovo	OSJEČKO-BARANJSKA
31400	Ivanovci Gorjanski	Đakovo	OSJEČKO-BARANJSKA
31400	Đakovo	Đakovo	OSJEČKO-BARANJSKA
31400	Budrovci	Đakovo	OSJEČKO-BARANJSKA
31401	Forkuševci	Viškovci	OSJEČKO-BARANJSKA
31401	Viškovci	Viškovci	OSJEČKO-BARANJSKA
31401	Vučevci	Viškovci	OSJEČKO-BARANJSKA
31402	Semeljci	Semeljci	OSJEČKO-BARANJSKA
31402	Koritna	Semeljci	OSJEČKO-BARANJSKA
31402	Kešinci	Semeljci	OSJEČKO-BARANJSKA
31403	Beketinci	Vuka	OSJEČKO-BARANJSKA
31403	Hrastovac	Vuka	OSJEČKO-BARANJSKA
31403	Lipovac Hrastinski	Vuka	OSJEČKO-BARANJSKA
31403	Široko Polje	Vuka	OSJEČKO-BARANJSKA
31403	Vuka	Vuka	OSJEČKO-BARANJSKA
31404	Vladislavci	Vladislavci	OSJEČKO-BARANJSKA
31404	Hrastin	Vladislavci	OSJEČKO-BARANJSKA
31404	Dopsin	Vladislavci	OSJEČKO-BARANJSKA
31410	Merolino Sikirevačko	Strizivojna	OSJEČKO-BARANJSKA
31410	Strizivojna	Strizivojna	OSJEČKO-BARANJSKA
31411	Trnava	Trnava	OSJEČKO-BARANJSKA
31411	Svetoblažje	Trnava	OSJEČKO-BARANJSKA
31411	Lapovci	Trnava	OSJEČKO-BARANJSKA
31411	Kondrić	Trnava	OSJEČKO-BARANJSKA
31411	Hrkanovci Đakovački	Trnava	OSJEČKO-BARANJSKA
31411	Dragotin	Trnava	OSJEČKO-BARANJSKA
31415	Selci Đakovački	Selci Đakovački	OSJEČKO-BARANJSKA
31416	Slobodna Vlast	Levanjska Varoš	OSJEČKO-BARANJSKA
31416	Ratkov Dol	Levanjska Varoš	OSJEČKO-BARANJSKA
31416	Paučje	Levanjska Varoš	OSJEČKO-BARANJSKA
31416	Ovčara	Levanjska Varoš	OSJEČKO-BARANJSKA
31416	Musić	Levanjska Varoš	OSJEČKO-BARANJSKA
31416	Milinac	Levanjska Varoš	OSJEČKO-BARANJSKA
31416	Majar	Levanjska Varoš	OSJEČKO-BARANJSKA
31416	Levanjska Varoš	Levanjska Varoš	OSJEČKO-BARANJSKA
31416	Čenkovo	Levanjska Varoš	OSJEČKO-BARANJSKA
31416	Breznica Đakovačka	Levanjska Varoš	OSJEČKO-BARANJSKA
31416	Borojevci	Levanjska Varoš	OSJEČKO-BARANJSKA
31417	Piškorevci	Piškorevci	OSJEČKO-BARANJSKA
31417	Novi Perkovci	Piškorevci	OSJEČKO-BARANJSKA
31418	Slatinik Drenjski	Drenje	OSJEČKO-BARANJSKA
31418	Pridvorje	Drenje	OSJEČKO-BARANJSKA
31418	Preslatinci	Drenje	OSJEČKO-BARANJSKA
31418	Mandićevac	Drenje	OSJEČKO-BARANJSKA
31418	Kućanci Đakovački	Drenje	OSJEČKO-BARANJSKA
31418	Drenje	Drenje	OSJEČKO-BARANJSKA
31418	Borovik	Drenje	OSJEČKO-BARANJSKA
31421	Gašinci	Satnica Đakovačka	OSJEČKO-BARANJSKA
31421	Satnica Đakovačka	Satnica Đakovačka	OSJEČKO-BARANJSKA
31422	Gorjani	Gorjani	OSJEČKO-BARANJSKA
31422	Tomašinci	Gorjani	OSJEČKO-BARANJSKA
31423	Potnjani	Bračevci	OSJEČKO-BARANJSKA
31423	Podgorje Bračevačko	Bračevci	OSJEČKO-BARANJSKA
31423	Paljevina	Bračevci	OSJEČKO-BARANJSKA
31423	Bučje Gorjansko	Bračevci	OSJEČKO-BARANJSKA
31423	Bračevci	Bračevci	OSJEČKO-BARANJSKA
31424	Josipovac Punitovački	Punitovci	OSJEČKO-BARANJSKA
31424	Jurjevac Punitovački	Punitovci	OSJEČKO-BARANJSKA
31424	Krndija	Punitovci	OSJEČKO-BARANJSKA
31424	Punitovci	Punitovci	OSJEČKO-BARANJSKA
31431	Ovčara	Čepin	OSJEČKO-BARANJSKA
31431	Livana	Čepin	OSJEČKO-BARANJSKA
31431	Čokadinci	Čepin	OSJEČKO-BARANJSKA
31431	Čepinski Martinci	Čepin	OSJEČKO-BARANJSKA
31431	Čepin	Čepin	OSJEČKO-BARANJSKA
31432	Budimci	Budimci	OSJEČKO-BARANJSKA
31432	Poganovci	Budimci	OSJEČKO-BARANJSKA
31433	Stipanovci	Podgorač	OSJEČKO-BARANJSKA
31433	Razbojište	Podgorač	OSJEČKO-BARANJSKA
31433	Podgorač	Podgorač	OSJEČKO-BARANJSKA
31433	Ostrošinci	Podgorač	OSJEČKO-BARANJSKA
31433	Kršinci	Podgorač	OSJEČKO-BARANJSKA
31433	Kelešinka	Podgorač	OSJEČKO-BARANJSKA
31433	Bijela Loza	Podgorač	OSJEČKO-BARANJSKA
31500	Markovac Našički	Našice	OSJEČKO-BARANJSKA
31500	Martin	Našice	OSJEČKO-BARANJSKA
31500	Našice	Našice	OSJEČKO-BARANJSKA
31500	Polubaše	Našice	OSJEČKO-BARANJSKA
31500	Rozmajerovac	Našice	OSJEČKO-BARANJSKA
31500	Seona	Našice	OSJEČKO-BARANJSKA
31500	Velimirovac	Našice	OSJEČKO-BARANJSKA
31500	Vukojevci	Našice	OSJEČKO-BARANJSKA
31500	Zoljan	Našice	OSJEČKO-BARANJSKA
31500	Makloševac	Našice	OSJEČKO-BARANJSKA
31500	Londžica	Našice	OSJEČKO-BARANJSKA
31500	Brezik Našički	Našice	OSJEČKO-BARANJSKA
31500	Ceremošnjak	Našice	OSJEČKO-BARANJSKA
31500	Crna Klada	Našice	OSJEČKO-BARANJSKA
31500	Gradac Našički	Našice	OSJEČKO-BARANJSKA
31500	Gornja Motičina	Našice	OSJEČKO-BARANJSKA
31500	Granice	Našice	OSJEČKO-BARANJSKA
31500	Klokočevci	Našice	OSJEČKO-BARANJSKA
31500	Lila	Našice	OSJEČKO-BARANJSKA
31500	Lipine	Našice	OSJEČKO-BARANJSKA
31511	Teodorovac	Đurđenovac	OSJEČKO-BARANJSKA
31511	Šaptinovci	Đurđenovac	OSJEČKO-BARANJSKA
31511	Sušine	Đurđenovac	OSJEČKO-BARANJSKA
31511	Pribiševci	Đurđenovac	OSJEČKO-BARANJSKA
31511	Našičko Novo Selo	Đurđenovac	OSJEČKO-BARANJSKA
31511	Ličko Novo Selo	Đurđenovac	OSJEČKO-BARANJSKA
31511	Gabrilovac	Đurđenovac	OSJEČKO-BARANJSKA
31511	Đurđenovac	Đurđenovac	OSJEČKO-BARANJSKA
31511	Bokšić Lug	Đurđenovac	OSJEČKO-BARANJSKA
31511	Bokšić	Đurđenovac	OSJEČKO-BARANJSKA
31511	Beljevina	Đurđenovac	OSJEČKO-BARANJSKA
31512	Vučjak Feričanački	Feričanci	OSJEČKO-BARANJSKA
31512	Valenovac	Feričanci	OSJEČKO-BARANJSKA
31512	Gazije	Feričanci	OSJEČKO-BARANJSKA
31512	Feričanci	Feričanci	OSJEČKO-BARANJSKA
31513	Donja Motičina	Donja Motičina	OSJEČKO-BARANJSKA
31530	Podravska Moslavina	Podravska Moslavina	OSJEČKO-BARANJSKA
31530	Orešnjak	Podravska Moslavina	OSJEČKO-BARANJSKA
31530	Martinci Miholjački	Podravska Moslavina	OSJEČKO-BARANJSKA
31530	Krčenik	Podravska Moslavina	OSJEČKO-BARANJSKA
31530	Gezinci	Podravska Moslavina	OSJEČKO-BARANJSKA
31531	Čret Viljevski	Viljevo	OSJEČKO-BARANJSKA
31531	Kapelna	Viljevo	OSJEČKO-BARANJSKA
31531	Viljevo	Viljevo	OSJEČKO-BARANJSKA
31540	Ivanovo	Donji Miholjac	OSJEČKO-BARANJSKA
31540	Donji Miholjac	Donji Miholjac	OSJEČKO-BARANJSKA
31540	Bockovac	Donji Miholjac	OSJEČKO-BARANJSKA
31540	Blanje	Donji Miholjac	OSJEČKO-BARANJSKA
31542	Šljivoševci	Magadenovac	OSJEČKO-BARANJSKA
31542	Malinovac	Magadenovac	OSJEČKO-BARANJSKA
31542	Magadenovac	Magadenovac	OSJEČKO-BARANJSKA
31542	Lacići	Magadenovac	OSJEČKO-BARANJSKA
31542	Kućanci	Magadenovac	OSJEČKO-BARANJSKA
31542	Beničanci	Magadenovac	OSJEČKO-BARANJSKA
31542	Brezovica	Magadenovac	OSJEČKO-BARANJSKA
31543	Čamagajevci	Miholjački Poreč	OSJEČKO-BARANJSKA
31543	Rakitovica	Miholjački Poreč	OSJEČKO-BARANJSKA
31543	Radikovci	Miholjački Poreč	OSJEČKO-BARANJSKA
31543	Miholjački Poreč	Miholjački Poreč	OSJEČKO-BARANJSKA
31543	Krunoslavje	Miholjački Poreč	OSJEČKO-BARANJSKA
31543	Golinci	Miholjački Poreč	OSJEČKO-BARANJSKA
31550	Valpovo	Valpovo	OSJEČKO-BARANJSKA
31550	Šag	Valpovo	OSJEČKO-BARANJSKA
31550	Nard	Valpovo	OSJEČKO-BARANJSKA
31550	Ladimirevci	Valpovo	OSJEČKO-BARANJSKA
31550	Gorica Valpovačka	Valpovo	OSJEČKO-BARANJSKA
31550	Bocanjevci	Valpovo	OSJEČKO-BARANJSKA
31551	Belišće	Belišće	OSJEČKO-BARANJSKA
31551	Bistrinci	Belišće	OSJEČKO-BARANJSKA
31552	Sveti Đurađ	Podgajci Podravski	OSJEČKO-BARANJSKA
31552	Podgajci Podravski	Podgajci Podravski	OSJEČKO-BARANJSKA
31552	Bočkinci	Podgajci Podravski	OSJEČKO-BARANJSKA
31553	Črnkovci	Črnkovci	OSJEČKO-BARANJSKA
31554	Vinogradci	Gat	OSJEČKO-BARANJSKA
31554	Veliškovci	Gat	OSJEČKO-BARANJSKA
31554	Tiborjanci	Gat	OSJEČKO-BARANJSKA
31554	Kitišanci	Gat	OSJEČKO-BARANJSKA
31554	Gat	Gat	OSJEČKO-BARANJSKA
31555	Kunišinci	Marijanci	OSJEČKO-BARANJSKA
31555	Marijanci	Marijanci	OSJEČKO-BARANJSKA
31555	Marijanski Ivanovci	Marijanci	OSJEČKO-BARANJSKA
32000	Vukovar	Vukovar	VUKOVARSKO-SRIJEMSKA
32000	Bogdanovci	Vukovar	VUKOVARSKO-SRIJEMSKA
32010	Lipovača	Vukovar	VUKOVARSKO-SRIJEMSKA
32100	Vinkovci	Vinkovci	VUKOVARSKO-SRIJEMSKA
32100	Mirkovci	Vinkovci	VUKOVARSKO-SRIJEMSKA
32211	Ostrovo	Ostrovo	VUKOVARSKO-SRIJEMSKA
32212	Gaboš	Gaboš	VUKOVARSKO-SRIJEMSKA
32213	Markušica	Markušica	VUKOVARSKO-SRIJEMSKA
32213	Podrinje	Markušica	VUKOVARSKO-SRIJEMSKA
32214	Tordinci	Tordinci	VUKOVARSKO-SRIJEMSKA
32214	Mlaka Antinska	Tordinci	VUKOVARSKO-SRIJEMSKA
32214	Antin	Tordinci	VUKOVARSKO-SRIJEMSKA
32221	Cerić	Nuštar	VUKOVARSKO-SRIJEMSKA
32221	Marinci	Nuštar	VUKOVARSKO-SRIJEMSKA
32221	Nuštar	Nuštar	VUKOVARSKO-SRIJEMSKA
32222	Bršadin	Bršadin	VUKOVARSKO-SRIJEMSKA
32222	Pačetin	Bršadin	VUKOVARSKO-SRIJEMSKA
32224	Vera	Trpinja	VUKOVARSKO-SRIJEMSKA
32224	Trpinja	Trpinja	VUKOVARSKO-SRIJEMSKA
32225	Bobota	Bobota	VUKOVARSKO-SRIJEMSKA
32225	Ćelija	Bobota	VUKOVARSKO-SRIJEMSKA
32225	Ludvinci	Bobota	VUKOVARSKO-SRIJEMSKA
32227	Borovo	Borovo	VUKOVARSKO-SRIJEMSKA
32229	Petrovci	Petrovci	VUKOVARSKO-SRIJEMSKA
32232	Grabovo	Sotin	VUKOVARSKO-SRIJEMSKA
32232	Sotin	Sotin	VUKOVARSKO-SRIJEMSKA
32233	Opatovac	Opatovac	VUKOVARSKO-SRIJEMSKA
32234	Mohovo	Šarengrad	VUKOVARSKO-SRIJEMSKA
32234	Šarengrad	Šarengrad	VUKOVARSKO-SRIJEMSKA
32235	Bapska	Bapska	VUKOVARSKO-SRIJEMSKA
32236	Ilok	Ilok	VUKOVARSKO-SRIJEMSKA
32237	Lovas	Lovas	VUKOVARSKO-SRIJEMSKA
32238	Tompojevci	Čakovci	VUKOVARSKO-SRIJEMSKA
32238	Novi Čakovci	Čakovci	VUKOVARSKO-SRIJEMSKA
32238	Mikluševci	Čakovci	VUKOVARSKO-SRIJEMSKA
32238	Čakovci	Čakovci	VUKOVARSKO-SRIJEMSKA
32238	Bokšić	Čakovci	VUKOVARSKO-SRIJEMSKA
32239	Negoslavci	Negoslavci	VUKOVARSKO-SRIJEMSKA
32241	Novi Jankovci	Stari Jankovci	VUKOVARSKO-SRIJEMSKA
32241	Stari Jankovci	Stari Jankovci	VUKOVARSKO-SRIJEMSKA
32242	Slakovci	Slakovci	VUKOVARSKO-SRIJEMSKA
32242	Srijemske Laze	Slakovci	VUKOVARSKO-SRIJEMSKA
32242	Svinjarevci	Slakovci	VUKOVARSKO-SRIJEMSKA
32243	Orolik	Orolik	VUKOVARSKO-SRIJEMSKA
32243	Berak	Orolik	VUKOVARSKO-SRIJEMSKA
32244	Đeletovci	Đeletovci	VUKOVARSKO-SRIJEMSKA
32245	Donje Novo Selo	Nijemci	VUKOVARSKO-SRIJEMSKA
32245	Nijemci	Nijemci	VUKOVARSKO-SRIJEMSKA
32245	Podgrađe	Nijemci	VUKOVARSKO-SRIJEMSKA
32246	Apševci	Lipovac	VUKOVARSKO-SRIJEMSKA
32246	Lipovac	Lipovac	VUKOVARSKO-SRIJEMSKA
32247	Banovci	Banovci	VUKOVARSKO-SRIJEMSKA
32247	Vinkovački Banovci	Banovci	VUKOVARSKO-SRIJEMSKA
32248	Ilača	Ilača	VUKOVARSKO-SRIJEMSKA
32249	Tovarnik	Tovarnik	VUKOVARSKO-SRIJEMSKA
32251	Privlaka	Privlaka	VUKOVARSKO-SRIJEMSKA
32252	Otok	Otok	VUKOVARSKO-SRIJEMSKA
32253	Komletinci	Komletinci	VUKOVARSKO-SRIJEMSKA
32254	Vrbanja	Vrbanja	VUKOVARSKO-SRIJEMSKA
32255	Soljani	Soljani	VUKOVARSKO-SRIJEMSKA
32256	Strošinci	Strošinci	VUKOVARSKO-SRIJEMSKA
32257	Drenovci	Drenovci	VUKOVARSKO-SRIJEMSKA
32258	Podgajci Posavski	Posavski Podgajci	VUKOVARSKO-SRIJEMSKA
32260	Gunja	Gunja	VUKOVARSKO-SRIJEMSKA
32261	Rajevo Selo	Rajevo Selo	VUKOVARSKO-SRIJEMSKA
32262	Račinovci	Račinovci	VUKOVARSKO-SRIJEMSKA
32263	Đurići	Đurići	VUKOVARSKO-SRIJEMSKA
32270	Županja	Županja	VUKOVARSKO-SRIJEMSKA
32271	Andrijaševci	Rokovci Andrijaševci	VUKOVARSKO-SRIJEMSKA
32271	Rokovci	Rokovci Andrijaševci	VUKOVARSKO-SRIJEMSKA
32272	Cerna	Cerna	VUKOVARSKO-SRIJEMSKA
32272	Šiškovci	Cerna	VUKOVARSKO-SRIJEMSKA
32273	Gradište	Gradište	VUKOVARSKO-SRIJEMSKA
32274	Štitar	Štitar	VUKOVARSKO-SRIJEMSKA
32275	Bošnjaci	Bošnjaci	VUKOVARSKO-SRIJEMSKA
32276	Babina Greda	Babina Greda	VUKOVARSKO-SRIJEMSKA
32280	Jarmina	Jarmina	VUKOVARSKO-SRIJEMSKA
32280	Karadžićevo	Jarmina	VUKOVARSKO-SRIJEMSKA
32281	Ivankovo	Ivankovo	VUKOVARSKO-SRIJEMSKA
32282	Prkovci	Retkovci	VUKOVARSKO-SRIJEMSKA
32282	Retkovci	Retkovci	VUKOVARSKO-SRIJEMSKA
32283	Vođinci	Vođinci	VUKOVARSKO-SRIJEMSKA
32283	Novi Mikanovci	Vođinci	VUKOVARSKO-SRIJEMSKA
32284	Đurđanci	Stari Mikanovci	VUKOVARSKO-SRIJEMSKA
32284	Mrzović	Stari Mikanovci	VUKOVARSKO-SRIJEMSKA
32284	Stari Mikanovci	Stari Mikanovci	VUKOVARSKO-SRIJEMSKA
32284	Vrbica	Stari Mikanovci	VUKOVARSKO-SRIJEMSKA
33000	Virovitica	Virovitica	VIROVITIČKO-PODRAVSKA
33000	Sveti Đurađ	Virovitica	VIROVITIČKO-PODRAVSKA
33000	Rezovačke Krčevine	Virovitica	VIROVITIČKO-PODRAVSKA
33000	Rezovac	Virovitica	VIROVITIČKO-PODRAVSKA
33000	Požari	Virovitica	VIROVITIČKO-PODRAVSKA
33000	Podgorje	Virovitica	VIROVITIČKO-PODRAVSKA
33000	Milanovac	Virovitica	VIROVITIČKO-PODRAVSKA
33000	Golo Brdo	Virovitica	VIROVITIČKO-PODRAVSKA
33000	Čemernica	Virovitica	VIROVITIČKO-PODRAVSKA
33404	Vukosavljevica	Špišić Bukovica	VIROVITIČKO-PODRAVSKA
33404	Špišić Bukovica	Špišić Bukovica	VIROVITIČKO-PODRAVSKA
33404	Rogovac	Špišić Bukovica	VIROVITIČKO-PODRAVSKA
33404	Okrugljača	Špišić Bukovica	VIROVITIČKO-PODRAVSKA
33404	Novi Antunovac	Špišić Bukovica	VIROVITIČKO-PODRAVSKA
33404	Lozan	Špišić Bukovica	VIROVITIČKO-PODRAVSKA
33404	Korija	Špišić Bukovica	VIROVITIČKO-PODRAVSKA
33404	Bušetina	Špišić Bukovica	VIROVITIČKO-PODRAVSKA
33405	Velika Črešnjevica	Pitomača	VIROVITIČKO-PODRAVSKA
33405	Turnašica	Pitomača	VIROVITIČKO-PODRAVSKA
33405	Starogradački Marof	Pitomača	VIROVITIČKO-PODRAVSKA
33405	Stari Gradac	Pitomača	VIROVITIČKO-PODRAVSKA
33405	Sedlarica	Pitomača	VIROVITIČKO-PODRAVSKA
33405	Pitomača	Pitomača	VIROVITIČKO-PODRAVSKA
33405	Otrovanec	Pitomača	VIROVITIČKO-PODRAVSKA
33405	Mala Črešnjevica	Pitomača	VIROVITIČKO-PODRAVSKA
33405	Križnica	Pitomača	VIROVITIČKO-PODRAVSKA
33405	Kladare	Pitomača	VIROVITIČKO-PODRAVSKA
33405	Grabrovnica	Pitomača	VIROVITIČKO-PODRAVSKA
33406	Turanovac	Lukač	VIROVITIČKO-PODRAVSKA
33406	Lukač	Lukač	VIROVITIČKO-PODRAVSKA
33406	Kapela Dvor	Lukač	VIROVITIČKO-PODRAVSKA
33406	Dugo Selo Lukačko	Lukač	VIROVITIČKO-PODRAVSKA
33406	Budrovac Lukački	Lukač	VIROVITIČKO-PODRAVSKA
33406	Brezik	Lukač	VIROVITIČKO-PODRAVSKA
33407	Gornje Bazje	Gornje Bazje	VIROVITIČKO-PODRAVSKA
33407	Katinka	Gornje Bazje	VIROVITIČKO-PODRAVSKA
33407	Rit	Gornje Bazje	VIROVITIČKO-PODRAVSKA
33407	Terezino Polje	Gornje Bazje	VIROVITIČKO-PODRAVSKA
33407	Turanovac/dio/	Gornje Bazje	VIROVITIČKO-PODRAVSKA
33407	Veliko Polje	Gornje Bazje	VIROVITIČKO-PODRAVSKA
33407	Zrinj Lukački	Gornje Bazje	VIROVITIČKO-PODRAVSKA
33410	Zvonimirevo	Suhopolje	VIROVITIČKO-PODRAVSKA
33410	Suhopolje	Suhopolje	VIROVITIČKO-PODRAVSKA
33410	Pčelić	Suhopolje	VIROVITIČKO-PODRAVSKA
33410	Orešac	Suhopolje	VIROVITIČKO-PODRAVSKA
33410	Naudovac	Suhopolje	VIROVITIČKO-PODRAVSKA
33410	Gaćište	Suhopolje	VIROVITIČKO-PODRAVSKA
33410	Bukova	Suhopolje	VIROVITIČKO-PODRAVSKA
33410	Borova	Suhopolje	VIROVITIČKO-PODRAVSKA
33411	Žlebina	Gradina	VIROVITIČKO-PODRAVSKA
33411	Vladimirovac	Gradina	VIROVITIČKO-PODRAVSKA
33411	Rušani	Gradina	VIROVITIČKO-PODRAVSKA
33411	Novi Gradac	Gradina	VIROVITIČKO-PODRAVSKA
33411	Lug Gradinski	Gradina	VIROVITIČKO-PODRAVSKA
33411	Lipovac	Gradina	VIROVITIČKO-PODRAVSKA
33411	Gradina	Gradina	VIROVITIČKO-PODRAVSKA
33411	Detkovac	Gradina	VIROVITIČKO-PODRAVSKA
33411	Budakovac	Gradina	VIROVITIČKO-PODRAVSKA
33411	Brezovica	Gradina	VIROVITIČKO-PODRAVSKA
33411	Bačevac	Gradina	VIROVITIČKO-PODRAVSKA
33412	Žubrica	Cabuna	VIROVITIČKO-PODRAVSKA
33412	Žiroslavlje	Cabuna	VIROVITIČKO-PODRAVSKA
33412	Trnava Cabunska	Cabuna	VIROVITIČKO-PODRAVSKA
33412	Jugovo Polje	Cabuna	VIROVITIČKO-PODRAVSKA
33412	Cabuna	Cabuna	VIROVITIČKO-PODRAVSKA
33412	Budanica	Cabuna	VIROVITIČKO-PODRAVSKA
33507	Žabnjača	Crnac	VIROVITIČKO-PODRAVSKA
33507	Veliki Rastovac	Crnac	VIROVITIČKO-PODRAVSKA
33507	Suha Mlaka	Crnac	VIROVITIČKO-PODRAVSKA
33507	Staro Petrovo Polje	Crnac	VIROVITIČKO-PODRAVSKA
33507	Novo Petrovo Polje	Crnac	VIROVITIČKO-PODRAVSKA
33507	Milanovac	Crnac	VIROVITIČKO-PODRAVSKA
33507	Mali Rastovac	Crnac	VIROVITIČKO-PODRAVSKA
33507	Krivaja Pustara	Crnac	VIROVITIČKO-PODRAVSKA
33507	Crnac	Crnac	VIROVITIČKO-PODRAVSKA
33507	Breštanovci	Crnac	VIROVITIČKO-PODRAVSKA
33513	Obradovci	Zdenci	VIROVITIČKO-PODRAVSKA
33513	Slavonske Bare	Zdenci	VIROVITIČKO-PODRAVSKA
33513	Zdenci	Zdenci	VIROVITIČKO-PODRAVSKA
33513	Zokov Gaj	Zdenci	VIROVITIČKO-PODRAVSKA
33513	Kutovi	Zdenci	VIROVITIČKO-PODRAVSKA
33513	Gutmanovci	Zdenci	VIROVITIČKO-PODRAVSKA
33513	Grudnjak	Zdenci	VIROVITIČKO-PODRAVSKA
33513	Duga Međa	Zdenci	VIROVITIČKO-PODRAVSKA
33513	Donje Predrijevo	Zdenci	VIROVITIČKO-PODRAVSKA
33513	Bankovci	Zdenci	VIROVITIČKO-PODRAVSKA
33514	Prekoračani	Čačinci	VIROVITIČKO-PODRAVSKA
33514	Pušina	Čačinci	VIROVITIČKO-PODRAVSKA
33514	Rajino Polje	Čačinci	VIROVITIČKO-PODRAVSKA
33514	Vojlovica	Čačinci	VIROVITIČKO-PODRAVSKA
33514	Paušinci	Čačinci	VIROVITIČKO-PODRAVSKA
33514	Kraskovići	Čačinci	VIROVITIČKO-PODRAVSKA
33514	Krajna	Čačinci	VIROVITIČKO-PODRAVSKA
33514	Humljani	Čačinci	VIROVITIČKO-PODRAVSKA
33514	Čačinci	Čačinci	VIROVITIČKO-PODRAVSKA
33514	Bukvik	Čačinci	VIROVITIČKO-PODRAVSKA
33514	Brezovljani Vojlovički	Čačinci	VIROVITIČKO-PODRAVSKA
33515	Magadinovac	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Nova Jošava	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Orahovica	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Stara Jošava	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Šumeđe	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Kokočak	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Karlovac Feričanački	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Gornja Pištana	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Duzluk	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Donja Pištana	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Dolci	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Crkvari	Orahovica	VIROVITIČKO-PODRAVSKA
33515	Bijeljevina Orahovička	Orahovica	VIROVITIČKO-PODRAVSKA
33516	Slatinski Drenovac	Slatinski Drenovac	VIROVITIČKO-PODRAVSKA
33517	Mikleuš	Mikleuš	VIROVITIČKO-PODRAVSKA
33517	Čojlug	Mikleuš	VIROVITIČKO-PODRAVSKA
33517	Četekovac	Mikleuš	VIROVITIČKO-PODRAVSKA
33517	Borik	Mikleuš	VIROVITIČKO-PODRAVSKA
33517	Balinci	Mikleuš	VIROVITIČKO-PODRAVSKA
33518	Nova Bukovica	Nova Bukovica	VIROVITIČKO-PODRAVSKA
33518	Miljevci	Nova Bukovica	VIROVITIČKO-PODRAVSKA
33518	Gornje Viljevo	Nova Bukovica	VIROVITIČKO-PODRAVSKA
33518	Donja Bukovica	Nova Bukovica	VIROVITIČKO-PODRAVSKA
33518	Dobrović	Nova Bukovica	VIROVITIČKO-PODRAVSKA
33518	Bukovački Antunovac	Nova Bukovica	VIROVITIČKO-PODRAVSKA
33518	Brezik	Nova Bukovica	VIROVITIČKO-PODRAVSKA
33518	Bjelkovac	Nova Bukovica	VIROVITIČKO-PODRAVSKA
33520	Medinci	Slatina	VIROVITIČKO-PODRAVSKA
33520	Nova Šarovka	Slatina	VIROVITIČKO-PODRAVSKA
33520	Novi Senkovac	Slatina	VIROVITIČKO-PODRAVSKA
33520	Novo Kusonje	Slatina	VIROVITIČKO-PODRAVSKA
33520	Podravska Slatina	Slatina	VIROVITIČKO-PODRAVSKA
33520	Radosavci	Slatina	VIROVITIČKO-PODRAVSKA
33520	Sladojevački Lug	Slatina	VIROVITIČKO-PODRAVSKA
33520	Sladojevci	Slatina	VIROVITIČKO-PODRAVSKA
33520	Španat	Slatina	VIROVITIČKO-PODRAVSKA
33520	Višnjica	Slatina	VIROVITIČKO-PODRAVSKA
33520	Lukavac	Slatina	VIROVITIČKO-PODRAVSKA
33520	Kozice	Slatina	VIROVITIČKO-PODRAVSKA
33520	Bakić	Slatina	VIROVITIČKO-PODRAVSKA
33520	Bistrica	Slatina	VIROVITIČKO-PODRAVSKA
33520	Donje Kusonje	Slatina	VIROVITIČKO-PODRAVSKA
33520	Donji Meljani	Slatina	VIROVITIČKO-PODRAVSKA
33520	Golenić	Slatina	VIROVITIČKO-PODRAVSKA
33520	Gornje Kusonje	Slatina	VIROVITIČKO-PODRAVSKA
33520	Gornji Miholjac	Slatina	VIROVITIČKO-PODRAVSKA
33520	Grabić	Slatina	VIROVITIČKO-PODRAVSKA
33520	Ivanbrijeg	Slatina	VIROVITIČKO-PODRAVSKA
33520	Josipovo	Slatina	VIROVITIČKO-PODRAVSKA
33521	Ćeralije	Ćeralije	VIROVITIČKO-PODRAVSKA
33522	Macute	Voćin	VIROVITIČKO-PODRAVSKA
33522	Mačkovac	Voćin	VIROVITIČKO-PODRAVSKA
33522	Popovac	Voćin	VIROVITIČKO-PODRAVSKA
33522	Rijenci	Voćin	VIROVITIČKO-PODRAVSKA
33522	Sekulinci	Voćin	VIROVITIČKO-PODRAVSKA
33522	Smude	Voćin	VIROVITIČKO-PODRAVSKA
33522	Voćin	Voćin	VIROVITIČKO-PODRAVSKA
33522	Lisičine	Voćin	VIROVITIČKO-PODRAVSKA
33522	Kuzma	Voćin	VIROVITIČKO-PODRAVSKA
33522	Kometnik-Zubići	Voćin	VIROVITIČKO-PODRAVSKA
33522	Bokane	Voćin	VIROVITIČKO-PODRAVSKA
33522	Dobrić	Voćin	VIROVITIČKO-PODRAVSKA
33522	Đuričić	Voćin	VIROVITIČKO-PODRAVSKA
33522	Gornji Meljani	Voćin	VIROVITIČKO-PODRAVSKA
33522	Hum	Voćin	VIROVITIČKO-PODRAVSKA
33522	Hum Varoš	Voćin	VIROVITIČKO-PODRAVSKA
33522	Kometnik-Jorgići	Voćin	VIROVITIČKO-PODRAVSKA
33523	Zvonimirovac	Čađavica	VIROVITIČKO-PODRAVSKA
33523	Vraneševci	Čađavica	VIROVITIČKO-PODRAVSKA
33523	Šaševo	Čađavica	VIROVITIČKO-PODRAVSKA
33523	Starin	Čađavica	VIROVITIČKO-PODRAVSKA
33523	Noskovci	Čađavica	VIROVITIČKO-PODRAVSKA
33523	Noskovačka Dubrava	Čađavica	VIROVITIČKO-PODRAVSKA
33523	Ilmin Dvor	Čađavica	VIROVITIČKO-PODRAVSKA
33523	Donje Bazije	Čađavica	VIROVITIČKO-PODRAVSKA
33523	Čađavički Lug	Čađavica	VIROVITIČKO-PODRAVSKA
33523	Čađavica	Čađavica	VIROVITIČKO-PODRAVSKA
33525	Vaška	Sopje	VIROVITIČKO-PODRAVSKA
33525	Sopje	Sopje	VIROVITIČKO-PODRAVSKA
33525	Sopjanska Greda	Sopje	VIROVITIČKO-PODRAVSKA
33525	Novaki	Sopje	VIROVITIČKO-PODRAVSKA
33525	Kapinci	Sopje	VIROVITIČKO-PODRAVSKA
33525	Gornje Predrijevo	Sopje	VIROVITIČKO-PODRAVSKA
33533	Velika Trapinska	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Velika Klisa	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Velika Babina Gora	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Sovjak	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Rodin Potok	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Pivnica Slavonska	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Pepelana	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Mala Trapinska	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Mala Klisa	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Levinovac	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Kravljak	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Gvozdanska	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
33533	Dvorska	Pivnica Slavonska	VIROVITIČKO-PODRAVSKA
34000	Seoci	Požega	POŽEŠKO-SLAVONSKA
34000	Požega	Požega	POŽEŠKO-SLAVONSKA
34000	Novo Selo	Požega	POŽEŠKO-SLAVONSKA
34000	Novi Štitnjak	Požega	POŽEŠKO-SLAVONSKA
34000	Novi Mihaljevci	Požega	POŽEŠKO-SLAVONSKA
34000	Nova Lipa	Požega	POŽEŠKO-SLAVONSKA
34000	Stara Lipa	Požega	POŽEŠKO-SLAVONSKA
34000	Šeovci	Požega	POŽEŠKO-SLAVONSKA
34000	Škrabutnik	Požega	POŽEŠKO-SLAVONSKA
34000	Štitnjak	Požega	POŽEŠKO-SLAVONSKA
34000	Turnić	Požega	POŽEŠKO-SLAVONSKA
34000	Ugarci	Požega	POŽEŠKO-SLAVONSKA
34000	Vasine Laze	Požega	POŽEŠKO-SLAVONSKA
34000	Vidovci	Požega	POŽEŠKO-SLAVONSKA
34000	Mihaljevci	Požega	POŽEŠKO-SLAVONSKA
34000	Marindvor	Požega	POŽEŠKO-SLAVONSKA
34000	Laze Prnjavor	Požega	POŽEŠKO-SLAVONSKA
34000	Alaginci	Požega	POŽEŠKO-SLAVONSKA
34000	Bankovci	Požega	POŽEŠKO-SLAVONSKA
34000	Crkveni Vrhovci	Požega	POŽEŠKO-SLAVONSKA
34000	Ćosine Laze	Požega	POŽEŠKO-SLAVONSKA
34000	Dervišaga	Požega	POŽEŠKO-SLAVONSKA
34000	Donji Emovci	Požega	POŽEŠKO-SLAVONSKA
34000	Drškovci	Požega	POŽEŠKO-SLAVONSKA
34000	Emovački Lug	Požega	POŽEŠKO-SLAVONSKA
34000	Kunovci	Požega	POŽEŠKO-SLAVONSKA
34000	Krivaj	Požega	POŽEŠKO-SLAVONSKA
34000	Komušina	Požega	POŽEŠKO-SLAVONSKA
34000	Gradski Vrhovci	Požega	POŽEŠKO-SLAVONSKA
34000	Gornji Emovci	Požega	POŽEŠKO-SLAVONSKA
34000	Golobrdci	Požega	POŽEŠKO-SLAVONSKA
34308	Treštanovci	Jakšić	POŽEŠKO-SLAVONSKA
34308	Tekić	Jakšić	POŽEŠKO-SLAVONSKA
34308	Šumanovci	Jakšić	POŽEŠKO-SLAVONSKA
34308	Svetinja	Jakšić	POŽEŠKO-SLAVONSKA
34308	Rajsavac	Jakšić	POŽEŠKO-SLAVONSKA
34308	Radnovac	Jakšić	POŽEŠKO-SLAVONSKA
34308	Jakšić	Jakšić	POŽEŠKO-SLAVONSKA
34308	Granje	Jakšić	POŽEŠKO-SLAVONSKA
34308	Eminovci	Jakšić	POŽEŠKO-SLAVONSKA
34308	Cerovac	Jakšić	POŽEŠKO-SLAVONSKA
34308	Bertelovci	Jakšić	POŽEŠKO-SLAVONSKA
34310	Sulkovci	Pleternica	POŽEŠKO-SLAVONSKA
34310	Srednje Selo	Pleternica	POŽEŠKO-SLAVONSKA
34310	Resnik	Pleternica	POŽEŠKO-SLAVONSKA
34310	Poloje	Pleternica	POŽEŠKO-SLAVONSKA
34310	Pleternički Mihaljevci	Pleternica	POŽEŠKO-SLAVONSKA
34310	Svilna	Pleternica	POŽEŠKO-SLAVONSKA
34310	Trapari	Pleternica	POŽEŠKO-SLAVONSKA
34310	Tulnik	Pleternica	POŽEŠKO-SLAVONSKA
34310	Vesela	Pleternica	POŽEŠKO-SLAVONSKA
34310	Viškovci	Pleternica	POŽEŠKO-SLAVONSKA
34310	Vrčin Dol	Pleternica	POŽEŠKO-SLAVONSKA
34310	Zagrađe	Pleternica	POŽEŠKO-SLAVONSKA
34310	Pleternica	Pleternica	POŽEŠKO-SLAVONSKA
34310	Novoselci	Pleternica	POŽEŠKO-SLAVONSKA
34310	Bilice	Pleternica	POŽEŠKO-SLAVONSKA
34310	Blacko	Pleternica	POŽEŠKO-SLAVONSKA
34310	Bresnica	Pleternica	POŽEŠKO-SLAVONSKA
34310	Buk	Pleternica	POŽEŠKO-SLAVONSKA
34310	Bzenica	Pleternica	POŽEŠKO-SLAVONSKA
34310	Frkljevci	Pleternica	POŽEŠKO-SLAVONSKA
34310	Gradac	Pleternica	POŽEŠKO-SLAVONSKA
34310	Mihaljevići	Pleternica	POŽEŠKO-SLAVONSKA
34310	Lakušija	Pleternica	POŽEŠKO-SLAVONSKA
34310	Koprivnica	Pleternica	POŽEŠKO-SLAVONSKA
34310	Kalenić	Pleternica	POŽEŠKO-SLAVONSKA
34310	Kadanovci	Pleternica	POŽEŠKO-SLAVONSKA
34311	Kuzmica	Kuzmica	POŽEŠKO-SLAVONSKA
34312	Ašikovci	Sesvete (kod Požege)	POŽEŠKO-SLAVONSKA
34312	Zarilac	Sesvete (kod Požege)	POŽEŠKO-SLAVONSKA
34312	Sesvete	Sesvete (kod Požege)	POŽEŠKO-SLAVONSKA
34312	Knežci	Sesvete (kod Požege)	POŽEŠKO-SLAVONSKA
34312	Grabarje	Sesvete (kod Požege)	POŽEŠKO-SLAVONSKA
34312	Ćosinci	Sesvete (kod Požege)	POŽEŠKO-SLAVONSKA
34315	Ratkovica	Ratkovica	POŽEŠKO-SLAVONSKA
34315	Komorica	Ratkovica	POŽEŠKO-SLAVONSKA
34315	Drenovac	Ratkovica	POŽEŠKO-SLAVONSKA
34320	Perenci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Pasikovci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Ozdakovci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Orljavac	Orljavac	POŽEŠKO-SLAVONSKA
34320	Oljasi	Orljavac	POŽEŠKO-SLAVONSKA
34320	Nježići	Orljavac	POŽEŠKO-SLAVONSKA
34320	Novo Zvečevo	Orljavac	POŽEŠKO-SLAVONSKA
34320	Mrkoplje	Orljavac	POŽEŠKO-SLAVONSKA
34320	Podsreće	Orljavac	POŽEŠKO-SLAVONSKA
34320	Požeški Brđani	Orljavac	POŽEŠKO-SLAVONSKA
34320	Rasna	Orljavac	POŽEŠKO-SLAVONSKA
34320	Vranić	Orljavac	POŽEŠKO-SLAVONSKA
34320	Šušnjari	Orljavac	POŽEŠKO-SLAVONSKA
34320	Šnjegavić	Orljavac	POŽEŠKO-SLAVONSKA
34320	Striježevica	Orljavac	POŽEŠKO-SLAVONSKA
34320	Smoljanovci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Sloboština	Orljavac	POŽEŠKO-SLAVONSKA
34320	Sažije	Orljavac	POŽEŠKO-SLAVONSKA
34320	Ruševac	Orljavac	POŽEŠKO-SLAVONSKA
34320	Milivojevci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Milanovac	Orljavac	POŽEŠKO-SLAVONSKA
34320	Jeminovac	Orljavac	POŽEŠKO-SLAVONSKA
34320	Deževci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Čečavački Vučjak	Orljavac	POŽEŠKO-SLAVONSKA
34320	Čečavac	Orljavac	POŽEŠKO-SLAVONSKA
34320	Crljenci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Bratuljevci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Bogdašići	Orljavac	POŽEŠKO-SLAVONSKA
34320	Amatovci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Kamenska	Orljavac	POŽEŠKO-SLAVONSKA
34320	Kamenski Šeovci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Kamenski Vučjak	Orljavac	POŽEŠKO-SLAVONSKA
34320	Mijači	Orljavac	POŽEŠKO-SLAVONSKA
34320	Mihajlije	Orljavac	POŽEŠKO-SLAVONSKA
34320	Markovac	Orljavac	POŽEŠKO-SLAVONSKA
34320	Lučinci	Orljavac	POŽEŠKO-SLAVONSKA
34320	Kujnik	Orljavac	POŽEŠKO-SLAVONSKA
34320	Kruševo	Orljavac	POŽEŠKO-SLAVONSKA
34320	Koprivna	Orljavac	POŽEŠKO-SLAVONSKA
34320	Klisa	Orljavac	POŽEŠKO-SLAVONSKA
34322	Nurkovac	Brestovac	POŽEŠKO-SLAVONSKA
34322	Oblakovac	Brestovac	POŽEŠKO-SLAVONSKA
34322	Pavlovci	Brestovac	POŽEŠKO-SLAVONSKA
34322	Skenderovci	Brestovac	POŽEŠKO-SLAVONSKA
34322	Vilić Selo	Brestovac	POŽEŠKO-SLAVONSKA
34322	Zakorenje	Brestovac	POŽEŠKO-SLAVONSKA
34322	Završje	Brestovac	POŽEŠKO-SLAVONSKA
34322	Žigerovci	Brestovac	POŽEŠKO-SLAVONSKA
34322	Jaguplije	Brestovac	POŽEŠKO-SLAVONSKA
34322	Ivandol	Brestovac	POŽEŠKO-SLAVONSKA
34322	Bolomače	Brestovac	POŽEŠKO-SLAVONSKA
34322	Boričevci	Brestovac	POŽEŠKO-SLAVONSKA
34322	Brestovac	Brestovac	POŽEŠKO-SLAVONSKA
34322	Busnovi	Brestovac	POŽEŠKO-SLAVONSKA
34322	Daranovci	Brestovac	POŽEŠKO-SLAVONSKA
34322	Dolac	Brestovac	POŽEŠKO-SLAVONSKA
34322	Donji Gučani	Brestovac	POŽEŠKO-SLAVONSKA
34322	Gornji Gučani	Brestovac	POŽEŠKO-SLAVONSKA
34330	Radovanci	Velika	POŽEŠKO-SLAVONSKA
34330	Stražeman	Velika	POŽEŠKO-SLAVONSKA
34330	Toranj	Velika	POŽEŠKO-SLAVONSKA
34330	Trenkovo	Velika	POŽEŠKO-SLAVONSKA
34330	Trnovac	Velika	POŽEŠKO-SLAVONSKA
34330	Velika	Velika	POŽEŠKO-SLAVONSKA
34330	Potočani	Velika	POŽEŠKO-SLAVONSKA
34330	Poljanska	Velika	POŽEŠKO-SLAVONSKA
34330	Aleksandrovac	Velika	POŽEŠKO-SLAVONSKA
34330	Biškupci	Velika	POŽEŠKO-SLAVONSKA
34330	Doljanci	Velika	POŽEŠKO-SLAVONSKA
34330	Draga	Velika	POŽEŠKO-SLAVONSKA
34330	Gornji Vrhovci	Velika	POŽEŠKO-SLAVONSKA
34330	Kantrovci	Velika	POŽEŠKO-SLAVONSKA
34334	Ramanovci	Kaptol	POŽEŠKO-SLAVONSKA
34334	Novi Bešinci	Kaptol	POŽEŠKO-SLAVONSKA
34334	Komarovci	Kaptol	POŽEŠKO-SLAVONSKA
34334	Kaptol	Kaptol	POŽEŠKO-SLAVONSKA
34334	Golo Brdo	Kaptol	POŽEŠKO-SLAVONSKA
34334	Doljanovci	Kaptol	POŽEŠKO-SLAVONSKA
34334	Češljakovci	Kaptol	POŽEŠKO-SLAVONSKA
34334	Bešinci	Kaptol	POŽEŠKO-SLAVONSKA
34334	Alilovci	Kaptol	POŽEŠKO-SLAVONSKA
34335	Vetovo	Vetovo	POŽEŠKO-SLAVONSKA
34335	Podgorje	Vetovo	POŽEŠKO-SLAVONSKA
34335	Ovčare	Vetovo	POŽEŠKO-SLAVONSKA
34335	Lukač	Vetovo	POŽEŠKO-SLAVONSKA
34335	Hrnjevac	Vetovo	POŽEŠKO-SLAVONSKA
34340	Venje	Kutjevo	POŽEŠKO-SLAVONSKA
34340	Tominovac	Kutjevo	POŽEŠKO-SLAVONSKA
34340	Mitrovac	Kutjevo	POŽEŠKO-SLAVONSKA
34340	Kutjevo	Kutjevo	POŽEŠKO-SLAVONSKA
34340	Ferovac	Kutjevo	POŽEŠKO-SLAVONSKA
34340	Bjeliševac	Kutjevo	POŽEŠKO-SLAVONSKA
34343	Poreč	Bektež	POŽEŠKO-SLAVONSKA
34343	Nova Lipovica	Bektež	POŽEŠKO-SLAVONSKA
34343	Kula	Bektež	POŽEŠKO-SLAVONSKA
34343	Gradište	Bektež	POŽEŠKO-SLAVONSKA
34343	Draganlug	Bektež	POŽEŠKO-SLAVONSKA
34343	Ciglenik	Bektež	POŽEŠKO-SLAVONSKA
34343	Bektež	Bektež	POŽEŠKO-SLAVONSKA
34350	Sibokovac	Čaglin	POŽEŠKO-SLAVONSKA
34350	Sapna	Čaglin	POŽEŠKO-SLAVONSKA
34350	Ruševo	Čaglin	POŽEŠKO-SLAVONSKA
34350	Paka	Čaglin	POŽEŠKO-SLAVONSKA
34350	Novi Zdenkovac	Čaglin	POŽEŠKO-SLAVONSKA
34350	Nova Ljeskovica	Čaglin	POŽEŠKO-SLAVONSKA
34350	Sovski Dol	Čaglin	POŽEŠKO-SLAVONSKA
34350	Stara Ljeskovica	Čaglin	POŽEŠKO-SLAVONSKA
34350	Stari Zdenkovac	Čaglin	POŽEŠKO-SLAVONSKA
34350	Stojčinovac	Čaglin	POŽEŠKO-SLAVONSKA
34350	Veliki Bilač	Čaglin	POŽEŠKO-SLAVONSKA
34350	Vlatkovac	Čaglin	POŽEŠKO-SLAVONSKA
34350	Vukojevica	Čaglin	POŽEŠKO-SLAVONSKA
34350	Mali Bilač	Čaglin	POŽEŠKO-SLAVONSKA
34350	Mokreš	Čaglin	POŽEŠKO-SLAVONSKA
34350	Milanlug	Čaglin	POŽEŠKO-SLAVONSKA
34350	Čaglin	Čaglin	POŽEŠKO-SLAVONSKA
34350	Darkovac	Čaglin	POŽEŠKO-SLAVONSKA
34350	Djedina Rijeka	Čaglin	POŽEŠKO-SLAVONSKA
34350	Dobra Voda	Čaglin	POŽEŠKO-SLAVONSKA
34350	Dobrogošće	Čaglin	POŽEŠKO-SLAVONSKA
34350	Duboka	Čaglin	POŽEŠKO-SLAVONSKA
34350	Imrijevci	Čaglin	POŽEŠKO-SLAVONSKA
34350	Ivanovci	Čaglin	POŽEŠKO-SLAVONSKA
34350	Migalovci	Čaglin	POŽEŠKO-SLAVONSKA
34350	Latinovac	Čaglin	POŽEŠKO-SLAVONSKA
34350	Kneževac	Čaglin	POŽEŠKO-SLAVONSKA
34350	Jurkovac	Čaglin	POŽEŠKO-SLAVONSKA
34350	Jezero	Čaglin	POŽEŠKO-SLAVONSKA
34350	Jasik	Čaglin	POŽEŠKO-SLAVONSKA
34543	Strižičevac	Poljana	POŽEŠKO-SLAVONSKA
34543	Ribnjaci	Poljana	POŽEŠKO-SLAVONSKA
34543	Poljana	Poljana	POŽEŠKO-SLAVONSKA
34543	Marino Selo	Poljana	POŽEŠKO-SLAVONSKA
34543	Gaj	Poljana	POŽEŠKO-SLAVONSKA
34543	Bujevica	Poljana	POŽEŠKO-SLAVONSKA
34543	Brezine	Poljana	POŽEŠKO-SLAVONSKA
34543	Brekinska	Poljana	POŽEŠKO-SLAVONSKA
34543	Antunovac	Poljana	POŽEŠKO-SLAVONSKA
34550	Mali Banovac	Pakrac	POŽEŠKO-SLAVONSKA
34550	Novi Majur	Pakrac	POŽEŠKO-SLAVONSKA
34550	Pakrac	Pakrac	POŽEŠKO-SLAVONSKA
34550	Prekopakra	Pakrac	POŽEŠKO-SLAVONSKA
34550	Srednji Grahovljani	Pakrac	POŽEŠKO-SLAVONSKA
34550	Stari Majur	Pakrac	POŽEŠKO-SLAVONSKA
34550	Šeovica	Pakrac	POŽEŠKO-SLAVONSKA
34550	Španovica	Pakrac	POŽEŠKO-SLAVONSKA
34550	Toranj	Pakrac	POŽEŠKO-SLAVONSKA
34550	Lipovac	Pakrac	POŽEŠKO-SLAVONSKA
34550	Kusonje	Pakrac	POŽEŠKO-SLAVONSKA
34550	Kraguj	Pakrac	POŽEŠKO-SLAVONSKA
34550	Batinjani	Pakrac	POŽEŠKO-SLAVONSKA
34550	Brusnik	Pakrac	POŽEŠKO-SLAVONSKA
34550	Donja Šumetlica	Pakrac	POŽEŠKO-SLAVONSKA
34550	Donji Grahovljani	Pakrac	POŽEŠKO-SLAVONSKA
34550	Dragović	Pakrac	POŽEŠKO-SLAVONSKA
34550	Gornja Šumetlica	Pakrac	POŽEŠKO-SLAVONSKA
34550	Gornji Grahovljani	Pakrac	POŽEŠKO-SLAVONSKA
34550	Japaga	Pakrac	POŽEŠKO-SLAVONSKA
34550	Klisa	Pakrac	POŽEŠKO-SLAVONSKA
34551	Kovačevac	Lipik	POŽEŠKO-SLAVONSKA
34551	Kukunjevac	Lipik	POŽEŠKO-SLAVONSKA
34551	Lipik	Lipik	POŽEŠKO-SLAVONSKA
34551	Livađani	Lipik	POŽEŠKO-SLAVONSKA
34551	Skenderovci	Lipik	POŽEŠKO-SLAVONSKA
34551	Subocka	Lipik	POŽEŠKO-SLAVONSKA
34551	Korita	Lipik	POŽEŠKO-SLAVONSKA
34551	Jagma	Lipik	POŽEŠKO-SLAVONSKA
34551	Bjelanovac	Lipik	POŽEŠKO-SLAVONSKA
34551	Bukovčani	Lipik	POŽEŠKO-SLAVONSKA
34551	Dobrovac	Lipik	POŽEŠKO-SLAVONSKA
34551	Donji Čaglić	Lipik	POŽEŠKO-SLAVONSKA
34551	Filipovac	Lipik	POŽEŠKO-SLAVONSKA
34551	Gornji Čagalić	Lipik	POŽEŠKO-SLAVONSKA
34552	Veliki Banovac	Badljevina	POŽEŠKO-SLAVONSKA
34552	Ploštine	Badljevina	POŽEŠKO-SLAVONSKA
34552	Omanovac	Badljevina	POŽEŠKO-SLAVONSKA
34552	Kapetanovo Polje	Badljevina	POŽEŠKO-SLAVONSKA
34552	Gornja Obrijež	Badljevina	POŽEŠKO-SLAVONSKA
34552	Donja Obrijež	Badljevina	POŽEŠKO-SLAVONSKA
34552	Dereza	Badljevina	POŽEŠKO-SLAVONSKA
34552	Badljevina	Badljevina	POŽEŠKO-SLAVONSKA
34553	Mali Budići	Bučje	POŽEŠKO-SLAVONSKA
34553	Ožegovci	Bučje	POŽEŠKO-SLAVONSKA
34553	Popovci	Bučje	POŽEŠKO-SLAVONSKA
34553	Prgomelje	Bučje	POŽEŠKO-SLAVONSKA
34553	Rogulje	Bučje	POŽEŠKO-SLAVONSKA
34553	Tisovac	Bučje	POŽEŠKO-SLAVONSKA
34553	Veliki Budići	Bučje	POŽEŠKO-SLAVONSKA
34553	Kričke	Bučje	POŽEŠKO-SLAVONSKA
34553	Koturić	Bučje	POŽEŠKO-SLAVONSKA
34553	Jakovci	Bučje	POŽEŠKO-SLAVONSKA
34553	Glavica	Bučje	POŽEŠKO-SLAVONSKA
34553	Cikote	Bučje	POŽEŠKO-SLAVONSKA
34553	Cicvare	Bučje	POŽEŠKO-SLAVONSKA
34553	Bučje	Bučje	POŽEŠKO-SLAVONSKA
34553	Branešci	Bučje	POŽEŠKO-SLAVONSKA
34553	Bjelajci	Bučje	POŽEŠKO-SLAVONSKA
35000	Slavonski Brod	Slavonski Brod	BRODSKO-POSAVSKA
35000	Gromačnik	Slavonski Brod	BRODSKO-POSAVSKA
35000	Brodski Varoš	Slavonski Brod	BRODSKO-POSAVSKA
35105		Slavonski Brod	BRODSKO-POSAVSKA
35106		Slavonski Brod	BRODSKO-POSAVSKA
35107	Tomica	Podvinje	BRODSKO-POSAVSKA
35107	Rastušje	Podvinje	BRODSKO-POSAVSKA
35107	Podvinje	Podvinje	BRODSKO-POSAVSKA
35201	Podcrkavlje	Podcrkavlje	BRODSKO-POSAVSKA
35201	Oriovčić	Podcrkavlje	BRODSKO-POSAVSKA
35201	Matković Mala	Podcrkavlje	BRODSKO-POSAVSKA
35201	Kindrovo	Podcrkavlje	BRODSKO-POSAVSKA
35201	Grabarje	Podcrkavlje	BRODSKO-POSAVSKA
35201	Gornji Slatinik	Podcrkavlje	BRODSKO-POSAVSKA
35201	Glogovica	Podcrkavlje	BRODSKO-POSAVSKA
35201	Dubovik	Podcrkavlje	BRODSKO-POSAVSKA
35201	Donji Slatinik	Podcrkavlje	BRODSKO-POSAVSKA
35201	Crni Potok	Podcrkavlje	BRODSKO-POSAVSKA
35201	Brodski Zdenci	Podcrkavlje	BRODSKO-POSAVSKA
35207	Zadubravlje	Gornja Vrba	BRODSKO-POSAVSKA
35207	Gornja Vrba	Gornja Vrba	BRODSKO-POSAVSKA
35207	Donja Vrba	Gornja Vrba	BRODSKO-POSAVSKA
35208	Ruščica	Ruščica	BRODSKO-POSAVSKA
35208	Klakar	Ruščica	BRODSKO-POSAVSKA
35208	Gornja Bebrina	Ruščica	BRODSKO-POSAVSKA
35208	Donja Bebrina	Ruščica	BRODSKO-POSAVSKA
35209	Bukovlje	Bukovlje	BRODSKO-POSAVSKA
35209	Ježevik	Bukovlje	BRODSKO-POSAVSKA
35209	Vranovci	Bukovlje	BRODSKO-POSAVSKA
35210	Vrpolje	Vrpolje	BRODSKO-POSAVSKA
35210	Stari Perkovci	Vrpolje	BRODSKO-POSAVSKA
35210	Čajkovci	Vrpolje	BRODSKO-POSAVSKA
35211	Klokočevik	Trnjani	BRODSKO-POSAVSKA
35211	Korduševci	Trnjani	BRODSKO-POSAVSKA
35211	Šušnjevci	Trnjani	BRODSKO-POSAVSKA
35211	Trnjani	Trnjani	BRODSKO-POSAVSKA
35211	Vrhovina	Trnjani	BRODSKO-POSAVSKA
35212	Selna	Garčin	BRODSKO-POSAVSKA
35212	Sapci	Garčin	BRODSKO-POSAVSKA
35212	Garčin	Garčin	BRODSKO-POSAVSKA
35212	Bicko Selo	Garčin	BRODSKO-POSAVSKA
35213	Oprisavci	Oprisavci	BRODSKO-POSAVSKA
35213	Poljanci	Oprisavci	BRODSKO-POSAVSKA
35213	Trnjanski Kuti	Oprisavci	BRODSKO-POSAVSKA
35214	Staro Topolje	Donji Andrijevci	BRODSKO-POSAVSKA
35214	Novo Topolje	Donji Andrijevci	BRODSKO-POSAVSKA
35214	Donji Andrijevci	Donji Andrijevci	BRODSKO-POSAVSKA
35214	Divoševci	Donji Andrijevci	BRODSKO-POSAVSKA
35215	Sredanci	Svilaj	BRODSKO-POSAVSKA
35215	Svilaj	Svilaj	BRODSKO-POSAVSKA
35215	Zoljani	Svilaj	BRODSKO-POSAVSKA
35216	Stružani	Prnjavor	BRODSKO-POSAVSKA
35216	Prnjavor	Prnjavor	BRODSKO-POSAVSKA
35216	Novi Grad	Prnjavor	BRODSKO-POSAVSKA
35216	Kupina	Prnjavor	BRODSKO-POSAVSKA
35220	Slavonski Šamac	Slavonski Šamac	BRODSKO-POSAVSKA
35220	Kruševica	Slavonski Šamac	BRODSKO-POSAVSKA
35221	Beravci	Velika Kopanica	BRODSKO-POSAVSKA
35221	Mala Kopanica	Velika Kopanica	BRODSKO-POSAVSKA
35221	Velika Kopanica	Velika Kopanica	BRODSKO-POSAVSKA
35222	Gundinci	Gundinci	BRODSKO-POSAVSKA
35224	Jaruge	Sikirevci	BRODSKO-POSAVSKA
35224	Sikirevci	Sikirevci	BRODSKO-POSAVSKA
35250	Radovanje	Oriovac	BRODSKO-POSAVSKA
35250	Oriovac	Oriovac	BRODSKO-POSAVSKA
35250	Kujnik	Oriovac	BRODSKO-POSAVSKA
35250	Ciglenik	Oriovac	BRODSKO-POSAVSKA
35250	Bečic	Oriovac	BRODSKO-POSAVSKA
35252	Brđani	Sibinj	BRODSKO-POSAVSKA
35252	Završje	Sibinj	BRODSKO-POSAVSKA
35252	Slobodnica	Sibinj	BRODSKO-POSAVSKA
35252	Sibinj	Sibinj	BRODSKO-POSAVSKA
35252	Ravan	Sibinj	BRODSKO-POSAVSKA
35252	Krajačići	Sibinj	BRODSKO-POSAVSKA
35252	Jakačina Mala	Sibinj	BRODSKO-POSAVSKA
35252	Grižići	Sibinj	BRODSKO-POSAVSKA
35252	Grgurevići	Sibinj	BRODSKO-POSAVSKA
35252	Gornji Andrijevci	Sibinj	BRODSKO-POSAVSKA
35252	Čelikovići	Sibinj	BRODSKO-POSAVSKA
35252	Brčino	Sibinj	BRODSKO-POSAVSKA
35252	Bartolovci	Sibinj	BRODSKO-POSAVSKA
35253	Stari Slatnik	Brodski Stupnik	BRODSKO-POSAVSKA
35253	Lovčić	Brodski Stupnik	BRODSKO-POSAVSKA
35253	Brodski Stupnik	Brodski Stupnik	BRODSKO-POSAVSKA
35254	Zbjeg	Bebrina	BRODSKO-POSAVSKA
35254	Šumeće	Bebrina	BRODSKO-POSAVSKA
35254	Stupnički Kuti	Bebrina	BRODSKO-POSAVSKA
35254	Kaniža	Bebrina	BRODSKO-POSAVSKA
35254	Dubočac	Bebrina	BRODSKO-POSAVSKA
35254	Bebrina	Bebrina	BRODSKO-POSAVSKA
35254	Banovci	Bebrina	BRODSKO-POSAVSKA
35255	Slavonski Kobaš	Slavonski Kobaš	BRODSKO-POSAVSKA
35257	Živike	Lužani	BRODSKO-POSAVSKA
35257	Pričac	Lužani	BRODSKO-POSAVSKA
35257	Malino	Lužani	BRODSKO-POSAVSKA
35257	Lužani	Lužani	BRODSKO-POSAVSKA
35400	Prvča	Nova Gradiška	BRODSKO-POSAVSKA
35400	Nova Gradiška	Nova Gradiška	BRODSKO-POSAVSKA
35400	Ljupina	Nova Gradiška	BRODSKO-POSAVSKA
35400	Kovačevac	Nova Gradiška	BRODSKO-POSAVSKA
35403	Bukovica	Rešetari	BRODSKO-POSAVSKA
35403	Rešetari	Rešetari	BRODSKO-POSAVSKA
35404	Šumetlica	Cernik	BRODSKO-POSAVSKA
35404	Šagovina Cernička	Cernik	BRODSKO-POSAVSKA
35404	Sinlije	Cernik	BRODSKO-POSAVSKA
35404	Podvrško	Cernik	BRODSKO-POSAVSKA
35404	Opršinac	Cernik	BRODSKO-POSAVSKA
35404	Opatovac	Cernik	BRODSKO-POSAVSKA
35404	Golobrdac	Cernik	BRODSKO-POSAVSKA
35404	Giletinci	Cernik	BRODSKO-POSAVSKA
35404	Cernik	Cernik	BRODSKO-POSAVSKA
35404	Banićevac	Cernik	BRODSKO-POSAVSKA
35404	Baćin Dol	Cernik	BRODSKO-POSAVSKA
35410	Pavlovci	Nova Kapela	BRODSKO-POSAVSKA
35410	Seoce	Nova Kapela	BRODSKO-POSAVSKA
35410	Siće	Nova Kapela	BRODSKO-POSAVSKA
35410	Srednji Lipovac	Nova Kapela	BRODSKO-POSAVSKA
35410	Stara Kapela	Nova Kapela	BRODSKO-POSAVSKA
35410	Nova Kapela	Nova Kapela	BRODSKO-POSAVSKA
35410	Magić Mala	Nova Kapela	BRODSKO-POSAVSKA
35410	Batrina	Nova Kapela	BRODSKO-POSAVSKA
35410	Bili Brig	Nova Kapela	BRODSKO-POSAVSKA
35410	Donji Lipovac	Nova Kapela	BRODSKO-POSAVSKA
35410	Dragovci	Nova Kapela	BRODSKO-POSAVSKA
35410	Gornji Lipovac	Nova Kapela	BRODSKO-POSAVSKA
35414	Blažević Dol	Vrbova	BRODSKO-POSAVSKA
35414	Vrbova	Vrbova	BRODSKO-POSAVSKA
35420	Vladisovo	Staro Petrovo Selo	BRODSKO-POSAVSKA
35420	Tisovac	Staro Petrovo Selo	BRODSKO-POSAVSKA
35420	Štivica	Staro Petrovo Selo	BRODSKO-POSAVSKA
35420	Staro Petrovo Selo	Staro Petrovo Selo	BRODSKO-POSAVSKA
35420	Starci	Staro Petrovo Selo	BRODSKO-POSAVSKA
35420	Oštri Vrh	Staro Petrovo Selo	BRODSKO-POSAVSKA
35420	Komarnica	Staro Petrovo Selo	BRODSKO-POSAVSKA
35422	Zapolje	Zapolje	BRODSKO-POSAVSKA
35422	Laze	Zapolje	BRODSKO-POSAVSKA
35422	Gunjevci	Zapolje	BRODSKO-POSAVSKA
35422	Gornji Crnogovci	Zapolje	BRODSKO-POSAVSKA
35422	Godinjak	Zapolje	BRODSKO-POSAVSKA
35422	Drežnik	Zapolje	BRODSKO-POSAVSKA
35422	Donji Crnogovci	Zapolje	BRODSKO-POSAVSKA
35422	Brđani	Zapolje	BRODSKO-POSAVSKA
35422	Bodovaljci	Zapolje	BRODSKO-POSAVSKA
35422	Adžamovci	Zapolje	BRODSKO-POSAVSKA
35423	Vrbje	Vrbje	BRODSKO-POSAVSKA
35423	Visoka Greda	Vrbje	BRODSKO-POSAVSKA
35423	Sičice	Vrbje	BRODSKO-POSAVSKA
35423	Savski Bok	Vrbje	BRODSKO-POSAVSKA
35423	Mačkovac	Vrbje	BRODSKO-POSAVSKA
35423	Dolina	Vrbje	BRODSKO-POSAVSKA
35424	Orubica	Orubica	BRODSKO-POSAVSKA
35425	Davor	Davor	BRODSKO-POSAVSKA
35428	Poljane	Dragalić	BRODSKO-POSAVSKA
35428	Gorice	Dragalić	BRODSKO-POSAVSKA
35428	Dragalić	Dragalić	BRODSKO-POSAVSKA
35428	Donji Bogićevci	Dragalić	BRODSKO-POSAVSKA
35429	Žuberkovac	Gornji Bogićevci	BRODSKO-POSAVSKA
35429	Trnava	Gornji Bogićevci	BRODSKO-POSAVSKA
35429	Širinci	Gornji Bogićevci	BRODSKO-POSAVSKA
35429	Šagovina Mašička	Gornji Bogićevci	BRODSKO-POSAVSKA
35429	Smrtić	Gornji Bogićevci	BRODSKO-POSAVSKA
35429	Ratkovac	Gornji Bogićevci	BRODSKO-POSAVSKA
35429	Mašić	Gornji Bogićevci	BRODSKO-POSAVSKA
35429	Gornji Bogićevci	Gornji Bogićevci	BRODSKO-POSAVSKA
35430	Gređani	Okučani	BRODSKO-POSAVSKA
35430	Kosovac	Okučani	BRODSKO-POSAVSKA
35430	Lađevac	Okučani	BRODSKO-POSAVSKA
35430	Lještani	Okučani	BRODSKO-POSAVSKA
35430	Okučani	Okučani	BRODSKO-POSAVSKA
35430	Trnakovac	Okučani	BRODSKO-POSAVSKA
35430	Vrbovljani	Okučani	BRODSKO-POSAVSKA
35430	Gornji Rogolji	Okučani	BRODSKO-POSAVSKA
35430	Dubovac	Okučani	BRODSKO-POSAVSKA
35430	Donji Rogolji	Okučani	BRODSKO-POSAVSKA
35430	Benkovac	Okučani	BRODSKO-POSAVSKA
35430	Bijela Stijena	Okučani	BRODSKO-POSAVSKA
35430	Bobare	Okučani	BRODSKO-POSAVSKA
35430	Bodegraj	Okučani	BRODSKO-POSAVSKA
35430	Cage	Okučani	BRODSKO-POSAVSKA
35430	Čaprginci	Okučani	BRODSKO-POSAVSKA
35430	Čovac	Okučani	BRODSKO-POSAVSKA
35432	Medari	Medari	BRODSKO-POSAVSKA
35435	Pivare	Stara Gradiška	BRODSKO-POSAVSKA
35435	Uskoci	Stara Gradiška	BRODSKO-POSAVSKA
35435	Stara Gradiška	Stara Gradiška	BRODSKO-POSAVSKA
35435	Novi Varoš	Stara Gradiška	BRODSKO-POSAVSKA
35435	Gornji Varoš	Stara Gradiška	BRODSKO-POSAVSKA
35435	Donji Varoš	Stara Gradiška	BRODSKO-POSAVSKA
40000	Slemenice	Čakovec	MEĐIMURSKA
40000	Strahoninec	Čakovec	MEĐIMURSKA
40000	Šandorovec	Čakovec	MEĐIMURSKA
40000	Šenkovec	Čakovec	MEĐIMURSKA
40000	Štefanec	Čakovec	MEĐIMURSKA
40000	Totovec	Čakovec	MEĐIMURSKA
40000	Savska Ves	Čakovec	MEĐIMURSKA
40000	Pribislavec	Čakovec	MEĐIMURSKA
40000	Novo Selo Rok	Čakovec	MEĐIMURSKA
40000	Čakovec	Čakovec	MEĐIMURSKA
40000	Ivanovec	Čakovec	MEĐIMURSKA
40000	Kuršanec	Čakovec	MEĐIMURSKA
40000	Mačkovec	Čakovec	MEĐIMURSKA
40000	Mihovljan	Čakovec	MEĐIMURSKA
40000	Novo Selo na Dravi	Čakovec	MEĐIMURSKA
40305	Slakovec	Nedelišče	MEĐIMURSKA
40305	Pušćine	Nedelišče	MEĐIMURSKA
40305	Pretetinec	Nedelišče	MEĐIMURSKA
40305	Nedelišće	Nedelišče	MEĐIMURSKA
40305	Gornji Kuršanec	Nedelišče	MEĐIMURSKA
40305	Dunjkovec	Nedelišče	MEĐIMURSKA
40306	Vukanovec	Macinec	MEĐIMURSKA
40306	Vugrišinec	Macinec	MEĐIMURSKA
40306	Trnovec	Macinec	MEĐIMURSKA
40306	Preseka	Macinec	MEĐIMURSKA
40306	Macinec	Macinec	MEĐIMURSKA
40306	Gornji Mihaljevec	Macinec	MEĐIMURSKA
40306	Gornji Hrašćan	Macinec	MEĐIMURSKA
40306	Gornja Dubrava	Macinec	MEĐIMURSKA
40306	Badličan	Macinec	MEĐIMURSKA
40306	Bogdanovec	Macinec	MEĐIMURSKA
40306	Črečan	Macinec	MEĐIMURSKA
40306	Dragoslavec Breg	Macinec	MEĐIMURSKA
40306	Dragoslavec Selo	Macinec	MEĐIMURSKA
40311	Zasadbreg	Lopatinec	MEĐIMURSKA
40311	Vučetinec	Lopatinec	MEĐIMURSKA
40311	Pleškovec	Lopatinec	MEĐIMURSKA
40311	Okrugli Vrh	Lopatinec	MEĐIMURSKA
40311	Mali Mihaljevec	Lopatinec	MEĐIMURSKA
40311	Lopatinec	Lopatinec	MEĐIMURSKA
40311	Knezovec	Lopatinec	MEĐIMURSKA
40311	Frkanovec	Lopatinec	MEĐIMURSKA
40311	Dragoslavec	Lopatinec	MEĐIMURSKA
40311	Brezje	Lopatinec	MEĐIMURSKA
40312	Stanetinec	Štrigova	MEĐIMURSKA
40312	Sveti Urban	Štrigova	MEĐIMURSKA
40312	Štrigova	Štrigova	MEĐIMURSKA
40312	Tupkovec	Štrigova	MEĐIMURSKA
40312	Železna Gora	Štrigova	MEĐIMURSKA
40312	Robađe	Štrigova	MEĐIMURSKA
40312	Prhovec	Štrigova	MEĐIMURSKA
40312	Prekopa	Štrigova	MEĐIMURSKA
40312	Martinuševec	Štrigova	MEĐIMURSKA
40312	Leskovec	Štrigova	MEĐIMURSKA
40312	Jalšovec	Štrigova	MEĐIMURSKA
40312	Grabrovnik	Štrigova	MEĐIMURSKA
40312	Banfi	Štrigova	MEĐIMURSKA
40313	Kapelščak	Sveti Martin na Muri	MEĐIMURSKA
40313	Lapšina	Sveti Martin na Muri	MEĐIMURSKA
40313	Marof	Sveti Martin na Muri	MEĐIMURSKA
40313	Sv. Martin na Muri	Sveti Martin na Muri	MEĐIMURSKA
40313	Vrhovljan	Sveti Martin na Muri	MEĐIMURSKA
40313	Žabnik	Sveti Martin na Muri	MEĐIMURSKA
40313	Jurovec	Sveti Martin na Muri	MEĐIMURSKA
40313	Jurovčak	Sveti Martin na Muri	MEĐIMURSKA
40313	Brezovec	Sveti Martin na Muri	MEĐIMURSKA
40313	Čestijanec	Sveti Martin na Muri	MEĐIMURSKA
40313	Gornji Koncovčak	Sveti Martin na Muri	MEĐIMURSKA
40313	Gradiščak	Sveti Martin na Muri	MEĐIMURSKA
40313	Grkaveščak	Sveti Martin na Muri	MEĐIMURSKA
40313	Hlapičina	Sveti Martin na Muri	MEĐIMURSKA
40314	Zebanec Selo	Selnica	MEĐIMURSKA
40314	Zaveščak	Selnica	MEĐIMURSKA
40314	Strukovec	Selnica	MEĐIMURSKA
40314	Selnica	Selnica	MEĐIMURSKA
40314	Praporčan	Selnica	MEĐIMURSKA
40314	Plešivica	Selnica	MEĐIMURSKA
40314	Merhatovec	Selnica	MEĐIMURSKA
40314	Gornji Zebanec	Selnica	MEĐIMURSKA
40314	Donji Zebanec	Selnica	MEĐIMURSKA
40314	Donji Koncovčak	Selnica	MEĐIMURSKA
40314	Bukovec	Selnica	MEĐIMURSKA
40315	Peklenica	Mursko Središče	MEĐIMURSKA
40315	Mursko Središće	Mursko Središče	MEĐIMURSKA
40316	Ferketinec	Vratišinec	MEĐIMURSKA
40316	Gornji Kraljevec	Vratišinec	MEĐIMURSKA
40316	Krištanovec	Vratišinec	MEĐIMURSKA
40316	Križovec	Vratišinec	MEĐIMURSKA
40316	Miklavec	Vratišinec	MEĐIMURSKA
40316	Vratišinec	Vratišinec	MEĐIMURSKA
40316	Žiškovec	Vratišinec	MEĐIMURSKA
40317	Sivica	Podturen	MEĐIMURSKA
40317	Podturen	Podturen	MEĐIMURSKA
40317	Celine	Podturen	MEĐIMURSKA
40318	Dekanovec	Dekanovec	MEĐIMURSKA
40318	Domašinec	Dekanovec	MEĐIMURSKA
40318	Novakovec	Dekanovec	MEĐIMURSKA
40318	Turčišće	Dekanovec	MEĐIMURSKA
40319	Belica	Belica	MEĐIMURSKA
40319	Gardinovec	Belica	MEĐIMURSKA
40320	Palinovec	Donji Kraljevec	MEĐIMURSKA
40320	Hodošan	Donji Kraljevec	MEĐIMURSKA
40320	Donji Kraljevec	Donji Kraljevec	MEĐIMURSKA
40320	Donji Hrašćan	Donji Kraljevec	MEĐIMURSKA
40321	Držimurec	Mala Subotica	MEĐIMURSKA
40321	Mala Subotica	Mala Subotica	MEĐIMURSKA
40321	Palovec	Mala Subotica	MEĐIMURSKA
40321	Strelec	Mala Subotica	MEĐIMURSKA
40321	Sveti Križ	Mala Subotica	MEĐIMURSKA
40322	Vularija	Orehovica	MEĐIMURSKA
40322	Podbrest	Orehovica	MEĐIMURSKA
40322	Orehovica	Orehovica	MEĐIMURSKA
40323	Sveti Juraj u Trnju	Prelog	MEĐIMURSKA
40323	Prelog	Prelog	MEĐIMURSKA
40323	Otok	Prelog	MEĐIMURSKA
40323	Donji Pustakovec	Prelog	MEĐIMURSKA
40323	Čehovec	Prelog	MEĐIMURSKA
40323	Cirkovljan	Prelog	MEĐIMURSKA
40324	Goričan	Goričan	MEĐIMURSKA
40325	Oporovec	Draškovec	MEĐIMURSKA
40325	Hemuševec	Draškovec	MEĐIMURSKA
40325	Draškovec	Draškovec	MEĐIMURSKA
40325	Čukovec	Draškovec	MEĐIMURSKA
40326	Donji Mihaljevec	Sveta Marija	MEĐIMURSKA
40326	Sveta Marija	Sveta Marija	MEĐIMURSKA
40327	Donji Vidovec	Donji Vidovec	MEĐIMURSKA
40328	Donja Dubrava	Donja Dubrava	MEĐIMURSKA
40329	Kotoriba	Kotoriba	MEĐIMURSKA
42000	Varaždin	Varaždin	VARAŽDINSKA
42000	Kućan Marof	Varaždin	VARAŽDINSKA
42000	Jalkovec	Varaždin	VARAŽDINSKA
42000	Hrašćica	Varaždin	VARAŽDINSKA
42000	Gornji Kućan	Varaždin	VARAŽDINSKA
42000	Donji Kućan	Varaždin	VARAŽDINSKA
42201	Poljana Biškupečka	Beretinec	VARAŽDINSKA
42201	Ledinec	Beretinec	VARAŽDINSKA
42201	Črešnjevo	Beretinec	VARAŽDINSKA
42201	Beretinec	Beretinec	VARAŽDINSKA
42202	Žabnik	Trnovec Bartolovečki	VARAŽDINSKA
42202	Zbelava	Trnovec Bartolovečki	VARAŽDINSKA
42202	Zamlaka	Trnovec Bartolovečki	VARAŽDINSKA
42202	Trnovec Bartolovečki	Trnovec Bartolovečki	VARAŽDINSKA
42202	Štefanec Bartolovečki	Trnovec Bartolovečki	VARAŽDINSKA
42202	Šemovec	Trnovec Bartolovečki	VARAŽDINSKA
42202	Bartolovec	Trnovec Bartolovečki	VARAŽDINSKA
42203	Pihovec	Jalžabet	VARAŽDINSKA
42203	Novakovec	Jalžabet	VARAŽDINSKA
42203	Leštakovec	Jalžabet	VARAŽDINSKA
42203	Kelemen	Jalžabet	VARAŽDINSKA
42203	Jalžabet	Jalžabet	VARAŽDINSKA
42203	Imbrijovec Jalžabetski	Jalžabet	VARAŽDINSKA
42204	Varaždin Breg	Turčin	VARAŽDINSKA
42204	Turčin	Turčin	VARAŽDINSKA
42204	Tomaševec Biškupečki	Turčin	VARAŽDINSKA
42204	Seketin	Turčin	VARAŽDINSKA
42204	Lužan Biškupečki	Turčin	VARAŽDINSKA
42204	Križanec	Turčin	VARAŽDINSKA
42204	Kaštelanec	Turčin	VARAŽDINSKA
42204	Jakopovec	Turčin	VARAŽDINSKA
42204	Gornji Kneginec	Turčin	VARAŽDINSKA
42204	Donji Kneginec	Turčin	VARAŽDINSKA
42204	Črnec Biškupečki	Turčin	VARAŽDINSKA
42205	Prekno	Vidovec	VARAŽDINSKA
42205	Šijanec	Vidovec	VARAŽDINSKA
42205	Vidovec	Vidovec	VARAŽDINSKA
42205	Zamlača	Vidovec	VARAŽDINSKA
42205	Papinec	Vidovec	VARAŽDINSKA
42205	Nedeljanec	Vidovec	VARAŽDINSKA
42205	Krkanec	Vidovec	VARAŽDINSKA
42205	Gojanec	Vidovec	VARAŽDINSKA
42205	Domitrovec	Vidovec	VARAŽDINSKA
42205	Čargovec	Vidovec	VARAŽDINSKA
42205	Budislavec	Vidovec	VARAŽDINSKA
42206	Strmec Podravski	Petrijanec	VARAŽDINSKA
42206	Petrijanec	Petrijanec	VARAŽDINSKA
42206	Nova Ves Petrijanečka	Petrijanec	VARAŽDINSKA
42206	Majerje	Petrijanec	VARAŽDINSKA
42206	Družbinec	Petrijanec	VARAŽDINSKA
42207	Vratno Donje	Vinica	VARAŽDINSKA
42207	Vinica Breg	Vinica	VARAŽDINSKA
42207	Vinica	Vinica	VARAŽDINSKA
42207	Pešćenica Vinička	Vinica	VARAŽDINSKA
42207	Marčan	Vinica	VARAŽDINSKA
42207	Goruševnjak	Vinica	VARAŽDINSKA
42207	Gornje Ladanje	Vinica	VARAŽDINSKA
42208	Malo Gradišće	Cestica	VARAŽDINSKA
42208	Natkrižovljan	Cestica	VARAŽDINSKA
42208	Otok Virje	Cestica	VARAŽDINSKA
42208	Radovec	Cestica	VARAŽDINSKA
42208	Radovec Polje	Cestica	VARAŽDINSKA
42208	Selci Križovljanski	Cestica	VARAŽDINSKA
42208	Veliki Lovrečan	Cestica	VARAŽDINSKA
42208	Virje Križovljansko	Cestica	VARAŽDINSKA
42208	Vratno Otok	Cestica	VARAŽDINSKA
42208	Mali Lovrečan	Cestica	VARAŽDINSKA
42208	Križovljan Radovečki	Cestica	VARAŽDINSKA
42208	Babinec	Cestica	VARAŽDINSKA
42208	Brezje Dravsko	Cestica	VARAŽDINSKA
42208	Cestica	Cestica	VARAŽDINSKA
42208	Dubrava Križovljanska	Cestica	VARAŽDINSKA
42208	Falinić Breg	Cestica	VARAŽDINSKA
42208	Gornje Vratno	Cestica	VARAŽDINSKA
42208	Jarki	Cestica	VARAŽDINSKA
42208	Kolarovec	Cestica	VARAŽDINSKA
42208	Križanče	Cestica	VARAŽDINSKA
42209	Svibovec Podravski	Sračinec	VARAŽDINSKA
42209	Sračinec	Sračinec	VARAŽDINSKA
42214	Žigrovec	Sveti Ilija	VARAŽDINSKA
42214	Sveti Ilija	Sveti Ilija	VARAŽDINSKA
42214	Krušljevec	Sveti Ilija	VARAŽDINSKA
42214	Doljan	Sveti Ilija	VARAŽDINSKA
42214	Beletinec	Sveti Ilija	VARAŽDINSKA
42220	Oštrice	Novi Marof	VARAŽDINSKA
42220	Paka	Novi Marof	VARAŽDINSKA
42220	Podevčevo	Novi Marof	VARAŽDINSKA
42220	Podrute	Novi Marof	VARAŽDINSKA
42220	Presečno	Novi Marof	VARAŽDINSKA
42220	Remetinec	Novi Marof	VARAŽDINSKA
42220	Strmec Remetinečki	Novi Marof	VARAŽDINSKA
42220	Sudovec	Novi Marof	VARAŽDINSKA
42220	Topličica	Novi Marof	VARAŽDINSKA
42220	Orehovec	Novi Marof	VARAŽDINSKA
42220	Novi Marof	Novi Marof	VARAŽDINSKA
42220	Donje Makojišće	Novi Marof	VARAŽDINSKA
42220	Gornje Makojišće	Novi Marof	VARAŽDINSKA
42220	Grana	Novi Marof	VARAŽDINSKA
42220	Jelenščak	Novi Marof	VARAŽDINSKA
42220	Kamena Gorica	Novi Marof	VARAŽDINSKA
42220	Ključ	Novi Marof	VARAŽDINSKA
42220	Krč	Novi Marof	VARAŽDINSKA
42220	Madžarevo	Novi Marof	VARAŽDINSKA
42220	Možđenec	Novi Marof	VARAŽDINSKA
42222	Rakovec	Ljubeščica	VARAŽDINSKA
42222	Ljubešćica	Ljubeščica	VARAŽDINSKA
42222	Ljubelj Kalnički	Ljubeščica	VARAŽDINSKA
42222	Ljubelj	Ljubeščica	VARAŽDINSKA
42222	Kapela Kalnička	Ljubeščica	VARAŽDINSKA
42222	Čurilovec	Ljubeščica	VARAŽDINSKA
42223	Martinkovec	Varaždinske Toplice	VARAŽDINSKA
42223	Petkovec Toplički	Varaždinske Toplice	VARAŽDINSKA
42223	Pišćanovec	Varaždinske Toplice	VARAŽDINSKA
42223	Retkovec Svibovečki	Varaždinske Toplice	VARAŽDINSKA
42223	Rukljevina	Varaždinske Toplice	VARAŽDINSKA
42223	Svibovec	Varaždinske Toplice	VARAŽDINSKA
42223	Škarnik	Varaždinske Toplice	VARAŽDINSKA
42223	Tuhovec	Varaždinske Toplice	VARAŽDINSKA
42223	Varaždinske Toplice	Varaždinske Toplice	VARAŽDINSKA
42223	Vrtlinovec	Varaždinske Toplice	VARAŽDINSKA
42223	Lukačevec Toplički	Varaždinske Toplice	VARAŽDINSKA
42223	Lovrentovec	Varaždinske Toplice	VARAŽDINSKA
42223	Boričevec Toplički	Varaždinske Toplice	VARAŽDINSKA
42223	Črnile	Varaždinske Toplice	VARAŽDINSKA
42223	Donja Poljana	Varaždinske Toplice	VARAŽDINSKA
42223	Drenovec	Varaždinske Toplice	VARAŽDINSKA
42223	Gornja Poljana	Varaždinske Toplice	VARAŽDINSKA
42223	Grešćevina	Varaždinske Toplice	VARAŽDINSKA
42223	Hrastovec Toplički	Varaždinske Toplice	VARAŽDINSKA
42223	Jalševec Svibovečki	Varaždinske Toplice	VARAŽDINSKA
42223	Jarki Horvatićevi	Varaždinske Toplice	VARAŽDINSKA
42223	Leskovec Toplički	Varaždinske Toplice	VARAŽDINSKA
42224	Vrh Visočki	Visoko	VARAŽDINSKA
42224	Visoko	Visoko	VARAŽDINSKA
42224	Vinično	Visoko	VARAŽDINSKA
42224	Presečno Visočko	Visoko	VARAŽDINSKA
42224	Kračevec	Visoko	VARAŽDINSKA
42224	Đurinovec	Visoko	VARAŽDINSKA
42224	Čanjevo	Visoko	VARAŽDINSKA
42225	Ščepanje	Breznički Hum	VARAŽDINSKA
42225	Radešić	Breznički Hum	VARAŽDINSKA
42225	Krščenovec	Breznički Hum	VARAŽDINSKA
42225	Butkovec	Breznički Hum	VARAŽDINSKA
42225	Breznički Hum	Breznički Hum	VARAŽDINSKA
42225	Breznica	Breznički Hum	VARAŽDINSKA
42226	Tkalec Breznički	Bisag	VARAŽDINSKA
42226	Podvorec	Bisag	VARAŽDINSKA
42226	Mirkovec Breznički	Bisag	VARAŽDINSKA
42226	Jarek Bisaški	Bisag	VARAŽDINSKA
42226	Jales Breznički	Bisag	VARAŽDINSKA
42226	Drašković	Bisag	VARAŽDINSKA
42226	Čret Bisaški	Bisag	VARAŽDINSKA
42226	Borenec	Bisag	VARAŽDINSKA
42226	Bisag	Bisag	VARAŽDINSKA
42230	Segovina	Ludbreg	VARAŽDINSKA
42230	Selnik	Ludbreg	VARAŽDINSKA
42230	Sigetec Ludbreški	Ludbreg	VARAŽDINSKA
42230	Slanje	Ludbreg	VARAŽDINSKA
42230	Slokovec	Ludbreg	VARAŽDINSKA
42230	Vinogradi Ludbreški	Ludbreg	VARAŽDINSKA
42230	Poljanec	Ludbreg	VARAŽDINSKA
42230	Ludbreg	Ludbreg	VARAŽDINSKA
42230	Kućan Ludbreški	Ludbreg	VARAŽDINSKA
42230	Apatija	Ludbreg	VARAŽDINSKA
42230	Bolfan	Ludbreg	VARAŽDINSKA
42230	Čukovec	Ludbreg	VARAŽDINSKA
42230	Globočec Ludbreški	Ludbreg	VARAŽDINSKA
42230	Hrastovsko	Ludbreg	VARAŽDINSKA
42230	Križovljan	Ludbreg	VARAŽDINSKA
42231	Županec	Mali Bukovec	VARAŽDINSKA
42231	Veliki Bukovec	Mali Bukovec	VARAŽDINSKA
42231	Sveti Petar Ludbreški	Mali Bukovec	VARAŽDINSKA
42231	Novo Selo Podravsko	Mali Bukovec	VARAŽDINSKA
42231	Martinić	Mali Bukovec	VARAŽDINSKA
42231	Mali Bukovec	Mali Bukovec	VARAŽDINSKA
42231	Lunjkovec	Mali Bukovec	VARAŽDINSKA
42231	Kapela	Mali Bukovec	VARAŽDINSKA
42231	Dubovica	Mali Bukovec	VARAŽDINSKA
42232	Vrbanovec	Donji Martijanec	VARAŽDINSKA
42232	Sudovčina	Donji Martijanec	VARAŽDINSKA
42232	Rivalno	Donji Martijanec	VARAŽDINSKA
42232	Madaraševec	Donji Martijanec	VARAŽDINSKA
42232	Hrastovljan	Donji Martijanec	VARAŽDINSKA
42232	Gornji Martijanec	Donji Martijanec	VARAŽDINSKA
42232	Donji Martijanec	Donji Martijanec	VARAŽDINSKA
42232	Čičkovina	Donji Martijanec	VARAŽDINSKA
42233	Sveti Đurđ	Sveti Đurđ	VARAŽDINSKA
42233	Struga	Sveti Đurđ	VARAŽDINSKA
42233	Sesvete Ludbreške	Sveti Đurđ	VARAŽDINSKA
42233	Priles	Sveti Đurđ	VARAŽDINSKA
42233	Obrankovec	Sveti Đurđ	VARAŽDINSKA
42233	Luka Ludbreška	Sveti Đurđ	VARAŽDINSKA
42233	Komarnica Ludbreška	Sveti Đurđ	VARAŽDINSKA
42233	Karlovec Ludbreški	Sveti Đurđ	VARAŽDINSKA
42233	Hrženica	Sveti Đurđ	VARAŽDINSKA
42240	Lančić	Ivanec	VARAŽDINSKA
42240	Prigorec	Ivanec	VARAŽDINSKA
42240	Punikve	Ivanec	VARAŽDINSKA
42240	Ribić Breg	Ivanec	VARAŽDINSKA
42240	Salinovec	Ivanec	VARAŽDINSKA
42240	Vitešinec	Ivanec	VARAŽDINSKA
42240	Vuglovec	Ivanec	VARAŽDINSKA
42240	Knapić	Ivanec	VARAŽDINSKA
42240	Kaniža	Ivanec	VARAŽDINSKA
42240	Bedenec	Ivanec	VARAŽDINSKA
42240	Gečkovec	Ivanec	VARAŽDINSKA
42240	Ivanec	Ivanec	VARAŽDINSKA
42240	Ivanečka Željeznica	Ivanec	VARAŽDINSKA
42240	Ivanečki Vrhovec	Ivanec	VARAŽDINSKA
42240	Ivanečko Naselje	Ivanec	VARAŽDINSKA
42240	Jerovec	Ivanec	VARAŽDINSKA
42242	Radovan	Radovan	VARAŽDINSKA
42242	Seljanec	Radovan	VARAŽDINSKA
42242	Stažnjevec	Radovan	VARAŽDINSKA
42242	Škriljevec	Radovan	VARAŽDINSKA
42242	Tužno	Radovan	VARAŽDINSKA
42242	Završje Podbelsko	Radovan	VARAŽDINSKA
42242	Željeznica	Radovan	VARAŽDINSKA
42242	Pece	Radovan	VARAŽDINSKA
42242	Osečka	Radovan	VARAŽDINSKA
42242	Bela	Radovan	VARAŽDINSKA
42242	Cerje Tužno	Radovan	VARAŽDINSKA
42242	Filipići	Radovan	VARAŽDINSKA
42242	Gačice	Radovan	VARAŽDINSKA
42242	Lovrečan	Radovan	VARAŽDINSKA
42242	Lukavec	Radovan	VARAŽDINSKA
42242	Margečan	Radovan	VARAŽDINSKA
42243	Kapelec	Maruševec	VARAŽDINSKA
42243	Korenjak	Maruševec	VARAŽDINSKA
42243	Koretinec	Maruševec	VARAŽDINSKA
42243	Koškovec	Maruševec	VARAŽDINSKA
42243	Maruševec	Maruševec	VARAŽDINSKA
42243	Novaki	Maruševec	VARAŽDINSKA
42243	Selnik	Maruševec	VARAŽDINSKA
42243	Jurketinec	Maruševec	VARAŽDINSKA
42243	Greda	Maruševec	VARAŽDINSKA
42243	Bikovec	Maruševec	VARAŽDINSKA
42243	Biljevec	Maruševec	VARAŽDINSKA
42243	Brodarovec	Maruševec	VARAŽDINSKA
42243	Cerje Nebojse	Maruševec	VARAŽDINSKA
42243	Čalinec	Maruševec	VARAŽDINSKA
42243	Donje Ladanje	Maruševec	VARAŽDINSKA
42243	Druškovec	Maruševec	VARAŽDINSKA
42244	Vukovoj	Klenovnik	VARAŽDINSKA
42244	Plemenšćina	Klenovnik	VARAŽDINSKA
42244	Lipovnik	Klenovnik	VARAŽDINSKA
42244	Klenovnik	Klenovnik	VARAŽDINSKA
42244	Horvatsko	Klenovnik	VARAŽDINSKA
42244	Goranec	Klenovnik	VARAŽDINSKA
42244	Dubravec	Klenovnik	VARAŽDINSKA
42245	Slivarsko	Donja Voća	VARAŽDINSKA
42245	Rijeka Voćanska	Donja Voća	VARAŽDINSKA
42245	Plitvica Voćanska	Donja Voća	VARAŽDINSKA
42245	Jelovec Voćanski	Donja Voća	VARAŽDINSKA
42245	Gornja Voća	Donja Voća	VARAŽDINSKA
42245	Fotez Breg	Donja Voća	VARAŽDINSKA
42245	Donja Voća	Donja Voća	VARAŽDINSKA
42245	Budinščak	Donja Voća	VARAŽDINSKA
42250	Žarovnica	Lepoglava	VARAŽDINSKA
42250	Vulišinec	Lepoglava	VARAŽDINSKA
42250	Viletinec	Lepoglava	VARAŽDINSKA
42250	Očura	Lepoglava	VARAŽDINSKA
42250	Muričevec	Lepoglava	VARAŽDINSKA
42250	Lepoglava	Lepoglava	VARAŽDINSKA
42250	Kameničko Podgorje	Lepoglava	VARAŽDINSKA
42250	Kamenički Vrhovec	Lepoglava	VARAŽDINSKA
42250	Kamenica	Lepoglava	VARAŽDINSKA
42250	Crkovec	Lepoglava	VARAŽDINSKA
42253	Rinkovec	Bednja	VARAŽDINSKA
42253	Šaša	Bednja	VARAŽDINSKA
42253	Šinkovica Bednjanska	Bednja	VARAŽDINSKA
42253	Šinkovica Šaška	Bednja	VARAŽDINSKA
42253	Trakošćan	Bednja	VARAŽDINSKA
42253	Veliki Gorenec	Bednja	VARAŽDINSKA
42253	Vranojelje	Bednja	VARAŽDINSKA
42253	Vrbno	Bednja	VARAŽDINSKA
42253	Vrhovec Bednjanski	Bednja	VARAŽDINSKA
42253	Purga Bednjanska	Bednja	VARAŽDINSKA
42253	Prebukovje	Bednja	VARAŽDINSKA
42253	Podgorje Bednjansko	Bednja	VARAŽDINSKA
42253	Bednja	Bednja	VARAŽDINSKA
42253	Benkovec	Bednja	VARAŽDINSKA
42253	Brezova Gora	Bednja	VARAŽDINSKA
42253	Ježovec	Bednja	VARAŽDINSKA
42253	Mali Gorenec	Bednja	VARAŽDINSKA
42253	Meljan	Bednja	VARAŽDINSKA
42253	Osonjak	Bednja	VARAŽDINSKA
42253	Pašnik	Bednja	VARAŽDINSKA
42253	Pleš	Bednja	VARAŽDINSKA
42254	Pleš	Trakošćan	VARAŽDINSKA
42255	Zlogonje	Donja Višnjica	VARAŽDINSKA
42255	Zalužje	Donja Višnjica	VARAŽDINSKA
42255	Jazbina Višnjička	Donja Višnjica	VARAŽDINSKA
42255	Jazbina Cvetlinska	Donja Višnjica	VARAŽDINSKA
42255	Jamno	Donja Višnjica	VARAŽDINSKA
42255	Gornja Višnjica	Donja Višnjica	VARAŽDINSKA
42255	Donja Višnjica	Donja Višnjica	VARAŽDINSKA
42255	Cvetlin	Donja Višnjica	VARAŽDINSKA
42255	Bednjica	Donja Višnjica	VARAŽDINSKA
43000	Patkovac	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Plavnice Gornje	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Plavnice Stare	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Prespa	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Prokljuvani	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Puričani	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Stari Pavljani	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Trojstveni Markovac	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Veliko Korenovo	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Zvijerci	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Ždralovi	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Obrovnica	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Novoseljani	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Novi Pavljani	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Bjelovar	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Brezovac	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Ciglena	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Ćurlovac	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Galovac	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Gornji Tomaš	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Kokinac	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Kupinovac	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Letičani	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Mala Ciglena	Bjelovar	BJELOVARSKO-BILOGORSKA
43000	Malo Korenovo	Bjelovar	BJELOVARSKO-BILOGORSKA
43202	Zrinski Topolovac	Zrinski Topolovac	BJELOVARSKO-BILOGORSKA
43202	Tvrda Reka	Zrinski Topolovac	BJELOVARSKO-BILOGORSKA
43202	Križ Gornji	Zrinski Topolovac	BJELOVARSKO-BILOGORSKA
43202	Jakopovac	Zrinski Topolovac	BJELOVARSKO-BILOGORSKA
43203	Pavlin Kloštar	Kapela	BJELOVARSKO-BILOGORSKA
43203	Poljančani	Kapela	BJELOVARSKO-BILOGORSKA
43203	Sredice Gornje	Kapela	BJELOVARSKO-BILOGORSKA
43203	Srednja Diklenica	Kapela	BJELOVARSKO-BILOGORSKA
43203	Srednji Mosti	Kapela	BJELOVARSKO-BILOGORSKA
43203	Stanići	Kapela	BJELOVARSKO-BILOGORSKA
43203	Stara Diklenica	Kapela	BJELOVARSKO-BILOGORSKA
43203	Starčevljani	Kapela	BJELOVARSKO-BILOGORSKA
43203	Stari Skucani	Kapela	BJELOVARSKO-BILOGORSKA
43203	Novi Skucani	Kapela	BJELOVARSKO-BILOGORSKA
43203	Nova Diklenica	Kapela	BJELOVARSKO-BILOGORSKA
43203	Babotok	Kapela	BJELOVARSKO-BILOGORSKA
43203	Botinac	Kapela	BJELOVARSKO-BILOGORSKA
43203	Donji Mosti	Kapela	BJELOVARSKO-BILOGORSKA
43203	Gornje Zdjelice	Kapela	BJELOVARSKO-BILOGORSKA
43203	Gornji Mosti	Kapela	BJELOVARSKO-BILOGORSKA
43203	Jabučeta	Kapela	BJELOVARSKO-BILOGORSKA
43203	Kapela	Kapela	BJELOVARSKO-BILOGORSKA
43203	Lalići	Kapela	BJELOVARSKO-BILOGORSKA
43203	Lipovo Brdo	Kapela	BJELOVARSKO-BILOGORSKA
43211	Prekobrdo	Predavac	BJELOVARSKO-BILOGORSKA
43211	Prnjavor	Predavac	BJELOVARSKO-BILOGORSKA
43211	Reškovci	Predavac	BJELOVARSKO-BILOGORSKA
43211	Šiptari	Predavac	BJELOVARSKO-BILOGORSKA
43211	Visovi	Predavac	BJELOVARSKO-BILOGORSKA
43211	Predavac	Predavac	BJELOVARSKO-BILOGORSKA
43211	Podgorci	Predavac	BJELOVARSKO-BILOGORSKA
43211	Dijebala	Predavac	BJELOVARSKO-BILOGORSKA
43211	Klokočevac	Predavac	BJELOVARSKO-BILOGORSKA
43211	Kobasičari	Predavac	BJELOVARSKO-BILOGORSKA
43211	Lipovčani	Predavac	BJELOVARSKO-BILOGORSKA
43211	Marići	Predavac	BJELOVARSKO-BILOGORSKA
43212	Žabjak	Rovišće	BJELOVARSKO-BILOGORSKA
43212	Tuk	Rovišće	BJELOVARSKO-BILOGORSKA
43212	Rovišće	Rovišće	BJELOVARSKO-BILOGORSKA
43212	Markovac Križevački	Rovišće	BJELOVARSKO-BILOGORSKA
43212	Kraljevac	Rovišće	BJELOVARSKO-BILOGORSKA
43212	Kovačevac	Rovišće	BJELOVARSKO-BILOGORSKA
43212	Kakinac	Rovišće	BJELOVARSKO-BILOGORSKA
43212	Draganić	Rovišće	BJELOVARSKO-BILOGORSKA
43212	Domankuš	Rovišće	BJELOVARSKO-BILOGORSKA
43226	Vrbica	Veliko Trojstvo	BJELOVARSKO-BILOGORSKA
43226	Višnjevac	Veliko Trojstvo	BJELOVARSKO-BILOGORSKA
43226	Veliko Trojstvo	Veliko Trojstvo	BJELOVARSKO-BILOGORSKA
43226	Paulovac	Veliko Trojstvo	BJELOVARSKO-BILOGORSKA
43226	Martinac	Veliko Trojstvo	BJELOVARSKO-BILOGORSKA
43226	Malo Trojstvo	Veliko Trojstvo	BJELOVARSKO-BILOGORSKA
43226	Maglenča	Veliko Trojstvo	BJELOVARSKO-BILOGORSKA
43226	Kegljevac	Veliko Trojstvo	BJELOVARSKO-BILOGORSKA
43226	Grginac	Veliko Trojstvo	BJELOVARSKO-BILOGORSKA
43226	Dominkovica	Veliko Trojstvo	BJELOVARSKO-BILOGORSKA
43227	Šandrovac	Šandrovac	BJELOVARSKO-BILOGORSKA
43227	Pupelica	Šandrovac	BJELOVARSKO-BILOGORSKA
43227	Jasenik	Šandrovac	BJELOVARSKO-BILOGORSKA
43231	Utiskani	Ivanska	BJELOVARSKO-BILOGORSKA
43231	Srijedska	Ivanska	BJELOVARSKO-BILOGORSKA
43231	Rastovac	Ivanska	BJELOVARSKO-BILOGORSKA
43231	Križic	Ivanska	BJELOVARSKO-BILOGORSKA
43231	Ivanska	Ivanska	BJELOVARSKO-BILOGORSKA
43231	Đurđic	Ivanska	BJELOVARSKO-BILOGORSKA
43232	Šimljanica	Berek	BJELOVARSKO-BILOGORSKA
43232	Šimljana	Berek	BJELOVARSKO-BILOGORSKA
43232	Stara Ploščica	Berek	BJELOVARSKO-BILOGORSKA
43232	Samarica	Berek	BJELOVARSKO-BILOGORSKA
43232	Ruškovac	Berek	BJELOVARSKO-BILOGORSKA
43232	Potok	Berek	BJELOVARSKO-BILOGORSKA
43232	Krivaja	Berek	BJELOVARSKO-BILOGORSKA
43232	Gornja Petrička	Berek	BJELOVARSKO-BILOGORSKA
43232	Donja Petrička	Berek	BJELOVARSKO-BILOGORSKA
43232	Berek	Berek	BJELOVARSKO-BILOGORSKA
43232	Babinac	Berek	BJELOVARSKO-BILOGORSKA
43233	Veliki Prokop	Trnovitički Popovac	BJELOVARSKO-BILOGORSKA
43233	Trnovitički Popovac	Trnovitički Popovac	BJELOVARSKO-BILOGORSKA
43233	Šimljanik	Trnovitički Popovac	BJELOVARSKO-BILOGORSKA
43233	Podgarić	Trnovitički Popovac	BJELOVARSKO-BILOGORSKA
43233	Oštri Zid	Trnovitički Popovac	BJELOVARSKO-BILOGORSKA
43233	Novo Selo Garešničko	Trnovitički Popovac	BJELOVARSKO-BILOGORSKA
43233	Kostanjevac	Trnovitički Popovac	BJELOVARSKO-BILOGORSKA
43233	Gornja Garešnica	Trnovitički Popovac	BJELOVARSKO-BILOGORSKA
43233	Begovača	Trnovitički Popovac	BJELOVARSKO-BILOGORSKA
43240	Pavličani	Čazma	BJELOVARSKO-BILOGORSKA
43240	Palančani	Čazma	BJELOVARSKO-BILOGORSKA
43240	Općevac	Čazma	BJELOVARSKO-BILOGORSKA
43240	Novo Selo	Čazma	BJELOVARSKO-BILOGORSKA
43240	Milaševac	Čazma	BJELOVARSKO-BILOGORSKA
43240	Pobjenik	Čazma	BJELOVARSKO-BILOGORSKA
43240	Pobrđani	Čazma	BJELOVARSKO-BILOGORSKA
43240	Prnjarovac	Čazma	BJELOVARSKO-BILOGORSKA
43240	Prokljuvani	Čazma	BJELOVARSKO-BILOGORSKA
43240	Sovari	Čazma	BJELOVARSKO-BILOGORSKA
43240	Suhaja	Čazma	BJELOVARSKO-BILOGORSKA
43240	Vrtlinska	Čazma	BJELOVARSKO-BILOGORSKA
43240	Vučani	Čazma	BJELOVARSKO-BILOGORSKA
43240	Martinac	Čazma	BJELOVARSKO-BILOGORSKA
43240	Marčani	Čazma	BJELOVARSKO-BILOGORSKA
43240	Grabovnica	Čazma	BJELOVARSKO-BILOGORSKA
43240	Andigola	Čazma	BJELOVARSKO-BILOGORSKA
43240	Bosiljevo	Čazma	BJELOVARSKO-BILOGORSKA
43240	Cerina	Čazma	BJELOVARSKO-BILOGORSKA
43240	Čazma	Čazma	BJELOVARSKO-BILOGORSKA
43240	Dapci	Čazma	BJELOVARSKO-BILOGORSKA
43240	Dereza	Čazma	BJELOVARSKO-BILOGORSKA
43240	Donji Dragičevci	Čazma	BJELOVARSKO-BILOGORSKA
43240	Donji Lipovčani	Čazma	BJELOVARSKO-BILOGORSKA
43240	Donji Miklouš	Čazma	BJELOVARSKO-BILOGORSKA
43240	Gornji Dragičevci	Čazma	BJELOVARSKO-BILOGORSKA
43240	Gornji Lipovčani	Čazma	BJELOVARSKO-BILOGORSKA
43240	Gornji Miklouš	Čazma	BJELOVARSKO-BILOGORSKA
43240	Grabik	Čazma	BJELOVARSKO-BILOGORSKA
43245	Zdenčec	Gornji Draganec	BJELOVARSKO-BILOGORSKA
43245	Vagovina	Gornji Draganec	BJELOVARSKO-BILOGORSKA
43245	Siščani	Gornji Draganec	BJELOVARSKO-BILOGORSKA
43245	Komuševac	Gornji Draganec	BJELOVARSKO-BILOGORSKA
43245	Gornji Draganec	Gornji Draganec	BJELOVARSKO-BILOGORSKA
43245	Donji Draganec	Gornji Draganec	BJELOVARSKO-BILOGORSKA
43245	Bojana	Gornji Draganec	BJELOVARSKO-BILOGORSKA
43246	Štefanje	Štefanje	BJELOVARSKO-BILOGORSKA
43246	Staro Štefanje	Štefanje	BJELOVARSKO-BILOGORSKA
43246	Starine	Štefanje	BJELOVARSKO-BILOGORSKA
43246	Laminac	Štefanje	BJELOVARSKO-BILOGORSKA
43246	Gornja Šušnjara	Štefanje	BJELOVARSKO-BILOGORSKA
43246	Donja Šušnjara	Štefanje	BJELOVARSKO-BILOGORSKA
43246	Daskatica	Štefanje	BJELOVARSKO-BILOGORSKA
43246	Blatnica	Štefanje	BJELOVARSKO-BILOGORSKA
43247	Paljevine	Narta	BJELOVARSKO-BILOGORSKA
43247	Narta	Narta	BJELOVARSKO-BILOGORSKA
43247	Kolarevo Selo	Narta	BJELOVARSKO-BILOGORSKA
43251	Gudovac	Gudovac	BJELOVARSKO-BILOGORSKA
43252	Stančići	Prgomelje	BJELOVARSKO-BILOGORSKA
43252	Raić	Prgomelje	BJELOVARSKO-BILOGORSKA
43252	Prgomelje	Prgomelje	BJELOVARSKO-BILOGORSKA
43252	Breza	Prgomelje	BJELOVARSKO-BILOGORSKA
43270	Zrinska	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43270	Veliki Grđevac	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43270	Topolovica	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43270	Sibenik	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43270	Pavlovac	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43270	Mali Grđevac	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43270	Mala Pisanica	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43270	Gornja Kovačica	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43270	Dražica	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43270	Donja Kovačica	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43270	Cremušina	Veliki Grđevac	BJELOVARSKO-BILOGORSKA
43271	Velika Pisanica	Velika Pisanica	BJELOVARSKO-BILOGORSKA
43271	Polum	Velika Pisanica	BJELOVARSKO-BILOGORSKA
43271	Nova Pisanica	Velika Pisanica	BJELOVARSKO-BILOGORSKA
43271	Čađavac	Velika Pisanica	BJELOVARSKO-BILOGORSKA
43271	Bedenička	Velika Pisanica	BJELOVARSKO-BILOGORSKA
43271	Bačkovica	Velika Pisanica	BJELOVARSKO-BILOGORSKA
43272	Tociljevac	Nova Rača	BJELOVARSKO-BILOGORSKA
43272	Stara Rača	Nova Rača	BJELOVARSKO-BILOGORSKA
43272	Slovinska Kovačica	Nova Rača	BJELOVARSKO-BILOGORSKA
43272	Sasovac	Nova Rača	BJELOVARSKO-BILOGORSKA
43272	Orlovac	Nova Rača	BJELOVARSKO-BILOGORSKA
43272	Nova Rača	Nova Rača	BJELOVARSKO-BILOGORSKA
43272	Nevinac	Nova Rača	BJELOVARSKO-BILOGORSKA
43272	Međurača	Nova Rača	BJELOVARSKO-BILOGORSKA
43272	Kozarevac Račanski	Nova Rača	BJELOVARSKO-BILOGORSKA
43272	Drljanovac	Nova Rača	BJELOVARSKO-BILOGORSKA
43272	Dautan	Nova Rača	BJELOVARSKO-BILOGORSKA
43273	Ribnjačka	Bulinac	BJELOVARSKO-BILOGORSKA
43273	Lasovac-Brdo	Bulinac	BJELOVARSKO-BILOGORSKA
43273	Lasovac	Bulinac	BJELOVARSKO-BILOGORSKA
43273	Bulinac	Bulinac	BJELOVARSKO-BILOGORSKA
43273	Bedenik	Bulinac	BJELOVARSKO-BILOGORSKA
43273	Babinac	Bulinac	BJELOVARSKO-BILOGORSKA
43274	Severin	Severin	BJELOVARSKO-BILOGORSKA
43274	Ravneš	Severin	BJELOVARSKO-BILOGORSKA
43274	Orovac	Severin	BJELOVARSKO-BILOGORSKA
43274	Kašljavac	Severin	BJELOVARSKO-BILOGORSKA
43280	Zdenčac	Garešnica	BJELOVARSKO-BILOGORSKA
43280	Veliki Pašijan	Garešnica	BJELOVARSKO-BILOGORSKA
43280	Tomašica	Garešnica	BJELOVARSKO-BILOGORSKA
43280	Mali Pašijan	Garešnica	BJELOVARSKO-BILOGORSKA
43280	Kapelica	Garešnica	BJELOVARSKO-BILOGORSKA
43280	Kajgana	Garešnica	BJELOVARSKO-BILOGORSKA
43280	Hrastovac	Garešnica	BJELOVARSKO-BILOGORSKA
43280	Garešnički Brestovac	Garešnica	BJELOVARSKO-BILOGORSKA
43280	Garešnica	Garešnica	BJELOVARSKO-BILOGORSKA
43280	Dišnik	Garešnica	BJELOVARSKO-BILOGORSKA
43280	Ciglenica	Garešnica	BJELOVARSKO-BILOGORSKA
43282	Veliko Vukovje	Veliko Vukovje	BJELOVARSKO-BILOGORSKA
43282	Velika Bršljanica	Veliko Vukovje	BJELOVARSKO-BILOGORSKA
43282	Rogoža	Veliko Vukovje	BJELOVARSKO-BILOGORSKA
43282	Mala Bršljanica	Veliko Vukovje	BJELOVARSKO-BILOGORSKA
43283	Malo Vukovje	Kaniška Iva	BJELOVARSKO-BILOGORSKA
43283	Kaniška Iva	Kaniška Iva	BJELOVARSKO-BILOGORSKA
43284	Velika Trnava	Hercegovac	BJELOVARSKO-BILOGORSKA
43284	Palešnik	Hercegovac	BJELOVARSKO-BILOGORSKA
43284	Ladislav	Hercegovac	BJELOVARSKO-BILOGORSKA
43284	Ilovski Klokočevac	Hercegovac	BJELOVARSKO-BILOGORSKA
43284	Hercegovac	Hercegovac	BJELOVARSKO-BILOGORSKA
43285	Velika Trnovitica	Velika Trnovitica	BJELOVARSKO-BILOGORSKA
43285	Velika Mlinska	Velika Trnovitica	BJELOVARSKO-BILOGORSKA
43285	Nova Ploščica	Velika Trnovitica	BJELOVARSKO-BILOGORSKA
43285	Mlinski Vinogradi	Velika Trnovitica	BJELOVARSKO-BILOGORSKA
43285	Mala Trnovitica	Velika Trnovitica	BJELOVARSKO-BILOGORSKA
43285	Mala Mlinska	Velika Trnovitica	BJELOVARSKO-BILOGORSKA
43285	Gornja Trnovitica	Velika Trnovitica	BJELOVARSKO-BILOGORSKA
43285	Gornja Ploščica	Velika Trnovitica	BJELOVARSKO-BILOGORSKA
43290	Poljani	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Treglava	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Velika Barna	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Velika Dapčevica	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Velika Jasenovača	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Velika Peratovica	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Mala Peratovica	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Mala Jasenovača	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Mala Barna	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Lončarica	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Grubišno Polje	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Grbavac	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Gornja Rašenica	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Donja Rašenica	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43290	Brđani Dapčevački	Grubišno Polje	BJELOVARSKO-BILOGORSKA
43293	Veliki Zdenci	Veliki Zdenci	BJELOVARSKO-BILOGORSKA
43293	Orlovac Zdenački	Veliki Zdenci	BJELOVARSKO-BILOGORSKA
43293	Mali Zdenci	Veliki Zdenci	BJELOVARSKO-BILOGORSKA
43500	Ivanovo Polje	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Kip	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Lipovac Majur	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Ljudevit Selo	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Markovac	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Pakrani	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Srednji Borki	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Šibovac	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Vrbovac	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Vukovije	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Gornji Daruvar	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Gornji Borki	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Batinjani	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Batinjska Rijeka	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Bijela	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Daruvar	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Daruvarski Vinogradi	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Dobra Kuća	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Doljani	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Donji Borki	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Donji Daruvar	Daruvar	BJELOVARSKO-BILOGORSKA
43500	Golubnjak	Daruvar	BJELOVARSKO-BILOGORSKA
43504	Turčević Polje	Ivanovo Selo	BJELOVARSKO-BILOGORSKA
43504	Rastovac	Ivanovo Selo	BJELOVARSKO-BILOGORSKA
43504	Munije	Ivanovo Selo	BJELOVARSKO-BILOGORSKA
43504	Mala Dapčevica	Ivanovo Selo	BJELOVARSKO-BILOGORSKA
43504	Ivanovo Selo	Ivanovo Selo	BJELOVARSKO-BILOGORSKA
43504	Dijakovac	Ivanovo Selo	BJELOVARSKO-BILOGORSKA
43505	Šuplja Lipa	Končanica	BJELOVARSKO-BILOGORSKA
43505	Stražanac	Končanica	BJELOVARSKO-BILOGORSKA
43505	Otkopi	Končanica	BJELOVARSKO-BILOGORSKA
43505	Končanica	Končanica	BJELOVARSKO-BILOGORSKA
43505	Dioš	Končanica	BJELOVARSKO-BILOGORSKA
43505	Brestovačka Brda	Končanica	BJELOVARSKO-BILOGORSKA
43505	Brestovac Daruvarski	Končanica	BJELOVARSKO-BILOGORSKA
43505	Boriš	Končanica	BJELOVARSKO-BILOGORSKA
43506	Trojeglava	Dežanovac	BJELOVARSKO-BILOGORSKA
43506	Sokolovac	Dežanovac	BJELOVARSKO-BILOGORSKA
43506	Kreštelovac	Dežanovac	BJELOVARSKO-BILOGORSKA
43506	Kaštel Dežanovački	Dežanovac	BJELOVARSKO-BILOGORSKA
43506	Imsovac	Dežanovac	BJELOVARSKO-BILOGORSKA
43506	Goveđe Polje	Dežanovac	BJELOVARSKO-BILOGORSKA
43506	Gornji Sređani	Dežanovac	BJELOVARSKO-BILOGORSKA
43506	Drlež	Dežanovac	BJELOVARSKO-BILOGORSKA
43506	Donji Sređani	Dežanovac	BJELOVARSKO-BILOGORSKA
43506	Dežanovac	Dežanovac	BJELOVARSKO-BILOGORSKA
43507	Uljanik	Uljanik	BJELOVARSKO-BILOGORSKA
43507	Uljanički Brijeg	Uljanik	BJELOVARSKO-BILOGORSKA
43507	Gornji Uljanik	Uljanik	BJELOVARSKO-BILOGORSKA
43507	Duhovi	Uljanik	BJELOVARSKO-BILOGORSKA
43507	Blagorodovac	Uljanik	BJELOVARSKO-BILOGORSKA
43531	Veliki Miletinac	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43531	Veliki Bastaji	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43531	Škodinovac	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43531	Mali Miletinac	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43531	Mali Bastaji	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43531	Koreničani	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43531	Bastajski Brđani	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43531	Maslenjača	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43531	Gornja Vrijeska	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43531	Donja Vrijeska	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43531	Borova Kosa	Veliki Bastaji	BJELOVARSKO-BILOGORSKA
43532	Potočani	Đulovac	BJELOVARSKO-BILOGORSKA
43532	Puklica	Đulovac	BJELOVARSKO-BILOGORSKA
43532	Removac	Đulovac	BJELOVARSKO-BILOGORSKA
43532	Stara Krivaja	Đulovac	BJELOVARSKO-BILOGORSKA
43532	Nova Krivaja	Đulovac	BJELOVARSKO-BILOGORSKA
43532	Mala Babina Gora	Đulovac	BJELOVARSKO-BILOGORSKA
43532	Katinac	Đulovac	BJELOVARSKO-BILOGORSKA
43532	Jasenaš	Đulovac	BJELOVARSKO-BILOGORSKA
43532	Gornje Cjepidlake	Đulovac	BJELOVARSKO-BILOGORSKA
43532	Đulovac	Đulovac	BJELOVARSKO-BILOGORSKA
43532	Donje Cjepidlake	Đulovac	BJELOVARSKO-BILOGORSKA
43541	Sirač	Sirač	BJELOVARSKO-BILOGORSKA
43541	Miljanovac	Sirač	BJELOVARSKO-BILOGORSKA
43541	Barica	Sirač	BJELOVARSKO-BILOGORSKA
44000	Žirčica	Sisak	SISAČKO-MOSLAVAČKA
44000	Žabno	Sisak	SISAČKO-MOSLAVAČKA
44000	Tišina Kaptolska	Sisak	SISAČKO-MOSLAVAČKA
44000	Tišina Erdedska	Sisak	SISAČKO-MOSLAVAČKA
44000	Stupno	Sisak	SISAČKO-MOSLAVAČKA
44000	Strelečko	Sisak	SISAČKO-MOSLAVAČKA
44000	Staro Pračno	Sisak	SISAČKO-MOSLAVAČKA
44000	Sisak	Sisak	SISAČKO-MOSLAVAČKA
44000	Setuš	Sisak	SISAČKO-MOSLAVAČKA
44000	Palanjek	Sisak	SISAČKO-MOSLAVAČKA
44000	Odra Sisačka	Sisak	SISAČKO-MOSLAVAČKA
44000	Ljubljanica	Sisak	SISAČKO-MOSLAVAČKA
44000	Hrastelnica	Sisak	SISAČKO-MOSLAVAČKA
44000	Bok Palanječki	Sisak	SISAČKO-MOSLAVAČKA
44010	Novo Selo	Sisak-Caprag	SISAČKO-MOSLAVAČKA
44010	Novo Pračno	Sisak-Caprag	SISAČKO-MOSLAVAČKA
44010	Crnac	Sisak-Caprag	SISAČKO-MOSLAVAČKA
44201	Mahovo	Martinska Ves	SISAČKO-MOSLAVAČKA
44201	Lijevo Željezno	Martinska Ves	SISAČKO-MOSLAVAČKA
44201	Lijevo Trebarjevo	Martinska Ves	SISAČKO-MOSLAVAČKA
44201	Lijeva Martinska Ves	Martinska Ves	SISAČKO-MOSLAVAČKA
44201	Lijeva Luka	Martinska Ves	SISAČKO-MOSLAVAČKA
44201	Jezero Posavsko	Martinska Ves	SISAČKO-MOSLAVAČKA
44201	Desno Željezno	Martinska Ves	SISAČKO-MOSLAVAČKA
44201	Desno Trebarjevo	Martinska Ves	SISAČKO-MOSLAVAČKA
44201	Desni Dubrovčak	Martinska Ves	SISAČKO-MOSLAVAČKA
44201	Desna Martinska Ves	Martinska Ves	SISAČKO-MOSLAVAČKA
44202	Topolovac	Topolovac	SISAČKO-MOSLAVAČKA
44202	Prelošćica	Topolovac	SISAČKO-MOSLAVAČKA
44202	Novo Selo Palanječko	Topolovac	SISAČKO-MOSLAVAČKA
44202	Budaševo	Topolovac	SISAČKO-MOSLAVAČKA
44203	Veliko Svinjičko	Gušće	SISAČKO-MOSLAVAČKA
44203	Lukavec Posavski	Gušće	SISAČKO-MOSLAVAČKA
44203	Gušće	Gušće	SISAČKO-MOSLAVAČKA
44204	Tremušnjak	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Prnjavor Čuntićki	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Miočinovići	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Mačkovo Selo	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Kraljevčani	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Klinac	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Jabukovac	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Hrvatski Čuntić	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Gornja Pastuša	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Gornja Mlinoga	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Begovići	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Čuntić	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Deanovići	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Dodoši	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Donja Mlinoga	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Donja Pastuša	Jabukovac	SISAČKO-MOSLAVAČKA
44204	Dragotinci	Jabukovac	SISAČKO-MOSLAVAČKA
44205	Veliki Šušnjar	Donja Bačuga	SISAČKO-MOSLAVAČKA
44205	Pecki	Donja Bačuga	SISAČKO-MOSLAVAČKA
44205	Luščani	Donja Bačuga	SISAČKO-MOSLAVAČKA
44205	Grabovac Banski	Donja Bačuga	SISAČKO-MOSLAVAČKA
44205	Gornja Bačuga	Donja Bačuga	SISAČKO-MOSLAVAČKA
44205	Donja Bačuga	Donja Bačuga	SISAČKO-MOSLAVAČKA
44210	Petrinjci	Sunja	SISAČKO-MOSLAVAČKA
44210	Radonja Luka	Sunja	SISAČKO-MOSLAVAČKA
44210	Staza	Sunja	SISAČKO-MOSLAVAČKA
44210	Sunja	Sunja	SISAČKO-MOSLAVAČKA
44210	Vedro Polje	Sunja	SISAČKO-MOSLAVAČKA
44210	Žreme	Sunja	SISAČKO-MOSLAVAČKA
44210	Novoselci	Sunja	SISAČKO-MOSLAVAČKA
44210	Krivaj Sunjski	Sunja	SISAČKO-MOSLAVAČKA
44210	Četvrtkovac	Sunja	SISAČKO-MOSLAVAČKA
44210	Donja Letina	Sunja	SISAČKO-MOSLAVAČKA
44210	Drljača	Sunja	SISAČKO-MOSLAVAČKA
44210	Gornja Letina	Sunja	SISAČKO-MOSLAVAČKA
44210	Gradusa Posavska	Sunja	SISAČKO-MOSLAVAČKA
44210	Greda Sunjska	Sunja	SISAČKO-MOSLAVAČKA
44211	Klobučak	Blinjski Kut	SISAČKO-MOSLAVAČKA
44211	Kladari	Blinjski Kut	SISAČKO-MOSLAVAČKA
44211	Kinjačka	Blinjski Kut	SISAČKO-MOSLAVAČKA
44211	Gornje Komarevo	Blinjski Kut	SISAČKO-MOSLAVAČKA
44211	Donje Komarevo	Blinjski Kut	SISAČKO-MOSLAVAČKA
44211	Brđani Kosa	Blinjski Kut	SISAČKO-MOSLAVAČKA
44211	Brđani Cesta	Blinjski Kut	SISAČKO-MOSLAVAČKA
44211	Blinjski Kut	Blinjski Kut	SISAČKO-MOSLAVAČKA
44211	Blinjska Greda	Blinjski Kut	SISAČKO-MOSLAVAČKA
44211	Bestrma	Blinjski Kut	SISAČKO-MOSLAVAČKA
44212	Vukoševac	Mala Gradusa	SISAČKO-MOSLAVAČKA
44212	Velika Gradusa	Mala Gradusa	SISAČKO-MOSLAVAČKA
44212	Svinica	Mala Gradusa	SISAČKO-MOSLAVAČKA
44212	Staro Selo	Mala Gradusa	SISAČKO-MOSLAVAČKA
44212	Sjeverovac	Mala Gradusa	SISAČKO-MOSLAVAČKA
44212	Mala Paukova	Mala Gradusa	SISAČKO-MOSLAVAČKA
44212	Mala Gradusa	Mala Gradusa	SISAČKO-MOSLAVAČKA
44213	Suvoj	Kratečko	SISAČKO-MOSLAVAČKA
44213	Mužilovčica	Kratečko	SISAČKO-MOSLAVAČKA
44213	Lonja	Kratečko	SISAČKO-MOSLAVAČKA
44213	Kratečko	Kratečko	SISAČKO-MOSLAVAČKA
44213	Čigoč	Kratečko	SISAČKO-MOSLAVAČKA
44214	Strmen	Bobovac	SISAČKO-MOSLAVAČKA
44214	Selišće Sunjsko	Bobovac	SISAČKO-MOSLAVAČKA
44214	Ivanjski Bok	Bobovac	SISAČKO-MOSLAVAČKA
44214	Crkveni Bok	Bobovac	SISAČKO-MOSLAVAČKA
44214	Bobovac	Bobovac	SISAČKO-MOSLAVAČKA
44214	Bistrač	Bobovac	SISAČKO-MOSLAVAČKA
44221	Donji Hrastovac	Staza	SISAČKO-MOSLAVAČKA
44221	Pobrđani	Staza	SISAČKO-MOSLAVAČKA
44222	Utolica	Šaš	SISAČKO-MOSLAVAČKA
44222	Timarci	Šaš	SISAČKO-MOSLAVAČKA
44222	Šaš	Šaš	SISAČKO-MOSLAVAČKA
44222	Slovinci	Šaš	SISAČKO-MOSLAVAČKA
44222	Papići	Šaš	SISAČKO-MOSLAVAČKA
44222	Kostreši Šaški	Šaš	SISAČKO-MOSLAVAČKA
44222	Jasenovčani	Šaš	SISAČKO-MOSLAVAČKA
44222	Čapljani	Šaš	SISAČKO-MOSLAVAČKA
44231	Stražbenica	Blinja	SISAČKO-MOSLAVAČKA
44231	Petkovac	Blinja	SISAČKO-MOSLAVAČKA
44231	Moštanica	Blinja	SISAČKO-MOSLAVAČKA
44231	Madžari	Blinja	SISAČKO-MOSLAVAČKA
44231	Jošavica	Blinja	SISAČKO-MOSLAVAČKA
44231	Blinja	Blinja	SISAČKO-MOSLAVAČKA
44231	Bijelnik	Blinja	SISAČKO-MOSLAVAČKA
44250	Župić	Petrinja	SISAČKO-MOSLAVAČKA
44250	Taborište	Petrinja	SISAČKO-MOSLAVAČKA
44250	Petrinja	Petrinja	SISAČKO-MOSLAVAČKA
44250	Novo Selište	Petrinja	SISAČKO-MOSLAVAČKA
44250	Nova Drenčina	Petrinja	SISAČKO-MOSLAVAČKA
44250	Hrastovica	Petrinja	SISAČKO-MOSLAVAČKA
44250	Donja Budičina	Petrinja	SISAČKO-MOSLAVAČKA
44250	Brest Pokupski	Petrinja	SISAČKO-MOSLAVAČKA
44251	Strašnik	Gora	SISAČKO-MOSLAVAČKA
44251	Sibić	Gora	SISAČKO-MOSLAVAČKA
44251	Križ Hrastovački	Gora	SISAČKO-MOSLAVAČKA
44251	Graberje	Gora	SISAČKO-MOSLAVAČKA
44251	Gora	Gora	SISAČKO-MOSLAVAČKA
44251	Glinska Poljana	Gora	SISAČKO-MOSLAVAČKA
44251	Cepeliš	Gora	SISAČKO-MOSLAVAČKA
44253	Mošćenica	Mošćenica	SISAČKO-MOSLAVAČKA
44271	Žažina	Letovanić	SISAČKO-MOSLAVAČKA
44271	Vrh Letovanički	Letovanić	SISAČKO-MOSLAVAČKA
44271	Šišinec	Letovanić	SISAČKO-MOSLAVAČKA
44271	Stari Farkašić	Letovanić	SISAČKO-MOSLAVAČKA
44271	Stari Brod	Letovanić	SISAČKO-MOSLAVAČKA
44271	Pokupsko Vratečko	Letovanić	SISAČKO-MOSLAVAČKA
44271	Palanjek Pokupski	Letovanić	SISAČKO-MOSLAVAČKA
44271	Letovanić	Letovanić	SISAČKO-MOSLAVAČKA
44272	Poljana Lekenička	Lekenik	SISAČKO-MOSLAVAČKA
44272	Pešćenica	Lekenik	SISAČKO-MOSLAVAČKA
44272	Lekenik	Lekenik	SISAČKO-MOSLAVAČKA
44272	Gornji Vukojevac	Lekenik	SISAČKO-MOSLAVAČKA
44272	Dužica	Lekenik	SISAČKO-MOSLAVAČKA
44272	Donji Vukojevac	Lekenik	SISAČKO-MOSLAVAČKA
44272	Cerje Letovanićko	Lekenik	SISAČKO-MOSLAVAČKA
44272	Brežane Lekeničke	Lekenik	SISAČKO-MOSLAVAČKA
44273	Sela	Sela	SISAČKO-MOSLAVAČKA
44273	Slana	Sela	SISAČKO-MOSLAVAČKA
44273	Srednje Mokrice	Sela	SISAČKO-MOSLAVAČKA
44273	Stara Drenčina	Sela	SISAČKO-MOSLAVAČKA
44273	Vratečko	Sela	SISAČKO-MOSLAVAČKA
44273	Vurot	Sela	SISAČKO-MOSLAVAČKA
44273	Petrovec	Sela	SISAČKO-MOSLAVAČKA
44273	Novi Farkašić	Sela	SISAČKO-MOSLAVAČKA
44273	Nebojan	Sela	SISAČKO-MOSLAVAČKA
44273	Donje Mokrice	Sela	SISAČKO-MOSLAVAČKA
44273	Dumače	Sela	SISAČKO-MOSLAVAČKA
44273	Gornje Morkice	Sela	SISAČKO-MOSLAVAČKA
44273	Greda	Sela	SISAČKO-MOSLAVAČKA
44273	Jazvenik	Sela	SISAČKO-MOSLAVAČKA
44273	Međurače	Sela	SISAČKO-MOSLAVAČKA
44316	Vidrenjak	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Velika Ludina	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Ruškovica	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Okoli	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Mustafina Klada	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Mala Ludina	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Ludinica	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Kompator	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Donja Vlahinička	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Gornja Vlahinićka	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Grabričina	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Grabrov Potok	Velika Ludina	SISAČKO-MOSLAVAČKA
44316	Katoličko Selišće	Velika Ludina	SISAČKO-MOSLAVAČKA
44317	Stružec	Popovača	SISAČKO-MOSLAVAČKA
44317	Potok	Popovača	SISAČKO-MOSLAVAČKA
44317	Popovača	Popovača	SISAČKO-MOSLAVAČKA
44317	Podbrđe	Popovača	SISAČKO-MOSLAVAČKA
44317	Osekovo	Popovača	SISAČKO-MOSLAVAČKA
44317	Moslavačka Slatina	Popovača	SISAČKO-MOSLAVAČKA
44317	Gornja Jelenska	Popovača	SISAČKO-MOSLAVAČKA
44317	Donja Jelenska	Popovača	SISAČKO-MOSLAVAČKA
44318	Voloder	Voloder	SISAČKO-MOSLAVAČKA
44318	Gornja Gračenica	Voloder	SISAČKO-MOSLAVAČKA
44318	Donja Gračenica	Voloder	SISAČKO-MOSLAVAČKA
44320	Kutinica	Kutina	SISAČKO-MOSLAVAČKA
44320	Kutinska Slatina	Kutina	SISAČKO-MOSLAVAČKA
44320	Mikleuška	Kutina	SISAČKO-MOSLAVAČKA
44320	Mišinka	Kutina	SISAČKO-MOSLAVAČKA
44320	Repušnica	Kutina	SISAČKO-MOSLAVAČKA
44320	Selište	Kutina	SISAČKO-MOSLAVAČKA
44320	Stupovača	Kutina	SISAČKO-MOSLAVAČKA
44320	Šartovac	Kutina	SISAČKO-MOSLAVAČKA
44320	Kutina	Kutina	SISAČKO-MOSLAVAČKA
44320	Krajiška Kutinica	Kutina	SISAČKO-MOSLAVAČKA
44320	Kletište	Kutina	SISAČKO-MOSLAVAČKA
44320	Batina	Kutina	SISAČKO-MOSLAVAČKA
44320	Brinjani	Kutina	SISAČKO-MOSLAVAČKA
44320	Ciglenica	Kutina	SISAČKO-MOSLAVAČKA
44320	Čaire	Kutina	SISAČKO-MOSLAVAČKA
44320	Gojlo	Kutina	SISAČKO-MOSLAVAČKA
44320	Husain	Kutina	SISAČKO-MOSLAVAČKA
44320	Ilova	Kutina	SISAČKO-MOSLAVAČKA
44320	Katoličke Čaire	Kutina	SISAČKO-MOSLAVAČKA
44321	Zbjegovača	Banova Jaruga	SISAČKO-MOSLAVAČKA
44321	Piljenice	Banova Jaruga	SISAČKO-MOSLAVAČKA
44321	Međurić	Banova Jaruga	SISAČKO-MOSLAVAČKA
44321	Krivaj	Banova Jaruga	SISAČKO-MOSLAVAČKA
44321	Janja Lipa	Banova Jaruga	SISAČKO-MOSLAVAČKA
44321	Jamarica	Banova Jaruga	SISAČKO-MOSLAVAČKA
44321	Banova Jaruga	Banova Jaruga	SISAČKO-MOSLAVAČKA
44322	Novi Grabovac	Lipovljani	SISAČKO-MOSLAVAČKA
44322	Lipovljani	Lipovljani	SISAČKO-MOSLAVAČKA
44322	Kraljeva Velika	Lipovljani	SISAČKO-MOSLAVAČKA
44322	Kozarice	Lipovljani	SISAČKO-MOSLAVAČKA
44323	Roždanik	Rajić	SISAČKO-MOSLAVAČKA
44323	Rajić	Rajić	SISAČKO-MOSLAVAČKA
44323	Rajčići	Rajić	SISAČKO-MOSLAVAČKA
44323	Rađenovci	Rajić	SISAČKO-MOSLAVAČKA
44323	Jazavica	Rajić	SISAČKO-MOSLAVAČKA
44323	Borovac	Rajić	SISAČKO-MOSLAVAČKA
44324	Višnjica Uštička	Jasenovac	SISAČKO-MOSLAVAČKA
44324	Uštica	Jasenovac	SISAČKO-MOSLAVAČKA
44324	Tanac	Jasenovac	SISAČKO-MOSLAVAČKA
44324	Mlaka	Jasenovac	SISAČKO-MOSLAVAČKA
44324	Košutarica	Jasenovac	SISAČKO-MOSLAVAČKA
44324	Jasenovac	Jasenovac	SISAČKO-MOSLAVAČKA
44325	Trebež	Krapje	SISAČKO-MOSLAVAČKA
44325	Puska	Krapje	SISAČKO-MOSLAVAČKA
44325	Plesmo	Krapje	SISAČKO-MOSLAVAČKA
44325	Krapje	Krapje	SISAČKO-MOSLAVAČKA
44325	Drenov Bok	Krapje	SISAČKO-MOSLAVAČKA
44330	Voćarica	Novska	SISAČKO-MOSLAVAČKA
44330	Stari Grabovac	Novska	SISAČKO-MOSLAVAČKA
44330	Stara Subocka	Novska	SISAČKO-MOSLAVAČKA
44330	Sigetac Novski	Novska	SISAČKO-MOSLAVAČKA
44330	Popovac Subocki	Novska	SISAČKO-MOSLAVAČKA
44330	Paklenica	Novska	SISAČKO-MOSLAVAČKA
44330	Novska	Novska	SISAČKO-MOSLAVAČKA
44330	Nova Subocka	Novska	SISAČKO-MOSLAVAČKA
44330	Bair	Novska	SISAČKO-MOSLAVAČKA
44330	Brestača	Novska	SISAČKO-MOSLAVAČKA
44330	Brezovac Subocki	Novska	SISAČKO-MOSLAVAČKA
44330	Bročice	Novska	SISAČKO-MOSLAVAČKA
44330	Kričke	Novska	SISAČKO-MOSLAVAČKA
44330	Lovska	Novska	SISAČKO-MOSLAVAČKA
44400	Kihalac	Glina	SISAČKO-MOSLAVAČKA
44400	Majske Poljane	Glina	SISAČKO-MOSLAVAČKA
44400	Marinbrod	Glina	SISAČKO-MOSLAVAČKA
44400	Novo Selo Glinsko	Glina	SISAČKO-MOSLAVAČKA
44400	Prekopa	Glina	SISAČKO-MOSLAVAČKA
44400	Roviška	Glina	SISAČKO-MOSLAVAČKA
44400	Skela	Glina	SISAČKO-MOSLAVAČKA
44400	Šatornja	Glina	SISAČKO-MOSLAVAČKA
44400	Trtnik Glinski	Glina	SISAČKO-MOSLAVAČKA
44400	Turčenica	Glina	SISAČKO-MOSLAVAČKA
44400	Velika Solina	Glina	SISAČKO-MOSLAVAČKA
44400	Joševica	Glina	SISAČKO-MOSLAVAČKA
44400	Hađer	Glina	SISAČKO-MOSLAVAČKA
44400	Gornji Viduševac	Glina	SISAČKO-MOSLAVAČKA
44400	Baturi	Glina	SISAČKO-MOSLAVAČKA
44400	Bišćanovo	Glina	SISAČKO-MOSLAVAČKA
44400	Brnjeuška	Glina	SISAČKO-MOSLAVAČKA
44400	Donja Trstenica	Glina	SISAČKO-MOSLAVAČKA
44400	Donje Selište	Glina	SISAČKO-MOSLAVAČKA
44400	Donji Selkovac	Glina	SISAČKO-MOSLAVAČKA
44400	Donji Viduševac	Glina	SISAČKO-MOSLAVAČKA
44400	Dvorišće	Glina	SISAČKO-MOSLAVAČKA
44400	Glina	Glina	SISAČKO-MOSLAVAČKA
44400	Gornje Selište	Glina	SISAČKO-MOSLAVAČKA
44400	Gornji Selkovac	Glina	SISAČKO-MOSLAVAČKA
44401	Šibine	Hajtić	SISAČKO-MOSLAVAČKA
44401	Šaševa	Hajtić	SISAČKO-MOSLAVAČKA
44401	Hajtić	Hajtić	SISAČKO-MOSLAVAČKA
44401	Buzeta	Hajtić	SISAČKO-MOSLAVAČKA
44401	Borovita	Hajtić	SISAČKO-MOSLAVAČKA
44401	Balinac	Hajtić	SISAČKO-MOSLAVAČKA
44402	Veliki Obljaj	Mali Obljaj	SISAČKO-MOSLAVAČKA
44402	Mali Obljaj	Mali Obljaj	SISAČKO-MOSLAVAČKA
44402	Kobiljak	Mali Obljaj	SISAČKO-MOSLAVAČKA
44402	Bojna	Mali Obljaj	SISAČKO-MOSLAVAČKA
44403	Svračica	Maja	SISAČKO-MOSLAVAČKA
44403	Ravno Rašće	Maja	SISAČKO-MOSLAVAČKA
44403	Prijeka	Maja	SISAČKO-MOSLAVAČKA
44403	Majski Trtnik	Maja	SISAČKO-MOSLAVAČKA
44403	Maja	Maja	SISAČKO-MOSLAVAČKA
44403	Dragotina	Maja	SISAČKO-MOSLAVAČKA
44403	Dolnjaki	Maja	SISAČKO-MOSLAVAČKA
44403	Dabrina	Maja	SISAČKO-MOSLAVAČKA
44404	Gornji Klasnić	Gornji Klasnić	SISAČKO-MOSLAVAČKA
44404	Donji Klasnić	Gornji Klasnić	SISAČKO-MOSLAVAČKA
44404	Brubno	Gornji Klasnić	SISAČKO-MOSLAVAČKA
44404	Brezovo Polje	Gornji Klasnić	SISAČKO-MOSLAVAČKA
44405	Veliki Gradac	Mali Gradac	SISAČKO-MOSLAVAČKA
44405	Trnovac Glinski	Mali Gradac	SISAČKO-MOSLAVAČKA
44405	Momčilovića Kosa	Mali Gradac	SISAČKO-MOSLAVAČKA
44405	Martinovići	Mali Gradac	SISAČKO-MOSLAVAČKA
44405	Mali Gradac	Mali Gradac	SISAČKO-MOSLAVAČKA
44405	Kozaperovica	Mali Gradac	SISAČKO-MOSLAVAČKA
44405	Brestik	Mali Gradac	SISAČKO-MOSLAVAČKA
44406	Bijele Vode	Vlahović	SISAČKO-MOSLAVAČKA
44406	Drenovac Banski	Vlahović	SISAČKO-MOSLAVAČKA
44406	Vlahović	Vlahović	SISAČKO-MOSLAVAČKA
44410	Ostrožin	Gvozd	SISAČKO-MOSLAVAČKA
44410	Pješčanica	Gvozd	SISAČKO-MOSLAVAČKA
44410	Podgorje	Gvozd	SISAČKO-MOSLAVAČKA
44410	Slavsko Polje	Gvozd	SISAČKO-MOSLAVAČKA
44410	Trepča	Gvozd	SISAČKO-MOSLAVAČKA
44410	Malička	Gvozd	SISAČKO-MOSLAVAČKA
44410	Gvozd	Gvozd	SISAČKO-MOSLAVAČKA
44410	Gornja Čemernica	Gvozd	SISAČKO-MOSLAVAČKA
44410	Dugo Selo	Gvozd	SISAČKO-MOSLAVAČKA
44410	Donja Čemernica	Gvozd	SISAČKO-MOSLAVAČKA
44410	Crevarska Strana	Gvozd	SISAČKO-MOSLAVAČKA
44410	Brnjavac	Gvozd	SISAČKO-MOSLAVAČKA
44410	Blatuša	Gvozd	SISAČKO-MOSLAVAČKA
44412	Zaloj	Stankovac	SISAČKO-MOSLAVAČKA
44412	Stankovac	Stankovac	SISAČKO-MOSLAVAČKA
44412	Mala Solina	Stankovac	SISAČKO-MOSLAVAČKA
44412	Gračanica Šišinečka	Stankovac	SISAČKO-MOSLAVAČKA
44412	Gornje Jame	Stankovac	SISAČKO-MOSLAVAČKA
44412	Donje Jame	Stankovac	SISAČKO-MOSLAVAČKA
44414	Šljivovac	Bović	SISAČKO-MOSLAVAČKA
44414	Stipan	Bović	SISAČKO-MOSLAVAČKA
44414	Kozarac	Bović	SISAČKO-MOSLAVAČKA
44414	Kirin	Bović	SISAČKO-MOSLAVAČKA
44414	Gornja Trstenica	Bović	SISAČKO-MOSLAVAČKA
44414	Golinja	Bović	SISAČKO-MOSLAVAČKA
44414	Čremušnica	Bović	SISAČKO-MOSLAVAČKA
44414	Bović	Bović	SISAČKO-MOSLAVAČKA
44415	Perna	Topusko	SISAČKO-MOSLAVAČKA
44415	Ponikvari	Topusko	SISAČKO-MOSLAVAČKA
44415	Staro Selo Topusko	Topusko	SISAČKO-MOSLAVAČKA
44415	Topusko	Topusko	SISAČKO-MOSLAVAČKA
44415	Velika Vranovina	Topusko	SISAČKO-MOSLAVAČKA
44415	Vorkapić	Topusko	SISAČKO-MOSLAVAČKA
44415	Pecka	Topusko	SISAČKO-MOSLAVAČKA
44415	Mala Vranovina	Topusko	SISAČKO-MOSLAVAČKA
44415	Batinova Kosa	Topusko	SISAČKO-MOSLAVAČKA
44415	Bukovica	Topusko	SISAČKO-MOSLAVAČKA
44415	Crni Potok	Topusko	SISAČKO-MOSLAVAČKA
44415	Gređani	Topusko	SISAČKO-MOSLAVAČKA
44415	Hrvatsko Selo	Topusko	SISAČKO-MOSLAVAČKA
44415	Katinovac	Topusko	SISAČKO-MOSLAVAČKA
44425	Slatina Pokupska	Gornja Bučica	SISAČKO-MOSLAVAČKA
44425	Ilovačak	Gornja Bučica	SISAČKO-MOSLAVAČKA
44425	Gornje Taborište	Gornja Bučica	SISAČKO-MOSLAVAČKA
44425	Gornja Bučica	Gornja Bučica	SISAČKO-MOSLAVAČKA
44425	Donje Taborište	Gornja Bučica	SISAČKO-MOSLAVAČKA
44425	Donja Bučica	Gornja Bučica	SISAČKO-MOSLAVAČKA
44425	Desni Degoj	Gornja Bučica	SISAČKO-MOSLAVAČKA
44430	Selište Kostajničko	Hrvatska Kostajnica	SISAČKO-MOSLAVAČKA
44430	Rosulje	Hrvatska Kostajnica	SISAČKO-MOSLAVAČKA
44430	Rausovac	Hrvatska Kostajnica	SISAČKO-MOSLAVAČKA
44430	Hrvatska Kostajnica	Hrvatska Kostajnica	SISAČKO-MOSLAVAČKA
44430	Čukur	Hrvatska Kostajnica	SISAČKO-MOSLAVAČKA
44431	Donji Kukuruzari	Donji Kukuruzari	SISAČKO-MOSLAVAČKA
44431	Gornji Kukuruzari	Donji Kukuruzari	SISAČKO-MOSLAVAČKA
44432	Umetići	Mečenčani	SISAČKO-MOSLAVAČKA
44432	Prevršac	Mečenčani	SISAČKO-MOSLAVAČKA
44432	Mečenčani	Mečenčani	SISAČKO-MOSLAVAČKA
44432	Lovča	Mečenčani	SISAČKO-MOSLAVAČKA
44432	Kostreši Bjelovački	Mečenčani	SISAČKO-MOSLAVAČKA
44432	Komogovina	Mečenčani	SISAČKO-MOSLAVAČKA
44432	Knezovljani	Mečenčani	SISAČKO-MOSLAVAČKA
44432	Gornji Bjelovac	Mečenčani	SISAČKO-MOSLAVAČKA
44432	Donji Bjelovac	Mečenčani	SISAČKO-MOSLAVAČKA
44432	Borojevići	Mečenčani	SISAČKO-MOSLAVAČKA
44432	Babina Rijeka	Mečenčani	SISAČKO-MOSLAVAČKA
44433	Stubalj	Majur	SISAČKO-MOSLAVAČKA
44433	Panjani	Majur	SISAČKO-MOSLAVAČKA
44433	Majur	Majur	SISAČKO-MOSLAVAČKA
44433	Kostrići	Majur	SISAČKO-MOSLAVAČKA
44433	Gornja Velešnja	Majur	SISAČKO-MOSLAVAČKA
44433	Donja Velešnja	Majur	SISAČKO-MOSLAVAČKA
44434	Veliko Krčevo	Graboštani	SISAČKO-MOSLAVAČKA
44434	Srednja Meminska	Graboštani	SISAČKO-MOSLAVAČKA
44434	Mračaj	Graboštani	SISAČKO-MOSLAVAČKA
44434	Malo Krčevo	Graboštani	SISAČKO-MOSLAVAČKA
44434	Graboštani	Graboštani	SISAČKO-MOSLAVAČKA
44434	Gornji Hrastovac	Graboštani	SISAČKO-MOSLAVAČKA
44434	Gornja Meminska	Graboštani	SISAČKO-MOSLAVAČKA
44435	Kuljani	Divuša	SISAČKO-MOSLAVAČKA
44435	Lotine	Divuša	SISAČKO-MOSLAVAČKA
44435	Šakanlije	Divuša	SISAČKO-MOSLAVAČKA
44435	Šegestin	Divuša	SISAČKO-MOSLAVAČKA
44435	Unčani	Divuša	SISAČKO-MOSLAVAČKA
44435	Volinja	Divuša	SISAČKO-MOSLAVAČKA
44435	Kozibrod	Divuša	SISAČKO-MOSLAVAČKA
44435	Gornja Oraovica	Divuša	SISAČKO-MOSLAVAČKA
44435	Bujinja	Divuša	SISAČKO-MOSLAVAČKA
44435	Bujinjski Riječani	Divuša	SISAČKO-MOSLAVAČKA
44435	Divuša	Divuša	SISAČKO-MOSLAVAČKA
44435	Donja Oraovica	Divuša	SISAČKO-MOSLAVAČKA
44435	Draškovac	Divuša	SISAČKO-MOSLAVAČKA
44435	Golubovac Divuški	Divuša	SISAČKO-MOSLAVAČKA
44437	Trgovi	Rujevac	SISAČKO-MOSLAVAČKA
44437	Rujevac	Rujevac	SISAČKO-MOSLAVAČKA
44437	Pedalj	Rujevac	SISAČKO-MOSLAVAČKA
44437	Majdan	Rujevac	SISAČKO-MOSLAVAČKA
44437	Ljubina	Rujevac	SISAČKO-MOSLAVAČKA
44437	Ljeskovac	Rujevac	SISAČKO-MOSLAVAČKA
44437	Kosna	Rujevac	SISAČKO-MOSLAVAČKA
44437	Gvozdansko	Rujevac	SISAČKO-MOSLAVAČKA
44437	Gornja Stupnica	Rujevac	SISAČKO-MOSLAVAČKA
44437	Gage	Rujevac	SISAČKO-MOSLAVAČKA
44437	Donja Stupnica	Rujevac	SISAČKO-MOSLAVAČKA
44440	Stanić Polje	Dvor	SISAČKO-MOSLAVAČKA
44440	Sočanica	Dvor	SISAČKO-MOSLAVAČKA
44440	Matijevići	Dvor	SISAČKO-MOSLAVAČKA
44440	Kotarani	Dvor	SISAČKO-MOSLAVAČKA
44440	Struga Banska	Dvor	SISAČKO-MOSLAVAČKA
44440	Udetin	Dvor	SISAČKO-MOSLAVAČKA
44440	Vanići	Dvor	SISAČKO-MOSLAVAČKA
44440	Vrpolje Bansko	Dvor	SISAČKO-MOSLAVAČKA
44440	Zakopa	Dvor	SISAČKO-MOSLAVAČKA
44440	Zamlača	Dvor	SISAČKO-MOSLAVAČKA
44440	Zut	Dvor	SISAČKO-MOSLAVAČKA
44440	Kepčije	Dvor	SISAČKO-MOSLAVAČKA
44440	Jovac	Dvor	SISAČKO-MOSLAVAČKA
44440	Ćore	Dvor	SISAČKO-MOSLAVAČKA
44440	Donji Dobretin	Dvor	SISAČKO-MOSLAVAČKA
44440	Donji Javoranj	Dvor	SISAČKO-MOSLAVAČKA
44440	Dvor	Dvor	SISAČKO-MOSLAVAČKA
44440	Glavičani	Dvor	SISAČKO-MOSLAVAČKA
44440	Gornji Dobretin	Dvor	SISAČKO-MOSLAVAČKA
44440	Gornji Javoranj	Dvor	SISAČKO-MOSLAVAČKA
44440	Grmušani	Dvor	SISAČKO-MOSLAVAČKA
44440	Hrtić	Dvor	SISAČKO-MOSLAVAČKA
44440	Javnica	Dvor	SISAČKO-MOSLAVAČKA
44440	Javornik	Dvor	SISAČKO-MOSLAVAČKA
44441	Zrin	Brđani Šamarički	SISAČKO-MOSLAVAČKA
44441	Švrakarica	Brđani Šamarički	SISAČKO-MOSLAVAČKA
44441	Rudeži	Brđani Šamarički	SISAČKO-MOSLAVAČKA
44441	Rogulje	Brđani Šamarički	SISAČKO-MOSLAVAČKA
44441	Paukovac	Brđani Šamarički	SISAČKO-MOSLAVAČKA
44441	Grabovica	Brđani Šamarički	SISAČKO-MOSLAVAČKA
44441	Gorička	Brđani Šamarički	SISAČKO-MOSLAVAČKA
44441	Draga	Brđani Šamarički	SISAČKO-MOSLAVAČKA
44441	Brđani Šamarički	Brđani Šamarički	SISAČKO-MOSLAVAČKA
44443	Ostojići	Donji Žirovac	SISAČKO-MOSLAVAČKA
44443	Komora	Donji Žirovac	SISAČKO-MOSLAVAČKA
44443	Gornji Žirovac	Donji Žirovac	SISAČKO-MOSLAVAČKA
44443	Donji Žirovac	Donji Žirovac	SISAČKO-MOSLAVAČKA
44443	Čavlovica	Donji Žirovac	SISAČKO-MOSLAVAČKA
44450	Živaja	Hrvatska Dubica	SISAČKO-MOSLAVAČKA
44450	Slabinja	Hrvatska Dubica	SISAČKO-MOSLAVAČKA
44450	Hrvatska Dubica	Hrvatska Dubica	SISAČKO-MOSLAVAČKA
44450	Gornji Cerovljani	Hrvatska Dubica	SISAČKO-MOSLAVAČKA
44450	Donji Cerovljani	Hrvatska Dubica	SISAČKO-MOSLAVAČKA
44450	Baćin	Hrvatska Dubica	SISAČKO-MOSLAVAČKA
47000	Zadobarje	Karlovac	KARLOVAČKA
47000	Vodostaj	Karlovac	KARLOVAČKA
47000	Velika Jelsa	Karlovac	KARLOVAČKA
47000	Mala Jelsa	Karlovac	KARLOVAČKA
47000	Kobilić Pokupski	Karlovac	KARLOVAČKA
47000	Karlovac	Karlovac	KARLOVAČKA
47000	Kamensko	Karlovac	KARLOVAČKA
47000	Husje	Karlovac	KARLOVAČKA
47000	Hrnetić-Novaki	Karlovac	KARLOVAČKA
47000	Gradac Orlovac	Karlovac	KARLOVAČKA
47000	Gornje Stative	Karlovac	KARLOVAČKA
47000	Donje Mekušje	Karlovac	KARLOVAČKA
47201	Križančići	Draganići	KARLOVAČKA
47201	Lazina	Draganići	KARLOVAČKA
47201	Lug	Draganići	KARLOVAČKA
47201	Mrzljaki	Draganići	KARLOVAČKA
47201	Vrbanci	Draganići	KARLOVAČKA
47201	Vrh	Draganići	KARLOVAČKA
47201	Jazvaci	Draganići	KARLOVAČKA
47201	Goljak	Draganići	KARLOVAČKA
47201	Franjetići	Draganići	KARLOVAČKA
47201	Draganići	Draganići	KARLOVAČKA
47201	Darići	Draganići	KARLOVAČKA
47201	Budrovci	Draganići	KARLOVAČKA
47201	Bencetići	Draganići	KARLOVAČKA
47201	Barkovići	Draganići	KARLOVAČKA
47203	Zamršje	Rečica	KARLOVAČKA
47203	Rečica	Rečica	KARLOVAČKA
47203	Luka Pokupska	Rečica	KARLOVAČKA
47203	Karasi	Rečica	KARLOVAČKA
47204	Blatnica Pokupska	Šišljavić	KARLOVAČKA
47204	Ivančići Pokupski	Šišljavić	KARLOVAČKA
47204	Koritinja	Šišljavić	KARLOVAČKA
47204	Šišljavić	Šišljavić	KARLOVAČKA
47205	Vukmanić	Vukmanić	KARLOVAČKA
47205	Knez Gorica	Vukmanić	KARLOVAČKA
47206	Prkos Lasinjski	Lasinja	KARLOVAČKA
47206	Novo Selo Lasinjsko	Lasinja	KARLOVAČKA
47206	Lasinja	Lasinja	KARLOVAČKA
47206	Desno Sredičko	Lasinja	KARLOVAČKA
47206	Desni Štefanki	Lasinja	KARLOVAČKA
47206	Crna Draga	Lasinja	KARLOVAČKA
47206	Banski Kovačevac	Lasinja	KARLOVAČKA
47211	Manjerovići	Utinja	KARLOVAČKA
47211	Međeđak Utinjski	Utinja	KARLOVAČKA
47211	Podsedlo	Utinja	KARLOVAČKA
47211	Udbinja	Utinja	KARLOVAČKA
47211	Utinja	Utinja	KARLOVAČKA
47211	Utinja Vrelo	Utinja	KARLOVAČKA
47211	Mandić Selo	Utinja	KARLOVAČKA
47211	Malešević Selo	Utinja	KARLOVAČKA
47211	Kljaić Brdo	Utinja	KARLOVAČKA
47211	Bukovica Utinjska	Utinja	KARLOVAČKA
47211	Gaćeša Selo	Utinja	KARLOVAČKA
47211	Ivanković Selo	Utinja	KARLOVAČKA
47211	Ivošević Selo	Utinja	KARLOVAČKA
47211	Kartalije	Utinja	KARLOVAČKA
47211	Klipino Brdo	Utinja	KARLOVAČKA
47212	Slunjski Moravci	Skakavac	KARLOVAČKA
47212	Slunjska Selnica	Skakavac	KARLOVAČKA
47212	Skakavac	Skakavac	KARLOVAČKA
47212	Ribari	Skakavac	KARLOVAČKA
47212	Popović Brdo	Skakavac	KARLOVAČKA
47212	Lipje	Skakavac	KARLOVAČKA
47212	Kablar	Skakavac	KARLOVAČKA
47212	Gornja Trebinja	Skakavac	KARLOVAČKA
47212	Donja Trebinja	Skakavac	KARLOVAČKA
47212	Brođani	Skakavac	KARLOVAČKA
47212	Brežani	Skakavac	KARLOVAČKA
47212	Banski Moravci	Skakavac	KARLOVAČKA
47212	Banska Selnica	Skakavac	KARLOVAČKA
47213	Sjeničak Lasinjski	Sjeničak Lasinjski	KARLOVAČKA
47213	Gornji Sjeničak	Sjeničak Lasinjski	KARLOVAČKA
47213	Donji Sjeničak	Sjeničak Lasinjski	KARLOVAČKA
47220	Živković Kosa	Vojnić	KARLOVAČKA
47220	Vojnić	Vojnić	KARLOVAČKA
47220	Vojišnica	Vojnić	KARLOVAČKA
47220	Radonja	Vojnić	KARLOVAČKA
47220	Radmanovac	Vojnić	KARLOVAČKA
47220	Loskunja	Vojnić	KARLOVAČKA
47220	Kupljensko	Vojnić	KARLOVAČKA
47220	Krivaja Vojnićka	Vojnić	KARLOVAČKA
47220	Kolarić	Vojnić	KARLOVAČKA
47220	Brdo Utinjsko	Vojnić	KARLOVAČKA
47220	Jagrovac	Vojnić	KARLOVAČKA
47220	Johovo	Vojnić	KARLOVAČKA
47220	Jurga	Vojnić	KARLOVAČKA
47220	Ključar	Vojnić	KARLOVAČKA
47220	Knežević Kosa	Vojnić	KARLOVAČKA
47220	Kokirevo	Vojnić	KARLOVAČKA
47221	Miholjsko	Krstinja	KARLOVAČKA
47221	Mracelj	Krstinja	KARLOVAČKA
47221	Mračaj Krstinjski	Krstinja	KARLOVAČKA
47221	Petrova Poljana	Krstinja	KARLOVAČKA
47221	Prisjeka	Krstinja	KARLOVAČKA
47221	Rajić Brdo	Krstinja	KARLOVAČKA
47221	Selakova Poljana	Krstinja	KARLOVAČKA
47221	Svinica Krstinjska	Krstinja	KARLOVAČKA
47221	Široka Rijeka	Krstinja	KARLOVAČKA
47221	Štakorovica	Krstinja	KARLOVAČKA
47221	Lisine	Krstinja	KARLOVAČKA
47221	Lipovac Krstinjski	Krstinja	KARLOVAČKA
47221	Kusaja	Krstinja	KARLOVAČKA
47221	Donja Brusovača	Krstinja	KARLOVAČKA
47221	Dunjak	Krstinja	KARLOVAČKA
47221	Džaperovac	Krstinja	KARLOVAČKA
47221	Gejkovac	Krstinja	KARLOVAČKA
47221	Gornja Brusovača	Krstinja	KARLOVAČKA
47221	Jagrovac	Krstinja	KARLOVAČKA
47221	Kestenovac	Krstinja	KARLOVAČKA
47221	Klokoč	Krstinja	KARLOVAČKA
47221	Klupica	Krstinja	KARLOVAČKA
47221	Krstinja	Krstinja	KARLOVAČKA
47222	Pašin Potok	Cetingrad	KARLOVAČKA
47222	Maljevačko Selište	Cetingrad	KARLOVAČKA
47222	Maljevac	Cetingrad	KARLOVAČKA
47222	Luke	Cetingrad	KARLOVAČKA
47222	Kuk	Cetingrad	KARLOVAČKA
47222	Kruškovača	Cetingrad	KARLOVAČKA
47222	Komesarac	Cetingrad	KARLOVAČKA
47222	Polojski Varoš	Cetingrad	KARLOVAČKA
47222	Ponor	Cetingrad	KARLOVAČKA
47222	Potcetin	Cetingrad	KARLOVAČKA
47222	Ruševica	Cetingrad	KARLOVAČKA
47222	Sadikovac	Cetingrad	KARLOVAČKA
47222	Srednje Selo	Cetingrad	KARLOVAČKA
47222	Strmačka	Cetingrad	KARLOVAČKA
47222	Šiljkovača	Cetingrad	KARLOVAČKA
47222	Tatar Varoš	Cetingrad	KARLOVAČKA
47222	Trnovi	Cetingrad	KARLOVAČKA
47222	Kestenje	Cetingrad	KARLOVAČKA
47222	Kapljuv	Cetingrad	KARLOVAČKA
47222	Batnoga	Cetingrad	KARLOVAČKA
47222	Begovo Brdo	Cetingrad	KARLOVAČKA
47222	Bilo	Cetingrad	KARLOVAČKA
47222	Bogovolja	Cetingrad	KARLOVAČKA
47222	Buhača	Cetingrad	KARLOVAČKA
47222	Cetingrad	Cetingrad	KARLOVAČKA
47222	Cetinski Varoš	Cetingrad	KARLOVAČKA
47222	Delić Poljana	Cetingrad	KARLOVAČKA
47222	Donja Žrvnica	Cetingrad	KARLOVAČKA
47222	Donje Gnojnice	Cetingrad	KARLOVAČKA
47222	Grabarska	Cetingrad	KARLOVAČKA
47222	Gornje Gnojnice	Cetingrad	KARLOVAČKA
47222	Gornja Žrvnica	Cetingrad	KARLOVAČKA
47222	Gojkovac	Cetingrad	KARLOVAČKA
47222	Gnojnice	Cetingrad	KARLOVAČKA
47222	Glinice	Cetingrad	KARLOVAČKA
47222	Đurin Potok	Cetingrad	KARLOVAČKA
47240	Novo Selo	Slunj	KARLOVAČKA
47240	Miljevac	Slunj	KARLOVAČKA
47240	Marindolsko Brdo	Slunj	KARLOVAČKA
47240	Mali Vuković	Slunj	KARLOVAČKA
47240	Lumbardenik	Slunj	KARLOVAČKA
47240	Lađevačko Selište	Slunj	KARLOVAČKA
47240	Kosa	Slunj	KARLOVAČKA
47240	Jame	Slunj	KARLOVAČKA
47240	Pavlovac	Slunj	KARLOVAČKA
47240	Podmelnica	Slunj	KARLOVAČKA
47240	Zapoljak	Slunj	KARLOVAČKA
47240	Videkić Selo	Slunj	KARLOVAČKA
47240	Slušnica	Slunj	KARLOVAČKA
47240	Slunj	Slunj	KARLOVAČKA
47240	Sastavak	Slunj	KARLOVAČKA
47240	Salopek Luke	Slunj	KARLOVAČKA
47240	Rastoke	Slunj	KARLOVAČKA
47240	Polje	Slunj	KARLOVAČKA
47240	Gornji Popovac	Slunj	KARLOVAČKA
47240	Gornji Nikšić	Slunj	KARLOVAČKA
47240	Gornji Lađevac	Slunj	KARLOVAČKA
47240	Donji Kremen	Slunj	KARLOVAČKA
47240	Donji Furjan	Slunj	KARLOVAČKA
47240	Donji Cerovac	Slunj	KARLOVAČKA
47240	Donje Taborište	Slunj	KARLOVAČKA
47240	Donja Glina	Slunj	KARLOVAČKA
47240	Čamerovac	Slunj	KARLOVAČKA
47240	Cvitović	Slunj	KARLOVAČKA
47240	Arapovac	Slunj	KARLOVAČKA
47240	Donji Lađevac	Slunj	KARLOVAČKA
47240	Donji Nikšić	Slunj	KARLOVAČKA
47240	Gornji Kremen	Slunj	KARLOVAČKA
47240	Gornji Furjan	Slunj	KARLOVAČKA
47240	Gornji Cerovac	Slunj	KARLOVAČKA
47240	Gornje Taborište	Slunj	KARLOVAČKA
47240	Gornja Glina	Slunj	KARLOVAČKA
47240	Glinsko Vrelo	Slunj	KARLOVAČKA
47240	Dubrave	Slunj	KARLOVAČKA
47240	Donji Popovac	Slunj	KARLOVAČKA
47241	Zimić	Tušilović	KARLOVAČKA
47241	Tušilović	Tušilović	KARLOVAČKA
47241	Pavković Selo	Tušilović	KARLOVAČKA
47241	Okić	Tušilović	KARLOVAČKA
47241	Mlakovac	Tušilović	KARLOVAČKA
47241	Ladvenjak	Tušilović	KARLOVAČKA
47241	Koranski Brijeg	Tušilović	KARLOVAČKA
47241	Donji Budački	Tušilović	KARLOVAČKA
47241	Cerovac Vukmanički	Tušilović	KARLOVAČKA
47241	Brezova Glava	Tušilović	KARLOVAČKA
47242	Poljana Vojnićka	Krnjak	KARLOVAČKA
47242	Podgorje Krnjačko	Krnjak	KARLOVAČKA
47242	Perići	Krnjak	KARLOVAČKA
47242	Partizansko Žarište	Krnjak	KARLOVAČKA
47242	Mala Crkvina	Krnjak	KARLOVAČKA
47242	Ponorac	Krnjak	KARLOVAČKA
47242	Rastovac Budački	Krnjak	KARLOVAČKA
47242	Suhodol Budački	Krnjak	KARLOVAČKA
47242	Trupinjak	Krnjak	KARLOVAČKA
47242	Velika Crkvina	Krnjak	KARLOVAČKA
47242	Vojnović Brdo	Krnjak	KARLOVAČKA
47242	Zagorje	Krnjak	KARLOVAČKA
47242	Krnjak	Krnjak	KARLOVAČKA
47242	Keserov Potok	Krnjak	KARLOVAČKA
47242	Bijeli Klanac	Krnjak	KARLOVAČKA
47242	Brebornica	Krnjak	KARLOVAČKA
47242	Budačka Rijeka	Krnjak	KARLOVAČKA
47242	Burić Selo	Krnjak	KARLOVAČKA
47242	Čatrnja	Krnjak	KARLOVAČKA
47242	Dugi Dol	Krnjak	KARLOVAČKA
47242	Dvorište	Krnjak	KARLOVAČKA
47242	Jasnić Brdo	Krnjak	KARLOVAČKA
47242	Grabovac Vojnićki	Krnjak	KARLOVAČKA
47242	Grabovac Krnjački	Krnjak	KARLOVAČKA
47242	Gornji Skrad	Krnjak	KARLOVAČKA
47242	Gornji Budački	Krnjak	KARLOVAČKA
47243	Snos	Veljun	KARLOVAČKA
47243	Sparednjak	Veljun	KARLOVAČKA
47243	Stojmerić	Veljun	KARLOVAČKA
47243	Šljivnjak	Veljun	KARLOVAČKA
47243	Točak	Veljun	KARLOVAČKA
47243	Veljun	Veljun	KARLOVAČKA
47243	Veljunska Glina	Veljun	KARLOVAČKA
47243	Veljunski Ponorac	Veljun	KARLOVAČKA
47243	Rabinja	Veljun	KARLOVAČKA
47243	Kutanja	Veljun	KARLOVAČKA
47243	Kosijer Selo	Veljun	KARLOVAČKA
47243	Bandino Selo	Veljun	KARLOVAČKA
47243	Blagaj	Veljun	KARLOVAČKA
47243	Crno Vrelo	Veljun	KARLOVAČKA
47243	Cvijanović Brdo	Veljun	KARLOVAČKA
47243	Donja Visočka	Veljun	KARLOVAČKA
47243	Donji Poloj	Veljun	KARLOVAČKA
47243	Gornja Visočka	Veljun	KARLOVAČKA
47243	Grobnik	Veljun	KARLOVAČKA
47244	Zečev Varoš	Primišlje	KARLOVAČKA
47244	Tržić Primišljanski	Primišlje	KARLOVAČKA
47244	Mjesto Primišlje	Primišlje	KARLOVAČKA
47244	Gornje Primišlje	Primišlje	KARLOVAČKA
47244	Donje Primišlje	Primišlje	KARLOVAČKA
47245	Koranski Lug	Rakovica	KARLOVAČKA
47245	Kordunski Ljeskovac	Rakovica	KARLOVAČKA
47245	Korita Rakovička	Rakovica	KARLOVAČKA
47245	Lipovac	Rakovica	KARLOVAČKA
47245	Mašvina	Rakovica	KARLOVAČKA
47245	Nova Kršlja	Rakovica	KARLOVAČKA
47245	Oštarski Stanovi	Rakovica	KARLOVAČKA
47245	Rakovačko Selište	Rakovica	KARLOVAČKA
47245	Rakovica	Rakovica	KARLOVAČKA
47245	Stara Kršlja	Rakovica	KARLOVAČKA
47245	Klanac	Rakovica	KARLOVAČKA
47245	Jelov Klanac	Rakovica	KARLOVAČKA
47245	Basara	Rakovica	KARLOVAČKA
47245	Brajdić Selo	Rakovica	KARLOVAČKA
47245	Brezovac	Rakovica	KARLOVAČKA
47245	Broćanac	Rakovica	KARLOVAČKA
47245	Čatrnja	Rakovica	KARLOVAČKA
47245	Čuić Brdo	Rakovica	KARLOVAČKA
47245	Drage	Rakovica	KARLOVAČKA
47245	Gornja Močila	Rakovica	KARLOVAČKA
47245	Grabovac	Rakovica	KARLOVAČKA
47245	Jamarje	Rakovica	KARLOVAČKA
47246	Sadilovac	Drežnik Grad	KARLOVAČKA
47246	Lipovača Drežnička	Drežnik Grad	KARLOVAČKA
47246	Korana	Drežnik Grad	KARLOVAČKA
47246	Irinovac	Drežnik Grad	KARLOVAČKA
47246	Grabovac Drežnički	Drežnik Grad	KARLOVAČKA
47246	Drežnik Grad	Drežnik Grad	KARLOVAČKA
47246	Drežničko Selište	Drežnik Grad	KARLOVAČKA
47246	Čatrnja	Drežnik Grad	KARLOVAČKA
47250	Novigrad na Dobri	Duga Resa	KARLOVAČKA
47250	Mrežničko Dvorišće	Duga Resa	KARLOVAČKA
47250	Mrežnički Varoš	Duga Resa	KARLOVAČKA
47250	Mrežnički Novaki	Duga Resa	KARLOVAČKA
47250	Mrežnički Brig	Duga Resa	KARLOVAČKA
47250	Mrežničke Poljice	Duga Resa	KARLOVAČKA
47250	Mračin	Duga Resa	KARLOVAČKA
47250	Mihalić Selo	Duga Resa	KARLOVAČKA
47250	Pećurkovo Brdo	Duga Resa	KARLOVAČKA
47250	Petrakovo Brdo	Duga Resa	KARLOVAČKA
47250	Zagradci	Duga Resa	KARLOVAČKA
47250	Tončići	Duga Resa	KARLOVAČKA
47250	Šeketino Brdo	Duga Resa	KARLOVAČKA
47250	Sveti Petar Mrežnički	Duga Resa	KARLOVAČKA
47250	Straža	Duga Resa	KARLOVAČKA
47250	Skupica	Duga Resa	KARLOVAČKA
47250	Rešetarevo	Duga Resa	KARLOVAČKA
47250	Podvožić	Duga Resa	KARLOVAČKA
47250	Maletić	Duga Resa	KARLOVAČKA
47250	Lišnica	Duga Resa	KARLOVAČKA
47250	Jarče Polje	Duga Resa	KARLOVAČKA
47250	Bukovlje Netretičko	Duga Resa	KARLOVAČKA
47250	Bošt	Duga Resa	KARLOVAČKA
47250	Belavići	Duga Resa	KARLOVAČKA
47250	Belajski Malinci	Duga Resa	KARLOVAČKA
47250	Belajske Poljice	Duga Resa	KARLOVAČKA
47250	Belajska Vinica	Duga Resa	KARLOVAČKA
47250	Belaj	Duga Resa	KARLOVAČKA
47250	Banjsko Selo	Duga Resa	KARLOVAČKA
47250	Cerovački Galovići	Duga Resa	KARLOVAČKA
47250	Donje Mrzlo Polje Mrežničko	Duga Resa	KARLOVAČKA
47250	Gršćaki	Duga Resa	KARLOVAČKA
47250	Gornje Mrzlo Polje Mrežničko	Duga Resa	KARLOVAČKA
47250	Gorica	Duga Resa	KARLOVAČKA
47250	Galović Selo	Duga Resa	KARLOVAČKA
47250	Frketić Selo	Duga Resa	KARLOVAČKA
47250	Duga Resa	Duga Resa	KARLOVAČKA
47250	Dubravčani	Duga Resa	KARLOVAČKA
47250	Dubravci	Duga Resa	KARLOVAČKA
47251	Resnik Bosiljevski	Bosiljevo	KARLOVAČKA
47251	Rendulići	Bosiljevo	KARLOVAČKA
47251	Pribanjci	Bosiljevo	KARLOVAČKA
47251	Potok Bosiljevski	Bosiljevo	KARLOVAČKA
47251	Podumol	Bosiljevo	KARLOVAČKA
47251	Podrebar	Bosiljevo	KARLOVAČKA
47251	Otok na Dobri	Bosiljevo	KARLOVAČKA
47251	Orišje	Bosiljevo	KARLOVAČKA
47251	Novo Selo Bosiljevsko	Bosiljevo	KARLOVAČKA
47251	Sela Bosiljevska	Bosiljevo	KARLOVAČKA
47251	Skoblić Brdo	Bosiljevo	KARLOVAČKA
47251	Žubrinci	Bosiljevo	KARLOVAČKA
47251	Vrhova Gorica	Bosiljevo	KARLOVAČKA
47251	Vodena Draga	Bosiljevo	KARLOVAČKA
47251	Varoš Bosiljevski	Bosiljevo	KARLOVAČKA
47251	Umol	Bosiljevo	KARLOVAČKA
47251	Špehari	Bosiljevo	KARLOVAČKA
47251	Strgari	Bosiljevo	KARLOVAČKA
47251	Spahići	Bosiljevo	KARLOVAČKA
47251	Soline	Bosiljevo	KARLOVAČKA
47251	Milani	Bosiljevo	KARLOVAČKA
47251	Mateše	Bosiljevo	KARLOVAČKA
47251	Malik	Bosiljevo	KARLOVAČKA
47251	Glavica	Bosiljevo	KARLOVAČKA
47251	Fučkovac	Bosiljevo	KARLOVAČKA
47251	Fratrovci	Bosiljevo	KARLOVAČKA
47251	Dugače	Bosiljevo	KARLOVAČKA
47251	Dani	Bosiljevo	KARLOVAČKA
47251	Bosiljevo	Bosiljevo	KARLOVAČKA
47251	Bosanci	Bosiljevo	KARLOVAČKA
47251	Bitorajci	Bosiljevo	KARLOVAČKA
47251	Beč	Bosiljevo	KARLOVAČKA
47251	Grabrk	Bosiljevo	KARLOVAČKA
47251	Hrsina	Bosiljevo	KARLOVAČKA
47251	Lisičina Gorica	Bosiljevo	KARLOVAČKA
47251	Lipošćaki	Bosiljevo	KARLOVAČKA
47251	Laslavići	Bosiljevo	KARLOVAČKA
47251	Krč Bosiljevski	Bosiljevo	KARLOVAČKA
47251	Kraljevo Selo	Bosiljevo	KARLOVAČKA
47251	Korenić Brdo	Bosiljevo	KARLOVAČKA
47251	Kasuni	Bosiljevo	KARLOVAČKA
47251	Johi	Bosiljevo	KARLOVAČKA
47251	Jančani	Bosiljevo	KARLOVAČKA
47252	Leskovac Barilovićki	Barilović	KARLOVAČKA
47252	Lučica	Barilović	KARLOVAČKA
47252	Mali Kozinac	Barilović	KARLOVAČKA
47252	Siča	Barilović	KARLOVAČKA
47252	Šćulac	Barilović	KARLOVAČKA
47252	Veliki Kozinac	Barilović	KARLOVAČKA
47252	Križ Koranski	Barilović	KARLOVAČKA
47252	Kosijersko Selo	Barilović	KARLOVAČKA
47252	Gornji Velemerić	Barilović	KARLOVAČKA
47252	Donji Velemerić	Barilović	KARLOVAČKA
47252	Donji Skrad	Barilović	KARLOVAČKA
47252	Cerovac Barilovički	Barilović	KARLOVAČKA
47252	Carevo Selo	Barilović	KARLOVAČKA
47252	Barilović	Barilović	KARLOVAČKA
47252	Vijenac Barilovićki	Barilović	KARLOVAČKA
47252	Žabljak	Barilović	KARLOVAČKA
47253	Novi Dol	Perjasica	KARLOVAČKA
47253	Novo Selo Perjasičko	Perjasica	KARLOVAČKA
47253	Orijevac	Perjasica	KARLOVAČKA
47253	Perjasica	Perjasica	KARLOVAČKA
47253	Ponorac Perjasički	Perjasica	KARLOVAČKA
47253	Potplaninsko	Perjasica	KARLOVAČKA
47253	Srednji Poloj	Perjasica	KARLOVAČKA
47253	Svojić	Perjasica	KARLOVAČKA
47253	Štirkovac	Perjasica	KARLOVAČKA
47253	Točak Perjasički	Perjasica	KARLOVAČKA
47253	Zinajevac	Perjasica	KARLOVAČKA
47253	Mrežnica	Perjasica	KARLOVAČKA
47253	Miloševac	Perjasica	KARLOVAČKA
47253	Maurovac	Perjasica	KARLOVAČKA
47253	Bukovac Perjasički	Perjasica	KARLOVAČKA
47253	Donja Perjasica	Perjasica	KARLOVAČKA
47253	Gaćeško Selo	Perjasica	KARLOVAČKA
47253	Gornji Poloj	Perjasica	KARLOVAČKA
47253	Kestenjak	Perjasica	KARLOVAČKA
47253	Klanac Perjasički	Perjasica	KARLOVAČKA
47253	Koranska Strana	Perjasica	KARLOVAČKA
47253	Koransko Selo	Perjasica	KARLOVAČKA
47253	Kuzma Perjasička	Perjasica	KARLOVAČKA
47253	Mala Kosa	Perjasica	KARLOVAČKA
47253	Marlovac	Perjasica	KARLOVAČKA
47261	Lipov Pesak	Zvečaj	KARLOVAČKA
47261	Novo Brdo Mrežničko	Zvečaj	KARLOVAČKA
47261	Protulipa	Zvečaj	KARLOVAČKA
47261	Sarovo	Zvečaj	KARLOVAČKA
47261	Trnovo	Zvečaj	KARLOVAČKA
47261	Venac Mrežnički	Zvečaj	KARLOVAČKA
47261	Zvečaj	Zvečaj	KARLOVAČKA
47261	Lipa	Zvečaj	KARLOVAČKA
47261	Kozalj Vrh	Zvečaj	KARLOVAČKA
47261	Grganjica	Zvečaj	KARLOVAČKA
47261	Brcković Draga	Zvečaj	KARLOVAČKA
47261	Donje Bukovlje	Zvečaj	KARLOVAČKA
47261	Donji Zvečaj	Zvečaj	KARLOVAČKA
47261	Dvorjanci	Zvečaj	KARLOVAČKA
47261	Gornje Bukovlje	Zvečaj	KARLOVAČKA
47261	Gornji Zvečaj	Zvečaj	KARLOVAČKA
47261	Gradišće	Zvečaj	KARLOVAČKA
47262	Kejići	Generalski Stol	KARLOVAČKA
47262	Lešće	Generalski Stol	KARLOVAČKA
47262	Mateško Selo	Generalski Stol	KARLOVAČKA
47262	Mrežnički Brest	Generalski Stol	KARLOVAČKA
47262	Petrunići	Generalski Stol	KARLOVAČKA
47262	Radočaji	Generalski Stol	KARLOVAČKA
47262	Skukani	Generalski Stol	KARLOVAČKA
47262	Tomašići	Generalski Stol	KARLOVAČKA
47262	Jankovo Selište	Generalski Stol	KARLOVAČKA
47262	Gornji Zatezali	Generalski Stol	KARLOVAČKA
47262	Gorinci	Generalski Stol	KARLOVAČKA
47262	Crno Kamanje	Generalski Stol	KARLOVAČKA
47262	Dobrenići	Generalski Stol	KARLOVAČKA
47262	Donje Dubrave	Generalski Stol	KARLOVAČKA
47262	Donji Zatezeli	Generalski Stol	KARLOVAČKA
47262	Duga Gora	Generalski Stol	KARLOVAČKA
47262	Erdelj	Generalski Stol	KARLOVAČKA
47262	Generalski Stol	Generalski Stol	KARLOVAČKA
47262	Goričice Dobranske	Generalski Stol	KARLOVAČKA
47263	Ponikve	Gornje Dubrave	KARLOVAČKA
47263	Popovo Selo	Gornje Dubrave	KARLOVAČKA
47263	Trošmarija	Gornje Dubrave	KARLOVAČKA
47263	Višnjić Brdo	Gornje Dubrave	KARLOVAČKA
47263	Vucelići	Gornje Dubrave	KARLOVAČKA
47263	Perići	Gornje Dubrave	KARLOVAČKA
47263	Munjasi	Gornje Dubrave	KARLOVAČKA
47263	Mirići	Gornje Dubrave	KARLOVAČKA
47263	Mikašinovići	Gornje Dubrave	KARLOVAČKA
47263	Janjani	Gornje Dubrave	KARLOVAČKA
47263	Gornje Dubrave	Gornje Dubrave	KARLOVAČKA
47263	Gojak	Gornje Dubrave	KARLOVAČKA
47263	Bartolovići	Gornje Dubrave	KARLOVAČKA
47264	Zden	Tounj	KARLOVAČKA
47264	Tržić Tounjski	Tounj	KARLOVAČKA
47264	Tounj	Tounj	KARLOVAČKA
47264	Rebrovići	Tounj	KARLOVAČKA
47264	Potok Tounjski	Tounj	KARLOVAČKA
47264	Kamenica Skradnička	Tounj	KARLOVAČKA
47264	Gerovo Tounjsko	Tounj	KARLOVAČKA
47271	Mali Modrušpotok	Netretić	KARLOVAČKA
47271	Mrzljaki	Netretić	KARLOVAČKA
47271	Netretić	Netretić	KARLOVAČKA
47271	Pavičići	Netretić	KARLOVAČKA
47271	Piščetke	Netretić	KARLOVAČKA
47271	Planina Kunićka	Netretić	KARLOVAČKA
47271	Rosopajnik	Netretić	KARLOVAČKA
47271	Veliki Modrušpotok	Netretić	KARLOVAČKA
47271	Vinski Vrh	Netretić	KARLOVAČKA
47271	Zaborsko Selo	Netretić	KARLOVAČKA
47271	Završje Netretićko	Netretić	KARLOVAČKA
47271	Lonjgari	Netretić	KARLOVAČKA
47271	Lončar Brdo	Netretić	KARLOVAČKA
47271	Bajići	Netretić	KARLOVAČKA
47271	Bogovci	Netretić	KARLOVAČKA
47271	Brajakovo Brdo	Netretić	KARLOVAČKA
47271	Ćulibrki	Netretić	KARLOVAČKA
47271	Donje Stative	Netretić	KARLOVAČKA
47271	Goli Vrh Netretički	Netretić	KARLOVAČKA
47271	Jakovci Netretički	Netretić	KARLOVAČKA
47271	Kolenovac	Netretić	KARLOVAČKA
47271	Kućevice	Netretić	KARLOVAČKA
47271	Kunić Ribnički	Netretić	KARLOVAČKA
47271	Ladešići	Netretić	KARLOVAČKA
47272	Novaki Lipnički	Ribnik	KARLOVAČKA
47272	Obrh	Ribnik	KARLOVAČKA
47272	Ravnica	Ribnik	KARLOVAČKA
47272	Ribnik	Ribnik	KARLOVAČKA
47272	Skradsko Selo	Ribnik	KARLOVAČKA
47272	Sopčić Vrh	Ribnik	KARLOVAČKA
47272	Sračak	Ribnik	KARLOVAČKA
47272	Stankovci	Ribnik	KARLOVAČKA
47272	Veselići	Ribnik	KARLOVAČKA
47272	Mošanci	Ribnik	KARLOVAČKA
47272	Martinski Vrh	Ribnik	KARLOVAČKA
47272	Lipnik	Ribnik	KARLOVAČKA
47272	Donja Stranica	Ribnik	KARLOVAČKA
47272	Drenovica Lipnička	Ribnik	KARLOVAČKA
47272	Goli Vrh Lipnički	Ribnik	KARLOVAČKA
47272	Gorica Lipnička	Ribnik	KARLOVAČKA
47272	Gornja Stranica	Ribnik	KARLOVAČKA
47272	Griče	Ribnik	KARLOVAČKA
47272	Jadrići	Ribnik	KARLOVAČKA
47272	Jarnevići	Ribnik	KARLOVAČKA
47272	Jasenovica	Ribnik	KARLOVAČKA
47273	Vukova Gorica	Srednje Prilišće	KARLOVAČKA
47273	Srednje Prilišće	Srednje Prilišće	KARLOVAČKA
47273	Račak	Srednje Prilišće	KARLOVAČKA
47273	Gornje Prilišće	Srednje Prilišće	KARLOVAČKA
47273	Donje Prilišće	Srednje Prilišće	KARLOVAČKA
47276	Mala Paka	Žakanje	KARLOVAČKA
47276	Mišinci	Žakanje	KARLOVAČKA
47276	Prautina	Žakanje	KARLOVAČKA
47276	Sela Žakanjska	Žakanje	KARLOVAČKA
47276	Velika Paka	Žakanje	KARLOVAČKA
47276	Zaluka Lipnička	Žakanje	KARLOVAČKA
47276	Žakanje	Žakanje	KARLOVAČKA
47276	Kohanjac	Žakanje	KARLOVAČKA
47276	Jurovski Brod	Žakanje	KARLOVAČKA
47276	Jurovo	Žakanje	KARLOVAČKA
47276	Breznik Žakanjski	Žakanje	KARLOVAČKA
47276	Brihovo	Žakanje	KARLOVAČKA
47276	Bubnjarski Brod	Žakanje	KARLOVAČKA
47276	Donji Bukovac Žakanjski	Žakanje	KARLOVAČKA
47276	Ertić	Žakanje	KARLOVAČKA
47276	Gornji Bukovac Žakanjski	Žakanje	KARLOVAČKA
47276	Jugovac	Žakanje	KARLOVAČKA
47280	Polje Ozaljsko	Ozalj	KARLOVAČKA
47280	Požun	Ozalj	KARLOVAČKA
47280	Soldatići	Ozalj	KARLOVAČKA
47280	Škaljevica	Ozalj	KARLOVAČKA
47280	Trešćerovac	Ozalj	KARLOVAČKA
47280	Trg	Ozalj	KARLOVAČKA
47280	Vinivrh	Ozalj	KARLOVAČKA
47280	Vrhovac	Ozalj	KARLOVAČKA
47280	Vrhovački Sopot	Ozalj	KARLOVAČKA
47280	Zajačko Selo	Ozalj	KARLOVAČKA
47280	Zaluka	Ozalj	KARLOVAČKA
47280	Zorkovac	Ozalj	KARLOVAČKA
47280	Zorkovac na Kupi	Ozalj	KARLOVAČKA
47280	Podgraj	Ozalj	KARLOVAČKA
47280	Podbrežje	Ozalj	KARLOVAČKA
47280	Ozalj	Ozalj	KARLOVAČKA
47280	Belinsko Selo	Ozalj	KARLOVAČKA
47280	Boševci	Ozalj	KARLOVAČKA
47280	Donji Oštri Vrh Ozaljski	Ozalj	KARLOVAČKA
47280	Dvorišće Ozaljsko	Ozalj	KARLOVAČKA
47280	Ferenci	Ozalj	KARLOVAČKA
47280	Fratrovci Ozaljski	Ozalj	KARLOVAČKA
47280	Goli Vrh Ozaljski	Ozalj	KARLOVAČKA
47280	Gornji Oštri Vrh Ozaljski	Ozalj	KARLOVAČKA
47280	Novaki Ozaljski	Ozalj	KARLOVAČKA
47280	Lukšići Ozaljski	Ozalj	KARLOVAČKA
47280	Ilovac	Ozalj	KARLOVAČKA
47280	Grandić Breg	Ozalj	KARLOVAČKA
47280	Goršćaki Ozaljski	Ozalj	KARLOVAČKA
47281	Vuksani	Mali Erjavec	KARLOVAČKA
47281	Vrbanska Draga	Mali Erjavec	KARLOVAČKA
47281	Veliki Erjavec	Mali Erjavec	KARLOVAČKA
47281	Tomašnica	Mali Erjavec	KARLOVAČKA
47281	Svetičko Hrašće	Mali Erjavec	KARLOVAČKA
47281	Svetice	Mali Erjavec	KARLOVAČKA
47281	Slapno	Mali Erjavec	KARLOVAČKA
47281	Mali Erjavec	Mali Erjavec	KARLOVAČKA
47281	Jaškovo	Mali Erjavec	KARLOVAČKA
47281	Grdun	Mali Erjavec	KARLOVAČKA
47281	Breznik	Mali Erjavec	KARLOVAČKA
47282	Police Pirišće	Kamanje	KARLOVAČKA
47282	Preseka Ozaljska	Kamanje	KARLOVAČKA
47282	Reštovo	Kamanje	KARLOVAČKA
47282	Rujevo	Kamanje	KARLOVAČKA
47282	Veliki Vrh Kamanjski	Kamanje	KARLOVAČKA
47282	Orljakovo	Kamanje	KARLOVAČKA
47282	Mali Vrh Kamanjski	Kamanje	KARLOVAČKA
47282	Lukinić Draga	Kamanje	KARLOVAČKA
47282	Kamanje	Kamanje	KARLOVAČKA
47282	Durlinci	Kamanje	KARLOVAČKA
47282	Bubnjarci	Kamanje	KARLOVAČKA
47282	Brlog Ozaljski	Kamanje	KARLOVAČKA
47282	Bratovanci	Kamanje	KARLOVAČKA
47283	Radina Vas	Vivodina	KARLOVAČKA
47283	Petruš Vrh	Vivodina	KARLOVAČKA
47283	Pećarići	Vivodina	KARLOVAČKA
47283	Obrež Vivodinski	Vivodina	KARLOVAČKA
47283	Lović Prekriški	Vivodina	KARLOVAČKA
47283	Sršići	Vivodina	KARLOVAČKA
47283	Stojavnica	Vivodina	KARLOVAČKA
47283	Varaštovac	Vivodina	KARLOVAČKA
47283	Vivodina	Vivodina	KARLOVAČKA
47283	Vrškovac	Vivodina	KARLOVAČKA
47283	Vuketić	Vivodina	KARLOVAČKA
47283	Zorkovac Vivodinski	Vivodina	KARLOVAČKA
47283	Hrastovica Vivodinska	Vivodina	KARLOVAČKA
47283	Hodinci	Vivodina	KARLOVAČKA
47283	Belošići	Vivodina	KARLOVAČKA
47283	Brezje Vivodinsko	Vivodina	KARLOVAČKA
47283	Budim Vivodinski	Vivodina	KARLOVAČKA
47283	Cerje Vivodinsko	Vivodina	KARLOVAČKA
47283	Dojutrovica	Vivodina	KARLOVAČKA
47283	Donji Lović	Vivodina	KARLOVAČKA
47283	Dvorišće Vivodinsko	Vivodina	KARLOVAČKA
47283	Furjanići	Vivodina	KARLOVAČKA
47283	Galezova Draga	Vivodina	KARLOVAČKA
47283	Galin	Vivodina	KARLOVAČKA
47283	Gorniki Vivodinski	Vivodina	KARLOVAČKA
47283	Gornji Lović	Vivodina	KARLOVAČKA
47284	Kašt	Kašt	KARLOVAČKA
47284	Dančulovići	Kašt	KARLOVAČKA
47284	Brašljevica	Kašt	KARLOVAČKA
47284	Badovinci	Kašt	KARLOVAČKA
47285	Liješće	Radatovići	KARLOVAČKA
47285	Malinci	Radatovići	KARLOVAČKA
47285	Pilatovci	Radatovići	KARLOVAČKA
47285	Popovići Žumberački	Radatovići	KARLOVAČKA
47285	Radatovići	Radatovići	KARLOVAČKA
47285	Rajakovići	Radatovići	KARLOVAČKA
47285	Sekulići	Radatovići	KARLOVAČKA
47285	Šiljki	Radatovići	KARLOVAČKA
47285	Kunčani	Radatovići	KARLOVAČKA
47285	Kuljaji	Radatovići	KARLOVAČKA
47285	Keseri	Radatovići	KARLOVAČKA
47285	Bulići	Radatovići	KARLOVAČKA
47285	Ćetiše	Radatovići	KARLOVAČKA
47285	Doljani Žumberački	Radatovići	KARLOVAČKA
47285	Dragoševci	Radatovići	KARLOVAČKA
47285	Dučići	Radatovići	KARLOVAČKA
47285	Goleši Žumberački	Radatovići	KARLOVAČKA
47285	Gudalji	Radatovići	KARLOVAČKA
47285	Kamenci	Radatovići	KARLOVAČKA
47286	Zagraj	Mahično	KARLOVAČKA
47286	Vukoder	Mahično	KARLOVAČKA
47286	Tuškani	Mahično	KARLOVAČKA
47286	Šebreki	Mahično	KARLOVAČKA
47286	Priselci	Mahično	KARLOVAČKA
47286	Mahično	Mahično	KARLOVAČKA
47286	Levkušje	Mahično	KARLOVAČKA
47286	Konjkovsko	Mahično	KARLOVAČKA
47286	Goršćaki	Mahično	KARLOVAČKA
47286	Gornje Pokupje	Mahično	KARLOVAČKA
47300	Potok Muslinski	Ogulin	KARLOVAČKA
47300	Puškarići	Ogulin	KARLOVAČKA
47300	Turkovići Ogulinski	Ogulin	KARLOVAČKA
47300	Vitunj	Ogulin	KARLOVAČKA
47300	Zečica	Ogulin	KARLOVAČKA
47300	Okruglica	Ogulin	KARLOVAČKA
47300	Oklinak	Ogulin	KARLOVAČKA
47300	Ogulin	Ogulin	KARLOVAČKA
47300	Mirić Selo	Ogulin	KARLOVAČKA
47300	Marković Selo	Ogulin	KARLOVAČKA
47300	Kučaj	Ogulin	KARLOVAČKA
47300	Hreljin Ogulinski	Ogulin	KARLOVAČKA
47300	Brestovac Ogulinski	Ogulin	KARLOVAČKA
47302	Skradnik	Oštarije	KARLOVAČKA
47302	Otok Oštarijski	Oštarije	KARLOVAČKA
47302	Oštarije	Oštarije	KARLOVAČKA
47303	Vojnovac	Josipdol	KARLOVAČKA
47303	Vajin Vrh	Josipdol	KARLOVAČKA
47303	Trojvrh	Josipdol	KARLOVAČKA
47303	Salopeki Modruški	Josipdol	KARLOVAČKA
47303	Sabljaki Modruški	Josipdol	KARLOVAČKA
47303	Munjava	Josipdol	KARLOVAČKA
47303	Modruška Munjava	Josipdol	KARLOVAČKA
47303	Carevo Polje	Josipdol	KARLOVAČKA
47303	Cerovnik	Josipdol	KARLOVAČKA
47303	Istočni Trojvrh	Josipdol	KARLOVAČKA
47303	Josipdol	Josipdol	KARLOVAČKA
47303	Modruš	Josipdol	KARLOVAČKA
47304	Pothum Plaščanski	Plaški	KARLOVAČKA
47304	Plaški	Plaški	KARLOVAČKA
47304	Međeđak	Plaški	KARLOVAČKA
47304	Latin	Plaški	KARLOVAČKA
47304	Lapat	Plaški	KARLOVAČKA
47304	Kunić	Plaški	KARLOVAČKA
47304	Jezero I Dio	Plaški	KARLOVAČKA
47304	Janja Gora	Plaški	KARLOVAČKA
47305	Lička Jesenica	Lička Jesenica	KARLOVAČKA
47305	Blata	Lička Jesenica	KARLOVAČKA
47305	Begovac Plaščanski	Lička Jesenica	KARLOVAČKA
47306	Saborsko	Saborsko	KARLOVAČKA
47307	Zagorje Modruško	Gornje Zagorje	KARLOVAČKA
47307	Gornje Zagorje	Gornje Zagorje	KARLOVAČKA
47307	Dujmić Selo	Gornje Zagorje	KARLOVAČKA
47307	Donje Zagorje	Gornje Zagorje	KARLOVAČKA
47307	Desmerice	Gornje Zagorje	KARLOVAČKA
47313	Vukelići	Drežnica	KARLOVAČKA
47313	Vručac	Drežnica	KARLOVAČKA
47313	Trbovići	Drežnica	KARLOVAČKA
47313	Tomići	Drežnica	KARLOVAČKA
47313	Seočani	Drežnica	KARLOVAČKA
47313	Radojčići	Drežnica	KARLOVAČKA
47313	Podbitoraj	Drežnica	KARLOVAČKA
47313	Nikolići	Drežnica	KARLOVAČKA
47313	Maravić Draga	Drežnica	KARLOVAČKA
47313	Krakar	Drežnica	KARLOVAČKA
47313	Drežnica	Drežnica	KARLOVAČKA
47313	Brezno Drežničko	Drežnica	KARLOVAČKA
47313	Zrnići	Drežnica	KARLOVAČKA
47314	Jasenak	Jasenak	KARLOVAČKA
48000	Bakovčice	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48000	Štaglinec	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48000	Starigrad	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48000	Rovištanci	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48000	Pešćenik	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48000	Koprivnica	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48000	Jagnjedovac	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48000	Hudovljani	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48000	Herešin	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48000	Gornja Velika	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48000	Donja Velika	Koprivnica	KOPRIVNIČKO-KRIŽEVAČKA
48213	Markovac Križevački	Cirkvena	KOPRIVNIČKO-KRIŽEVAČKA
48213	Ladinec	Cirkvena	KOPRIVNIČKO-KRIŽEVAČKA
48213	Kuštani	Cirkvena	KOPRIVNIČKO-KRIŽEVAČKA
48213	Kenđelovec	Cirkvena	KOPRIVNIČKO-KRIŽEVAČKA
48213	Hrsovo	Cirkvena	KOPRIVNIČKO-KRIŽEVAČKA
48213	Cirkvena	Cirkvena	KOPRIVNIČKO-KRIŽEVAČKA
48213	Cepidlak	Cirkvena	KOPRIVNIČKO-KRIŽEVAČKA
48213	Brdo Cirkvensko	Cirkvena	KOPRIVNIČKO-KRIŽEVAČKA
48214	Trema	Sveti Ivan Žabno	KOPRIVNIČKO-KRIŽEVAČKA
48214	Škrinjari	Sveti Ivan Žabno	KOPRIVNIČKO-KRIŽEVAČKA
48214	Sveti Ivan Žabno	Sveti Ivan Žabno	KOPRIVNIČKO-KRIŽEVAČKA
48214	Predavec Križevački	Sveti Ivan Žabno	KOPRIVNIČKO-KRIŽEVAČKA
48214	Novi Glog	Sveti Ivan Žabno	KOPRIVNIČKO-KRIŽEVAČKA
48214	Brezovljani	Sveti Ivan Žabno	KOPRIVNIČKO-KRIŽEVAČKA
48260	Podgajec	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Pesek	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Osijek Vojakovački	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Novi Đurđic	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Marinovec	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Mali Potočec	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Poljana Križevačka	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Povelić	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Prikraj Križevački	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Ruševac	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Sveta Helena	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Sveti Martin	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Sveti Petar Čvrstec	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Veliki Potočec	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Majurec	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Lemeš Križevački	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Križevci	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Apatovec	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Bukovje Križevačko	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Cubinec	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Dijankovec	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Donja Brckovčina	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Donja Glogovnica	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Đurđic	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Erdovec	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Gornja Brckovčina	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Gornja Glogovnica	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Gračina	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Ivanec Križevački	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Jarčani	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48260	Karane	Križevci	KOPRIVNIČKO-KRIŽEVAČKA
48263	Stari Bošnjani	Carevdar	KOPRIVNIČKO-KRIŽEVAČKA
48263	Novi Bošnjani	Carevdar	KOPRIVNIČKO-KRIŽEVAČKA
48263	Mali Carevdar	Carevdar	KOPRIVNIČKO-KRIŽEVAČKA
48263	Kostadinovac	Carevdar	KOPRIVNIČKO-KRIŽEVAČKA
48263	Carevdar	Carevdar	KOPRIVNIČKO-KRIŽEVAČKA
48264	Vujići Vojakovački	Kloštar Vojakovački	KOPRIVNIČKO-KRIŽEVAČKA
48264	Vojakovac	Kloštar Vojakovački	KOPRIVNIČKO-KRIŽEVAČKA
48264	Velike Sesvete	Kloštar Vojakovački	KOPRIVNIČKO-KRIŽEVAČKA
48264	Večeslavec	Kloštar Vojakovački	KOPRIVNIČKO-KRIŽEVAČKA
48264	Raščani	Kloštar Vojakovački	KOPRIVNIČKO-KRIŽEVAČKA
48264	Podbrđani Vojkovački	Kloštar Vojakovački	KOPRIVNIČKO-KRIŽEVAČKA
48264	Mičijevac	Kloštar Vojakovački	KOPRIVNIČKO-KRIŽEVAČKA
48264	Male Sesvete	Kloštar Vojakovački	KOPRIVNIČKO-KRIŽEVAČKA
48264	Kloštar Vojakovački	Kloštar Vojakovački	KOPRIVNIČKO-KRIŽEVAČKA
48264	Čabraji	Kloštar Vojakovački	KOPRIVNIČKO-KRIŽEVAČKA
48265	Lemeš	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Mali Raven	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Novaki Ravenski	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Pavlovec Ravenski	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Sela Ravenska	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Srednji Dubovec	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Stara Ves Ravenska	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Špiranec	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Veliki Raven	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Kunđevec	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Kučari	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Bojnikovec	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Doljanec	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Donji Dubovec	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Donji Tkalec	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Ferežani	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Gornji Dubovec	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Gornji Tkalec	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Gregurovec	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48265	Kapela Ravenska	Raven	KOPRIVNIČKO-KRIŽEVAČKA
48267	Selanec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Rovci	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Podvinje Miholečko	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Piškovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Orehovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Selnica Miholečka	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Sveti Petar Orehovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Šalamunovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Viranec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Voljevec Riječki	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Vukovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Zaistovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Zamladinec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Mirkovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Miholec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Beketinec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Bočkovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Bogačevo	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Brdo Orehovečko	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Brežani	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Črnčevec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Donji Fodrovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Finčevec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Međa	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Hrgovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Gušćerovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Gornji Fodrovec	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48267	Gorica Miholečka	Orehovec	KOPRIVNIČKO-KRIŽEVAČKA
48268	Kostanjevec Riječki	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Kusijevec	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Lukačevec	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Mokrice Miholečke	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Nemčevac	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Pofuki	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Štrigovec	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Vukšinec Riječki	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Kolarec	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Gornja Rijeka	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Barlabaševec	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Bogačevo Riječko	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Brezje Miholečko	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Deklešanec	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Donja Rijeka	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Dropkovec	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Fajerovec	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48268	Fodrovac Riječki	Gornja Rijeka	KOPRIVNIČKO-KRIŽEVAČKA
48269	Žibrinovec	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48269	Vojnovec Kalnički	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48269	Šopron	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48269	Potok Kalnički	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48269	Popovec Kalnički	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48269	Obrež Kalnički	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48269	Kamešnica	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48269	Kalnik	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48269	Hižanovec	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48269	Dedina	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48269	Borje	Kalnik	KOPRIVNIČKO-KRIŽEVAČKA
48305	Reka	Reka	KOPRIVNIČKO-KRIŽEVAČKA
48305	Kamenica	Reka	KOPRIVNIČKO-KRIŽEVAČKA
48306	Miličani	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Paunovac	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Prnjavor Lepavinski	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Rijeka Koprivnička	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Sokolovac	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Srijem	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Široko Selo	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Trnovac Sokolovački	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Velika Branjska	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Velika Mučna	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Veliki Botinovac	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Vrhovac Sokolovački	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Mali Poganac	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Mali Grabičani	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Brđani Sokolovački	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Domaji	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Donjara	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Donji Maslarac	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Gornji Maslarac	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Grdak	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Jankovac	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Ladislav Sokolovački	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Lepavina	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Mala Branjska	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Mala Mučna	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48306	Mali Botinovac	Sokolovac	KOPRIVNIČKO-KRIŽEVAČKA
48311	Subotica Podravska	Kunovec	KOPRIVNIČKO-KRIŽEVAČKA
48311	Kunovec Breg	Kunovec	KOPRIVNIČKO-KRIŽEVAČKA
48311	Kunovec	Kunovec	KOPRIVNIČKO-KRIŽEVAČKA
48311	Goričko	Kunovec	KOPRIVNIČKO-KRIŽEVAČKA
48311	Botinovec	Kunovec	KOPRIVNIČKO-KRIŽEVAČKA
48312	Mala Rijeka	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Prkos	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Radeljevo Selo	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Rasinja	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Ribnjak	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Velika Rasinjica	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Veliki Grabičani	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Veliki Poganac	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Vojvodinec	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Mala Rasinjica	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Lukovec	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Belanovo Selo	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Cvetkovec	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Duga Rijeka	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Gorica	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Grbaševec	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Ivančec	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Koledinec	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Kuzminec	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48312	Ludbreški Ivanec	Rasinja	KOPRIVNIČKO-KRIŽEVAČKA
48314	Koprivnički Ivanec	Koprivnički Ivanec	KOPRIVNIČKO-KRIŽEVAČKA
48314	Pustakovec	Koprivnički Ivanec	KOPRIVNIČKO-KRIŽEVAČKA
48316	Zablatje	Đelekovec	KOPRIVNIČKO-KRIŽEVAČKA
48316	Imbriovec	Đelekovec	KOPRIVNIČKO-KRIŽEVAČKA
48316	Đelekovec	Đelekovec	KOPRIVNIČKO-KRIŽEVAČKA
48317	Veliki Otok	Legrad	KOPRIVNIČKO-KRIŽEVAČKA
48317	Selnica Podravska	Legrad	KOPRIVNIČKO-KRIŽEVAČKA
48317	Mali Otok	Legrad	KOPRIVNIČKO-KRIŽEVAČKA
48317	Legrad	Legrad	KOPRIVNIČKO-KRIŽEVAČKA
48317	Kutnjak	Legrad	KOPRIVNIČKO-KRIŽEVAČKA
48317	Antolovec	Legrad	KOPRIVNIČKO-KRIŽEVAČKA
48321	Peteranec	Peteranec	KOPRIVNIČKO-KRIŽEVAČKA
48321	Sigetec	Peteranec	KOPRIVNIČKO-KRIŽEVAČKA
48322	Botovo	Drnje	KOPRIVNIČKO-KRIŽEVAČKA
48322	Drnje	Drnje	KOPRIVNIČKO-KRIŽEVAČKA
48322	Torčec	Drnje	KOPRIVNIČKO-KRIŽEVAČKA
48323	Komatnica	Hlebine	KOPRIVNIČKO-KRIŽEVAČKA
48323	Hlebine	Hlebine	KOPRIVNIČKO-KRIŽEVAČKA
48323	Gambajeva Greda	Hlebine	KOPRIVNIČKO-KRIŽEVAČKA
48324	Borovljani	Koprivnički Bregi	KOPRIVNIČKO-KRIŽEVAČKA
48324	Glogovac	Koprivnički Bregi	KOPRIVNIČKO-KRIŽEVAČKA
48324	Jeduševac	Koprivnički Bregi	KOPRIVNIČKO-KRIŽEVAČKA
48324	Koprivnički Bregi	Koprivnički Bregi	KOPRIVNIČKO-KRIŽEVAČKA
48325	Vlaislav	Novigrad Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48325	Srdinac	Novigrad Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48325	Plavšinac	Novigrad Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48325	Novigrad Podravski	Novigrad Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48325	Javorovac	Novigrad Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48325	Delovi	Novigrad Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48326	Virje	Virje	KOPRIVNIČKO-KRIŽEVAČKA
48326	Miholjanec	Virje	KOPRIVNIČKO-KRIŽEVAČKA
48326	Donje Zdjelice	Virje	KOPRIVNIČKO-KRIŽEVAČKA
48327	Čingi-lingi	Molve	KOPRIVNIČKO-KRIŽEVAČKA
48327	Molve	Molve	KOPRIVNIČKO-KRIŽEVAČKA
48327	Molve Grede	Molve	KOPRIVNIČKO-KRIŽEVAČKA
48331	Otočka	Gola	KOPRIVNIČKO-KRIŽEVAČKA
48331	Novačka	Gola	KOPRIVNIČKO-KRIŽEVAČKA
48331	Gotalovo	Gola	KOPRIVNIČKO-KRIŽEVAČKA
48331	Gola	Gola	KOPRIVNIČKO-KRIŽEVAČKA
48332	Repaš	Ždala	KOPRIVNIČKO-KRIŽEVAČKA
48332	Ždala	Ždala	KOPRIVNIČKO-KRIŽEVAČKA
48350	Šemovci	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48350	Sveta Ana	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48350	Sirova Katalena	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48350	Severovci	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48350	Rakitnica	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48350	Mičetinac	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48350	Hampovica	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48350	Grkine	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48350	Đurđevac	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48350	Čepelovac	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48350	Budrovac	Đurđevac	KOPRIVNIČKO-KRIŽEVAČKA
48355	Novo Virje	Novo Virje	KOPRIVNIČKO-KRIŽEVAČKA
48356	Batinske	Ferdinandovac	KOPRIVNIČKO-KRIŽEVAČKA
48356	Brodić	Ferdinandovac	KOPRIVNIČKO-KRIŽEVAČKA
48356	Ferdinandovac	Ferdinandovac	KOPRIVNIČKO-KRIŽEVAČKA
48356	Molvice	Ferdinandovac	KOPRIVNIČKO-KRIŽEVAČKA
48361	Kalinovac	Kalinovac	KOPRIVNIČKO-KRIŽEVAČKA
48361	Hrastova Greda	Kalinovac	KOPRIVNIČKO-KRIŽEVAČKA
48361	Hladna Voda	Kalinovac	KOPRIVNIČKO-KRIŽEVAČKA
48362	Suha Katalena	Kloštar Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48362	Prugovac	Kloštar Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48362	Kozarevac	Kloštar Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48362	Kloštar Podravski	Kloštar Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48362	Dinjevac	Kloštar Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48362	Budančevica	Kloštar Podravski	KOPRIVNIČKO-KRIŽEVAČKA
48363	Podravske Sesvete	Podravske Sesvete	KOPRIVNIČKO-KRIŽEVAČKA
49000	Straža Krapinska	Krapina	KRAPINSKO-ZAGORSKA
49000	Šušelj Brijeg	Krapina	KRAPINSKO-ZAGORSKA
49000	Tkalci	Krapina	KRAPINSKO-ZAGORSKA
49000	Trški Vrh	Krapina	KRAPINSKO-ZAGORSKA
49000	Vidovec Krapinski	Krapina	KRAPINSKO-ZAGORSKA
49000	Zagora	Krapina	KRAPINSKO-ZAGORSKA
49000	Žutnica	Krapina	KRAPINSKO-ZAGORSKA
49000	Strahinje	Krapina	KRAPINSKO-ZAGORSKA
49000	Pristava Krapinska	Krapina	KRAPINSKO-ZAGORSKA
49000	Pretkovec	Krapina	KRAPINSKO-ZAGORSKA
49000	Bobovje	Krapina	KRAPINSKO-ZAGORSKA
49000	Dolići	Krapina	KRAPINSKO-ZAGORSKA
49000	Krapina	Krapina	KRAPINSKO-ZAGORSKA
49000	Lazi Krapinski	Krapina	KRAPINSKO-ZAGORSKA
49000	Mihaljekov Jarek	Krapina	KRAPINSKO-ZAGORSKA
49000	Podgora Krapinska	Krapina	KRAPINSKO-ZAGORSKA
49000	Polje Krapinsko	Krapina	KRAPINSKO-ZAGORSKA
49210	Martinišće	Zabok	KRAPINSKO-ZAGORSKA
49210	Pavlovec Zabočki	Zabok	KRAPINSKO-ZAGORSKA
49210	Repovec	Zabok	KRAPINSKO-ZAGORSKA
49210	Špičkovina	Zabok	KRAPINSKO-ZAGORSKA
49210	Tisanić Jarek	Zabok	KRAPINSKO-ZAGORSKA
49210	Zabok	Zabok	KRAPINSKO-ZAGORSKA
49210	Lug Zabočki	Zabok	KRAPINSKO-ZAGORSKA
49210	Jakuševec Zabočki	Zabok	KRAPINSKO-ZAGORSKA
49210	Bračak	Zabok	KRAPINSKO-ZAGORSKA
49210	Bregi Zabočki	Zabok	KRAPINSKO-ZAGORSKA
49210	Dubrava Zabočka	Zabok	KRAPINSKO-ZAGORSKA
49210	Grabrovec	Zabok	KRAPINSKO-ZAGORSKA
49210	Grdenci	Zabok	KRAPINSKO-ZAGORSKA
49210	Hum Zabočki	Zabok	KRAPINSKO-ZAGORSKA
49214	Prosenik Gubaševski	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Ravnice	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Strmec	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Turnišće Klanečko	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Veliko Trgovišće	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Vižovlje	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Požarkovec	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Mrzlo Polje	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Jezero Klanječko	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Bezavina/dio/	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Domahovo	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Družilovec	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Dubrovčan/dio/	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Gubaševo	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49214	Jalšje	Veliko Trgovišće	KRAPINSKO-ZAGORSKA
49215	Sveti Križ	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Trsteno	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Tuhelj	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Tuheljske Toplice	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Velika Erpenja	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Vilanci	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Prosenik	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Pristava	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Lipnica Zagorska	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Banska Gorica	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Bezavina/dio/	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Črešnjevec	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Dubrovčan/dio/	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Glogovec Zagorski	Tuhelj	KRAPINSKO-ZAGORSKA
49215	Lenišće	Tuhelj	KRAPINSKO-ZAGORSKA
49216	Jelenjak	Desinić	KRAPINSKO-ZAGORSKA
49216	Klanječno	Desinić	KRAPINSKO-ZAGORSKA
49216	Košnica	Desinić	KRAPINSKO-ZAGORSKA
49216	Nebojse	Desinić	KRAPINSKO-ZAGORSKA
49216	Osredek Desinički	Desinić	KRAPINSKO-ZAGORSKA
49216	Ravnice Desiničke	Desinić	KRAPINSKO-ZAGORSKA
49216	Stara Ves Košnička	Desinić	KRAPINSKO-ZAGORSKA
49216	Šimunci	Desinić	KRAPINSKO-ZAGORSKA
49216	Škalić Zagorski	Desinić	KRAPINSKO-ZAGORSKA
49216	Trnovec Desinički	Desinić	KRAPINSKO-ZAGORSKA
49216	Turnišće Desinićko	Desinić	KRAPINSKO-ZAGORSKA
49216	Turnovo	Desinić	KRAPINSKO-ZAGORSKA
49216	Velika Horvatska	Desinić	KRAPINSKO-ZAGORSKA
49216	Jazbina	Desinić	KRAPINSKO-ZAGORSKA
49216	Ivanić Košnički	Desinić	KRAPINSKO-ZAGORSKA
49216	Desinić	Desinić	KRAPINSKO-ZAGORSKA
49216	Desinić Gora	Desinić	KRAPINSKO-ZAGORSKA
49216	Donji Jalšovec	Desinić	KRAPINSKO-ZAGORSKA
49216	Donji Zbilj	Desinić	KRAPINSKO-ZAGORSKA
49216	Dubravica Desinićka	Desinić	KRAPINSKO-ZAGORSKA
49216	Gaber	Desinić	KRAPINSKO-ZAGORSKA
49216	Gora Košnička	Desinić	KRAPINSKO-ZAGORSKA
49216	Gornji Jalšovec	Desinić	KRAPINSKO-ZAGORSKA
49216	Gornji Zbilj	Desinić	KRAPINSKO-ZAGORSKA
49216	Gostenje	Desinić	KRAPINSKO-ZAGORSKA
49216	Grohot	Desinić	KRAPINSKO-ZAGORSKA
49216	Hum Košnički	Desinić	KRAPINSKO-ZAGORSKA
49216	Ivanić Desinićki	Desinić	KRAPINSKO-ZAGORSKA
49217	Mala Erpenja	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Maturovec	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Oratje	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Selno	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Slivonja Jarek	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Viča Sela	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Vrtnjakovec	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Lovreća Sela	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Krapinske Toplice	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Klupci	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Čret	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Donje Vino	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Gregurovec	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Hršak Breg	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Jasenovec Zagorski	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Jurjevec Začretski	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49217	Klokovec	Krapinske Toplice	KRAPINSKO-ZAGORSKA
49218	Pavlovec Pregradski	Pregrada	KRAPINSKO-ZAGORSKA
49218	Pregrada	Pregrada	KRAPINSKO-ZAGORSKA
49218	Sopot	Pregrada	KRAPINSKO-ZAGORSKA
49218	Stipernica	Pregrada	KRAPINSKO-ZAGORSKA
49218	Svetojurski Vrh	Pregrada	KRAPINSKO-ZAGORSKA
49218	Valentinovo	Pregrada	KRAPINSKO-ZAGORSKA
49218	Velika Gora	Pregrada	KRAPINSKO-ZAGORSKA
49218	Vinagora	Pregrada	KRAPINSKO-ZAGORSKA
49218	Višnjevec	Pregrada	KRAPINSKO-ZAGORSKA
49218	Vojsak	Pregrada	KRAPINSKO-ZAGORSKA
49218	Vrhi Pregradski	Pregrada	KRAPINSKO-ZAGORSKA
49218	Vrhi Vinagorski	Pregrada	KRAPINSKO-ZAGORSKA
49218	Martiša Ves	Pregrada	KRAPINSKO-ZAGORSKA
49218	Marinec	Pregrada	KRAPINSKO-ZAGORSKA
49218	Benkovo	Pregrada	KRAPINSKO-ZAGORSKA
49218	Bregi Kostelski	Pregrada	KRAPINSKO-ZAGORSKA
49218	Bušin	Pregrada	KRAPINSKO-ZAGORSKA
49218	Cigrovec	Pregrada	KRAPINSKO-ZAGORSKA
49218	Donja Plemenšćina	Pregrada	KRAPINSKO-ZAGORSKA
49218	Gabrovec	Pregrada	KRAPINSKO-ZAGORSKA
49218	Gorjakovo	Pregrada	KRAPINSKO-ZAGORSKA
49218	Gornja Plemenšćina	Pregrada	KRAPINSKO-ZAGORSKA
49218	Klenice	Pregrada	KRAPINSKO-ZAGORSKA
49218	Kostel	Pregrada	KRAPINSKO-ZAGORSKA
49218	Kostelsko	Pregrada	KRAPINSKO-ZAGORSKA
49218	Mala Gora	Pregrada	KRAPINSKO-ZAGORSKA
49221	Židovnjak	Bedekovčina	KRAPINSKO-ZAGORSKA
49221	Vučak	Bedekovčina	KRAPINSKO-ZAGORSKA
49221	Križanče	Bedekovčina	KRAPINSKO-ZAGORSKA
49221	Kebel	Bedekovčina	KRAPINSKO-ZAGORSKA
49221	Bedekovčina	Bedekovčina	KRAPINSKO-ZAGORSKA
49222	Lug Poznanovečki	Poznanovec	KRAPINSKO-ZAGORSKA
49222	Poznanovec	Poznanovec	KRAPINSKO-ZAGORSKA
49223	Sekirišće	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Sveti Križ Začretje	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Štrucljevo	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Švaljkovec/dio/	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Temovec	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Vrankovec	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Zleć	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Pustodol Začretski	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Prosenik Začretski	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Mirkovec	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Brezova	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Ciglenica Zagorska	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Donja Pačetina	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Dukovec	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Komor Začretski	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Kotarice	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49223	Kozjak Začretski	Sveti Križ Začretje	KRAPINSKO-ZAGORSKA
49224	Završje Začretsko	Lepajci	KRAPINSKO-ZAGORSKA
49224	Vidovec Petrovski	Lepajci	KRAPINSKO-ZAGORSKA
49224	Velika Ves	Lepajci	KRAPINSKO-ZAGORSKA
49224	Švaljkovec/dio/	Lepajci	KRAPINSKO-ZAGORSKA
49224	Škarićevo	Lepajci	KRAPINSKO-ZAGORSKA
49224	Lepajci	Lepajci	KRAPINSKO-ZAGORSKA
49224	Kraljevec Radobojski	Lepajci	KRAPINSKO-ZAGORSKA
49224	Gornja Pačetina	Lepajci	KRAPINSKO-ZAGORSKA
49224	Galovec Začretski	Lepajci	KRAPINSKO-ZAGORSKA
49224	Donja Šemnica/dio/	Lepajci	KRAPINSKO-ZAGORSKA
49224	Bregi Radobojski	Lepajci	KRAPINSKO-ZAGORSKA
49225	Koprivnica Zagorska	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Lukovčak	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Podbrezovica	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Prigorje	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Putkovec	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Ravninsko	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Jezerišće	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Hromec	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Brezovica Petrovska	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Donji Macelj	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Đurmanec	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Goričanovec	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Gornji Macelj	Đurmanec	KRAPINSKO-ZAGORSKA
49225	Hlevnica	Đurmanec	KRAPINSKO-ZAGORSKA
49228	Zadravec	Brestovec Orehovički	KRAPINSKO-ZAGORSKA
49228	Vojnić Breg	Brestovec Orehovički	KRAPINSKO-ZAGORSKA
49228	Pustodol Orehovički	Brestovec Orehovički	KRAPINSKO-ZAGORSKA
49228	Orehovica	Brestovec Orehovički	KRAPINSKO-ZAGORSKA
49228	Martinec Orehovički	Brestovec Orehovički	KRAPINSKO-ZAGORSKA
49228	Lug Orehovički	Brestovec Orehovički	KRAPINSKO-ZAGORSKA
49228	Grabe	Brestovec Orehovički	KRAPINSKO-ZAGORSKA
49228	Brestovec Orehovički	Brestovec Orehovički	KRAPINSKO-ZAGORSKA
49228	Belovar Zlatarski	Brestovec Orehovički	KRAPINSKO-ZAGORSKA
49231	Mali Tabor	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Orešje Humsko	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Poredje	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Prišlin	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Rusnica	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Strmec Humski	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Vrbišnica	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Zalug	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Lupinjak	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Lastine	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Brezno Gora	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Donje Brezno	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Druškovec Gora	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Druškovec Humski	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Gornje Brezno	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Grletinec	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Hum na Sutli	Hum na Sutli	KRAPINSKO-ZAGORSKA
49231	Klenovec Humski	Hum na Sutli	KRAPINSKO-ZAGORSKA
49232	Strahinje Radobojsko	Radoboj	KRAPINSKO-ZAGORSKA
49232	Radoboj	Radoboj	KRAPINSKO-ZAGORSKA
49232	Orehovec Radobojski	Radoboj	KRAPINSKO-ZAGORSKA
49232	Jazvine	Radoboj	KRAPINSKO-ZAGORSKA
49232	Gornja Šemnica/dio/	Radoboj	KRAPINSKO-ZAGORSKA
49232	Gorjani Sutinski	Radoboj	KRAPINSKO-ZAGORSKA
49233	Lužani Zagorski	Gornje Jesenje	KRAPINSKO-ZAGORSKA
49233	Gornje Jesenje	Gornje Jesenje	KRAPINSKO-ZAGORSKA
49233	Donje Jesenje	Gornje Jesenje	KRAPINSKO-ZAGORSKA
49233	Cerje Jesenjsko	Gornje Jesenje	KRAPINSKO-ZAGORSKA
49233	Brdo Jesenjsko	Gornje Jesenje	KRAPINSKO-ZAGORSKA
49234	Štuparje	Petrovsko	KRAPINSKO-ZAGORSKA
49234	Svedruža	Petrovsko	KRAPINSKO-ZAGORSKA
49234	Stara Ves Petrovska	Petrovsko	KRAPINSKO-ZAGORSKA
49234	Slatina Svedruška	Petrovsko	KRAPINSKO-ZAGORSKA
49234	Rovno	Petrovsko	KRAPINSKO-ZAGORSKA
49234	Preseka Petrovska	Petrovsko	KRAPINSKO-ZAGORSKA
49234	Podgaj Petrovski	Petrovsko	KRAPINSKO-ZAGORSKA
49234	Petrovsko	Petrovsko	KRAPINSKO-ZAGORSKA
49234	Mala Pačetina	Petrovsko	KRAPINSKO-ZAGORSKA
49234	Gredenec	Petrovsko	KRAPINSKO-ZAGORSKA
49234	Benkovec Petrovski	Petrovsko	KRAPINSKO-ZAGORSKA
49240	Pustodol	Donja Stubica	KRAPINSKO-ZAGORSKA
49240	Milekovo Selo	Donja Stubica	KRAPINSKO-ZAGORSKA
49240	Matenci	Donja Stubica	KRAPINSKO-ZAGORSKA
49240	Lepa Ves	Donja Stubica	KRAPINSKO-ZAGORSKA
49240	Hruševec	Donja Stubica	KRAPINSKO-ZAGORSKA
49240	Hižakovec	Donja Stubica	KRAPINSKO-ZAGORSKA
49240	Gornja Podgora	Donja Stubica	KRAPINSKO-ZAGORSKA
49240	Donja Stubica	Donja Stubica	KRAPINSKO-ZAGORSKA
49240	Donja Podgora	Donja Stubica	KRAPINSKO-ZAGORSKA
49243	Stubička Slatina	Oroslavje	KRAPINSKO-ZAGORSKA
49243	Oroslavje	Oroslavje	KRAPINSKO-ZAGORSKA
49243	Mokrice	Oroslavje	KRAPINSKO-ZAGORSKA
49243	Krušljevo Selo	Oroslavje	KRAPINSKO-ZAGORSKA
49243	Andraševec	Oroslavje	KRAPINSKO-ZAGORSKA
49244	Stubičke Toplice	Stubičke Toplice	KRAPINSKO-ZAGORSKA
49244	Strmec Stubički	Stubičke Toplice	KRAPINSKO-ZAGORSKA
49244	Pila	Stubičke Toplice	KRAPINSKO-ZAGORSKA
49245	Pasanska Gorica	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Repićevo Selo	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Samci	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Sekirevo Selo	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Slani Potok	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Sveti Matej	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Šagudovec	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Vinterovec	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Volavec	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Orehova Gorica	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Modrovec	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Banšćica	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Brezje	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Dobri Zdenci	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Dubovec	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Gornja Stubica	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Gusakovec	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Hum Stubički	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Jakšinec	Gornja Stubica	KRAPINSKO-ZAGORSKA
49245	Karivaroš	Gornja Stubica	KRAPINSKO-ZAGORSKA
49246	Selnica	Marija Bistrica	KRAPINSKO-ZAGORSKA
49246	Poljanica Bistrička	Marija Bistrica	KRAPINSKO-ZAGORSKA
49246	Podgorje Bistričko	Marija Bistrica	KRAPINSKO-ZAGORSKA
49246	Marija Bistrica	Marija Bistrica	KRAPINSKO-ZAGORSKA
49246	Laz Stubički	Marija Bistrica	KRAPINSKO-ZAGORSKA
49246	Laz Bistrički	Marija Bistrica	KRAPINSKO-ZAGORSKA
49246	Hum Bistrički	Marija Bistrica	KRAPINSKO-ZAGORSKA
49246	Globočec	Marija Bistrica	KRAPINSKO-ZAGORSKA
49247	Zlatar-Bistrica	Zlatar Bistrica	KRAPINSKO-ZAGORSKA
49247	Veleškovec	Zlatar Bistrica	KRAPINSKO-ZAGORSKA
49247	Tugonica	Zlatar Bistrica	KRAPINSKO-ZAGORSKA
49247	Podgrađe	Zlatar Bistrica	KRAPINSKO-ZAGORSKA
49247	Opasanjek	Zlatar Bistrica	KRAPINSKO-ZAGORSKA
49247	Lovrečan	Zlatar Bistrica	KRAPINSKO-ZAGORSKA
49247	Ervenik Zlatarski	Zlatar Bistrica	KRAPINSKO-ZAGORSKA
49250	Znož/dio/	Zlatar	KRAPINSKO-ZAGORSKA
49250	Zlatar	Zlatar	KRAPINSKO-ZAGORSKA
49250	Ratkovec	Zlatar	KRAPINSKO-ZAGORSKA
49250	Martinšćina	Zlatar	KRAPINSKO-ZAGORSKA
49250	Ladislavec	Zlatar	KRAPINSKO-ZAGORSKA
49250	Donja Batina/dio/	Zlatar	KRAPINSKO-ZAGORSKA
49250	Cetinovec	Zlatar	KRAPINSKO-ZAGORSKA
49250	Borkovec	Zlatar	KRAPINSKO-ZAGORSKA
49251	Vukanci	Mače	KRAPINSKO-ZAGORSKA
49251	Veliki Komor	Mače	KRAPINSKO-ZAGORSKA
49251	Veliki Bukovec	Mače	KRAPINSKO-ZAGORSKA
49251	Sutinske Toplice	Mače	KRAPINSKO-ZAGORSKA
49251	Peršaves	Mače	KRAPINSKO-ZAGORSKA
49251	Mali Komor	Mače	KRAPINSKO-ZAGORSKA
49251	Mali Bukovec	Mače	KRAPINSKO-ZAGORSKA
49251	Mače	Mače	KRAPINSKO-ZAGORSKA
49251	Frkuljevec Peršaveški	Mače	KRAPINSKO-ZAGORSKA
49251	Delkovec	Mače	KRAPINSKO-ZAGORSKA
49252	Veternica/dio/	Mihovljan	KRAPINSKO-ZAGORSKA
49252	Velika Veternička	Mihovljan	KRAPINSKO-ZAGORSKA
49252	Mihovljan	Mihovljan	KRAPINSKO-ZAGORSKA
49252	Kuzminec/dio/	Mihovljan	KRAPINSKO-ZAGORSKA
49252	Kraljevec Šemnički	Mihovljan	KRAPINSKO-ZAGORSKA
49252	Gregurovec	Mihovljan	KRAPINSKO-ZAGORSKA
49252	Gornja Šemnica/dio/	Mihovljan	KRAPINSKO-ZAGORSKA
49252	Frkuljevec Mihovljanski	Mihovljan	KRAPINSKO-ZAGORSKA
49252	Donja Šemnica/dio/	Mihovljan	KRAPINSKO-ZAGORSKA
49253	Završje Loborsko	Lobor	KRAPINSKO-ZAGORSKA
49253	Vojnovec Loborski	Lobor	KRAPINSKO-ZAGORSKA
49253	Vinipotok	Lobor	KRAPINSKO-ZAGORSKA
49253	Velika Petrovagorska	Lobor	KRAPINSKO-ZAGORSKA
49253	Šipki	Lobor	KRAPINSKO-ZAGORSKA
49253	Petrova Gora	Lobor	KRAPINSKO-ZAGORSKA
49253	Markušbrijeg	Lobor	KRAPINSKO-ZAGORSKA
49253	Lobor	Lobor	KRAPINSKO-ZAGORSKA
49253	Cebovec	Lobor	KRAPINSKO-ZAGORSKA
49254	Znož /dio/	Belec	KRAPINSKO-ZAGORSKA
49254	Završje Belečko	Belec	KRAPINSKO-ZAGORSKA
49254	Vižanovec	Belec	KRAPINSKO-ZAGORSKA
49254	Šćrbinec	Belec	KRAPINSKO-ZAGORSKA
49254	Repno	Belec	KRAPINSKO-ZAGORSKA
49254	Petruševec	Belec	KRAPINSKO-ZAGORSKA
49254	Juranšćina	Belec	KRAPINSKO-ZAGORSKA
49254	Gornja Selnica	Belec	KRAPINSKO-ZAGORSKA
49254	Gornja Batina	Belec	KRAPINSKO-ZAGORSKA
49254	Donja Selnica	Belec	KRAPINSKO-ZAGORSKA
49254	Belec	Belec	KRAPINSKO-ZAGORSKA
49255	Veternica/dio/	Novi Golubovec	KRAPINSKO-ZAGORSKA
49255	Stari Golubovec	Novi Golubovec	KRAPINSKO-ZAGORSKA
49255	Očura	Novi Golubovec	KRAPINSKO-ZAGORSKA
49255	Novi Golubovec	Novi Golubovec	KRAPINSKO-ZAGORSKA
49255	Kuzminec/dio/	Novi Golubovec	KRAPINSKO-ZAGORSKA
49255	Gora Veternička	Novi Golubovec	KRAPINSKO-ZAGORSKA
49282	Konjščina	Konjščina	KRAPINSKO-ZAGORSKA
49282	Kosovečko	Konjščina	KRAPINSKO-ZAGORSKA
49282	Krapina Selo	Konjščina	KRAPINSKO-ZAGORSKA
49282	Lipovec	Konjščina	KRAPINSKO-ZAGORSKA
49282	Pešćeno	Konjščina	KRAPINSKO-ZAGORSKA
49282	Sušobreg	Konjščina	KRAPINSKO-ZAGORSKA
49282	Turnišće	Konjščina	KRAPINSKO-ZAGORSKA
49282	Klimen	Konjščina	KRAPINSKO-ZAGORSKA
49282	Jertovec	Konjščina	KRAPINSKO-ZAGORSKA
49282	Jelovec	Konjščina	KRAPINSKO-ZAGORSKA
49282	Bočadir	Konjščina	KRAPINSKO-ZAGORSKA
49282	Bočaki	Konjščina	KRAPINSKO-ZAGORSKA
49282	Brlekovo	Konjščina	KRAPINSKO-ZAGORSKA
49282	Donja Batina/dio/	Konjščina	KRAPINSKO-ZAGORSKA
49282	Donja Konjščina	Konjščina	KRAPINSKO-ZAGORSKA
49282	Galovec	Konjščina	KRAPINSKO-ZAGORSKA
49282	Gornja Konjščina	Konjščina	KRAPINSKO-ZAGORSKA
49283	Vrbovo	Hraščina-Trgovišće	KRAPINSKO-ZAGORSKA
49283	Trgovišće	Hraščina-Trgovišće	KRAPINSKO-ZAGORSKA
49283	Maretić	Hraščina-Trgovišće	KRAPINSKO-ZAGORSKA
49283	Jarek Habekov	Hraščina-Trgovišće	KRAPINSKO-ZAGORSKA
49283	Husinec	Hraščina-Trgovišće	KRAPINSKO-ZAGORSKA
49283	Hrašćina	Hraščina-Trgovišće	KRAPINSKO-ZAGORSKA
49283	Gornji Kraljevec	Hraščina-Trgovišće	KRAPINSKO-ZAGORSKA
49283	Gornjaki	Hraščina-Trgovišće	KRAPINSKO-ZAGORSKA
49283	Donji Kraljevec	Hraščina-Trgovišće	KRAPINSKO-ZAGORSKA
49283	Domovec	Hraščina-Trgovišće	KRAPINSKO-ZAGORSKA
49284	Pokojec	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Pomperovec	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Prepuštovec	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Sveti Križ	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Topličica	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Zajezda	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Pece	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Pažurovec	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Budinščina	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Gornji Kraljevec /dio/	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Gotalovac	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Grtovec	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Krapinica	Budinšćina	KRAPINSKO-ZAGORSKA
49284	Marigutić	Budinšćina	KRAPINSKO-ZAGORSKA
49290	Letovčan Tomaševečki	Klanjec	KRAPINSKO-ZAGORSKA
49290	Lučelnica Tomaševečka	Klanjec	KRAPINSKO-ZAGORSKA
49290	Mihanovićev Dol	Klanjec	KRAPINSKO-ZAGORSKA
49290	Novi Dvori Klanječki	Klanjec	KRAPINSKO-ZAGORSKA
49290	Police	Klanjec	KRAPINSKO-ZAGORSKA
49290	Rakovec Tomaševečki	Klanjec	KRAPINSKO-ZAGORSKA
49290	Tomaševec	Klanjec	KRAPINSKO-ZAGORSKA
49290	Letovčan Novodvorski	Klanjec	KRAPINSKO-ZAGORSKA
49290	Lepoglavec	Klanjec	KRAPINSKO-ZAGORSKA
49290	Ledine Klanječke	Klanjec	KRAPINSKO-ZAGORSKA
49290	Bobovec Tomaševečki	Klanjec	KRAPINSKO-ZAGORSKA
49290	Cesarska Ves	Klanjec	KRAPINSKO-ZAGORSKA
49290	Dol Klanječki	Klanjec	KRAPINSKO-ZAGORSKA
49290	Florijan	Klanjec	KRAPINSKO-ZAGORSKA
49290	Gorkovec	Klanjec	KRAPINSKO-ZAGORSKA
49290	Gredice	Klanjec	KRAPINSKO-ZAGORSKA
49290	Klanjec	Klanjec	KRAPINSKO-ZAGORSKA
49294	Strmec Sutlanski	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Radakovo	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Pušava	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Movrač	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Lukavec Klanječki	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Kraljevec na Sutli	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Kapelski Vrh	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Bratovski Vrh	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Draše	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Goljak Klanječki	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Gornji Čemehovec	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49294	Kačkovec	Kraljevec na Sutli	KRAPINSKO-ZAGORSKA
49295	Velinci	Kumrovec	KRAPINSKO-ZAGORSKA
49295	Risvica	Kumrovec	KRAPINSKO-ZAGORSKA
49295	Razvor	Kumrovec	KRAPINSKO-ZAGORSKA
49295	Razdrto Tuheljsko	Kumrovec	KRAPINSKO-ZAGORSKA
49295	Ravno Brezje	Kumrovec	KRAPINSKO-ZAGORSKA
49295	Podgora	Kumrovec	KRAPINSKO-ZAGORSKA
49295	Kumrovec	Kumrovec	KRAPINSKO-ZAGORSKA
49295	Kladnik	Kumrovec	KRAPINSKO-ZAGORSKA
49295	Dugnjevec	Kumrovec	KRAPINSKO-ZAGORSKA
49295	Donji Škrnik	Kumrovec	KRAPINSKO-ZAGORSKA
49296	Miljana	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Plavić	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Poljana Sultanska	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Pušća	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Zagorska Sela	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Luke Poljanske	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Kuzminec Miljanski	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Ivanić Miljanski	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Bojačno	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Bratkovec	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Brezakovec	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Gornji Škrnik	Zagorska Sela	KRAPINSKO-ZAGORSKA
49296	Harina Žlaka	Zagorska Sela	KRAPINSKO-ZAGORSKA
51000	Rijeka	Rijeka	PRIMORSKO-GORANSKA
51211	Rukavac	Matulji	PRIMORSKO-GORANSKA
51211	Pobri	Matulji	PRIMORSKO-GORANSKA
51211	Mihotići	Matulji	PRIMORSKO-GORANSKA
51211	Matulji	Matulji	PRIMORSKO-GORANSKA
51211	Kučeli	Matulji	PRIMORSKO-GORANSKA
51211	Bregi	Matulji	PRIMORSKO-GORANSKA
51212	Žejane	Vele Mune	PRIMORSKO-GORANSKA
51212	Vele Mune	Vele Mune	PRIMORSKO-GORANSKA
51212	Male Mune	Vele Mune	PRIMORSKO-GORANSKA
51213	Zvoneća	Jurdani	PRIMORSKO-GORANSKA
51213	Zaluki	Jurdani	PRIMORSKO-GORANSKA
51213	Veli Brgud	Jurdani	PRIMORSKO-GORANSKA
51213	Ružići	Jurdani	PRIMORSKO-GORANSKA
51213	Permani	Jurdani	PRIMORSKO-GORANSKA
51213	Mučići	Jurdani	PRIMORSKO-GORANSKA
51213	Mali Brgud	Jurdani	PRIMORSKO-GORANSKA
51213	Jušići	Jurdani	PRIMORSKO-GORANSKA
51213	Jurdani	Jurdani	PRIMORSKO-GORANSKA
51213	Breza	Jurdani	PRIMORSKO-GORANSKA
51213	Brešca	Jurdani	PRIMORSKO-GORANSKA
51214	Šapjane	Šapjane	PRIMORSKO-GORANSKA
51214	Rupa	Šapjane	PRIMORSKO-GORANSKA
51214	Pasjak	Šapjane	PRIMORSKO-GORANSKA
51214	Lipa	Šapjane	PRIMORSKO-GORANSKA
51214	Brdce	Šapjane	PRIMORSKO-GORANSKA
51215	Trinajstići	Kastav	PRIMORSKO-GORANSKA
51215	Spinčići	Kastav	PRIMORSKO-GORANSKA
51215	Rubeši	Kastav	PRIMORSKO-GORANSKA
51215	Kastav	Kastav	PRIMORSKO-GORANSKA
51215	Ćikovići	Kastav	PRIMORSKO-GORANSKA
51215	Brnčići	Kastav	PRIMORSKO-GORANSKA
51216	Viškovo	Viškovo	PRIMORSKO-GORANSKA
51216	Sroki	Viškovo	PRIMORSKO-GORANSKA
51216	Saršoni	Viškovo	PRIMORSKO-GORANSKA
51216	Mladenići	Viškovo	PRIMORSKO-GORANSKA
51216	Marinići	Viškovo	PRIMORSKO-GORANSKA
51216	Marčelji	Viškovo	PRIMORSKO-GORANSKA
51216	Kosi	Viškovo	PRIMORSKO-GORANSKA
51217	Škalnica	Klana	PRIMORSKO-GORANSKA
51217	Studena	Klana	PRIMORSKO-GORANSKA
51217	Lisac	Klana	PRIMORSKO-GORANSKA
51217	Klana	Klana	PRIMORSKO-GORANSKA
51218	Martinovo Selo	Dražice	PRIMORSKO-GORANSKA
51218	Milaši	Dražice	PRIMORSKO-GORANSKA
51218	Podhum	Dražice	PRIMORSKO-GORANSKA
51218	Podkilavac	Dražice	PRIMORSKO-GORANSKA
51218	Ratulje	Dražice	PRIMORSKO-GORANSKA
51218	Trnovica	Dražice	PRIMORSKO-GORANSKA
51218	Zoretići	Dražice	PRIMORSKO-GORANSKA
51218	Lukeži	Dražice	PRIMORSKO-GORANSKA
51218	Lubarska	Dražice	PRIMORSKO-GORANSKA
51218	Baštijani	Dražice	PRIMORSKO-GORANSKA
51218	Brnelići	Dražice	PRIMORSKO-GORANSKA
51218	Drastin	Dražice	PRIMORSKO-GORANSKA
51218	Dražice	Dražice	PRIMORSKO-GORANSKA
51218	Jelenje	Dražice	PRIMORSKO-GORANSKA
51218	Kukuljani	Dražice	PRIMORSKO-GORANSKA
51218	Lopača	Dražice	PRIMORSKO-GORANSKA
51219	Zastenice	Čavle	PRIMORSKO-GORANSKA
51219	Valići	Čavle	PRIMORSKO-GORANSKA
51219	Soboli	Čavle	PRIMORSKO-GORANSKA
51219	Podrvanj	Čavle	PRIMORSKO-GORANSKA
51219	Podčudnič	Čavle	PRIMORSKO-GORANSKA
51219	Mavrinci	Čavle	PRIMORSKO-GORANSKA
51219	Grobnik	Čavle	PRIMORSKO-GORANSKA
51219	Čavle	Čavle	PRIMORSKO-GORANSKA
51219	Cernik	Čavle	PRIMORSKO-GORANSKA
51219	Buzdohanj	Čavle	PRIMORSKO-GORANSKA
51221	Rožići	Kostrena	PRIMORSKO-GORANSKA
51221	Rožmanići	Kostrena	PRIMORSKO-GORANSKA
51221	Šodići	Kostrena	PRIMORSKO-GORANSKA
51221	Šoići	Kostrena	PRIMORSKO-GORANSKA
51221	Urinj	Kostrena	PRIMORSKO-GORANSKA
51221	Vrh Martinšćice	Kostrena	PRIMORSKO-GORANSKA
51221	Žuknica	Kostrena	PRIMORSKO-GORANSKA
51221	Žurkovo	Kostrena	PRIMORSKO-GORANSKA
51221	Randići	Kostrena	PRIMORSKO-GORANSKA
51221	Plešići	Kostrena	PRIMORSKO-GORANSKA
51221	Perovići	Kostrena	PRIMORSKO-GORANSKA
51221	Dorčići	Kostrena	PRIMORSKO-GORANSKA
51221	Dujmići	Kostrena	PRIMORSKO-GORANSKA
51221	Glavani	Kostrena	PRIMORSKO-GORANSKA
51221	Kostrena Sveta Barbara	Kostrena	PRIMORSKO-GORANSKA
51221	Kostrena Sveta Lucija	Kostrena	PRIMORSKO-GORANSKA
51221	Maračići	Kostrena	PRIMORSKO-GORANSKA
51221	Martinšćica	Kostrena	PRIMORSKO-GORANSKA
51221	Paveki	Kostrena	PRIMORSKO-GORANSKA
51222	Bakar-dio	Bakar	PRIMORSKO-GORANSKA
51223	Kukuljanovo	Škrljevo	PRIMORSKO-GORANSKA
51223	Plosna	Škrljevo	PRIMORSKO-GORANSKA
51223	Ponikve	Škrljevo	PRIMORSKO-GORANSKA
51223	Škrljevo	Škrljevo	PRIMORSKO-GORANSKA
51224	Krasica	Krasica	PRIMORSKO-GORANSKA
51225	Praputnjak	Praputnjak	PRIMORSKO-GORANSKA
51226	Hreljin	Hreljin	PRIMORSKO-GORANSKA
51226	Meja Gaj	Hreljin	PRIMORSKO-GORANSKA
51226	Ružić Selo	Hreljin	PRIMORSKO-GORANSKA
51241	Veli Dol	Križišće	PRIMORSKO-GORANSKA
51241	Mali Dol	Križišće	PRIMORSKO-GORANSKA
51241	Križišće	Križišće	PRIMORSKO-GORANSKA
51242	Šimići	Drivenik	PRIMORSKO-GORANSKA
51242	Plišići	Drivenik	PRIMORSKO-GORANSKA
51242	Petrinovići	Drivenik	PRIMORSKO-GORANSKA
51242	Kokanj	Drivenik	PRIMORSKO-GORANSKA
51242	Klarići	Drivenik	PRIMORSKO-GORANSKA
51242	Jerčinovići	Drivenik	PRIMORSKO-GORANSKA
51242	Goričine	Drivenik	PRIMORSKO-GORANSKA
51242	Drivenik	Drivenik	PRIMORSKO-GORANSKA
51242	Čandrli	Drivenik	PRIMORSKO-GORANSKA
51242	Cerovići	Drivenik	PRIMORSKO-GORANSKA
51242	Benkovići	Drivenik	PRIMORSKO-GORANSKA
51242	Benići Drivenički	Drivenik	PRIMORSKO-GORANSKA
51242	Bačići	Drivenik	PRIMORSKO-GORANSKA
51243	Ropci	Tribalj	PRIMORSKO-GORANSKA
51243	Semičevići	Tribalj	PRIMORSKO-GORANSKA
51243	Sušik	Tribalj	PRIMORSKO-GORANSKA
51243	Tribalj	Tribalj	PRIMORSKO-GORANSKA
51243	Tribalj Gornji	Tribalj	PRIMORSKO-GORANSKA
51243	Ričina	Tribalj	PRIMORSKO-GORANSKA
51243	Podsopalj Drivenički	Tribalj	PRIMORSKO-GORANSKA
51243	Podsopalj Belgradski	Tribalj	PRIMORSKO-GORANSKA
51243	Pećca	Tribalj	PRIMORSKO-GORANSKA
51243	Janjevalj	Tribalj	PRIMORSKO-GORANSKA
51243	Blažići	Tribalj	PRIMORSKO-GORANSKA
51243	Belobrajići	Tribalj	PRIMORSKO-GORANSKA
51243	Bašunje Male	Tribalj	PRIMORSKO-GORANSKA
51244	Kamenjak	Grižane	PRIMORSKO-GORANSKA
51244	Kostelj	Grižane	PRIMORSKO-GORANSKA
51244	Marušići	Grižane	PRIMORSKO-GORANSKA
51244	Mavrići	Grižane	PRIMORSKO-GORANSKA
51244	Miroši	Grižane	PRIMORSKO-GORANSKA
51244	Saftići	Grižane	PRIMORSKO-GORANSKA
51244	Šarari	Grižane	PRIMORSKO-GORANSKA
51244	Grižane	Grižane	PRIMORSKO-GORANSKA
51244	Franovići	Grižane	PRIMORSKO-GORANSKA
51244	Antovo	Grižane	PRIMORSKO-GORANSKA
51244	Barci	Grižane	PRIMORSKO-GORANSKA
51244	Baretići	Grižane	PRIMORSKO-GORANSKA
51244	Bašunje Vele	Grižane	PRIMORSKO-GORANSKA
51244	Belgrad	Grižane	PRIMORSKO-GORANSKA
51244	Blaškovići	Grižane	PRIMORSKO-GORANSKA
51244	Dolinci	Grižane	PRIMORSKO-GORANSKA
51250	Novi Vinodolski	Novi Vinodolski	PRIMORSKO-GORANSKA
51250	Povile	Novi Vinodolski	PRIMORSKO-GORANSKA
51251	Ledenice	Ledenice	PRIMORSKO-GORANSKA
51251	Gornji Zagon	Ledenice	PRIMORSKO-GORANSKA
51251	Donji Zagon	Ledenice	PRIMORSKO-GORANSKA
51251	Crno	Ledenice	PRIMORSKO-GORANSKA
51251	Breze	Ledenice	PRIMORSKO-GORANSKA
51251	Bater	Ledenice	PRIMORSKO-GORANSKA
51252	Zabukovac	Klenovica	PRIMORSKO-GORANSKA
51252	Smokvica Krmpotska	Klenovica	PRIMORSKO-GORANSKA
51252	Sibinj Krmpotski	Klenovica	PRIMORSKO-GORANSKA
51252	Ruševo Krmpotsko	Klenovica	PRIMORSKO-GORANSKA
51252	Podmelnik	Klenovica	PRIMORSKO-GORANSKA
51252	Luka Krmpotska	Klenovica	PRIMORSKO-GORANSKA
51252	Krmpotske Vodice	Klenovica	PRIMORSKO-GORANSKA
51252	Klenovica	Klenovica	PRIMORSKO-GORANSKA
51252	Javorje	Klenovica	PRIMORSKO-GORANSKA
51252	Jakov Polje	Klenovica	PRIMORSKO-GORANSKA
51252	Drinak	Klenovica	PRIMORSKO-GORANSKA
51252	Bile	Klenovica	PRIMORSKO-GORANSKA
51253	Podugrinac	Bribir	PRIMORSKO-GORANSKA
51253	Poduljin	Bribir	PRIMORSKO-GORANSKA
51253	Sveti Mikula	Bribir	PRIMORSKO-GORANSKA
51253	Sveti Vid	Bribir	PRIMORSKO-GORANSKA
51253	Štale	Bribir	PRIMORSKO-GORANSKA
51253	Ugrini	Bribir	PRIMORSKO-GORANSKA
51253	Podskoči	Bribir	PRIMORSKO-GORANSKA
51253	Podgori	Bribir	PRIMORSKO-GORANSKA
51253	Kričina	Bribir	PRIMORSKO-GORANSKA
51253	Bribir	Bribir	PRIMORSKO-GORANSKA
51253	Dragaljin	Bribir	PRIMORSKO-GORANSKA
51253	Gradac	Bribir	PRIMORSKO-GORANSKA
51253	Jargovo	Bribir	PRIMORSKO-GORANSKA
51253	Kičeri	Bribir	PRIMORSKO-GORANSKA
51253	Kosavin	Bribir	PRIMORSKO-GORANSKA
51260	Zoričići	Crikvenica	PRIMORSKO-GORANSKA
51260	Šupera	Crikvenica	PRIMORSKO-GORANSKA
51260	Sopaljska	Crikvenica	PRIMORSKO-GORANSKA
51260	Ladvić	Crikvenica	PRIMORSKO-GORANSKA
51260	Kotor	Crikvenica	PRIMORSKO-GORANSKA
51260	Draga Crikvenička	Crikvenica	PRIMORSKO-GORANSKA
51260	Dolac Crikvenički	Crikvenica	PRIMORSKO-GORANSKA
51260	Crikvenica	Crikvenica	PRIMORSKO-GORANSKA
51260	Benići	Crikvenica	PRIMORSKO-GORANSKA
51261	Bakarac	Bakarac	PRIMORSKO-GORANSKA
51262	Kraljevica	Kraljevica	PRIMORSKO-GORANSKA
51263	Šmrika	Šmrika	PRIMORSKO-GORANSKA
51264	Smokovo	Jadranovo	PRIMORSKO-GORANSKA
51264	Kloštar Šiljevički	Jadranovo	PRIMORSKO-GORANSKA
51264	Katun	Jadranovo	PRIMORSKO-GORANSKA
51264	Jadranovo	Jadranovo	PRIMORSKO-GORANSKA
51265	Dramalj	Dramalj	PRIMORSKO-GORANSKA
51266	Selce	Selce	PRIMORSKO-GORANSKA
51280	Supetarska Draga	Rab	PRIMORSKO-GORANSKA
51280	Rab	Rab	PRIMORSKO-GORANSKA
51280	Palit	Rab	PRIMORSKO-GORANSKA
51280	Mundanije	Rab	PRIMORSKO-GORANSKA
51280	Kampor	Rab	PRIMORSKO-GORANSKA
51280	Barbat na Rabu	Rab	PRIMORSKO-GORANSKA
51280	Banjol	Rab	PRIMORSKO-GORANSKA
51281	Lopar	Lopar	PRIMORSKO-GORANSKA
51300	Raskrižje Tihovo	Delnice	PRIMORSKO-GORANSKA
51300	Marija Trošt	Delnice	PRIMORSKO-GORANSKA
51300	Lučice	Delnice	PRIMORSKO-GORANSKA
51300	Gornji Turni	Delnice	PRIMORSKO-GORANSKA
51300	Donji Turni	Delnice	PRIMORSKO-GORANSKA
51300	Delnice	Delnice	PRIMORSKO-GORANSKA
51301	Mala Lešnica	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Radočaj Brodski	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Raskrižje	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Rasohe	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Rogi	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Velika Lešnica	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Vrh Brodski	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Zakrajc Brodski	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Zamost Brodski	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Zapolje Brodsko	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Kupa	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Krivac	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Iševnica	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Belo	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Belski Ravan	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Brod na Kupi	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Buzin	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Čedanj	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Donje Tihovo	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Donji Ložac	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Golik	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Gornje Tihovo	Brod na Kupi	PRIMORSKO-GORANSKA
51301	Gusti Laz	Brod na Kupi	PRIMORSKO-GORANSKA
51302	Sedalce	Kuželj	PRIMORSKO-GORANSKA
51302	Suhor	Kuželj	PRIMORSKO-GORANSKA
51302	Ševalj	Kuželj	PRIMORSKO-GORANSKA
51302	Turke	Kuželj	PRIMORSKO-GORANSKA
51302	Zagolik	Kuželj	PRIMORSKO-GORANSKA
51302	Zakrajc Turkovski	Kuželj	PRIMORSKO-GORANSKA
51302	Požar	Kuželj	PRIMORSKO-GORANSKA
51302	Podgora Turkovska	Kuželj	PRIMORSKO-GORANSKA
51302	Kuželj	Kuželj	PRIMORSKO-GORANSKA
51302	Gašparci	Kuželj	PRIMORSKO-GORANSKA
51302	Gornji Ložac	Kuželj	PRIMORSKO-GORANSKA
51302	Grbajel	Kuželj	PRIMORSKO-GORANSKA
51302	Guće Selo	Kuželj	PRIMORSKO-GORANSKA
51302	Kalić	Kuželj	PRIMORSKO-GORANSKA
51302	Kočičin	Kuželj	PRIMORSKO-GORANSKA
51303	Zamost	Plešce	PRIMORSKO-GORANSKA
51303	Smrekari	Plešce	PRIMORSKO-GORANSKA
51303	Požarnica	Plešce	PRIMORSKO-GORANSKA
51303	Podstene	Plešce	PRIMORSKO-GORANSKA
51303	Plešce	Plešce	PRIMORSKO-GORANSKA
51303	Okrivje	Plešce	PRIMORSKO-GORANSKA
51303	Mandli	Plešce	PRIMORSKO-GORANSKA
51303	Kamenski Hrib	Plešce	PRIMORSKO-GORANSKA
51303	Hrvatsko	Plešce	PRIMORSKO-GORANSKA
51303	Fažonci	Plešce	PRIMORSKO-GORANSKA
51303	Donji Žagari	Plešce	PRIMORSKO-GORANSKA
51304	Vode	Gerovo	PRIMORSKO-GORANSKA
51304	Smrečje	Gerovo	PRIMORSKO-GORANSKA
51304	Mali Lug	Gerovo	PRIMORSKO-GORANSKA
51304	Hrib	Gerovo	PRIMORSKO-GORANSKA
51304	Gerovski Kraj	Gerovo	PRIMORSKO-GORANSKA
51304	Gerovo	Gerovo	PRIMORSKO-GORANSKA
51305	Ravnice	Tršće	PRIMORSKO-GORANSKA
51305	Selo	Tršće	PRIMORSKO-GORANSKA
51305	Sokoli	Tršće	PRIMORSKO-GORANSKA
51305	Srednja Draga	Tršće	PRIMORSKO-GORANSKA
51305	Tršće	Tršće	PRIMORSKO-GORANSKA
51305	Vrhovci	Tršće	PRIMORSKO-GORANSKA
51305	Pršleti	Tršće	PRIMORSKO-GORANSKA
51305	Prhutova Draga	Tršće	PRIMORSKO-GORANSKA
51305	Prhci	Tršće	PRIMORSKO-GORANSKA
51305	Makov Hrib	Tršće	PRIMORSKO-GORANSKA
51305	Lazi	Tršće	PRIMORSKO-GORANSKA
51305	Kraljev Vrh	Tršće	PRIMORSKO-GORANSKA
51305	Ferbežari	Tršće	PRIMORSKO-GORANSKA
51305	Crni Lazi	Tršće	PRIMORSKO-GORANSKA
51305	Brinjeva Draga	Tršće	PRIMORSKO-GORANSKA
51306	Tropeti	Čabar	PRIMORSKO-GORANSKA
51306	Parg	Čabar	PRIMORSKO-GORANSKA
51306	Gornji Žagari	Čabar	PRIMORSKO-GORANSKA
51306	Gorači	Čabar	PRIMORSKO-GORANSKA
51306	Čabar	Čabar	PRIMORSKO-GORANSKA
51307	Zbitke	Prezid	PRIMORSKO-GORANSKA
51307	Prezid	Prezid	PRIMORSKO-GORANSKA
51307	Lautari	Prezid	PRIMORSKO-GORANSKA
51307	Kranjci	Prezid	PRIMORSKO-GORANSKA
51307	Kozji Vrh	Prezid	PRIMORSKO-GORANSKA
51307	Bazli	Prezid	PRIMORSKO-GORANSKA
51311	Planina Skradska	Skrad	PRIMORSKO-GORANSKA
51311	Podslemski Lazi	Skrad	PRIMORSKO-GORANSKA
51311	Podstena	Skrad	PRIMORSKO-GORANSKA
51311	Pucak	Skrad	PRIMORSKO-GORANSKA
51311	Resnatac	Skrad	PRIMORSKO-GORANSKA
51311	Skrad	Skrad	PRIMORSKO-GORANSKA
51311	Sleme Skradsko	Skrad	PRIMORSKO-GORANSKA
51311	Trški Lazi	Skrad	PRIMORSKO-GORANSKA
51311	Tusti Vrh	Skrad	PRIMORSKO-GORANSKA
51311	Veliko Selce	Skrad	PRIMORSKO-GORANSKA
51311	Žrnovac	Skrad	PRIMORSKO-GORANSKA
51311	Pećišće	Skrad	PRIMORSKO-GORANSKA
51311	Malo Selce	Skrad	PRIMORSKO-GORANSKA
51311	Brezje Dobransko	Skrad	PRIMORSKO-GORANSKA
51311	Bukov Vrh	Skrad	PRIMORSKO-GORANSKA
51311	Bukovac Podvrški	Skrad	PRIMORSKO-GORANSKA
51311	Divjake	Skrad	PRIMORSKO-GORANSKA
51311	Gorani	Skrad	PRIMORSKO-GORANSKA
51311	Gorica Skradska	Skrad	PRIMORSKO-GORANSKA
51311	Gornja Dobra	Skrad	PRIMORSKO-GORANSKA
51311	Gramalj	Skrad	PRIMORSKO-GORANSKA
51311	Hosnik	Skrad	PRIMORSKO-GORANSKA
51311	Hribac	Skrad	PRIMORSKO-GORANSKA
51311	Mala Dobra	Skrad	PRIMORSKO-GORANSKA
51312	Podgorani	Brod Moravice	PRIMORSKO-GORANSKA
51312	Planica	Brod Moravice	PRIMORSKO-GORANSKA
51312	Pauci	Brod Moravice	PRIMORSKO-GORANSKA
51312	Novi Lazi	Brod Moravice	PRIMORSKO-GORANSKA
51312	Nove Hiže	Brod Moravice	PRIMORSKO-GORANSKA
51312	Naglići	Brod Moravice	PRIMORSKO-GORANSKA
51312	Moravička Sela	Brod Moravice	PRIMORSKO-GORANSKA
51312	Male Drage	Brod Moravice	PRIMORSKO-GORANSKA
51312	Podstene	Brod Moravice	PRIMORSKO-GORANSKA
51312	Razdrto	Brod Moravice	PRIMORSKO-GORANSKA
51312	Završje	Brod Moravice	PRIMORSKO-GORANSKA
51312	Zavrh	Brod Moravice	PRIMORSKO-GORANSKA
51312	Zahrt	Brod Moravice	PRIMORSKO-GORANSKA
51312	Vele Drage	Brod Moravice	PRIMORSKO-GORANSKA
51312	Šimatovo	Brod Moravice	PRIMORSKO-GORANSKA
51312	Šepci Podstenski	Brod Moravice	PRIMORSKO-GORANSKA
51312	Stari Lazi	Brod Moravice	PRIMORSKO-GORANSKA
51312	Smišljak	Brod Moravice	PRIMORSKO-GORANSKA
51312	Maklen	Brod Moravice	PRIMORSKO-GORANSKA
51312	Lokvica	Brod Moravice	PRIMORSKO-GORANSKA
51312	Donji Šajn	Brod Moravice	PRIMORSKO-GORANSKA
51312	Donja Lamana Draga	Brod Moravice	PRIMORSKO-GORANSKA
51312	Donja Dobra	Brod Moravice	PRIMORSKO-GORANSKA
51312	Doluš	Brod Moravice	PRIMORSKO-GORANSKA
51312	Delači	Brod Moravice	PRIMORSKO-GORANSKA
51312	Čučak	Brod Moravice	PRIMORSKO-GORANSKA
51312	Colnari	Brod Moravice	PRIMORSKO-GORANSKA
51312	Brod Moravice	Brod Moravice	PRIMORSKO-GORANSKA
51312	Donji Šehovac	Brod Moravice	PRIMORSKO-GORANSKA
51312	Goliki	Brod Moravice	PRIMORSKO-GORANSKA
51312	Kocijani	Brod Moravice	PRIMORSKO-GORANSKA
51312	Klepeće Selo	Brod Moravice	PRIMORSKO-GORANSKA
51312	Kavrani	Brod Moravice	PRIMORSKO-GORANSKA
51312	Goršeti	Brod Moravice	PRIMORSKO-GORANSKA
51312	Gornji Šehovac	Brod Moravice	PRIMORSKO-GORANSKA
51312	Gornji Šajn	Brod Moravice	PRIMORSKO-GORANSKA
51312	Gornji Kuti	Brod Moravice	PRIMORSKO-GORANSKA
51312	Gornja Lamana Draga	Brod Moravice	PRIMORSKO-GORANSKA
51313	Zalesina	Kupjak	PRIMORSKO-GORANSKA
51313	Šije	Kupjak	PRIMORSKO-GORANSKA
51313	Leskova Draga	Kupjak	PRIMORSKO-GORANSKA
51313	Kupjak	Kupjak	PRIMORSKO-GORANSKA
51313	Dedin	Kupjak	PRIMORSKO-GORANSKA
51314	Hlevci	Ravna Gora	PRIMORSKO-GORANSKA
51314	Ravna Gora	Ravna Gora	PRIMORSKO-GORANSKA
51314	Stara Sušica	Ravna Gora	PRIMORSKO-GORANSKA
51314	Stari Laz	Ravna Gora	PRIMORSKO-GORANSKA
51315	Tuk Vojni	Mrkopalj	PRIMORSKO-GORANSKA
51315	Tuk Mrkopaljski	Mrkopalj	PRIMORSKO-GORANSKA
51315	Sunger	Mrkopalj	PRIMORSKO-GORANSKA
51315	Mrkopalj	Mrkopalj	PRIMORSKO-GORANSKA
51315	Brestova Draga	Mrkopalj	PRIMORSKO-GORANSKA
51315	Begovo Razdolje	Mrkopalj	PRIMORSKO-GORANSKA
51316	Sopač	Lokve	PRIMORSKO-GORANSKA
51316	Lokve	Lokve	PRIMORSKO-GORANSKA
51316	Lazac Lokvarski	Lokve	PRIMORSKO-GORANSKA
51316	Homer	Lokve	PRIMORSKO-GORANSKA
51317	Plajzi	Crni Lug	PRIMORSKO-GORANSKA
51317	Podtisovac	Crni Lug	PRIMORSKO-GORANSKA
51317	Razloge	Crni Lug	PRIMORSKO-GORANSKA
51317	Razloški Okrug	Crni Lug	PRIMORSKO-GORANSKA
51317	Srednja Krašićevica	Crni Lug	PRIMORSKO-GORANSKA
51317	Vela Voda	Crni Lug	PRIMORSKO-GORANSKA
51317	Zelin Crnoluški	Crni Lug	PRIMORSKO-GORANSKA
51317	Zelin Mrzlovodički	Crni Lug	PRIMORSKO-GORANSKA
51317	Mrzla Vodica	Crni Lug	PRIMORSKO-GORANSKA
51317	Malo Selo	Crni Lug	PRIMORSKO-GORANSKA
51317	Bela Vodica	Crni Lug	PRIMORSKO-GORANSKA
51317	Biljevina	Crni Lug	PRIMORSKO-GORANSKA
51317	Crni Lug	Crni Lug	PRIMORSKO-GORANSKA
51317	Donja Krašićevica	Crni Lug	PRIMORSKO-GORANSKA
51317	Donji Okrug	Crni Lug	PRIMORSKO-GORANSKA
51317	Gornja Krašićevica	Crni Lug	PRIMORSKO-GORANSKA
51317	Gornji Okrug	Crni Lug	PRIMORSKO-GORANSKA
51317	Leska	Crni Lug	PRIMORSKO-GORANSKA
51321	Vrata	Vrata	PRIMORSKO-GORANSKA
51321	Sljeme	Vrata	PRIMORSKO-GORANSKA
51321	Slavica	Vrata	PRIMORSKO-GORANSKA
51321	Belo Selo	Vrata	PRIMORSKO-GORANSKA
51322	Benkovac Fužinski	Fužine	PRIMORSKO-GORANSKA
51322	Fužine	Fužine	PRIMORSKO-GORANSKA
51323	Potkobiljak	Lič	PRIMORSKO-GORANSKA
51323	Pirovište	Lič	PRIMORSKO-GORANSKA
51323	Lič	Lič	PRIMORSKO-GORANSKA
51323	Drivenik-Stanica	Lič	PRIMORSKO-GORANSKA
51323	Banovina	Lič	PRIMORSKO-GORANSKA
51324	Zlobin	Zlobin	PRIMORSKO-GORANSKA
51325	Moravice	Moravice	PRIMORSKO-GORANSKA
51325	Nikšići	Moravice	PRIMORSKO-GORANSKA
51325	Petrovići	Moravice	PRIMORSKO-GORANSKA
51325	Radigojna	Moravice	PRIMORSKO-GORANSKA
51325	Radoševići	Moravice	PRIMORSKO-GORANSKA
51325	Tići	Moravice	PRIMORSKO-GORANSKA
51325	Tomići	Moravice	PRIMORSKO-GORANSKA
51325	Topolovica	Moravice	PRIMORSKO-GORANSKA
51325	Vučinci	Moravice	PRIMORSKO-GORANSKA
51325	Vukelići	Moravice	PRIMORSKO-GORANSKA
51325	Žakule	Moravice	PRIMORSKO-GORANSKA
51325	Mlinari	Moravice	PRIMORSKO-GORANSKA
51325	Međedi	Moravice	PRIMORSKO-GORANSKA
51325	Bunjevci	Moravice	PRIMORSKO-GORANSKA
51325	Carevići	Moravice	PRIMORSKO-GORANSKA
51325	Dokmanovići	Moravice	PRIMORSKO-GORANSKA
51325	Donji Vučkovići	Moravice	PRIMORSKO-GORANSKA
51325	Donji Vukšići	Moravice	PRIMORSKO-GORANSKA
51325	Dragovići	Moravice	PRIMORSKO-GORANSKA
51325	Gornji Vučkovići	Moravice	PRIMORSKO-GORANSKA
51325	Gornji Vukšići	Moravice	PRIMORSKO-GORANSKA
51325	Jakšići	Moravice	PRIMORSKO-GORANSKA
51325	Komlenići	Moravice	PRIMORSKO-GORANSKA
51325	Matići	Moravice	PRIMORSKO-GORANSKA
51326	Stubica	Vrbovsko	PRIMORSKO-GORANSKA
51326	Tuk	Vrbovsko	PRIMORSKO-GORANSKA
51326	Vrbovsko	Vrbovsko	PRIMORSKO-GORANSKA
51326	Vujnovići	Vrbovsko	PRIMORSKO-GORANSKA
51326	Presika	Vrbovsko	PRIMORSKO-GORANSKA
51326	Poljana	Vrbovsko	PRIMORSKO-GORANSKA
51326	Kamensko	Vrbovsko	PRIMORSKO-GORANSKA
51326	Jablan	Vrbovsko	PRIMORSKO-GORANSKA
51326	Hambarište	Vrbovsko	PRIMORSKO-GORANSKA
51326	Hajdine	Vrbovsko	PRIMORSKO-GORANSKA
51327	Musulini	Gomirje	PRIMORSKO-GORANSKA
51327	Majer	Gomirje	PRIMORSKO-GORANSKA
51327	Ljubošina	Gomirje	PRIMORSKO-GORANSKA
51327	Gomirje	Gomirje	PRIMORSKO-GORANSKA
51328	Zaumol	Lukovdol	PRIMORSKO-GORANSKA
51328	Zapeć	Lukovdol	PRIMORSKO-GORANSKA
51328	Vučnik	Lukovdol	PRIMORSKO-GORANSKA
51328	Štefanci	Lukovdol	PRIMORSKO-GORANSKA
51328	Rtić	Lukovdol	PRIMORSKO-GORANSKA
51328	Razdrto II dio	Lukovdol	PRIMORSKO-GORANSKA
51328	Podvučnik	Lukovdol	PRIMORSKO-GORANSKA
51328	Plemenitaš	Lukovdol	PRIMORSKO-GORANSKA
51328	Blaževci	Lukovdol	PRIMORSKO-GORANSKA
51328	Dolenci	Lukovdol	PRIMORSKO-GORANSKA
51328	Gorenci	Lukovdol	PRIMORSKO-GORANSKA
51328	Lesci	Lukovdol	PRIMORSKO-GORANSKA
51328	Lukovdol	Lukovdol	PRIMORSKO-GORANSKA
51328	Nadvučnik	Lukovdol	PRIMORSKO-GORANSKA
51329	Ponikve	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Rim	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Severin na Kupi	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Smišljak	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Veliki Jadrč	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Zdihovo	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Plešivica	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Osojnik	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Damalj	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Draga Lukovdolska	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Klanac	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Liplje	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Mali Jadrč	Severin na Kupi	PRIMORSKO-GORANSKA
51329	Močile	Severin na Kupi	PRIMORSKO-GORANSKA
51410	Opatija	Opatija	PRIMORSKO-GORANSKA
51414	Veprinac	Ičići	PRIMORSKO-GORANSKA
51414	Vela Učka	Ičići	PRIMORSKO-GORANSKA
51414	Poljane	Ičići	PRIMORSKO-GORANSKA
51414	Ika	Ičići	PRIMORSKO-GORANSKA
51414	Ičići	Ičići	PRIMORSKO-GORANSKA
51414	Gornje Selo	Ičići	PRIMORSKO-GORANSKA
51414	Donje Selo	Ičići	PRIMORSKO-GORANSKA
51415	Tuliševica	Lovran	PRIMORSKO-GORANSKA
51415	Oprič	Lovran	PRIMORSKO-GORANSKA
51415	Medveja	Lovran	PRIMORSKO-GORANSKA
51415	Lovranska Draga	Lovran	PRIMORSKO-GORANSKA
51415	Lovran	Lovran	PRIMORSKO-GORANSKA
51415	Liganj	Lovran	PRIMORSKO-GORANSKA
51415	Dobreć	Lovran	PRIMORSKO-GORANSKA
51417	Sveti Petar	Mošćenička Draga	PRIMORSKO-GORANSKA
51417	Sveti Anton	Mošćenička Draga	PRIMORSKO-GORANSKA
51417	Sučići	Mošćenička Draga	PRIMORSKO-GORANSKA
51417	Obrš	Mošćenička Draga	PRIMORSKO-GORANSKA
51417	Mošćenička Draga	Mošćenička Draga	PRIMORSKO-GORANSKA
51417	Mošćenice	Mošćenička Draga	PRIMORSKO-GORANSKA
51417	Kalac	Mošćenička Draga	PRIMORSKO-GORANSKA
51417	Grabrova	Mošćenička Draga	PRIMORSKO-GORANSKA
51417	Donji Kraj	Mošćenička Draga	PRIMORSKO-GORANSKA
51418	Zagore	Brseč	PRIMORSKO-GORANSKA
51418	Sveta Jelena	Brseč	PRIMORSKO-GORANSKA
51418	Martina	Brseč	PRIMORSKO-GORANSKA
51418	Golovik	Brseč	PRIMORSKO-GORANSKA
51418	Brseč	Brseč	PRIMORSKO-GORANSKA
51500	Krk	Krk	PRIMORSKO-GORANSKA
51500	Pinezići	Krk	PRIMORSKO-GORANSKA
51500	Skrbčići	Krk	PRIMORSKO-GORANSKA
51500	Vrh	Krk	PRIMORSKO-GORANSKA
51511	Strilčići	Malinska	PRIMORSKO-GORANSKA
51511	Sršići	Malinska	PRIMORSKO-GORANSKA
51511	Sabljići	Malinska	PRIMORSKO-GORANSKA
51511	Rasopasno	Malinska	PRIMORSKO-GORANSKA
51511	Radići	Malinska	PRIMORSKO-GORANSKA
51511	Porat	Malinska	PRIMORSKO-GORANSKA
51511	Sveti Anton	Malinska	PRIMORSKO-GORANSKA
51511	Sveti Ivan	Malinska	PRIMORSKO-GORANSKA
51511	Sveti Vid Miholjice	Malinska	PRIMORSKO-GORANSKA
51511	Turčić	Malinska	PRIMORSKO-GORANSKA
51511	Vantačići	Malinska	PRIMORSKO-GORANSKA
51511	Zidarići	Malinska	PRIMORSKO-GORANSKA
51511	Žgaljići	Malinska	PRIMORSKO-GORANSKA
51511	Žgombići	Malinska	PRIMORSKO-GORANSKA
51511	Poljica	Malinska	PRIMORSKO-GORANSKA
51511	Oštrobradić	Malinska	PRIMORSKO-GORANSKA
51511	Nenadići	Malinska	PRIMORSKO-GORANSKA
51511	Bajčići	Malinska	PRIMORSKO-GORANSKA
51511	Barušići	Malinska	PRIMORSKO-GORANSKA
51511	Bogovići	Malinska	PRIMORSKO-GORANSKA
51511	Brusići	Malinska	PRIMORSKO-GORANSKA
51511	Brzac	Malinska	PRIMORSKO-GORANSKA
51511	Gabonjin	Malinska	PRIMORSKO-GORANSKA
51511	Kremenići	Malinska	PRIMORSKO-GORANSKA
51511	Linardići	Malinska	PRIMORSKO-GORANSKA
51511	Ljutići	Malinska	PRIMORSKO-GORANSKA
51511	Malinska	Malinska	PRIMORSKO-GORANSKA
51511	Maršići	Malinska	PRIMORSKO-GORANSKA
51511	Milčetići	Malinska	PRIMORSKO-GORANSKA
51511	Milohnići	Malinska	PRIMORSKO-GORANSKA
51511	Milovčići	Malinska	PRIMORSKO-GORANSKA
51512	Njivice	Njivice	PRIMORSKO-GORANSKA
51513	Omišalj	Omišalj	PRIMORSKO-GORANSKA
51514	Tribulje	Dobrinj	PRIMORSKO-GORANSKA
51514	Sveti Vid Dobrinjski	Dobrinj	PRIMORSKO-GORANSKA
51514	Sveti Ivan Dobrinjski	Dobrinj	PRIMORSKO-GORANSKA
51514	Sužan	Dobrinj	PRIMORSKO-GORANSKA
51514	Soline	Dobrinj	PRIMORSKO-GORANSKA
51514	Rudine	Dobrinj	PRIMORSKO-GORANSKA
51514	Kras	Dobrinj	PRIMORSKO-GORANSKA
51514	Klimno	Dobrinj	PRIMORSKO-GORANSKA
51514	Čižići	Dobrinj	PRIMORSKO-GORANSKA
51514	Dobrinj	Dobrinj	PRIMORSKO-GORANSKA
51514	Dolovo	Dobrinj	PRIMORSKO-GORANSKA
51514	Gostinjac	Dobrinj	PRIMORSKO-GORANSKA
51514	Hlapa	Dobrinj	PRIMORSKO-GORANSKA
51514	Klanice	Dobrinj	PRIMORSKO-GORANSKA
51515	Polje	Šilo	PRIMORSKO-GORANSKA
51515	Šilo	Šilo	PRIMORSKO-GORANSKA
51515	Žestilac	Šilo	PRIMORSKO-GORANSKA
51515	Županje	Šilo	PRIMORSKO-GORANSKA
51516	Vrbnik	Vrbnik	PRIMORSKO-GORANSKA
51516	Risika	Vrbnik	PRIMORSKO-GORANSKA
51516	Kampelje	Vrbnik	PRIMORSKO-GORANSKA
51516	Garica	Vrbnik	PRIMORSKO-GORANSKA
51517	Kornić	Kornić	PRIMORSKO-GORANSKA
51517	Lakmartin	Kornić	PRIMORSKO-GORANSKA
51517	Muraj	Kornić	PRIMORSKO-GORANSKA
51521	Punat	Punat	PRIMORSKO-GORANSKA
51521	Stara Baška	Punat	PRIMORSKO-GORANSKA
51522	Draga Bašćanska	Draga Bašćanska	PRIMORSKO-GORANSKA
51523	Jurandvor	Baška	PRIMORSKO-GORANSKA
51523	Batomalj	Baška	PRIMORSKO-GORANSKA
51523	Baška	Baška	PRIMORSKO-GORANSKA
51550	Male Srakane	Mali Lošinj	PRIMORSKO-GORANSKA
51550	Mali Lošinj	Mali Lošinj	PRIMORSKO-GORANSKA
51550	Vele Srakane	Mali Lošinj	PRIMORSKO-GORANSKA
51551	Veli Lošinj	Veli Lošinj	PRIMORSKO-GORANSKA
51552	Ilovik	Ilovik	PRIMORSKO-GORANSKA
51554	Nerezine	Nerezine	PRIMORSKO-GORANSKA
51554	Osor	Nerezine	PRIMORSKO-GORANSKA
51554	Punta Križa	Nerezine	PRIMORSKO-GORANSKA
51554	Sveti Jakov	Nerezine	PRIMORSKO-GORANSKA
51555	Ustrine	Belej	PRIMORSKO-GORANSKA
51555	Štivan	Belej	PRIMORSKO-GORANSKA
51555	Belej	Belej	PRIMORSKO-GORANSKA
51556	Grmov	Martinšćica	PRIMORSKO-GORANSKA
51556	Martinšćica	Martinšćica	PRIMORSKO-GORANSKA
51556	Miholašćica	Martinšćica	PRIMORSKO-GORANSKA
51556	Vidovići	Martinšćica	PRIMORSKO-GORANSKA
51557	Predošćica	Cres	PRIMORSKO-GORANSKA
51557	Stanić	Cres	PRIMORSKO-GORANSKA
51557	Valun	Cres	PRIMORSKO-GORANSKA
51557	Vodice	Cres	PRIMORSKO-GORANSKA
51557	Vrana	Cres	PRIMORSKO-GORANSKA
51557	Zbičina	Cres	PRIMORSKO-GORANSKA
51557	Zbišina	Cres	PRIMORSKO-GORANSKA
51557	Porozina	Cres	PRIMORSKO-GORANSKA
51557	Pernat	Cres	PRIMORSKO-GORANSKA
51557	Orlec	Cres	PRIMORSKO-GORANSKA
51557	Cres	Cres	PRIMORSKO-GORANSKA
51557	Dragozetići	Cres	PRIMORSKO-GORANSKA
51557	Filozići	Cres	PRIMORSKO-GORANSKA
51557	Loznati	Cres	PRIMORSKO-GORANSKA
51557	Lubenice	Cres	PRIMORSKO-GORANSKA
51557	Mali Podol	Cres	PRIMORSKO-GORANSKA
51557	Merag	Cres	PRIMORSKO-GORANSKA
51559	Beli	Beli	PRIMORSKO-GORANSKA
51559	Ivanje	Beli	PRIMORSKO-GORANSKA
51559	Sveti Petar	Beli	PRIMORSKO-GORANSKA
51559	Važminec	Beli	PRIMORSKO-GORANSKA
51561	Susak	Susak	PRIMORSKO-GORANSKA
51562	Unije	Unije	PRIMORSKO-GORANSKA
51564	Ćunski	Ćunski	PRIMORSKO-GORANSKA
52000	Lindar	Pazin	ISTARSKA
52000	Pazin	Pazin	ISTARSKA
52000	Stari Pazin	Pazin	ISTARSKA
52000	Trviž	Pazin	ISTARSKA
52000	Vela Traba	Pazin	ISTARSKA
52000	Zamask	Pazin	ISTARSKA
52000	Zamaski Dol	Pazin	ISTARSKA
52000	Zarečje	Pazin	ISTARSKA
52000	Kršikla	Pazin	ISTARSKA
52000	Kašćerga	Pazin	ISTARSKA
52000	Bazgalji	Pazin	ISTARSKA
52000	Beram	Pazin	ISTARSKA
52000	Bertoši	Pazin	ISTARSKA
52000	Brajkovići	Pazin	ISTARSKA
52000	Butoniga	Pazin	ISTARSKA
52000	Grdoselo	Pazin	ISTARSKA
52000	Heki	Pazin	ISTARSKA
52000	Ježenj	Pazin	ISTARSKA
52100	Valtura	Pula	ISTARSKA
52100	Šišan	Pula	ISTARSKA
52100	Pula	Pula	ISTARSKA
52100	Premantura	Pula	ISTARSKA
52100	Pomer	Pula	ISTARSKA
52100	Jadreški	Pula	ISTARSKA
52100	Banjole	Pula	ISTARSKA
52203	Medulin	Medulin	ISTARSKA
52203	Ližnjan	Medulin	ISTARSKA
52206	Šarići	Marčana	ISTARSKA
52206	Pinežići	Marčana	ISTARSKA
52206	Orbanići	Marčana	ISTARSKA
52206	Muntić	Marčana	ISTARSKA
52206	Marčana	Marčana	ISTARSKA
52206	Loborika	Marčana	ISTARSKA
52206	Filipana	Marčana	ISTARSKA
52206	Divšići	Marčana	ISTARSKA
52207	Petehi	Barban	ISTARSKA
52207	Pačići	Barban	ISTARSKA
52207	Orihi	Barban	ISTARSKA
52207	Melnica	Barban	ISTARSKA
52207	Manjadvorci	Barban	ISTARSKA
52207	Prhati	Barban	ISTARSKA
52207	Puntera	Barban	ISTARSKA
52207	Rajki	Barban	ISTARSKA
52207	Rebići	Barban	ISTARSKA
52207	Rojnići	Barban	ISTARSKA
52207	Šajini	Barban	ISTARSKA
52207	Vadreš	Barban	ISTARSKA
52207	Želiski	Barban	ISTARSKA
52207	Kujići	Barban	ISTARSKA
52207	Kožljani	Barban	ISTARSKA
52207	Balići II	Barban	ISTARSKA
52207	Barban	Barban	ISTARSKA
52207	Belavići	Barban	ISTARSKA
52207	Bičići	Barban	ISTARSKA
52207	Borinići	Barban	ISTARSKA
52207	Bratulići	Barban	ISTARSKA
52207	Draguzeti	Barban	ISTARSKA
52207	Glavani	Barban	ISTARSKA
52207	Koromani	Barban	ISTARSKA
52207	Jurićev Kal	Barban	ISTARSKA
52207	Hreljići	Barban	ISTARSKA
52207	Hrboki	Barban	ISTARSKA
52207	Grandići	Barban	ISTARSKA
52208	Veliki Vareški	Krnica	ISTARSKA
52208	Šegotići	Krnica	ISTARSKA
52208	Rakalj	Krnica	ISTARSKA
52208	Prodol	Krnica	ISTARSKA
52208	Peruški	Krnica	ISTARSKA
52208	Pavićini	Krnica	ISTARSKA
52208	Mutvoran	Krnica	ISTARSKA
52208	Mali Vareški	Krnica	ISTARSKA
52208	Krnica	Krnica	ISTARSKA
52208	Kavran	Krnica	ISTARSKA
52208	Cokuni	Krnica	ISTARSKA
52210	Rovinjsko Selo	Rovinj (Rovigno)	ISTARSKA
52210	Rovinj	Rovinj (Rovigno)	ISTARSKA
52211	Bale	Bale (Valle)	ISTARSKA
52212	Fažana	Fažana	ISTARSKA
52212	Peroj	Fažana	ISTARSKA
52212	Štinjan	Fažana	ISTARSKA
52215	Vodnjan	Vodnjan (Dignano)	ISTARSKA
52215	Gajana	Vodnjan (Dignano)	ISTARSKA
52216	Galižana	Galižana (Gallesano)	ISTARSKA
52220	Rogočana	Labin	ISTARSKA
52220	Ripenda Verbanci	Labin	ISTARSKA
52220	Ripenda Kras	Labin	ISTARSKA
52220	Ripenda Kosi	Labin	ISTARSKA
52220	Ravni	Labin	ISTARSKA
52220	Presika	Labin	ISTARSKA
52220	Markoci	Labin	ISTARSKA
52220	Salakovci	Labin	ISTARSKA
52220	Snašići	Labin	ISTARSKA
52220	Sveta Marina	Labin	ISTARSKA
52220	Sveti Bartul	Labin	ISTARSKA
52220	Štrmac	Labin	ISTARSKA
52220	Topid	Labin	ISTARSKA
52220	Veli Golji	Labin	ISTARSKA
52220	Veli Turini	Labin	ISTARSKA
52220	Vinež	Labin	ISTARSKA
52220	Marići	Labin	ISTARSKA
52220	Marceljani	Labin	ISTARSKA
52220	Barbići	Labin	ISTARSKA
52220	Bartići	Labin	ISTARSKA
52220	Breg	Labin	ISTARSKA
52220	Crni	Labin	ISTARSKA
52220	Drenje	Labin	ISTARSKA
52220	Duga Luka	Labin	ISTARSKA
52220	Frančići	Labin	ISTARSKA
52220	Glušići	Labin	ISTARSKA
52220	Gondolići	Labin	ISTARSKA
52220	Mali Turini	Labin	ISTARSKA
52220	Mali Golji	Labin	ISTARSKA
52220	Letajac	Labin	ISTARSKA
52220	Labin	Labin	ISTARSKA
52220	Kunj	Labin	ISTARSKA
52220	Kranjci	Labin	ISTARSKA
52220	Kapelica	Labin	ISTARSKA
52221	Rabac	Rabac	ISTARSKA
52222	Viškovići	Koromačno	ISTARSKA
52222	Škvaransko	Koromačno	ISTARSKA
52222	Stanišovi	Koromačno	ISTARSKA
52222	Skitača	Koromačno	ISTARSKA
52222	Koromačno	Koromačno	ISTARSKA
52222	Diminići	Koromačno	ISTARSKA
52222	Brovinje	Koromačno	ISTARSKA
52223	Krapan	Raša	ISTARSKA
52223	Most Raša	Raša	ISTARSKA
52223	Raša	Raša	ISTARSKA
52224	Trgetari	Trget	ISTARSKA
52224	Trget	Trget	ISTARSKA
52224	Bršica	Trget	ISTARSKA
52224	Brgod	Trget	ISTARSKA
52231	Županići	Nedešćina	ISTARSKA
52231	Vrećari	Nedešćina	ISTARSKA
52231	Šumber	Nedešćina	ISTARSKA
52231	Sveti Martin	Nedešćina	ISTARSKA
52231	Santalezi	Nedešćina	ISTARSKA
52231	Ržišće	Nedešćina	ISTARSKA
52231	Ružići	Nedešćina	ISTARSKA
52231	Nedešćina	Nedešćina	ISTARSKA
52231	Kraj Drage	Nedešćina	ISTARSKA
52231	Jurazini	Nedešćina	ISTARSKA
52231	Cere	Nedešćina	ISTARSKA
52232	Polje Ćepić	Kršan	ISTARSKA
52232	Purgarija Ćepić	Kršan	ISTARSKA
52232	Veljaki	Kršan	ISTARSKA
52232	Zatka Ćepić	Kršan	ISTARSKA
52232	Lazarići	Kršan	ISTARSKA
52232	Lanišće	Kršan	ISTARSKA
52232	Kršan	Kršan	ISTARSKA
52232	Čambarelići	Kršan	ISTARSKA
52232	Boljevići	Kršan	ISTARSKA
52232	Blaškovići	Kršan	ISTARSKA
52233	Zankovci	Šušnjevica	ISTARSKA
52233	Šušnjevica	Šušnjevica	ISTARSKA
52233	Nova Vas	Šušnjevica	ISTARSKA
52233	Letaj	Šušnjevica	ISTARSKA
52233	Kožljak	Šušnjevica	ISTARSKA
52233	Kostrčani	Šušnjevica	ISTARSKA
52233	Jasenovik	Šušnjevica	ISTARSKA
52233	Grobnik	Šušnjevica	ISTARSKA
52234	Zagorje	Plomin	ISTARSKA
52234	Vozilići	Plomin	ISTARSKA
52234	Stepčići	Plomin	ISTARSKA
52234	Plomin Luka	Plomin	ISTARSKA
52234	Plomin	Plomin	ISTARSKA
52332	Sveta Katarina	Pićan	ISTARSKA
52332	Pićan	Pićan	ISTARSKA
52332	Orić	Pićan	ISTARSKA
52332	Mantovani	Pićan	ISTARSKA
52332	Kukurini	Pićan	ISTARSKA
52332	Jakačići	Pićan	ISTARSKA
52333	Zajci	Podpićan	ISTARSKA
52333	Tupljak	Podpićan	ISTARSKA
52333	Podpićan	Podpićan	ISTARSKA
52333	Krbune	Podpićan	ISTARSKA
52333	Jakomići	Podpićan	ISTARSKA
52341	Prkačini	Žminj	ISTARSKA
52341	Pifari	Žminj	ISTARSKA
52341	Pamići	Žminj	ISTARSKA
52341	Orbanići	Žminj	ISTARSKA
52341	Mužini	Žminj	ISTARSKA
52341	Modrušani	Žminj	ISTARSKA
52341	Milotski Brijeg	Žminj	ISTARSKA
52341	Medančići	Žminj	ISTARSKA
52341	Matijaši	Žminj	ISTARSKA
52341	Pucići	Žminj	ISTARSKA
52341	Rudani	Žminj	ISTARSKA
52341	Žminj	Žminj	ISTARSKA
52341	Žagrići	Žminj	ISTARSKA
52341	Zeci	Žminj	ISTARSKA
52341	Vidulini	Žminj	ISTARSKA
52341	Varož	Žminj	ISTARSKA
52341	Vadediji	Žminj	ISTARSKA
52341	Tomišići	Žminj	ISTARSKA
52341	Šivati	Žminj	ISTARSKA
52341	Sutivanac	Žminj	ISTARSKA
52341	Laginji	Žminj	ISTARSKA
52341	Kršanci	Žminj	ISTARSKA
52341	Domijanići	Žminj	ISTARSKA
52341	Dolica	Žminj	ISTARSKA
52341	Debeljuhi	Žminj	ISTARSKA
52341	Cvitići	Žminj	ISTARSKA
52341	Cere	Žminj	ISTARSKA
52341	Benčići	Žminj	ISTARSKA
52341	Batlug	Žminj	ISTARSKA
52341	Bašići	Žminj	ISTARSKA
52341	Balići	Žminj	ISTARSKA
52341	Gorica	Žminj	ISTARSKA
52341	Gradišće	Žminj	ISTARSKA
52341	Krničari	Žminj	ISTARSKA
52341	Križanci	Žminj	ISTARSKA
52341	Kresini	Žminj	ISTARSKA
52341	Krculi	Žminj	ISTARSKA
52341	Krajcar Brijeg	Žminj	ISTARSKA
52341	Klimni	Žminj	ISTARSKA
52341	Karlovići	Žminj	ISTARSKA
52341	Jurići	Žminj	ISTARSKA
52341	Gržini	Žminj	ISTARSKA
52342	Pusti	Svetvinčenat	ISTARSKA
52342	Peresiji	Svetvinčenat	ISTARSKA
52342	Paradiž	Svetvinčenat	ISTARSKA
52342	Pajkovići	Svetvinčenat	ISTARSKA
52342	Orlići	Svetvinčenat	ISTARSKA
52342	Muškovići	Svetvinčenat	ISTARSKA
52342	Rapanji	Svetvinčenat	ISTARSKA
52342	Režanci	Svetvinčenat	ISTARSKA
52342	Salambati	Svetvinčenat	ISTARSKA
52342	Smoljanci	Svetvinčenat	ISTARSKA
52342	Sveti Kirin	Svetvinčenat	ISTARSKA
52342	Svetvinčenat	Svetvinčenat	ISTARSKA
52342	Škicini	Svetvinčenat	ISTARSKA
52342	Štancija Grgur	Svetvinčenat	ISTARSKA
52342	Štokovci	Svetvinčenat	ISTARSKA
52342	Mandelići	Svetvinčenat	ISTARSKA
52342	Krančići	Svetvinčenat	ISTARSKA
52342	Klarići	Svetvinčenat	ISTARSKA
52342	Bankovići	Svetvinčenat	ISTARSKA
52342	Bibići	Svetvinčenat	ISTARSKA
52342	Bokordići	Svetvinčenat	ISTARSKA
52342	Bonašini	Svetvinčenat	ISTARSKA
52342	Boškari	Svetvinčenat	ISTARSKA
52342	Bričanci	Svetvinčenat	ISTARSKA
52342	Brščići	Svetvinčenat	ISTARSKA
52342	Butkovići	Svetvinčenat	ISTARSKA
52342	Cirka	Svetvinčenat	ISTARSKA
52342	Juršići	Svetvinčenat	ISTARSKA
52342	Gilešići	Svetvinčenat	ISTARSKA
52342	Foli	Svetvinčenat	ISTARSKA
52342	Dokići	Svetvinčenat	ISTARSKA
52342	Čabrunići	Svetvinčenat	ISTARSKA
52342	Cukrići	Svetvinčenat	ISTARSKA
52352	Marići	Kanfanar	ISTARSKA
52352	Maružini	Kanfanar	ISTARSKA
52352	Matohanci	Kanfanar	ISTARSKA
52352	Mrgani	Kanfanar	ISTARSKA
52352	Okreti	Kanfanar	ISTARSKA
52352	Pilkovići	Kanfanar	ISTARSKA
52352	Putini	Kanfanar	ISTARSKA
52352	Sošići	Kanfanar	ISTARSKA
52352	Šorići	Kanfanar	ISTARSKA
52352	Žuntići	Kanfanar	ISTARSKA
52352	Ladići	Kanfanar	ISTARSKA
52352	Kurili	Kanfanar	ISTARSKA
52352	Krmed	Kanfanar	ISTARSKA
52352	Barat	Kanfanar	ISTARSKA
52352	Brajkovići	Kanfanar	ISTARSKA
52352	Bubani	Kanfanar	ISTARSKA
52352	Burići	Kanfanar	ISTARSKA
52352	Červari	Kanfanar	ISTARSKA
52352	Dubravci	Kanfanar	ISTARSKA
52352	Golaš	Kanfanar	ISTARSKA
52352	Jural	Kanfanar	ISTARSKA
52352	Kanfanar	Kanfanar	ISTARSKA
52352	Korenići	Kanfanar	ISTARSKA
52402	Korelići	Cerovlje	ISTARSKA
52402	Krbune	Cerovlje	ISTARSKA
52402	Novaki Pazinski	Cerovlje	ISTARSKA
52402	Oslići	Cerovlje	ISTARSKA
52402	Pagubice	Cerovlje	ISTARSKA
52402	Previž	Cerovlje	ISTARSKA
52402	Grimalda	Cerovlje	ISTARSKA
52402	Gradinje	Cerovlje	ISTARSKA
52402	Gologorički Dol	Cerovlje	ISTARSKA
52402	Gologorica	Cerovlje	ISTARSKA
52402	Duričići	Cerovlje	ISTARSKA
52402	Draguć	Cerovlje	ISTARSKA
52402	Ćusi	Cerovlje	ISTARSKA
52402	Cerovlje	Cerovlje	ISTARSKA
52402	Borut	Cerovlje	ISTARSKA
52403	Škopljak	Gračišće	ISTARSKA
52403	Mandalenčići	Gračišće	ISTARSKA
52403	Gračišće	Gračišće	ISTARSKA
52404	Sveti Petar u šumi	Sveti Petar u šumi	ISTARSKA
52404	Zabrežani	Sveti Petar u šumi	ISTARSKA
52420	Sveti Martin	Buzet	ISTARSKA
52420	Sveti Ivan	Buzet	ISTARSKA
52420	Sveti Donat	Buzet	ISTARSKA
52420	Strana	Buzet	ISTARSKA
52420	Sovinjsko Polje	Buzet	ISTARSKA
52420	Sovinjska Brda	Buzet	ISTARSKA
52420	Sovinjak	Buzet	ISTARSKA
52420	Sirotići	Buzet	ISTARSKA
52420	Senj	Buzet	ISTARSKA
52420	Seljaci	Buzet	ISTARSKA
52420	Selca	Buzet	ISTARSKA
52420	Salež	Buzet	ISTARSKA
52420	Šćulci	Buzet	ISTARSKA
52420	Škuljari	Buzet	ISTARSKA
52420	Štrped	Buzet	ISTARSKA
52420	Vodice	Buzet	ISTARSKA
52420	Trstenik	Buzet	ISTARSKA
52420	Slum	Buzet	ISTARSKA
52420	Kropinjak	Buzet	ISTARSKA
52420	Klenovščak	Buzet	ISTARSKA
52420	Jelovice	Buzet	ISTARSKA
52420	Dane	Buzet	ISTARSKA
52420	Brest	Buzet	ISTARSKA
52420	Žonti	Buzet	ISTARSKA
52420	Vrh	Buzet	ISTARSKA
52420	Veli Mlun	Buzet	ISTARSKA
52420	Ugrini	Buzet	ISTARSKA
52420	Rimnjak	Buzet	ISTARSKA
52420	Račički Brijeg	Buzet	ISTARSKA
52420	Baredine	Buzet	ISTARSKA
52420	Mali Mlun	Buzet	ISTARSKA
52420	Mala Huba	Buzet	ISTARSKA
52420	Krušvari	Buzet	ISTARSKA
52420	Krbavčići	Buzet	ISTARSKA
52420	Kosoriga	Buzet	ISTARSKA
52420	Kajini	Buzet	ISTARSKA
52420	Juričići	Buzet	ISTARSKA
52420	Juradi	Buzet	ISTARSKA
52420	Črnica	Buzet	ISTARSKA
52420	Cunj	Buzet	ISTARSKA
52420	Buzet	Buzet	ISTARSKA
52420	Barušići	Buzet	ISTARSKA
52420	Marčenegla	Buzet	ISTARSKA
52420	Marinci	Buzet	ISTARSKA
52420	Račice	Buzet	ISTARSKA
52420	Prodani	Buzet	ISTARSKA
52420	Pračana	Buzet	ISTARSKA
52420	Podrebar	Buzet	ISTARSKA
52420	Podkuk	Buzet	ISTARSKA
52420	Počekaji	Buzet	ISTARSKA
52420	Perci	Buzet	ISTARSKA
52420	Peničići	Buzet	ISTARSKA
52420	Pengari	Buzet	ISTARSKA
52420	Paladini	Buzet	ISTARSKA
52420	Negnar	Buzet	ISTARSKA
52420	Medveje	Buzet	ISTARSKA
52420	Martinci	Buzet	ISTARSKA
52422	Rašpor	Lanišće	ISTARSKA
52422	Račja Vas	Lanišće	ISTARSKA
52422	Prapoče	Lanišće	ISTARSKA
52422	Podgače	Lanišće	ISTARSKA
52422	Lanišće	Lanišće	ISTARSKA
52422	Brgudac	Lanišće	ISTARSKA
52423	Karojba	Karojba	ISTARSKA
52423	Motovunski Novaki	Karojba	ISTARSKA
52423	Rakotule	Karojba	ISTARSKA
52423	Škropeti	Karojba	ISTARSKA
52424	Sveti Bartol	Motovun	ISTARSKA
52424	Motovun	Motovun	ISTARSKA
52424	Kaldir	Motovun	ISTARSKA
52424	Brkač	Motovun	ISTARSKA
52425	Kras	Roč	ISTARSKA
52425	Krkuž	Roč	ISTARSKA
52425	Rim	Roč	ISTARSKA
52425	Roč	Roč	ISTARSKA
52425	Ročko Polje	Roč	ISTARSKA
52425	Stanica Roč	Roč	ISTARSKA
52425	Sušići	Roč	ISTARSKA
52425	Kotli	Roč	ISTARSKA
52425	Kompanj	Roč	ISTARSKA
52425	Hum	Roč	ISTARSKA
52425	Benčići	Roč	ISTARSKA
52425	Blatna Vas	Roč	ISTARSKA
52425	Brnobići	Roč	ISTARSKA
52425	Čiritež	Roč	ISTARSKA
52425	Erkovčići	Roč	ISTARSKA
52425	Forčići	Roč	ISTARSKA
52425	Gornja Nugla	Roč	ISTARSKA
52426	Semić	Lupoglav	ISTARSKA
52426	Lupoglav	Lupoglav	ISTARSKA
52426	Lesišćina	Lupoglav	ISTARSKA
52426	Dolenja Vas	Lupoglav	ISTARSKA
52426	Brest pod Učkom	Lupoglav	ISTARSKA
52427	Pirelići	Livade	ISTARSKA
52427	Livade	Livade	ISTARSKA
52427	Krti	Livade	ISTARSKA
52427	Ipši	Livade	ISTARSKA
52427	Gradinje	Livade	ISTARSKA
52427	Golubići	Livade	ISTARSKA
52427	Bartolići	Livade	ISTARSKA
52428	Žnjidarići	Oprtalj (Portole)	ISTARSKA
52428	Zrenj	Oprtalj (Portole)	ISTARSKA
52428	Vižintini	Oprtalj (Portole)	ISTARSKA
52428	Šterna	Oprtalj (Portole)	ISTARSKA
52428	Šorgi	Oprtalj (Portole)	ISTARSKA
52428	Sveti Ivan	Oprtalj (Portole)	ISTARSKA
52428	Sveta Lucija	Oprtalj (Portole)	ISTARSKA
52428	Oprtalj	Oprtalj (Portole)	ISTARSKA
52428	Krajići	Oprtalj (Portole)	ISTARSKA
52428	Čepić	Oprtalj (Portole)	ISTARSKA
52428	Bencani	Oprtalj (Portole)	ISTARSKA
52428	Antonci	Oprtalj (Portole)	ISTARSKA
52429	Završje	Grožnjan (Grisignana)	ISTARSKA
52429	Vižintini Vrhi	Grožnjan (Grisignana)	ISTARSKA
52429	Martinčići	Grožnjan (Grisignana)	ISTARSKA
52429	Makovci	Grožnjan (Grisignana)	ISTARSKA
52429	Kostanjica	Grožnjan (Grisignana)	ISTARSKA
52429	Grožnjan	Grožnjan (Grisignana)	ISTARSKA
52429	Bijele Zemlje	Grožnjan (Grisignana)	ISTARSKA
52434	Vranja	Boljun	ISTARSKA
52434	Ravno Brdo	Boljun	ISTARSKA
52434	Paz	Boljun	ISTARSKA
52434	Boljunsko Polje	Boljun	ISTARSKA
52434	Boljun	Boljun	ISTARSKA
52434	Belaj	Boljun	ISTARSKA
52440	Radoši kod Žbandaja	Poreč	ISTARSKA
52440	Radmani	Poreč	ISTARSKA
52440	Poreč	Poreč	ISTARSKA
52440	Mušalež	Poreč	ISTARSKA
52440	Mugeba	Poreč	ISTARSKA
52440	Montižana	Poreč	ISTARSKA
52440	Ružići	Poreč	ISTARSKA
52440	Starići	Poreč	ISTARSKA
52440	Špadići	Poreč	ISTARSKA
52440	Valkarin	Poreč	ISTARSKA
52440	Veleniki	Poreč	ISTARSKA
52440	Veli Maj	Poreč	ISTARSKA
52440	Vranići kod Poreča	Poreč	ISTARSKA
52440	Vrvari	Poreč	ISTARSKA
52440	Žbandaj	Poreč	ISTARSKA
52440	Mihelići	Poreč	ISTARSKA
52440	Mičetići	Poreč	ISTARSKA
52440	Materada Maj	Poreč	ISTARSKA
52440	Antonci	Poreč	ISTARSKA
52440	Buići	Poreč	ISTARSKA
52440	Čuši	Poreč	ISTARSKA
52440	Dračevac	Poreč	ISTARSKA
52440	Filipini	Poreč	ISTARSKA
52440	Fuškulin	Poreč	ISTARSKA
52440	Garbina	Poreč	ISTARSKA
52440	Gulići	Poreč	ISTARSKA
52440	Jasenovica	Poreč	ISTARSKA
52440	Mali Maj	Poreč	ISTARSKA
52440	Ladrovići	Poreč	ISTARSKA
52440	Kosinožići	Poreč	ISTARSKA
52440	Kirmenjak	Poreč	ISTARSKA
52440	Kadumi	Poreč	ISTARSKA
52440	Jehnići	Poreč	ISTARSKA
52444	Žužići	Tinjan	ISTARSKA
52444	Tinjan	Tinjan	ISTARSKA
52444	Radetići	Tinjan	ISTARSKA
52444	Muntrilj	Tinjan	ISTARSKA
52444	Kringa	Tinjan	ISTARSKA
52444	Jakovici	Tinjan	ISTARSKA
52444	Brečevići	Tinjan	ISTARSKA
52444	Brčići	Tinjan	ISTARSKA
52445	Štifanići	Baderna	ISTARSKA
52445	Sinožići	Baderna	ISTARSKA
52445	Rupeni	Baderna	ISTARSKA
52445	Rakovci	Baderna	ISTARSKA
52445	Matulini	Baderna	ISTARSKA
52445	Katun	Baderna	ISTARSKA
52445	Jurići	Baderna	ISTARSKA
52445	Bratovići	Baderna	ISTARSKA
52445	Bonaci	Baderna	ISTARSKA
52445	Banki	Baderna	ISTARSKA
52445	Baderna	Baderna	ISTARSKA
52446	Nova Vas	Nova Vas	ISTARSKA
52446	Rošini	Nova Vas	ISTARSKA
52446	Stanići kod Nove Vasi	Nova Vas	ISTARSKA
52446	Vežnaveri	Nova Vas	ISTARSKA
52446	Mihatovići	Nova Vas	ISTARSKA
52446	Kukci	Nova Vas	ISTARSKA
52446	Gedići	Nova Vas	ISTARSKA
52446	Dekovići	Nova Vas	ISTARSKA
52446	Cancini	Nova Vas	ISTARSKA
52446	Brčići	Nova Vas	ISTARSKA
52446	Blagdanići	Nova Vas	ISTARSKA
52447	Trombal	Vižinada	ISTARSKA
52447	Staniši	Vižinada	ISTARSKA
52447	Piškovica	Vižinada	ISTARSKA
52447	Ohnići	Vižinada	ISTARSKA
52447	Narduči	Vižinada	ISTARSKA
52447	Velići	Vižinada	ISTARSKA
52447	Vižinada	Vižinada	ISTARSKA
52447	Vranići kod Vižinade	Vižinada	ISTARSKA
52447	Vranje Selo	Vižinada	ISTARSKA
52447	Vrbani	Vižinada	ISTARSKA
52447	Vrh Lašići	Vižinada	ISTARSKA
52447	Žudetići	Vižinada	ISTARSKA
52447	Mekiši kod Vižinade	Vižinada	ISTARSKA
52447	Mastelići	Vižinada	ISTARSKA
52447	Markovići	Vižinada	ISTARSKA
52447	Bajkini	Vižinada	ISTARSKA
52447	Baldaši	Vižinada	ISTARSKA
52447	Brig	Vižinada	ISTARSKA
52447	Bukori	Vižinada	ISTARSKA
52447	Crklada	Vižinada	ISTARSKA
52447	Čuki	Vižinada	ISTARSKA
52447	Danci	Vižinada	ISTARSKA
52447	Lašići	Vižinada	ISTARSKA
52447	Jadruhi	Vižinada	ISTARSKA
52447	Grubići	Vižinada	ISTARSKA
52447	Filipi	Vižinada	ISTARSKA
52447	Ferenci	Vižinada	ISTARSKA
52448	Pajari	Sveti Lovreč	ISTARSKA
52448	Perini	Sveti Lovreč	ISTARSKA
52448	Radići	Sveti Lovreč	ISTARSKA
52448	Rajki	Sveti Lovreč	ISTARSKA
52448	Selina	Sveti Lovreč	ISTARSKA
52448	Stranići kod Sv. Lovreča	Sveti Lovreč	ISTARSKA
52448	Sveti Lovreč	Sveti Lovreč	ISTARSKA
52448	Šeraje	Sveti Lovreč	ISTARSKA
52448	Šušnjići	Sveti Lovreč	ISTARSKA
52448	Vošteni	Sveti Lovreč	ISTARSKA
52448	Zgrabljići	Sveti Lovreč	ISTARSKA
52448	Orbani	Sveti Lovreč	ISTARSKA
52448	Medvidići	Sveti Lovreč	ISTARSKA
52448	Medaki	Sveti Lovreč	ISTARSKA
52448	Čehići	Sveti Lovreč	ISTARSKA
52448	Frnjolići	Sveti Lovreč	ISTARSKA
52448	Heraki	Sveti Lovreč	ISTARSKA
52448	Ivići	Sveti Lovreč	ISTARSKA
52448	Jakići I i II	Sveti Lovreč	ISTARSKA
52448	Jurcani	Sveti Lovreč	ISTARSKA
52448	Kapovići	Sveti Lovreč	ISTARSKA
52448	Knapići	Sveti Lovreč	ISTARSKA
52448	Kršuli	Sveti Lovreč	ISTARSKA
52448	Krunčići	Sveti Lovreč	ISTARSKA
52448	Lakovići	Sveti Lovreč	ISTARSKA
52449	Červar Porat	Červar Porat	ISTARSKA
52449	Črvar	Červar Porat	ISTARSKA
52449	Bašarinka	Červar Porat	ISTARSKA
52450	Vrsar	Vrsar	ISTARSKA
52450	Marasi	Vrsar	ISTARSKA
52450	Kontešići	Vrsar	ISTARSKA
52450	Kloštar	Vrsar	ISTARSKA
52450	Gradina	Vrsar	ISTARSKA
52450	Flengi	Vrsar	ISTARSKA
52450	Delići	Vrsar	ISTARSKA
52450	Bralići	Vrsar	ISTARSKA
52450	Begi	Vrsar	ISTARSKA
52452	Funtana	Funtana	ISTARSKA
52460	Lozari	Buje (Buie)	ISTARSKA
52460	Plovanija	Buje (Buie)	ISTARSKA
52460	Sveta Marija na Krasu	Buje (Buie)	ISTARSKA
52460	Škrile	Buje (Buie)	ISTARSKA
52460	Škudelin	Buje (Buie)	ISTARSKA
52460	Triban	Buje (Buie)	ISTARSKA
52460	Veli Mlin	Buje (Buie)	ISTARSKA
52460	Krasica	Buje (Buie)	ISTARSKA
52460	Kaštel	Buje (Buie)	ISTARSKA
52460	Baredine	Buje (Buie)	ISTARSKA
52460	Bibali	Buje (Buie)	ISTARSKA
52460	Buje	Buje (Buie)	ISTARSKA
52460	Bužin	Buje (Buie)	ISTARSKA
52460	Gamboci	Buje (Buie)	ISTARSKA
52460	Kaldanija	Buje (Buie)	ISTARSKA
52460	Kanegra	Buje (Buie)	ISTARSKA
52462	Vrnjak	Momjan (Momiano)	ISTARSKA
52462	Oskoruš	Momjan (Momiano)	ISTARSKA
52462	Momjan	Momjan (Momiano)	ISTARSKA
52462	Merišće	Momjan (Momiano)	ISTARSKA
52462	Marušići	Momjan (Momiano)	ISTARSKA
52462	Kućibreg	Momjan (Momiano)	ISTARSKA
52462	Kuberton	Momjan (Momiano)	ISTARSKA
52462	Brič	Momjan (Momiano)	ISTARSKA
52462	Brdo	Momjan (Momiano)	ISTARSKA
52463	Anžići	Višnjan	ISTARSKA
52463	Bačva	Višnjan	ISTARSKA
52463	Barat	Višnjan	ISTARSKA
52463	Barići	Višnjan	ISTARSKA
52463	Žužići	Višnjan	ISTARSKA
52463	Srebrnići	Višnjan	ISTARSKA
52463	Smolići	Višnjan	ISTARSKA
52463	Rapavel	Višnjan	ISTARSKA
52463	Rafaeli	Višnjan	ISTARSKA
52463	Radovani	Višnjan	ISTARSKA
52463	Radoši kod Višnjana	Višnjan	ISTARSKA
52463	Pršurići	Višnjan	ISTARSKA
52463	Prhati	Višnjan	ISTARSKA
52463	Strpančići	Višnjan	ISTARSKA
52463	Sveti Ivan	Višnjan	ISTARSKA
52463	Žikovići	Višnjan	ISTARSKA
52463	Ženodraga	Višnjan	ISTARSKA
52463	Zoričići	Višnjan	ISTARSKA
52463	Vrhjani	Višnjan	ISTARSKA
52463	Vranići kod Višnjana	Višnjan	ISTARSKA
52463	Višnjan	Višnjan	ISTARSKA
52463	Vejaki	Višnjan	ISTARSKA
52463	Štuti	Višnjan	ISTARSKA
52463	Prašćari	Višnjan	ISTARSKA
52463	Milanezi	Višnjan	ISTARSKA
52463	Markovac	Višnjan	ISTARSKA
52463	Deklevi	Višnjan	ISTARSKA
52463	Cvitani	Višnjan	ISTARSKA
52463	Cerion	Višnjan	ISTARSKA
52463	Bujarići	Višnjan	ISTARSKA
52463	Bucalovići	Višnjan	ISTARSKA
52463	Broskvari	Višnjan	ISTARSKA
52463	Benčani	Višnjan	ISTARSKA
52463	Baškoti	Višnjan	ISTARSKA
52463	Diklići	Višnjan	ISTARSKA
52463	Fabci	Višnjan	ISTARSKA
52463	Farini	Višnjan	ISTARSKA
52463	Majkusi	Višnjan	ISTARSKA
52463	Legovići	Višnjan	ISTARSKA
52463	Kurjavići	Višnjan	ISTARSKA
52463	Košutići	Višnjan	ISTARSKA
52463	Korlevići	Višnjan	ISTARSKA
52463	Kolumbera	Višnjan	ISTARSKA
52463	Kočići	Višnjan	ISTARSKA
52463	Gambetići	Višnjan	ISTARSKA
52464	Labinci	Kaštelir	ISTARSKA
52464	Mekiši kod Kaštelira	Kaštelir	ISTARSKA
52464	Rojci	Kaštelir	ISTARSKA
52464	Roškići	Kaštelir	ISTARSKA
52464	Tadini	Kaštelir	ISTARSKA
52464	Valentići	Kaštelir	ISTARSKA
52464	Krančići	Kaštelir	ISTARSKA
52464	Kovači	Kaštelir	ISTARSKA
52464	Kaštelir	Kaštelir	ISTARSKA
52464	Dvori	Kaštelir	ISTARSKA
52464	Deklići	Kaštelir	ISTARSKA
52464	Cerjani	Kaštelir	ISTARSKA
52464	Brnobići	Kaštelir	ISTARSKA
52464	Babići	Kaštelir	ISTARSKA
52465	Vabriga	Tar	ISTARSKA
52465	Tar	Tar	ISTARSKA
52465	Rogovići	Tar	ISTARSKA
52465	Perci	Tar	ISTARSKA
52465	Frata	Tar	ISTARSKA
52466	Novigrad	Novigrad (Cittanova)	ISTARSKA
52466	Mareda	Novigrad (Cittanova)	ISTARSKA
52466	Dajla	Novigrad (Cittanova)	ISTARSKA
52466	Bužinija	Novigrad (Cittanova)	ISTARSKA
52466	Antenal	Novigrad (Cittanova)	ISTARSKA
52470	Murine	Umag (Umago)	ISTARSKA
52470	Petrovija	Umag (Umago)	ISTARSKA
52470	Seget	Umag (Umago)	ISTARSKA
52470	Sv. Marija na Krasu	Umag (Umago)	ISTARSKA
52470	Umag	Umag (Umago)	ISTARSKA
52470	Valica	Umag (Umago)	ISTARSKA
52470	Vardica	Umag (Umago)	ISTARSKA
52470	Vilanija	Umag (Umago)	ISTARSKA
52470	Monterol	Umag (Umago)	ISTARSKA
52470	Materada	Umag (Umago)	ISTARSKA
52470	Lovrečica	Umag (Umago)	ISTARSKA
52470	Babići	Umag (Umago)	ISTARSKA
52470	Čepljani	Umag (Umago)	ISTARSKA
52470	Đuba	Umag (Umago)	ISTARSKA
52470	Finida	Umag (Umago)	ISTARSKA
52470	Juricani	Umag (Umago)	ISTARSKA
52470	Katoro	Umag (Umago)	ISTARSKA
52470	Kmeti	Umag (Umago)	ISTARSKA
52470	Križine	Umag (Umago)	ISTARSKA
52474	Radini	Brtonigla (Verteneglio)	ISTARSKA
52474	Nova Vas	Brtonigla (Verteneglio)	ISTARSKA
52474	Kršete	Brtonigla (Verteneglio)	ISTARSKA
52474	Karigador	Brtonigla (Verteneglio)	ISTARSKA
52474	Fiorini	Brtonigla (Verteneglio)	ISTARSKA
52474	Buroli	Brtonigla (Verteneglio)	ISTARSKA
52474	Brtonigla	Brtonigla (Verteneglio)	ISTARSKA
52475	Zambratija	Savudrija (Salvore)	ISTARSKA
52475	Savudrija	Savudrija (Salvore)	ISTARSKA
52475	Crveni Vrh	Savudrija (Salvore)	ISTARSKA
52475	Bašanija	Savudrija (Salvore)	ISTARSKA
53000	Lički Ribnik	Gospić	LIČKO-SENJSKA
53000	Novoselo Bilajsko	Gospić	LIČKO-SENJSKA
53000	Novoselo Trnovačko	Gospić	LIČKO-SENJSKA
53000	Ornice	Gospić	LIČKO-SENJSKA
53000	Podoštra	Gospić	LIČKO-SENJSKA
53000	Trnovac	Gospić	LIČKO-SENJSKA
53000	Žabica	Gospić	LIČKO-SENJSKA
53000	Lički Novi	Gospić	LIČKO-SENJSKA
53000	Lički Čitluk	Gospić	LIČKO-SENJSKA
53000	Barlete	Gospić	LIČKO-SENJSKA
53000	Bilaj	Gospić	LIČKO-SENJSKA
53000	Debelo Brdo I	Gospić	LIČKO-SENJSKA
53000	Debelo Brdo II	Gospić	LIČKO-SENJSKA
53000	Divoselo	Gospić	LIČKO-SENJSKA
53000	Gospić	Gospić	LIČKO-SENJSKA
53000	Kaniža Gospićka	Gospić	LIČKO-SENJSKA
53201	Široka Kula	Lički Osik	LIČKO-SENJSKA
53201	Ostrvica	Lički Osik	LIČKO-SENJSKA
53201	Mušaluk	Lički Osik	LIČKO-SENJSKA
53201	Lički Osik	Lički Osik	LIČKO-SENJSKA
53201	Budak	Lički Osik	LIČKO-SENJSKA
53202	Sveti Marko	Perušić	LIČKO-SENJSKA
53202	Studenci	Perušić	LIČKO-SENJSKA
53202	Prvan Selo	Perušić	LIČKO-SENJSKA
53202	Perušić	Perušić	LIČKO-SENJSKA
53202	Mezinovac	Perušić	LIČKO-SENJSKA
53202	Malo Polje	Perušić	LIČKO-SENJSKA
53202	Kvarte	Perušić	LIČKO-SENJSKA
53202	Bukovac Perušićki	Perušić	LIČKO-SENJSKA
53202	Kaluđerovac	Perušić	LIČKO-SENJSKA
53202	Klenovac	Perušić	LIČKO-SENJSKA
53202	Konjsko Brdo	Perušić	LIČKO-SENJSKA
53202	Kosa Janjačka	Perušić	LIČKO-SENJSKA
53203	Vukelići	Kosinj	LIČKO-SENJSKA
53203	Rudinka	Kosinj	LIČKO-SENJSKA
53203	Mlakva	Kosinj	LIČKO-SENJSKA
53203	Lipovo Polje	Kosinj	LIČKO-SENJSKA
53203	Kruščica	Kosinj	LIČKO-SENJSKA
53203	Krš	Kosinj	LIČKO-SENJSKA
53203	Kosinjski Bakovac	Kosinj	LIČKO-SENJSKA
53203	Gornji Kosinj	Kosinj	LIČKO-SENJSKA
53203	Donji Kosinj	Kosinj	LIČKO-SENJSKA
53205	Zavođe	Medak	LIČKO-SENJSKA
53205	Vrebac	Medak	LIČKO-SENJSKA
53205	Počitelj	Medak	LIČKO-SENJSKA
53205	Pavlovac Vrebački	Medak	LIČKO-SENJSKA
53205	Mogorić	Medak	LIČKO-SENJSKA
53205	Medak	Medak	LIČKO-SENJSKA
53205	Kukljić	Medak	LIČKO-SENJSKA
53205	Kruškovac	Medak	LIČKO-SENJSKA
53205	Drenovac Radučki	Medak	LIČKO-SENJSKA
53205	Breznik	Medak	LIČKO-SENJSKA
53206	Rizvanuša	Brušane	LIČKO-SENJSKA
53206	Ravni Dabar	Brušane	LIČKO-SENJSKA
53206	Došen Dabar	Brušane	LIČKO-SENJSKA
53206	Crni Dabar	Brušane	LIČKO-SENJSKA
53206	Brušane	Brušane	LIČKO-SENJSKA
53206	Baške Oštarije	Brušane	LIČKO-SENJSKA
53211	Smiljansko Polje	Smiljan	LIČKO-SENJSKA
53211	Smiljan	Smiljan	LIČKO-SENJSKA
53211	Rastoka	Smiljan	LIČKO-SENJSKA
53211	Bužim	Smiljan	LIČKO-SENJSKA
53212	Vranovine	Klanac	LIČKO-SENJSKA
53212	Veliki Žitnik	Klanac	LIČKO-SENJSKA
53212	Vaganac	Klanac	LIČKO-SENJSKA
53212	Oteš	Klanac	LIČKO-SENJSKA
53212	Klanac	Klanac	LIČKO-SENJSKA
53212	Aleksinica	Klanac	LIČKO-SENJSKA
53213	Velika Plana	Donje Pazarište	LIČKO-SENJSKA
53213	Popovača Pazariška	Donje Pazarište	LIČKO-SENJSKA
53213	Podstrana	Donje Pazarište	LIČKO-SENJSKA
53213	Novoselija	Donje Pazarište	LIČKO-SENJSKA
53213	Mala Plana	Donje Pazarište	LIČKO-SENJSKA
53213	Kalinovača	Donje Pazarište	LIČKO-SENJSKA
53213	Donje Pazarište	Donje Pazarište	LIČKO-SENJSKA
53220	Otočac	Otočac	LIČKO-SENJSKA
53220	Prozor	Otočac	LIČKO-SENJSKA
53220	Staro Selo	Otočac	LIČKO-SENJSKA
53221	Škare	Škare	LIČKO-SENJSKA
53221	Podum	Škare	LIČKO-SENJSKA
53221	Glavace	Škare	LIČKO-SENJSKA
53221	Doljani	Škare	LIČKO-SENJSKA
53222	Dabar	Dabar	LIČKO-SENJSKA
53223	Zalužnica	Vrhovine	LIČKO-SENJSKA
53223	Vrhovine	Vrhovine	LIČKO-SENJSKA
53223	Turjanski	Vrhovine	LIČKO-SENJSKA
53223	Rudopolje	Vrhovine	LIČKO-SENJSKA
53223	Gornji Babin Potok	Vrhovine	LIČKO-SENJSKA
53223	Gornje Vrhovine	Vrhovine	LIČKO-SENJSKA
53223	Donji Babin Potok	Vrhovine	LIČKO-SENJSKA
53224	Čovići	Ličko Lešće	LIČKO-SENJSKA
53224	Ličko Lešće	Ličko Lešće	LIČKO-SENJSKA
53224	Ramljani	Ličko Lešće	LIČKO-SENJSKA
53224	Sinac	Ličko Lešće	LIČKO-SENJSKA
53225	Švica	Švica	LIČKO-SENJSKA
53225	Ponori	Švica	LIČKO-SENJSKA
53225	Lipovlje	Švica	LIČKO-SENJSKA
53225	Kuterevo	Švica	LIČKO-SENJSKA
53225	Gorići	Švica	LIČKO-SENJSKA
53226	Kompolje	Kompolje	LIČKO-SENJSKA
53226	Hrvatsko Polje	Kompolje	LIČKO-SENJSKA
53226	Drenov Klanac	Kompolje	LIČKO-SENJSKA
53226	Brloška Dubrava	Kompolje	LIČKO-SENJSKA
53226	Brlog	Kompolje	LIČKO-SENJSKA
53230	Novo Selo Koreničko	Korenica	LIČKO-SENJSKA
53230	Oravac	Korenica	LIČKO-SENJSKA
53230	Ponor Korenički	Korenica	LIČKO-SENJSKA
53230	Rudanovac	Korenica	LIČKO-SENJSKA
53230	Šeganovac	Korenica	LIČKO-SENJSKA
53230	Trnavac	Korenica	LIČKO-SENJSKA
53230	Tuk Bjelopoljski	Korenica	LIČKO-SENJSKA
53230	Vedašići	Korenica	LIČKO-SENJSKA
53230	Vranovača	Korenica	LIČKO-SENJSKA
53230	Vrelo Koreničko	Korenica	LIČKO-SENJSKA
53230	Vrpile	Korenica	LIČKO-SENJSKA
53230	Mihaljevac	Korenica	LIČKO-SENJSKA
53230	Korenica	Korenica	LIČKO-SENJSKA
53230	Bjelopolje	Korenica	LIČKO-SENJSKA
53230	Drakulić Rijeka	Korenica	LIČKO-SENJSKA
53230	Frkašić	Korenica	LIČKO-SENJSKA
53230	Grabušić	Korenica	LIČKO-SENJSKA
53230	Gradina Korenička	Korenica	LIČKO-SENJSKA
53230	Homoljac	Korenica	LIČKO-SENJSKA
53230	Jasikovac	Korenica	LIČKO-SENJSKA
53230	Kalebovac	Korenica	LIČKO-SENJSKA
53230	Kapela Korenička	Korenica	LIČKO-SENJSKA
53230	Klašnjica	Korenica	LIČKO-SENJSKA
53230	Kompolje Koreničko	Korenica	LIČKO-SENJSKA
53231	Poljanak	Plitvička Jezera	LIČKO-SENJSKA
53231	Prijeboj	Plitvička Jezera	LIČKO-SENJSKA
53231	Rastovača	Plitvička Jezera	LIČKO-SENJSKA
53231	Sertić Poljana	Plitvička Jezera	LIČKO-SENJSKA
53231	Smoljanac	Plitvička Jezera	LIČKO-SENJSKA
53231	Plitvički Ljeskovac	Plitvička Jezera	LIČKO-SENJSKA
53231	Plitvička Jezera	Plitvička Jezera	LIČKO-SENJSKA
53231	Plitvica Selo	Plitvička Jezera	LIČKO-SENJSKA
53231	Korana	Plitvička Jezera	LIČKO-SENJSKA
53231	Končarev Kraj	Plitvička Jezera	LIČKO-SENJSKA
53231	Jezerce	Plitvička Jezera	LIČKO-SENJSKA
53231	Čujića Krčevina	Plitvička Jezera	LIČKO-SENJSKA
53233	Željava	Ličko Petrovo Selo	LIČKO-SENJSKA
53233	Zaklopača	Ličko Petrovo Selo	LIČKO-SENJSKA
53233	Rešetar	Ličko Petrovo Selo	LIČKO-SENJSKA
53233	Ličko Petrovo Selo	Ličko Petrovo Selo	LIČKO-SENJSKA
53233	Gornji Vaganac	Ličko Petrovo Selo	LIČKO-SENJSKA
53233	Donji Vaganac	Ličko Petrovo Selo	LIČKO-SENJSKA
53234	Visuć	Udbina	LIČKO-SENJSKA
53234	Udbina	Udbina	LIČKO-SENJSKA
53234	Rebić	Udbina	LIČKO-SENJSKA
53234	Poljice	Udbina	LIČKO-SENJSKA
53234	Ondić	Udbina	LIČKO-SENJSKA
53234	Mutilić	Udbina	LIČKO-SENJSKA
53234	Kurjak	Udbina	LIČKO-SENJSKA
53234	Komić	Udbina	LIČKO-SENJSKA
53234	Jošan	Udbina	LIČKO-SENJSKA
53234	Čojluk	Udbina	LIČKO-SENJSKA
53234	Breštane	Udbina	LIČKO-SENJSKA
53235	Šalamunić	Bunić	LIČKO-SENJSKA
53235	Pećane	Bunić	LIČKO-SENJSKA
53235	Krbavica	Bunić	LIČKO-SENJSKA
53235	Kozjan	Bunić	LIČKO-SENJSKA
53235	Debelo Brdo	Bunić	LIČKO-SENJSKA
53235	Čanak	Bunić	LIČKO-SENJSKA
53235	Bunić	Bunić	LIČKO-SENJSKA
53236	Tolić	Podlapača	LIČKO-SENJSKA
53236	Svračkovo Selo	Podlapača	LIČKO-SENJSKA
53236	Podlapača	Podlapača	LIČKO-SENJSKA
53236	Krbava	Podlapača	LIČKO-SENJSKA
53236	Jagodnje	Podlapača	LIČKO-SENJSKA
53236	Donji Mekinjar	Podlapača	LIČKO-SENJSKA
53244	Vranik	Lovinac	LIČKO-SENJSKA
53244	Štikada	Lovinac	LIČKO-SENJSKA
53244	Sveti Rok	Lovinac	LIČKO-SENJSKA
53244	Smokrić	Lovinac	LIČKO-SENJSKA
53244	Ričice	Lovinac	LIČKO-SENJSKA
53244	Raduč	Lovinac	LIČKO-SENJSKA
53244	Lovinac	Lovinac	LIČKO-SENJSKA
53244	Ličko Cerje	Lovinac	LIČKO-SENJSKA
53244	Kik	Lovinac	LIČKO-SENJSKA
53244	Gornja Ploča	Lovinac	LIČKO-SENJSKA
53250	Oraovac	Donji Lapac	LIČKO-SENJSKA
53250	Mišljenovac	Donji Lapac	LIČKO-SENJSKA
53250	Gornji Lapac	Donji Lapac	LIČKO-SENJSKA
53250	Gajine	Donji Lapac	LIČKO-SENJSKA
53250	Donji Lapac	Donji Lapac	LIČKO-SENJSKA
53250	Dnopolje	Donji Lapac	LIČKO-SENJSKA
53250	Bušević	Donji Lapac	LIČKO-SENJSKA
53250	Borićevac	Donji Lapac	LIČKO-SENJSKA
53250	Birovača	Donji Lapac	LIČKO-SENJSKA
53251	Nebljusi	Nebljusi	LIČKO-SENJSKA
53251	Melinovac	Nebljusi	LIČKO-SENJSKA
53251	Kruge	Nebljusi	LIČKO-SENJSKA
53251	Kestenovac	Nebljusi	LIČKO-SENJSKA
53251	Gornji Štrbci	Nebljusi	LIČKO-SENJSKA
53251	Donji Štrbci	Nebljusi	LIČKO-SENJSKA
53252	Brezovac Dobroselski	Doljani	LIČKO-SENJSKA
53252	Dobroselo	Doljani	LIČKO-SENJSKA
53252	Doljani	Doljani	LIČKO-SENJSKA
53260	Žuta Lokva	Brinje	LIČKO-SENJSKA
53260	Vodoteč	Brinje	LIČKO-SENJSKA
53260	Rapain Klanac	Brinje	LIČKO-SENJSKA
53260	Prokike	Brinje	LIČKO-SENJSKA
53260	Letinac	Brinje	LIČKO-SENJSKA
53260	Brinje	Brinje	LIČKO-SENJSKA
53261	Lipice	Križpolje	LIČKO-SENJSKA
53261	Križpolje	Križpolje	LIČKO-SENJSKA
53261	Križ Kamenica	Križpolje	LIČKO-SENJSKA
53261	Glibodol	Križpolje	LIČKO-SENJSKA
53262	Jezerane	Jezerane	LIČKO-SENJSKA
53262	Stajnica	Jezerane	LIČKO-SENJSKA
53270	Stolac	Senj	LIČKO-SENJSKA
53270	Senjska Draga	Senj	LIČKO-SENJSKA
53270	Senj	Senj	LIČKO-SENJSKA
53271	Alan	Krivi Put	LIČKO-SENJSKA
53271	Krivi Put	Krivi Put	LIČKO-SENJSKA
53271	Mrzli Dol	Krivi Put	LIČKO-SENJSKA
53271	Podbilo	Krivi Put	LIČKO-SENJSKA
53271	Veljun Primorski	Krivi Put	LIČKO-SENJSKA
53271	Vrataruša	Krivi Put	LIČKO-SENJSKA
53273	Vrzići	Vratnik	LIČKO-SENJSKA
53273	Vratnik	Vratnik	LIČKO-SENJSKA
53273	Melnice	Vratnik	LIČKO-SENJSKA
53273	Crni Kal	Vratnik	LIČKO-SENJSKA
53274	Krasno	Krasno	LIČKO-SENJSKA
53284	Velike Brisnice	Sveti Juraj	LIČKO-SENJSKA
53284	Starigrad	Sveti Juraj	LIČKO-SENJSKA
53284	Klada	Sveti Juraj	LIČKO-SENJSKA
53284	Lukovo	Sveti Juraj	LIČKO-SENJSKA
53284	Volarice	Sveti Juraj	LIČKO-SENJSKA
53284	Sveti Juraj	Sveti Juraj	LIČKO-SENJSKA
53284	Biljevine	Sveti Juraj	LIČKO-SENJSKA
53287	Stinica	Jablanac	LIČKO-SENJSKA
53287	Prizna	Jablanac	LIČKO-SENJSKA
53287	Jablanac	Jablanac	LIČKO-SENJSKA
53288	Vidovac Cesarički	Karlobag	LIČKO-SENJSKA
53288	Sušanj Cesarički	Karlobag	LIČKO-SENJSKA
53288	Staništa	Karlobag	LIČKO-SENJSKA
53288	Ledenik Cesarički	Karlobag	LIČKO-SENJSKA
53288	Kućišta Cesarička	Karlobag	LIČKO-SENJSKA
53288	Konjsko	Karlobag	LIČKO-SENJSKA
53288	Karlobag	Karlobag	LIČKO-SENJSKA
53289	Barić Draga	Lukovo Šugarje	LIČKO-SENJSKA
53289	Lukovo Šugarje	Lukovo Šugarje	LIČKO-SENJSKA
53291	Stara Novalja	Novalja	LIČKO-SENJSKA
53291	Potočnica	Novalja	LIČKO-SENJSKA
53291	Novalja	Novalja	LIČKO-SENJSKA
53291	Gajac-dio	Novalja	LIČKO-SENJSKA
53294	Lun	Lun	LIČKO-SENJSKA
53296	Caska	Zubovići	LIČKO-SENJSKA
53296	Kustići	Zubovići	LIČKO-SENJSKA
53296	Metajna	Zubovići	LIČKO-SENJSKA
53296	Vidalići	Zubovići	LIČKO-SENJSKA
53296	Zubovići	Zubovići	LIČKO-SENJSKA"""

###########################################################

SHORTER = """10000 Zagreb
10010 Zagreb-Sloboština
10020 Zagreb-Novi Zagreb
10040 Zagreb-Dubrava
10090 Zagreb-Susedgrad
10110 Zagreb
10250 Lučko
10251 Hrvatski Leskovac
10253 Donji Dragonožec
10255 Gornji Stupnik
10257 Brezovica
10290 Zaprešić
10291 Prigorje Brdovečko
10292 Šenkovec
10293 Dubravica
10294 Donja Pušća
10295 Kupljenovo
10296 Luka
10297 Jakovlje
10298 Donja Bistra
10299 Marija Gorica
10310 Ivanić-Grad
10311 Posavski Bregi
10312 Kloštar Ivanić
10313 Graberje Ivaničko
10314 Križ
10315 Novoselec
10316 Lijevi Dubrovčak
10340 Vrbovec
10341 Lonjica
10342 Dubrava
10343 Nova Kapela
10344 Farkaševac
10345 Gradec
10346 Preseka
10347 Rakovec
10360 Sesvete
10361 Sesvete-Kraljevec
10362 Kašina
10363 Belovar
10370 Dugo Selo
10372 Oborovo
10373 Ivanja Reka
10380 Sveti Ivan Zelina
10381 Bedenica
10382 Donja Zelina
10383 Komin
10408 Velika Mlaka
10410 Velika Gorica
10411 Orle
10412 Donja Lomnica
10413 Kravarsko
10414 Pokupsko
10415 Novo Čiče
10417 Buševec
10418 Dubranec
10419 Vukovina
10430 Samobor
10431 Sveta Nedjelja
10432 Bregana
10434 Strmec Samoborski
10435 Sveti Martin pod Okićem
10436 Rakov Potok
10437 Bestovje
10450 Jastrebarsko
10451 Pisarovina
10453 Gorica Svetojanska
10454 Krašić
10455 Kostanjevac
10456 Kalje
10457 Sošice
20000 Dubrovnik
20205 Topolo
20207 Mlini
20210 Cavtat
20213 Čilipi
20215 Gruda
20216 Dubravka
20217 Pridvorje
20218 Pločice
20221 Koločep
20222 Lopud
20223 Šipanjska Luka
20224 Maranovići
20225 Babino Polje
20226 Goveđari
20230 Ston
20231 Doli
20232 Slano
20233 Trsteno
20234 Orašac
20235 Zaton Veliki
20236 Mokošica
20240 Trpanj
20242 Oskorušno
20243 Kuna
20244 Potomje
20245 Trstenik
20246 Janjina
20247 Žuljana
20248 Putniković
20250 Orebić
20260 Korčula
20263 Lumbarda
20264 Račišće
20267 Kućište
20269 Lovište
20270 Vela Luka
20271 Blato
20272 Smokvica
20273 Čara
20274 Pupnat
20275 Žrnovo
20278 Nova Sela
20290 Lastovo
20340 Ploče
20341 Kula Norinska
20342 Otrić Seoci
20343 Rogotin
20344 Komin (Dalma)
20345 Staševica
20350 Metković
20352 Vid
20353 Mlinište
20355 Opuzen
20356 Klek
20357 Blace
21233 Hrvace
21236 Vrlika
21238 Otok (Dalmacija)
21240 Trilj
21241 Obrovac Sinjski
21242 Grab
21243 Ugljane
21244 Cista Velika
21245 Tijarica
21246 Aržano
21247 Neorić
21250 Šestanovac
21251 Žrnovnica
21252 Tugare
21253 Gata
21254 Blato na Cetini
21255 Zadvarje
21256 Cista Provo
21257 Lovreć
21260 Imotski
21261 Runović
21262 Kamenmost
21263 Krivodol
21264 Donji Proložac
21265 Studenci
21266 Zmijavci
21267 Ričice
21270 Zagvozd
21271 Grabovac
21272 Slivno
21273 Župa
21275 Dragljane
21276 Vrgorac
21277 Veliki Prolog
21292 Srinjine
21300 Makarska
21310 Omiš
21311 Stobreč
21312 Podstrana
21314 Jesenice
21315 Dugi Rat
21317 Lokva Rogoznica
21318 Mimice
21320 Baška Voda
21322 Brela
21323 Promajna
21325 Tučepi
21327 Podgora
21328 Drašnice
21329 Igrane
21330 Gradac
21333 Drvenik
21334 Zaostrog
21335 Podaca
21400 Supetar
21403 Sutivan
21404 Ložišća
21405 Milna
21410 Postira
21412 Pučišća
21413 Povlja
21420 Bol
21423 Nerežišća
21424 Pražnica
21425 Selca
21430 Grohote
21432 Stomorska
21450 Hvar
21454 Brusje
21460 Stari Grad
21462 Vrbanj
21463 Vrboska
21465 Jelsa
21466 Zastražišće
21467 Gdinj
21469 Sućuraj
21480 Vis
21483 Podšpilje
21485 Komiža
22000 Šibenik
22030 Šibenik-Zablaće
22202 Primošten
22203 Rogoznica
22204 Široke
22205 Perković
22206 Boraja
22211 Vodice
22212 Tribunj
22213 Pirovac
22214 Čista Velika
22215 Zaton
22221 Lozovac
22222 Skradin
22232 Zlarin
22233 Prvić Luka
22234 Prvić Šepurine
22235 Kaprije
22236 Žirje
22240 Tisno
22242 Jezera
22243 Murter
22244 Betina
22300 Knin
22301 Golubić
22303 Oklaj
22305 Kistanje
22310 Kijevo
22320 Drniš
22321 Siverić
22322 Ružić
22323 Unešić
22324 Drinovci
23000 Zadar
23205 Bibinje
23206 Sukošan
23207 Sveti Filip i Jakov
23210 Biograd na moru
23211 Pakoštane
23212 Tkon
23222 Zemunik
23223 Škabrnja
23226 Pridraga
23231 Petrčane
23232 Nin
23233 Privlaka (Dalmacija)
23234 Vir
23235 Vrsi
23241 Poličnik
23242 Posedarje
23243 Jasenice
23244 Starigrad Paklenica
23245 Tribanj
23247 Vinjerac
23248 Ražanac
23249 Povljana
23250 Pag
23251 Kolan
23262 Pašman
23263 Ždrelac
23264 Neviđane
23271 Kukljica
23272 Kali
23273 Preko
23274 Lukoran
23275 Ugljan
23281 Sali
23282 Žman
23283 Rava
23284 Veli Iž
23285 Brbinj
23286 Božava
23287 Veli Rat
23291 Sestrunj
23292 Molat
23293 Ist
23294 Premuda
23295 Silba
23296 Olib
23312 Novigrad (Dalmacija)
23420 Benkovac
23422 Stankovci
23423 Polača
23440 Gračac
23445 Srb
23450 Obrovac
23452 Karin
32000 Vukovar
32010 Vukovar
32100 Vinkovci
32211 Ostrovo
32212 Gaboš
32213 Markušica
32214 Tordinci
32221 Nuštar
32222 Bršadin
32224 Trpinja
32225 Bobota
32227 Borovo
32229 Petrovci
32232 Sotin
32233 Opatovac
32234 Šarengrad
32235 Bapska
32236 Ilok
32237 Lovas
32238 Čakovci
32239 Negoslavci
32241 Stari Jankovci
32242 Slakovci
32243 Orolik
32244 Đeletovci
32245 Nijemci
32246 Lipovac
32247 Banovci
32248 Ilača
32249 Tovarnik
32251 Privlaka
32252 Otok
32253 Komletinci
32254 Vrbanja
32255 Soljani
32256 Strošinci
32257 Drenovci
32258 Posavski Podgajci
32260 Gunja
32261 Rajevo Selo
32262 Račinovci
32263 Đurići
32270 Županja
32271 Rokovci Andrijaševci
32272 Cerna
32273 Gradište
32274 Štitar
32275 Bošnjaci
32276 Babina Greda
32280 Jarmina
32281 Ivankovo
32282 Retkovci
32283 Vođinci
32284 Stari Mikanovci
33000 Virovitica
33404 Špišić Bukovica
33405 Pitomača
33406 Lukač
33407 Gornje Bazje
33410 Suhopolje
33411 Gradina
33412 Cabuna
33507 Crnac
33513 Zdenci
33514 Čačinci
33515 Orahovica
33517 Mikleuš
33518 Nova Bukovica
33520 Slatina
33522 Voćin
33523 Čađavica
33525 Sopje
33533 Pivnica Slavonska
34000 Požega
34308 Jakšić
34310 Pleternica
34311 Kuzmica
34312 Sesvete (kod Požege)
34315 Ratkovica
34322 Brestovac
34330 Velika
34334 Kaptol
34335 Vetovo
34340 Kutjevo
34343 Bektež
34350 Čaglin
34543 Poljana
34550 Pakrac
34551 Lipik
34552 Badljevina
34553 Bučje
35105 Slavonski Brod
35106 Slavonski Brod
35107 Podvinje
35201 Podcrkavlje
35209 Bukovlje
35214 Donji Andrijevci
35250 Oriovac
35252 Sibinj
35254 Bebrina
35404 Cernik
35410 Nova Kapela
35422 Zapolje
35428 Dragalić
35430 Okučani
40000 Čakovec
40305 Nedelišće
40306 Macinec
40311 Lopatinec
40312 Štrigova
40313 Sveti Martin na Muri
40314 Selnica
40315 Mursko Središče
40317 Podturen
40318 Dekanovec
40319 Belica
40320 Donji Kraljevec
40321 Mala Subotica
40322 Orehovica
40323 Prelog
40324 Goričan
40325 Draškovec
40326 Sveta Marija
40327 Donji Vidovec
40328 Donja Dubrava
40329 Kotoriba
42000 Varaždin
42201 Beretinec
42202 Trnovec Bartolovečki
42203 Jalžabet
42204 Turčin
42205 Vidovec
42206 Petrijanec
42207 Vinica
42208 Cestica
42209 Sračinec
42214 Sveti Ilija
42220 Novi Marof
42222 Ljubeščica
42223 Varaždinske Toplice
42225 Breznički Hum
42230 Ludbreg
42231 Mali Bukovec
42232 Donji Martijanec
42233 Sveti Đurđ
42240 Ivanec
42242 Radovan
42243 Maruševec
42244 Klenovnik
42245 Donja Voća
42250 Lepoglava
42253 Bednja
42254 Trakošćan
42255 Donja Višnjica
43000 Bjelovar
43202 Zrinski Topolovac
43203 Kapela
43211 Predava
43212 Rovišće
43226 Veliko Trojstvo
43227 Šandrovac
43231 Ivanska
43232 Berek
43233 Trnovitički Popovac
43240 Čazma
43246 Štefanje
43247 Narta
43251 Gudovac
43252 Prgomelje
43270 Veliki Grđevac
43272 Nova Rača
43273 Bulinac
43274 Severin
43280 Garešnica
43282 Veliko Vukovje
43283 Kaniška Iva
43284 Hercegovac
43290 Grubišno Polje
43293 Veliki Zdenci
43500 Daruvar
43505 Končanica (Končenice)
43506 Dežanovac
43507 Uljanik
43531 Veliki Bastaji
43532 Đulovac
43541 Sirač
44000 Sisak
44010 Sisak-Caprag
44201 Martinska Ves
44202 Topolovac
44203 Gušće
44204 Jabukovac
44210 Sunja
44211 Blinjski Kut
44213 Kratečko
44250 Petrinja
44253 Mošćenica
44272 Lekenik
44273 Sela
44316 Velika Ludina
44317 Popovača
44318 Voloder
44320 Kutina
44321 Banova Jaruga
44322 Lipovljani
44323 Rajić
44324 Jasenovac
44325 Krapje
44330 Novska
44400 Glina
44410 Gvozd
44415 Topusko
44430 Hrvatska Kostajnica
44431 Donji Kukuruzari
44435 Divuša
44440 Dvor
44450 Hrvatska Dubica
47000 Karlovac
47201 Draganići
47203 Rečica
47204 Šišljavić
47206 Lasinja
47212 Skakavac
47220 Vojnić
47222 Cetingrad
47240 Slunj
47241 Cerovac Vukmanički
47242 Krnjak
47245 Rakovica
47246 Drežnik Grad
47250 Duga Resa
47251 Bosiljevo
47252 Barilović
47261 Zvečaj
47262 Generalski Stol
47264 Tounj
47271 Netretić
47272 Ribnik
47276 Žakanje
47280 Ozalj
47281 Mali Erjavec
47282 Kamanje
47283 Vivodina
47284 Kašt
47285 Radatovići
47286 Mahično
47300 Ogulin
47302 Oštarije
47303 Josipdol
47304 Plaški
47306 Saborsko
47307 Gornje Zagorje
47313 Drežnica
47314 Jasenak
48000 Koprivnica
48214 Sveti Ivan Žabno
48260 Križevci
48264 Kloštar Vojakovački
48265 Raven
48267 Orehovec
48268 Gornja Rijeka
48269 Kalnik
48306 Sokolovac
48311 Kunovec
48312 Rasinja
48314 Koprivnički Ivanec
48316 Đelekovec
48317 Legrad
48321 Peteranec
48322 Drnje
48323 Hlebine
48325 Novigrad Podravski
48326 Virje
48327 Molve
48331 Gola
48332 Ždala
48350 Đurđevac
48355 Novo Virje
48356 Ferdinandovac
48361 Kalinovac
48362 Kloštar Podravski
48363 Podravske Sesvete
49000 Krapina
49210 Zabok
49214 Veliko Trgovišće
49215 Tuhelj
49216 Desinić
49217 Krapinske Toplice
49218 Pregrada
49221 Bedekovčina
49222 Poznanovec
49223 Sveti Križ Začretje
49224 Lepajci
49225 Đurmanec
49228 Brestovec Orehovički
49231 Hum na Sutli
49232 Radoboj
49233 Gornje Jesenje
49234 Petrovsko
49240 Donja Stubica
49243 Oroslavje
49244 Stubičke Toplice
49245 Gornja Stubica
49246 Marija Bistrica
49247 Zlatar Bistrica
49250 Zlatar
49251 Mače
49252 Mihovljan
49253 Lobor
49254 Belec
49255 Novi Golubovec
49282 Konjščina
49283 Hraščina-Trgovišće
49284 Budinšćina
49290 Klanjec
49294 Kraljevec na Sutli
49295 Kumrovec
49296 Zagorska Sela
51000 Rijeka
51211 Matulji
51212 Vele Mune
51213 Jurdani
51214 Šapjane
51215 Kastav
51216 Viškovo
51217 Klana
51218 Dražice
51221 Kostrena
51222 Bakar
51223 Škrljevo
51224 Krasica
51225 Praputnjak
51226 Hreljin
51227 Kukuljanovo
51241 Križišće
51242 Drivenik
51243 Tribalj
51244 Grižane
51250 Novi Vinodolski
51251 Ledenice
51252 Klenovica
51253 Bribir
51260 Crikvenica
51261 Bakarac
51262 Kraljevica
51263 Šmrika
51264 Jadranovo
51265 Dramalj
51266 Selce
51280 Rab
51281 Lopar
51300 Delnice
51301 Brod na Kupi
51302 Kuželj
51303 Plešce
51304 Gerovo
51305 Tršće
51306 Čabar
51307 Prezid
51311 Skrad
51312 Brod Moravice
51313 Kupjak
51314 Ravna Gora
51315 Mrkopalj
51316 Lokve
51317 Crni Lug
51322 Fužine
51323 Lič
51324 Zlobin
51325 Moravice
51326 Vrbovsko
51327 Gomirje
51328 Lukovdol
51329 Severin na Kupi
51410 Opatija
51414 Ičići
51415 Lovran
51417 Mošćenička Draga
51418 Brseč
51500 Krk
51511 Malinska
51512 Njivice
51513 Omišalj
51514 Dobrinj
51515 Šilo
51516 Vrbnik
51517 Kornić
51521 Punat
51522 Draga Bašćanska
51523 Baška
51550 Mali Lošinj
51551 Veli Lošinj
51552 Ilovik
51554 Nerezine
51555 Belej
51556 Martinšćica
51557 Cres
51559 Beli
51561 Susak
51562 Unije
51564 Ćunski
52000 Pazin
52100 Pula (Pola)
52203 Medulin
52204 Ližnjan (Lisignano)
52206 Marčana
52207 Barban
52208 Krnica
52210 Rovinj (Rovigno)
52211 Bale (Valle)
52212 Fažana (Fasana)
52215 Vodnjan (Dignano)
52216 Galižana (Gallesano)
52220 Labin
52221 Rabac
52222 Koromačno
52223 Raša
52224 Trget
52231 Nedešćina
52232 Kršan
52233 Šušnjevica
52234 Plomin
52332 Pićan
52333 Podpićan
52341 Žminj
52342 Svetvinčenat
52352 Kanfanar
52402 Cerovlje
52403 Gračišće
52404 Sveti Petar u šumi
52420 Buzet
52422 Lanišće
52423 Karojba
52424 Motovun (Montana)
52425 Roč
52426 Lupoglav
52427 Livade (Levade)
52428 Oprtalj (Portole)
52429 Grožnjan (Grisignana)
52434 Boljun
52440 Poreč (Parenzo)
52444 Tinjan
52445 Baderna
52446 Nova Vas
52447 Vižinada (Visinada)
52448 Sveti Lovreč
52449 Červar Porat
52450 Vrsar (Orsera)
52452 Funtana (Fontane)
52460 Buje (Buie)
52462 Momjan (Momiano)
52463 Višnjan (Visignano)
52464 Kaštelir (Castelliere)
52465 Tar (Torre)
52466 Novigrad (Cittanova)
52470 Umag (Umago)
52474 Brtonigla (Verteneglio)
52475 Savudrija (Salvore)
53000 Gospić
53201 Lički Osik
53202 Perušić
53203 Kosinj
53206 Brušane
53211 Smiljan
53212 Klanac
53213 Donje Pazarište
53220 Otočac
53223 Vrhovine
53224 Ličko Lešće
53230 Korenica
53231 Plitvička Jezera
53233 Ličko Petrovo Selo
53234 Udbina
53236 Podlapača
53244 Lovinac
53250 Donji Lapac
53260 Brinje
53261 Križpolje
53262 Jezerane
53270 Senj
53271 Krivi Put
53273 Vratnik
53274 Krasno
53284 Sveti Juraj
53287 Jablanac
53288 Karlobag
53289 Lukovo Šugarje
53291 Novalja
53294 Lun
53296 Zubovići"""


##############################


def main():
    LONGER.encode('iso-8859-1')
    SHORTER.encode('iso-8859-1')
    LONGER_set = set()
    SHORTER_set = set()
    TOTAL = []
    LONGER_id = 0

    for item in LONGER.split('\n'):
        LONGER_set |= {item[:5]}
        
        temp = item.split('\t')
        
        if LONGER_id != temp[0]:
            TOTAL.append([temp[0], temp[2]])
            LONGER_id = temp[0]

    del temp, item

    for item in SHORTER.split('\n'):
        SHORTER_set |= {item[:5]}
        
        temp0 = item[:5]
        temp1 = item[6:]
        
        for element in TOTAL:
            if element[0] == temp0:
                break

        else:
            TOTAL.append([temp0, temp1])
            
    FINISHED = sorted(TOTAL, key = lambda x: int(x[0]))

    for item in FINISHED:
        if item[0] == '10110':
            item[1] = 'Zagreb-Jarun'
            break
    
    print('Extra in SHORTER: {}\n'. format(SHORTER_set - LONGER_set))

    check = set()
    for pair in FINISHED:
        x = pair[1]
        if x in check:
            print("DUPLO!", x)
        check |= {x}

    db = open("PopulateTableCity.sql", "w")

    for item in FINISHED:
        print(item[0], item[1])
        db.write("INSERT INTO \"City\" VALUES({}, '{}');\n". format(item[0], item[1]))

    db.close()
    
    print('\nSQL file successfully generated.\n')

    return



main()


