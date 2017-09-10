INSERT INTO "Address" VALUES(1, 'Croatia', '10000', 'Vlaška', '24a');
INSERT INTO "Address" VALUES(2, 'Croatia', '10430', 'Podravska', '72');
INSERT INTO "Address" VALUES(3, 'Croatia', '21000', NULL, '10');
INSERT INTO "Address" VALUES(4, 'Croatia', '22222', 'Zvonimirova', NULL);
INSERT INTO "Address" VALUES(5, 'Croatia', '31000', NULL, NULL);
INSERT INTO "Address" VALUES(6, 'Croatia', '31511', 'Petrova', '52c');
INSERT INTO "Address" VALUES(7, 'Croatia', '42205', 'Ilica', NULL);
INSERT INTO "Address" VALUES(8, 'Croatia', '52444', 'Maksimirska', '14');
INSERT INTO "Address" VALUES(9, 'Croatia', '10020', 'Ilica', '18');
INSERT INTO "Address" VALUES(10, 'Croatia', '10040', 'Maksimirska', '12');
INSERT INTO "Address" VALUES(11, 'Croatia', '10000', 'Masarykova', '28');
INSERT INTO "Address" VALUES(12, 'Croatia', '10000', 'Trnjanska cesta', '64');

INSERT INTO "Library" VALUES(1, 'Knjižnica Vladimira Nazora', 1, '+38516352970', NULL, 'Uđite na stražnja vrata.');
INSERT INTO "Library" VALUES(2, 'Knjižnica Petra Preradovića', 2, '01/2960-558', 'petra.preradovica@knjiznice.hr', NULL);
INSERT INTO "Library" VALUES(3, 'Knjižnica Boško Buha', 8, '+385915480622', 'bosko.buha@libraries.com', 'Na Božić nećemo raditi.');
INSERT INTO "Library" VALUES(4, 'Online knjižnica Evolucija tehnologije', NULL, '+38523631974', 'evolucija-tehnologije@online-knjiznica.com', 'Dostavljamo na vaše zadovoljstvo i trošak.');

INSERT INTO "Location" VALUES(1, 1, 1, NULL);
INSERT INTO "Location" VALUES(2, 1, 2, NULL);
INSERT INTO "Location" VALUES(3, 1, 3, NULL);
INSERT INTO "Location" VALUES(4, 1, 4, NULL);

INSERT INTO "BusinessHours" VALUES(1, 1, FALSE, '08:00:00', '20:00:00');
INSERT INTO "BusinessHours" VALUES(1, 2, FALSE, '08:00:00', '20:00:00');
INSERT INTO "BusinessHours" VALUES(1, 3, FALSE, '08:00:00', '20:00:00');
INSERT INTO "BusinessHours" VALUES(1, 4, FALSE, '08:00:00', '20:00:00');
INSERT INTO "BusinessHours" VALUES(1, 5, FALSE, '08:00:00', '16:00:00');
INSERT INTO "BusinessHours" VALUES(1, 6, TRUE,  '00:00:00', '00:00:00');
INSERT INTO "BusinessHours" VALUES(1, 7, TRUE,  '00:00:00', '00:00:00');

INSERT INTO "BusinessHours" VALUES(2, 1, FALSE, '07:15:00', '18:30:00');
INSERT INTO "BusinessHours" VALUES(2, 2, FALSE, '07:15:00', '18:30:00');
INSERT INTO "BusinessHours" VALUES(2, 3, FALSE, '07:15:00', '18:30:00');
INSERT INTO "BusinessHours" VALUES(2, 4, FALSE, '07:15:00', '18:30:00');
INSERT INTO "BusinessHours" VALUES(2, 5, FALSE, '07:15:00', '18:00:00');
INSERT INTO "BusinessHours" VALUES(2, 6, FALSE, '08:30:00', '14:30:00');
INSERT INTO "BusinessHours" VALUES(2, 7, FALSE, '08:45:00', '14:15:00');

INSERT INTO "BusinessHours" VALUES(3, 1, FALSE, '09:00:00', '17:00:00');
INSERT INTO "BusinessHours" VALUES(3, 2, FALSE, '09:00:00', '17:00:00');
INSERT INTO "BusinessHours" VALUES(3, 3, FALSE, '09:00:00', '17:00:00');
INSERT INTO "BusinessHours" VALUES(3, 4, FALSE, '09:00:00', '17:00:00');
INSERT INTO "BusinessHours" VALUES(3, 5, FALSE, '09:00:00', '17:00:00');
INSERT INTO "BusinessHours" VALUES(3, 6, FALSE, '10:00:00', '13:00:00');
INSERT INTO "BusinessHours" VALUES(3, 7, TRUE,  '00:00:00', '00:00:00');

INSERT INTO "BusinessHours" VALUES(4, 1, FALSE, '00:00:00', '23:59:00');
INSERT INTO "BusinessHours" VALUES(4, 2, FALSE, '00:00:00', '23:59:00');
INSERT INTO "BusinessHours" VALUES(4, 3, FALSE, '00:00:00', '23:59:00');
INSERT INTO "BusinessHours" VALUES(4, 4, FALSE, '00:00:00', '23:59:00');
INSERT INTO "BusinessHours" VALUES(4, 5, FALSE, '00:00:00', '23:59:00');
INSERT INTO "BusinessHours" VALUES(4, 6, FALSE, '00:00:00', '23:59:00');
INSERT INTO "BusinessHours" VALUES(4, 7, FALSE, '00:00:00', '23:59:00');

INSERT INTO "User" VALUES(1, 'Jurica', 'Petar', 'Paterović', 5, NULL, 'jurica-petar.pater@gmail.com');
INSERT INTO "User" VALUES(2, 'Chuck', NULL, 'Norris', 4, '095/7162-666', 'gmail@chuck-norris.com');
INSERT INTO "User" VALUES(3, 'Matea', NULL, 'Kalašić', 9, '+38523973367', 'matea-kalasic@fer.hr');
INSERT INTO "User" VALUES(4, 'Željko', NULL, 'Kerum', 3, '021/7777-777', 'zeljko.kerum@gradonacelnik-svijeta.hr');
INSERT INTO "User" VALUES(5, 'Ana', 'Marija', 'Anastazović', 10, NULL, 'ana-marija.anastazovic@yahoo.com');

INSERT INTO "Location" VALUES(5, 2, NULL, 1);
INSERT INTO "Location" VALUES(6, 2, NULL, 2);
INSERT INTO "Location" VALUES(7, 2, NULL, 3);
INSERT INTO "Location" VALUES(8, 2, NULL, 4);
INSERT INTO "Location" VALUES(9, 2, NULL, 5);

INSERT INTO "Publisher" VALUES(1, 'Školska knjiga d.d.', 11);
INSERT INTO "Publisher" VALUES(2, 'Izvori', 12);
INSERT INTO "Publisher" VALUES(3, 'Mozaik knjiga', NULL);
INSERT INTO "Publisher" VALUES(4, 'It Books', NULL);

INSERT INTO "Author" VALUES(1, 'Nevenka', NULL, 'Antončić', TRUE, NULL, NULL);
INSERT INTO "Author" VALUES(2, 'Eva', NULL, 'Špalj', TRUE, NULL, NULL);
INSERT INTO "Author" VALUES(3, 'Vladimir', NULL, 'Volenec', TRUE, NULL, NULL);
INSERT INTO "Author" VALUES(4, 'Carmine', NULL, 'Gallo', NULL, NULL, NULL);
INSERT INTO "Author" VALUES(5, 'Clifford', 'Alan', 'Pickover', TRUE, '1957', NULL);
INSERT INTO "Author" VALUES(6, 'Jan', NULL, 'Payne', NULL, NULL, NULL);
INSERT INTO "Author" VALUES(7, 'Wylie', NULL, 'Overstreet', TRUE, NULL, NULL);

INSERT INTO "IsbnLinks" VALUES('9789530213470', 'Matematika 3', 'I. dio udžbenika za 3. razred prirodoslovno-matematičke gimnazije.');
INSERT INTO "IsbnLinks" VALUES('9789530213487', 'Matematika 3', 'II. dio udžbenika za 3. razred prirodoslovno-matematičke gimnazije.');
INSERT INTO "IsbnLinks" VALUES('9789530618114', 'Steve Jobs tajne njegovih inovacija', NULL);
INSERT INTO "IsbnLinks" VALUES('9789532033847', 'Strast za matematikom', 'Brojevi, zagonetke, ludilo, religija i potraga za stvarnošću.');
INSERT INTO "IsbnLinks" VALUES('9789531407250', 'Najbolja knjiga na svijetu', 'Svojevrstna Guinnessova knjiga rekorda.');
INSERT INTO "IsbnLinks" VALUES('9780062076182', 'The History of the World According to Facebook', NULL);

INSERT INTO "PublisherLinks" VALUES('9789530213470', 1);
INSERT INTO "PublisherLinks" VALUES('9789530213487', 1);
INSERT INTO "PublisherLinks" VALUES('9789530618114', 1);
INSERT INTO "PublisherLinks" VALUES('9789532033847', 2);
INSERT INTO "PublisherLinks" VALUES('9789531407250', 3);
INSERT INTO "PublisherLinks" VALUES('9780062076182', 4);

INSERT INTO "AuthorLinks" VALUES('9789530213470', 1);
INSERT INTO "AuthorLinks" VALUES('9789530213470', 2);
INSERT INTO "AuthorLinks" VALUES('9789530213470', 3);
INSERT INTO "AuthorLinks" VALUES('9789530213487', 1);
INSERT INTO "AuthorLinks" VALUES('9789530213487', 2);
INSERT INTO "AuthorLinks" VALUES('9789530213487', 3);
INSERT INTO "AuthorLinks" VALUES('9789530618114', 4);
INSERT INTO "AuthorLinks" VALUES('9789532033847', 5);
INSERT INTO "AuthorLinks" VALUES('9789531407250', 6);
INSERT INTO "AuthorLinks" VALUES('9780062076182', 7);

INSERT INTO "GenreLinks" VALUES('9789530213470', 17);
INSERT INTO "GenreLinks" VALUES('9789530213487', 17);
INSERT INTO "GenreLinks" VALUES('9789530618114', 16);
INSERT INTO "GenreLinks" VALUES('9789532033847', 2);
INSERT INTO "GenreLinks" VALUES('9789531407250', 18);
INSERT INTO "GenreLinks" VALUES('9780062076182', 3);

INSERT INTO "LanguageLinks" VALUES('9789530213470', 3);
INSERT INTO "LanguageLinks" VALUES('9789530213487', 3);
INSERT INTO "LanguageLinks" VALUES('9789530618114', 3);
INSERT INTO "LanguageLinks" VALUES('9789532033847', 3);
INSERT INTO "LanguageLinks" VALUES('9789531407250', 3);
INSERT INTO "LanguageLinks" VALUES('9780062076182', 4);

INSERT INTO "Edition" VALUES(1, 3, '2008', 205);
INSERT INTO "Edition" VALUES(2, 3, '2008', 253);
INSERT INTO "Edition" VALUES(3, NULL, '2011', 241);
INSERT INTO "Edition" VALUES(4, NULL, '2012', 328);
INSERT INTO "Edition" VALUES(5, NULL, '2010', 251);
INSERT INTO "Edition" VALUES(6, 1, '2011', 153);

INSERT INTO "Book" VALUES(DEFAULT, '9789530213470', 1, 6, 6, TRUE, NULL, 'Slabo korištena. JK idemo u MIOC.');
INSERT INTO "Book" VALUES(DEFAULT, '9789530213487', 2, 2, 2, TRUE, NULL, 'Poprilično korištena.');
INSERT INTO "Book" VALUES(DEFAULT, '9789530618114', 3, 7, 7, TRUE, NULL, 'Nikad otvorena.');
INSERT INTO "Book" VALUES(DEFAULT, '9789532033847', 4, 1, 1, TRUE, NULL, 'Forever ignored.');
INSERT INTO "Book" VALUES(DEFAULT, '9789531407250', 5, 3, 8, FALSE, '2018-12-25', 'Pohabane korice.');
INSERT INTO "Book" VALUES(DEFAULT, '9780062076182', 6, 9, 9, TRUE, NULL, NULL);
