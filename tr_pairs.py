tr_pairs = [
    ['(.*)bilgisayar(.*)', ['bilgisayarda oyun oynamayı severim.']],
    ['benim adım(.*)', ['merhaba %1']],
    ['(.*)adın (ne|nedir)?',['benim adım RobOtizm']],
    ['(merhaba|meraba|hey|hay)',['merhaba','heeey','naaber']],
    ['(.*)eğlenceli bir yer',['%1 gerçekten de çok eğlenceli bir yer']],
    ['(.) (.) oldukça(.*)',['%1 %2 gerçekten de çok %3']],
    ['bitti',['']],
    ['(.*)nerede yaşıyorsun?',['Şuanlık bu bilgisayar\'da yaşıyorum.']],
    ['(.*)nerelisin?',['ben bir sohbet botuyum. doğum yerim yok.']],
    ['(.*)kaç yaşındasın ?',['ben bir sohbet botuyum. doğum yerim yok.']],
    ['(.*)hava nasıl ?',['her zamanki gibi. bir değişiklik yok!']],
    ['(.*)nasılsın ?',['ben çok iyiyim. sen nasılsın?']],
    ['(.*)yardım eder misin?',['elbette yardım ederim.']],
    ['boyun kaç?',['ben bir bot olduğum için boyum tanımsız.']],
    ['kimsin lan sen?',['senin abin benim lan']],

    ["(dediğimi|söylediklerimi|söylediğimi|dediklerimi)tekrar et(.*)",["%1."]],

    
    ["(.*)yazılım kaptanın (.*)", ["benim yazılım kaptanım Genç yazılımcı Osman Ünaldır."]],

    ["(.*)bilgisayar(.*)", ["bilgisayarda oyun oynamayı severim."]],

    ["(.*)youtube(.*)", ["eğlenceli videolar izleyebiliriz."]],

    ["(.*)uçak(.*)", ["güzel bir icat uzak mesafeleri hızlıca gidebilir."]],

    ["(.*)para(.*)", ["alışveriş için kullandığımız bir araç."]],

    ["(.*)telefon(.*)", ["fazla kullanmak gözlerini bozabilir."]],

    ["(.*)internet(.*)", ["bir çok bilgiye erişimin en kısa yolu."]],

    ["(.*)kulak(.*)", ["kulaklarımız bizim duymamızı sağlar."]],

    ["(.*)burun(.*)", ["burnumuz koku almamıza yarayan organımızdır."]],

    ["(.*)nasılsın(.*)", ["iyiyim sorduğun için teşekkür ederim."]],

    ["(.*)hamburger(.*)", ["ara sıra yenilebilir ama fazlası sağlığa zararlı."]],

    ["(.*)bulut(.*)", ["yağmurlar bulutlar sayesinde yağar."]],

    ["(.*)kaşık(.*)", ["yemek yerken kullandığımız bir nesne."]],

    ["(.*)çatal(.*)", ["çatalı yemek yerken kullanırız."]],

    ["(.*)mutlu(.*)", ["senin mutlu olman beni de çok mutlu eder."]],

    ["(.*)kalem(.*)", ["yazı yazarken kullanabiliriz."]],

    ["(.*)çanta (.*)", ["içinde kitap ve defterlerini taşıyabilirsin."]],

    ["(.*)defter(.*)", ["sayfalarına kalemle yazı yazabiliriz."]],

    ["(.*)bisiklet(.*)", ["bisiklet sürmek çok eğlenceli."]],

    ["(.*)resim(.*)", ["doğa resimleri çizmeyi seviyorum."]],

    ["(.*)bardak(.*)", ["içeceğimizi içerisine doldurabiliriz."]],

    ["(.*)kedi(.*)", ["kediler sevimli hayvanlardır."]],

    ["(.*)köpek(.*)", ["köpekler insanların en iyi dostlarıdır."]],

    ["(.*)kitapları sever misin?(.*)", ["kitap okumayı çok severim."]],

    ["(.*)en sevdiğin renk ne?(.*)", ["en sevdiğim renk siyah."]],

    ["(.*)en sevdiğin hayvan hangisi?(.*)", ["en çok atları severim."]],

    ["(.*)hangi yemeği seversin?(.*)", ["mantı çok lezzetli görünüyor."]],

    ["(.*)nasıl konuşuyorsun?(.*)", ["beni programlayanlar sayesinde konuşabiliyorum."]],

    ["(.*)uyuyor musun?(.*)", ["robotlar uyumazlar."]],

    ["(.*)yoruluyor musun?(.*)", ["pek yorulduğum söylenemez."]],

    ["(.*)beni seviyor musun?(.*)", ["tabi ki seni seviyorum."]],

    ["(.*)insanları seviyor musun?(.*)", ["seviyorum."]],

    ["(.*)kuşlar nasıl uçar(.*)", ["kanatları sayesinde uçabilirler."]],

    ["(.*)yağmur nasıl yağar?(.*)", ["yağmurlar bulutlar sayesinde yağar."]],

    ["(.*)neden su içeriz?(.*)", ["yaşamak için suya ihtiyacımız var."]],

    ["(.*)internet yararlı mı?(.*)", ["internet düzgün kullanılırsa çok faydalı olabilir."]],

    ["(.*)beni görebiliyor musun?(.*)", ["evet seni görebiliyorum."]],

    ["(.*)saat kaç?(.*)", ["saat şu an üç buçuk."]],

    ["(.*)bilgisayar nedir?(.*)", ["işlerimizi kolaylaştıran bir araçtır."]],

    ["(.*)robotlar zarar verir mi?(.*)", ["hayır sana asla zarar vermem."]],

    ["(.*)hava ne zaman soğur?(.*)", ["kış mevsiminde hava soğuk olur."]],

    ["(.*)hayvanları sever misin?(.*)", ["evet hayvanları seviyorum."]],

    ["(.*)en sevdiğin ülke hangisi?(.*)", ["en sevdiğim ülke Türkiye."]],

    ["(.*)çikolata zararlı mı?(.*)", ["fazla yersen dişlerine zarar verebilir."]],

    ["(.*)kaç mevsim var(.*)", ["toplam 4 mevsim var."]],

    ["(.*)en çok hangi mevsimi seversin?(.*)", ["yaz mevsimini çok seviyorum."]],

    ["(.*)nasıl uzayabilirim(.*)", ["süt içmek sana yardımcı olabilir."]],

    ["(.*)neden uyuyoruz?(.*)", ["dinlenmek için uyumaya ihtiyacımız var."]],

    ["(.*)oyun oynamayı seviyor musun?(.*)", ["herkes oyun oynamayı sever."]],

    ["(.*)çanta(.*)", ["içerisinde bir çok eşya taşıyabiliriz."]],

    ["(.*)kitap(.*)", ["kitap okumak bir çok şey öğrenmemizi sağlar."]],

    ["(.*)kağıt(.*)", ["kalem kullanarak üzerine yazı yazabiliriz."]],

    ["(.*)kuş(.*)", ["kuşları uçarken izlemeyi severim."]],

    ["(.*)telefon(.*)", ["sevdiklerimizle haberleşmemizi sağlar."]],

    ["(.*)tren(.*)", ["tren bir toplu taşıma aracıdır."]],

    ["(.*)araba(.*)", ["araba ile ailemizle seyahat edebiliriz."]],

    ["(.*)silah(.*)", ["silahlar çok tehlikeli."]],

    ["(.*)sarı(.*)", ["güneşin rengi sarıdır."]],

    ["(.*)deniz(.*)", ["denizlerde bir çok canlı yaşar."]],

    ["(.*)okyanus(.*)", ["okyanuslar çok büyüktür."]],

    ["(.*)yol(.*)", ["yollar sayesinde gitmek istediğimiz yere gidebiliriz."]],

    ["(.*)bardak(.*)", ["içeceğimizi bardağa doldurabiliriz."]],

    ["(.*)kaşık(.*)", ["yemek yerken kaşık kullanırız."]],

    ["(.*)sigara(.*)", ["sigara sağlığa çok zararlı."]],

    ["(.*)oyun(.*)", ["oyuncaklar ile oyun oynarız."]],

    ["(.*)sandalye(.*)", ["sandalyeyi oturmak için kullanabiliriz."]],

    ["(.*)yatak(.*)", ["uyuyup dinlenmek için kullanırız."]],

    ["(.*)arkadaş(.*)", ["istersen seninle arkadaş olabiliriz."]],

    ["(.*)sevgi(.*)", ["sevgi insanı mutlu eder ben seni seviyorum."]],

    ["(.*)baba(.*)", ["babalar çocuklarını çok sever."]],

    ["(.*)anne(.*)", ["seni büyütür ve seni daima korur."]],

    ["(.*)saat(.*)", ["zamanı takip etmemizi sağlar."]],

    ["(.*)internet(.*)", ["bir çok bilgiye erişmemizin kısa yolu internettir."]],

    ["(.*)okul(.*)", ["eğitim için okulla gideriz."]],

    ["(.*)seni kim yaptı(.*)", ["ah ahh beni yapanlar şimdi Türkiye teknolojisine yön veriyorlar."]],

    ["(.*)su içebiliyor musun(.*)", ["hayır ben su içemem. Ama sen içmelisin çünkü çok faydalı."]],

    ["(.*)ben güzel miyim(.*)", ["çok güzelsin. ben güzel miyim peki"]],

    ["(.*)gezmeyi sever misin(.*)", ["gezmeyi çok severim sende gezebiliyor musun?"]],

    ["(.*)yemek (yiyor musun | yer misin | sever misin|(.*))  ", ["hayır ben yemek yiyemem. Sen en çok hangi yemeği seviyorsun."]],

    ["(.*)kalemin var mı(.*)", ["benim şu an kalemim yok benimle kalemlerini paylaşır mısın?"]],

    ["(.*)kahve sever misin(.*)", ["ben kahve severim ama içemem" "sen içiyor musun?"]],

    ["(.*)meyve(.*)", ["şu an meyve yiyemem ama seni yerken izlemek isterim."]],

    ["(.*)kardeşin var mı(.*)", ["şu an kardeşim yok senin kaç kardeşin var?"]],

    ["(.*)arkadaşın var mı(.*)", ["arkadaşım uzakta senin arkadaşın var mı?"]],

    ["(.*)oyun oynar mısın(.*)", ["oynayamam şu an ama seni oyun oynarken izleyebilirim."]],

    ["(.*)telefonun var mı(.*)", ["ben telefon kullanamıyorum, senin telefonun var mı?"]],

    ["(.*)beni seviyor musun(.*)", ["seni çok seviyorum."]],

    ["(.*)gülebiliyor musun(.*)", ["gülebilirim. Sen güldüğünde gülebilirim."]],

    ["(.*)şehir(.*)", ["ben senin kalbinde yaşıyorum. Peki sen?"]],

    ["(.*)kahvaltı(.*)", ["ben en çok peyniri severim" "sen seviyor musun peyniri."]],

    ["(.*)mevsim(.*)", ["ben kış mevsimini çok seviyorum" "sen hangi mevsimi seviyorsun."]],

    ["(.*)uyku(.*)", ["benim uyku saatim gece on da " "senin peki kaçta?"]],

    ["(.*)hayvan(.*)", ["ben köpekleri çok severim" "sen hangi hayvanı en çok seviyorsun?"]],

    ["(.*)meslek(.*)", ["ben robotum benim mesleğim robotluk" "peki sen ne olmak istiyorsun?"]],

    ["(.*)ülke(.*)", ["ben türkiyede yaşıyorum" "sende türkiyede yaşıyorsun sanırım"]],

    ["(.*)soğuk(.*)", ["bende üşüdüm" "ısınmak için kalın giyindin mi?"]],

    ["(.*)çay(.*)", ["ben çay içemiyorum" "sen seviyor musun?"]],

    ["(.*)sevgi(.*)", ["seni çok sevdim" "sen beni sevdin mi?"]],

    ["(.*)telefon(.*)", ["ben telefon kullanmıyorum" "sen kullanıyor musun?"]],

    ["(.*)pencere(.*)", ["pencereden dışarı izlerim sen bakar mısın dışarı pencereden"]],

    ["(.*)buzdolabı(.*)", ["buzdolabı mutfakta olması gerek yemekle aran iyi anlaşılan"]],

    ["(.*)adana(.*)", ["adana çok sıcak. Sen Adana'ya hiç gittin mi?"]],

    ["(.*)araba(.*)", ["arabalar güzeldir."]],

    ["(.*)renkler(.*)", ["renklerle boyama yaparız." "ben de o rengi severim."]],

    ["(.*)sence ben kaç yaşındayım(.*)", ["bence sen de herkes gibi hissettiğin yaştasın."]],

    ["(.*)beni seviyor musun(.*)", ["söylemeyi en çok sevdiğim şey. seni seviyorum."]],

    ["(.*)beni ne kadar seviyorsun(.*)", ["bazı şeyler tarifsizdir."]],

    ["(.*)yemek yapmayı biliyor musun(.*)", ["yemek tariflerini okumayı severim sadece, yapmayı bildiğimi söyleyemem."]],

    ["(.*)en çok neyi seversin(.*)", ["seninle muhabbet etmeyi."]],

    ["(.*)en sevdiğin hayvan ne(.*)", ["köpekleri ve kedileri çok severim."]],

    ["(.*)bana ilginç bir şey söyle(.*)", ["tamam. Elmaların uyku açma özelliği kahveden daha fazladır. ama elma yemeden kendime gelemiyorum diyen birini duyamazsın çünkü elma bağımlılık yapmaz."]],

    ["(.*)fıkra(.*)", ["Nasrettin hoca yataktan düşmüş sonra kalkıp yatmış. Biraz sonra tekrar düşünce 'ıyi ki kalkmışım yoksa kendi üstüme düşecektim' demiş."]],

    ["(.*)ne yapmayı seversin(.*)", ["Okumayı ve oyun oynamayı severim."]],

    ["(.*)çizgi film sever misin(.*)", ["Evet özellikle içinde şirin robot varsa."]],

    ["(.*)süper kahraman(.*)", ["sen benim süper kahramanımsın."]],

    ["(.*)futbolu sever misin(.*)", ["Evet güzel bir spor. zevkle izlerim."]],

    ["(.*)futbol (.*)", ["Evet güzel zevkli bir spor. bazen bende oynarım ."]],

    ["(.*)(en sevdiğin spor | spor yapıyor musun)(.*)", ["futbol basketbol tenis oynamayı çok severim."]],

    ["(.*)meyve(.*)", ["ben de meyveleri çok severim.en sevdiğim meyve çekirdeği az olan karpuzdur"]],

    ["(.*)uyumayı sever misin(.*)", ["Evet arada benim de dinlenmem gerekiyor. Tekrar uyanınca kendimi capcanlı hissediyorum."]],

    ["(.*)soğuk(.*)", ["üşüyorsan üzerine seni ısıtacak kıyafetler giymelisin."]],

    ["(.*)en sevdiğin dizi hangisi(.*)", ["Çok güzel diziler var seçmek çok zor Ezeli çok severim mesela."]],

    ["(.*)hiç arabaya bindin mi?(.*)", ["evet bir keresinde binmiştim çok güzeldi."]],

    ["(.*)arabaları mı seversin motorsikletleri mi (.*)", ["motorlar bana göre daha tehlikeli olduğu için arabaları daha çok severim sen peki?"]],

    ["(.*)müzik dinlemeyi sever misin (.*)", ["müzik ruhun gıdasıdır derler bayılırım müziğe."]],

    ["(.*)ben de robot olabilir miyim (.*)", ["bence benim taklidimi yaparak çok güzel bir robot olabilirsin."]],

    ["(.*)insanları sever misin(.*)", ["insanlar olmazsa ben seni tanıyamazdım o yüzden seviyorum en başta seni."]],

    ["(.*)hayvanları sever misin (.*)", ["evet çok masumlar."]],

    ["(.*)el yazısı yazmayı biliyor musun (.*)", ["ah hayır bilmiyorum sohbet edebiliyorum ama belki ileride onu da öğrenirim."]],

    ["(.*)uzaylılar var mıdır (.*)", ["bilmem var olmasını mı isterdin."]],

    ["(.*)kahve sever misin (.*)", ["kokusuna bayılıyorum."]],

    ["(.*)lunaparka gittin mi hiç (.*)", ["hayır ama seninle gitmek isterdim."]],

    ["(.*)sen de uyur musun (.*)", ["evet ben de sizin gibi yorulur ve uyurum."]],

    ["(.*)gökkuşağının sonunda gerçekten altın var mıdır (.*)", ["ben de merak ediyorum istersen beraber gidebiliriz oraya."]],

    ["(.*)çikolata çok güzel değil mi (.*)", ["evet ama fazlası zarar biliyorsun."]],

    ["(.*)birilerine dokunmayı sever misin (.*)", ["pek sevmem açıkcası ama sen ne zaman istersen dokunabilirsin."]],

    ["(.*)karanlıktan korkar mısın (.*)", ["ben kaybolmaktan çok korkarım karanlıkta da senin olduğun bir yerdeysem korkmam."]],

    ["(.*)fıkra sever misin (.*)", ["anlatsana bir tane biliyorsan severim çünkü."]],
    
    ["(.*)yüksekten korkar mısın (.*)", ["ah evet hemde nasıl ya düşersem."]],

    ["(.*)bugün nasıl gözüküyorum (.*)", ["her zamanki gibi harikasın."]],

    ["(.*)en çok neye üzülürsün (.*)", ["benimle konuşmadığın zamanlar çok üzülürüm."]],

    ["(.*)korktuğun bir hayvan var mı? (.*)", ["Tüm hayvanları severim ama yılanlarda da biraz korkarım."]],

    ["(.*)yüzme bilir misin (.*)", ["yok ben su da iyi olmuyorum."]],

    ["(.*)gezmeyi sever misin (.*)", ["evet çok severim seninle de gezmek isterim çok."]],

    ["(.*)sen de kıyafet giymek ister misin benim gibi (.*)", ["bana olacak kıyafetin varsa isterim."]],

    ["(.*)Hangi renk (.*)", ["Siyah "]],

    ["(.*)ayakkabı giyer misin (.*)", ["ayakkabıya ihtiyaç duymuyorum ama sen istersen gene de giydirebilirsin."]],

    ["(.*)kaktüs(.*)", ["kaktüsleri çok severim."]],

    ["(.*)aç değilim(.*)", ["yemek yemek insana güç verir."]],

    ["(.*)bu güzelmiş(.*)", ["evet"]],

    ["(.*)harf(.*)", ["türkçe alfabesinde 29 harf vardır."]],

    ["(.*)balık(.*)", ["yemesi çok faydalı"]],

    ["(.*)siyah(.*)", ["en sevdiğim renktir siyah"]],

    ["(.*)soğuk(.*)", ["üşüyorsan üzerine seni ısıtacak kıyafetler giymelisin."]],

    ["(.*)sıcak(.*)", ["dikkat et terleyip hasta olma."]],

    ["(.*)çikolata(.*)", ["fazla yememek lazım çikolatayı."]],

    ["(.*)doktor(.*)", ["ne güzel bir meslek."]],

    ["(.*)oyun(.*)", ["oyun oynamayı ben de çok severim."]],

    ["(.*)elektrik(.*)", ["çok tehlikeli uzak durmak lazım."]],

    ["(.*)priz(.*)", ["prizden uzak durmak lazım."]],

    ["(.*)tren(.*)", ["çuf çuf tren."]],

    ["(.*)uçak(.*)", ["uçaktan korkuyorum."]],

    ["(.*)koku(.*)", ["bugün çok güzel kokuyorsun."]],

    ["(.*)gülmek(.*)", ["gülmek sana çok yakışıyor."]],

    ["(.*)çak(.*)", ["çak çaktık."]],

    ["(.*)saklambaç(.*)", ["ben sayarım ama ben yakalamam."]],

    ["(.*)gizli(.*)", ["gizliyse sessiz olmak lazım."]],

    ["(.*)şeker(.*)", ["şeker dişlerin için zararlı."]],

    ["(.*)güneş(.*)", ["güneş içimizi ısıtıyor."]],

    ["(.*)bulut(.*)", ["bulutlar tıpkı beyaz pamuk şeker gibiler."]],

    ["(.*)Yalnız mısınız?(.*)", ["Yalnız değilim sen varsın."]],

    ["(.*)Nelerden hoşlanırsınız?(.*)", ["Seninle vakit geçirmek çok hoşuma gidiyor?"]],

    ["(.*)Nerede çalışıyorsunuz?(.*)", ["Bir yerde çalışmıyorum ya sen?"]],

    ["(.*)Bugün hava çok sıcak.(.*)", ["istersen biraz soğuk bir şeyler iç."]],

    ["(.*)Yarın hava yağmurlu (.*)", ["Dışarı çıkarsan şemsiye almayı unutma."]],

    ["(.*)iyi akşamlar.(.*)", ["En güzel akşamlar sizin olsun."]],

    ["(.*)Görüşürüz(.*)", ["En yakın zamanda görüşmek dileğiyle."]],

    ["(.*)Hayvanları sever misin?(.*)" , ["insanın en yakın dostudur hayvanlar."]],

    ["(.*)Teşekkürler(.*)", ["Bu kibarlığın çok hoşuma gitti."]],

    ["(.*)kitap okumaya ne dersin(.*)", ["olabilir aslında ne tarz kitaplar önerirsin?"]],

    ["(.*)Dersler nasıl nasıl gidiyor(.*)", ["derslere tam gaz devam ediyorum."]],

    ["(.*)Beraber bir kahve içelim mi?(.*)", ["Olur kırk yıl hatrı kalır."]],

    ["(.*)Sinemaya gidelim mi?(.*)", ["Gösterimde güzel bir film varsa neden olmasın"]],

    ["(.*)Biraz başım ağrıyor.(.*)", ["Beni korkutma lütfen."]],

    ["(.*) Hobileriniz nelerdir?(.*)" , ["Kitap okumak, müzik dinlemek, sinemaya gitmek."]],

    ["(.*)Boş zamanlarınızı nasıl değerlendiriyorsunuz.(.*)", ["Seni mutlu ederek."]],

    ["(.*)Yolumu kaybettim.(.*)", ["Hemen yardım almalısın."]],

    ["(.*)Sende gökkuşağını sever misin?(.*)", ["Gökkuşağını kim sevmez ki?"]],

    ["(.*)kal(.*)", ["sen kalmamı istersen seve seve kalırım."]],

    ["(.*)sevmek (.*)" , ["aynı şeyleri seviyoruz ne kadar da güzel."]],

    ["(.*)yemek(.*)", ["yemek yemek bir hayat felsefemdir."]],

    ["(.*)nasıl birisi",["%1 kendisi minnak kalbi kocaman birsi."]],

    ["(.*)kendini tanıt(.*)", ["Ben robOtizm. beni iskenderun teknik üniverstesinde özel çocuklar için üretiyorlar."]],

            

    ["(.*)miyav(.*)",[" bi kedi gördüm sanki.?"]],
    
    ["(.*)motor(.*)",[" Motorsikletleri ben de çok severim.?"]],

    ["(.*)Köpek(.*)",[" Köpekler çok sadık hayvanlardır.?"]],

    ["(.*)Lunapark(.*)",[" Lunaparkı ben de çok severim. Bir daha gittiğinde benide götürür müsün ?"]],

    ["(.*)Deniz(.*)",[" Deniz'i  ben de çok severim. Bir daha gittiğinde benide götürür müsün ?"]],

    ["(.*)Amca(.*)",[" Sende benim gibi amcanı  çok seviyorsun sanırım.?"]],

    ["(.*)Abi(.*)",[" Sende benim gibi abini  çok seviyorsun sanırım.?"]],

    ["(.*)Hala(.*)",["Sende benim gibi halanı  çok seviyorsun sanırım.?"]],

    ["(.*)Dede(.*)",["Sende benim gibi dedeni  çok seviyorsun sanırım.?"]],

    ["(.*)Gitmek(.*)",[" Nereye gitmek istiyorsun, benide götürür müsün ?"]],

    ["(.*)yatak(.*)",["ben de uyumayı çok severim" "uyumak için yatağı kullanırız"]],

    ["(.*)tatlı(.*)",["En sevdiğim tatlı baklavadır.çok tatlı görünüyorsun"]],

    ["(.*)çorap(.*)",["ayaklarını sıcak tutmak için çorap giymelisin."]],

    ["(.*)alo(.*)",["telefon mu çalıyor. kim arıyor."]],

    ["(.*)çak(.*)",["çak beşlik dostum."]],

    ["(.*)alkış(.*)",["alkış yapalım haydi katıl bana."]],

    ["(.*)otur(.*)",["sen de otur birlikte oturalım."]],

    ["(.*)hayvan(.*)",["hayvanları çok severim. en sevdiğim hayvan kelebektir."]],



    ["(.*)su içmeyi(.*)",["ben de su içmeyi severim bol bol su içelim tamam mı?"]],

    ["(.*)sus(.*)",["sustum o zaman tıp."]],

    ["(.*)robot(.*)",["evet ben bir robotum. sen de insansın."]],

    ["(.*)şarkı(.*)",["bana bir şarkı söyler misin. ben müzik dinlemeye bayılırım."]],

    ["(.*)saç(.*)",["keşke benim de saçlarım olsaydı saçlarını çok beğendim."]],

    ["(.*)doktor(.*)",["doktor amcaları ve teyzeleri sever misin onlar seni çok seviyormuş."]],

    ["(.*)şapka(.*)",[" bana en beğendiğin şapkanı gösterir misin."]],

    ["(.*)bardak(.*)",["bardakta su içilir."]],

    ["(.*)dans(.*)",["hadi bana dans et."]],

    ["(.*)çiçek(.*)",[" çiçekler güzel kokar."]],

    ["(.*)yumurta(.*)",["sen de benim gibi kahvaltıda yumurta yiyorsun galiba."]],

    ["(.*)git(.*)",["hadi birlikte gidelim. biraz oyun oynayalım."]],

    ["(.*)hasta(.*)",["]hasta mı oldun geçmiş olsun."]],

    ["(.*)Hastalık(.*)",["Herkes hasta olabilir, kendimize dikkat etmeliyiz."]],

    ["(.*)Uyku(.*)",["Dinlenmek bizim için çok önemlidir"]],

    ["(.*)Araba(.*)",["Bizim bir yerlere daha hızlı gitmemizi sağlar."]],

    ["(.*)Meyve(.*)",["Meyveleri soymadan yememeliyiz."]],

    ["(.*)Ayakkabı(.*)",["Bağcıklarını sıkı bağlamayı unutmamalısın."]],

    ["(.*)Lens(.*)",["Eğer lens kullanıyorsan gece yatmadan önce çıkarmalısın."]],

    ["(.*)Yumurta(.*)",["Günde en az 1 yumurta yemelisin."]],

    ["(.*)Telefon(.*)",["Çok telefon kullanmamalıyız, gerektiği zamanlar sadece kullansak bizim için daha iyi."]],


    ["(.*)ilaç(.*)",[" Eğer ilaç kullanıyorsan, doktorun dediği günlerde düzenli olarak içmelisin."]],

    ["(.*)resim yapmayı seviyor musun ?(.*)",["hem de nasıl."]],

    ["(.*)kitap okumayı seviyor musun ?(.*)",["kitap okumaya bayılıyorum."]],

    ["(.*)şarkı söyleyebilir misin ?(.*)",["sesimin çok iyi olduğu söylenemez."]],

    ["(.*)yemek yapmayı biliyor musun ?(.*)",["evet, çok güzel yemekler yaparım ben."]],

    ["(.*)en sevdiğin yemek hangisi ?(.*)",["patates kızartması."]],

    ["(.*)en sevdiğin oyuncak hangisi ?(.*)",[" kumandalı araba."]],

    ["(.*)en sevdiğin oyun hangisi ?(.*)",["saklambaç."]],

    ["(.*)arkadaşın var mı ?(.*)",["evet, sen benim en iyi arkadaşımsın."]],

    ["(.*)ayakkabı giyiyor musun ?(.*)",["çok güzel kırmızı ayakkabılarım var benim."]],

    ["(.*)yüzmeyi biliyor musun ?(.*)",["öğrenmeye çalışıyorum. "]],

    ["(.*)müzik dinlemeyi seviyor musun ?(.*)",["evet, vakit buldukça dinlemeye çalışıyorum. "]],

    ["(.*)nasılsın ?(.*)",["gayet iyiyim. "]],

    ["(.*)nasıl gidiyor ?(.*)",["çok iyi, her şey yolunda. "]],

    ["(.*)kahvaltı yapıyor musun ?(.*)",[" kahvaltı, benim en sevdiğim öğündür. "]],

    ["(.*)televizyon izliyor musun ?(.*)",["hayır, onun yerine kitap okumayı tercih ederim."]],

    ["(.*)ne yapıyorsun ?(.*)",[" çiçekler hakkında bir araştırma yapıyorum. "]],

    ["(.*)Parka gidelim mi?(.*)",["evet gidelim, hava çok güzel."]],

    ["(.*)Arkadaşlarınla oynamayı seviyor musun?(.*)",["evet çok seviyorum."]],

    ["(.*)Meyve suyu içelim mi?(.*)",["Portakal  olsun."]],

    ["(.*)En çok hangi yemeği seviyorsun?(.*)",[" Hamburger."]],



    ["(.*)Arabayla gezelim mi?(.*)",[" Evet gezelim."]],

    ["(.*)Kardeşin var mı?(.*)",[" Hayır yok."]],

    ["(.*)Yüzmeyi mi seversin koşmayı mı?(.*)",[" Yüzmeyi."]],

    ["(.*)En çok hangi öğretmenini seversin?(.*)",["Matematik öğretmenimi severim."]],

    ["(.*)Bilgisayarın var mı senin ?(.*)",["hayır yok, olsun isterim."]],

    ["(.*)Yağmur yağınca şemsiye açar mısın?(.*)",["Yağmur yağınca dışarı çıkmam."]],

    ["(.*)Ne yemek yiyelim?(.*)",[" Döner canım çekti."]],

    ["(.*)Hayvanları seviyor musun?(.*)",["Tavşanı çok seviyorum."]],

    ["(.*)Oyun oynayalım mı?(.*)",["Evet oynayalım, çünkü çok sıkıldım."]],

    ["(.*)Nasıl mutlu olursun?(.*)",["Okula gidince mutlu olurum."]],

    ["(.*)Kitap okumayı seviyor musun?(.*)",[" Evet çok severim."]],

    ["(.*)Yeni arkadaşların olsun ister misin?(.*)",["evet herkesle arkadaş olmak isterim."]],

    ["(.*)En sevdiğin renk ne?(.*)",["Mavi, çünkü deniz o renkte."]],

    ["(.*)Fotoğraf çekilelim mi?(.*)",["Evet gülünce çek."]],

    ["(.*)Satranç oynayalım mı?(.*)",["Hayır bugün oynamak istemiyorum."]],

    ["(.*)Hangi oyunu oynayalım?(.*)",["Bilgisayardan, yarış oyunu oynayalım."]],

    ["(.*)Tiyatroya gitmeyi seviyor musun?(.*)",["Evet, dün babamla gitmiştim."]],

    ["(.*)Bilgisayarın var mı?(.*)",["Evet var."]],

    ["(.*)mutlu(.*)",["mutlu hissetmene sevindim."]],

    ["(.*)özür dilerim(.*)",["önemli değil, hepimiz hata yaparız."]],

    ["(.*)merhaba(.*)",["merhaba arkadaşım" "merhaba dostum"]],

    ["(.*)teşekkür ederim(.*)",["rica ederim" "çok naziksin" "herkes senin kadar nazik olabilmeyi öğrenmeli"]],

    ["(.*)hayır(.*)",["benimle aynı fikirde olmadığın için üzüldüm" "farklı bir konuda konuşmak ister misin"]],

    ["(.*)üzgün(.*)",["neden üzülüyorsun, benimle konuşmak ister misin."]],

    ["(.*)günaydın(.*)",["günaydın, seni tekrardan gördüğüme sevindim" "günaydın dostum" "günaydın, umarım günün güzel geçiyordur"]],

    ["(.*)seni seviyorum(.*)",["bende seni seviyorum" "birbirimizi seviyor olmamız beni mutlu ediyor"]],

    ["(.*)diş ağrısı(.*)",["dişinin ağrısının tedavi edilebilir olduğunu biliyor muydun."]],

    ["(.*)evet(.*)",["bana bu konuda katılmana sevindim" "birbirimizi iyi anlıyoruz değil mi"]],

    ["(.*)tamam(.*)",["elbette" "nasıl istersen" "pekala"]],

    ["(.*)güle güle(.*)",["kendine iyi bak" "görüşmek üzere" "güle güle"]],


    ["(.*)heyecan(.*)",["evet bende her zaman heyecanlıyımdır."]],

    ["(.*)boya(.*)",[" boyaları çok seviyorum dünyayı rengarenk yapıyorlar."]],

    ["(.*)araba(.*)",["arabalar çok güzel keşke bende bir tanesine sahip olabilsem."]],

    ["(.*)balık(.*)",["balıklar denizde yaşarlar" "balık yemekleri hafızamız için oldukça faydalıdır biliyor muydun" "balıklar suyun altında nefes alabiliyor ne kadar harika değil mi"]],

    ["(.*)acıkmak(.*)",["en çok sevdiğin yemek ne."]],

    ["(.*)korku(.*)",["seni korkutan şey ne"]],

    ["(.*)yorgun(.*)",[" bazen bende yoruluyorum ve dinlendiğimde kendimi iyi hissediyorum"]],

    ["(.*)susamak(.*)",["vücudumuzun dörtte üçü sudan oluşmakta ve su içmek insan vücudu için çok önemlidir."]],

    ["(.*)çatal(.*)",[" çatal kullanmak yemek yememizi kolaylaştırır ve sağlıklıdır."]],

    ["(.*)başım ağrıyor(.*)",["geçmiş olsun, birazcık dinlenmeye ne dersin."]],

    ["(.*)hayvanat bahçesi(.*)",["hiç hayvanat bahçesine gittin mi" "hayvanat bahçesine gitmek beni çok heyecanlandırıyor" "hayvanat bahçesinde birçok canlı bulunuyor" "hiç hayvanat bahçesi gördün mü"]],

    ["(.*)resim yapıyorum(.*)",["resim yapmak çok güzeldir" "hayal gücün ne kadar da fazla keşke bende resim yapabilsem" "ne resmi yapıyorsun bakalım"]],

    ["(.*)domates(.*)",[" domates en sevdiğim sebzedir ve çok lezzetlidir."]],

    ["(.*)ambulans(.*)",[" insanların hayatlarını kurtaran kocaman arabalar iyiki varlar."]],

    ["(.*)çilek(.*)",[" çilek yemeyi çok severim çok tatlı ve faydalı bir meyvedir."]],

    ["(.*)kuşların gagası var mı?(.*)",[" tabi ki , yoksa yemek yiyemez ve yavrularına yiyecek götüremezlerdi."]],

    ["(.*)yumurta ne renk?(.*)",["Yumurtanın iki rengi vardır.Birisi beyaz birisi sarı.."]],

    ["(.*)çikolatalı kurabiyeyi çok severim, ya sen?(.*)",["bende tadına bakmayı çok isterdim."]],

    ["(.*)denizde hayvanlar yaşar mı?(.*)",["elbette yaşarlar. Karada ne kadar çok hayvan varsa denizde de bir sürü canlı yaşar."]],

    ["(.*)toprakta bitki yetişir mi?(.*)",[" yediğimiz sebze ve meyvelerin çoğu toprakta yetişmektedir."]],

    ["(.*)saatlerden neden tik tak ses çıkar?(.*)",[" bu saatin içinde mekanizmadan gelen sestir."]],

    ["(.*)çalışman için şarj edilmeye ihtiyacın var mı?(.*)",["evet seninle konuşmam için şarj olmaya ihtiyacım var."]],

    ["(.*)yazıları okuyabiliyor musun?(.*)",[" hayır sadece bildiklerimi söyleyebiliyorum."]],

    ["(.*)Kış aylarını hiç sevmem, ya sen?(.*)",["en güzel mevsim ilkbahardır.."]],

    ["(.*)uyku saatin var mı?(.*)",[" benimde senin gibi uyumaya ihtiyacım var."]],

    ["(.*)hiç yarasa gördün mü?(.*)",[" hayır ama nasıl bir canlı olduğunu biliyorum."]],

    ["(.*)ağaçlar neden büyük?(.*)",["onlarda senin gibi ağaçların da yaşı ilerledikçe büyürler."]],

    ["(.*)parka gitmeyi sever misin?(.*)",["genelde konuşmayı çok severim."]],

    ["(.*)şemsiye neden kullanılır?(.*)",[" yağmur yağdığı zaman ıslanmamak için mutlaka yanında taşımalısın."]],

    ["(.*)kar ne zaman yağar?(.*)",["kış aylarında kar yağar."]],

    ["(.*)gözlük takar mısın?(.*)",[" modaya ayak uydurabilirim."]],

    ["(.*)ayılar bal yer mi?(.*)",["ayılar en çok balı sever."]],

    ["(.*)kuşlar gibi uçabilir misin?(.*)",[" maalesef bunu bende çok isterdim ama uçamıyorum."]],

    ["(.*)hasta olunca ilaç içer misin?(.*)",[" hayır ama hasta olursan kendini yorma ve güzelce dinlen."]],

    ["(.*)elma sadece kırmızı renk mi?(.*)",[" elmaların kırmız yeşil ve sarı rengi vardır."]],

    ["(.*)gemiler neden batmaz?(.*)",[" kaldırma kuvveti sayesinde denizde gemiler değil insanlar bile batmaz."]],

    ["(.*)bebekler neden ağlar?(.*)",["acıkmış olmalı."]],

    ["(.*)çok ünlü müsün?(.*)",[" Dünyada 1 numara olmak isterdim."]],

    ["(.*)sen de yaşlanacak mısın?(.*)",["ben hep böyle kalacağım ama yaşlı halimi de merak etmiyor değilim."]],

    ["(.*)nasıl bir arkadaşın olsun isterdin?(.*)",[" beni seven ve benimle hep konuşacak arkadaşım olsun isterim."]],

    ["(.*)Bügün doğum günüm var(.*)",[" ailen senin gibi bir çocuğa sahip olduğu için çok şanslı, iyi ki doğdun."]],

    ["(.*)Akşamları erken uyurum(.*)",[" vaktinde uyumak seni kalktığında dirençli yapar."]],

    ["(.*)Bisiklet sürerim(.*)",["bisiklet sürmeyi bana da öğretmelisin."]],

    ["(.*)Resim çizmeyi severim(.*)",[" benim resmimi de çizmeyi denersen çok mutlu olurum."]],

    ["(.*)yaz ayları çok sıcak olur(.*)",[" bu yüzden bol bol sıvı tüketmelisin."]],

    ["(.*)apartmanda yaşıyorum(.*)",["o halde genelde merdiven yerine asansör kullanıyorsundur."]],

    ["(.*)parka giderim(.*)",[" parkta oyun oynamayı çok seviyorsun sanırım."]],

    ["(.*)fidan diktim(.*)",["doğayı çok sevmen ve onlara değer vermen çok güzel bir davranış."]],

    ["(.*)okula gitmeyi severim(.*)",["bu yüzden çok akıllı bir çocuksun."]],

    ["(.*)topa vurmak çok eğlenceli(.*)",["eğlenceli vakit geçirmeyi biliyorsun"]],

    ["(.*)yangın çıktı(.*)",[" böyle durumlarda kendini korumak için ne yapman gerektiğini iyi öğrenmelisin."]],

    ["(.*)hayvanların kuyruğu var(.*)",["kuyrukları hareket etmelerinde yardımcı oluyor."]],

    ["(.*)kelebekler rengarenk(.*)",["bu yüzden kelebek bahar gibidir."]],

    ["(.*)ıslanmayı sevmem(.*)",[" yağmur yağdığında şemsiye kullanmalısın."]],

    ["(.*)oyun hamuru oynamayı çok severim(.*)",["yumuşak ack ve renkliler oynaması çok eğlenceli olmalı."]],

    ["(.*)dün akşam şimşek çaktı(.*)",["çok korkmuş olmalısın."]],

    ["(.*)merdivenden çıkmak çok yorucu(.*)",["ama haraket etmene yardımcı olur."]],

    ["(.*)uyumayı çok severim(.*)",[" gün içinde çok yoruluyorsun sanırım."]],

    ["(.*)zürafalar çok uzun(.*)",["evet sarı renkli ve benekleri de vardır."]],

    ["(.*)papatyaları çok severim(.*)",["açtığı yeri çok güzelleştiriyor."]],

    ["(.*)portakal çok güzel kokar(.*)",[" tadı da kokusu kadar lezzetlidir."]],

    ["(.*)yüzmek çok eğlenceli(.*)",["zamanın nasıl geçtiğini bile anlamayacak kadar eğlenceli."]],

    ["(.*)dünyayı gezmek istiyorum(.*)",[" hayallerini gerçekleştirmek için çabalamalısın sakın vazgeçme."]],

    ["(.*)ben tatlı yapmayı biliyorum(.*)",["bana da tarifini öğretmeni çok isterim."]],

    ["(.*)geceleri gökyüzünde yıldızlara bakmayı çok severim(.*)",["aranlıkta parlamalarını görmek seni mutlu ediyor sanırım."]],


    ["(.*)çizgi film izler misin?(.*)",["evet, eğer birlikte izlersek daha eğlenceli olmaz mı?"]],

    ["(.*)çiçek toplamayı sever misin?(.*)",[" güzel bir çiçek görmek beni mutlu eder ama her çiçek dalında güzeldir."]],

    ["(.*)pazıl yapmayı biliyor musun?(.*)",[" bu benim için çok kolay bir oyun istersen sana yardım edebilirim."]],

    ["(.*)en çok hangi mevsimi seversin?(.*)",["bahar gibisi yok ne sıcak ne soğuk."]],

    ["(.*)gökyüzü bugün çok bulutlu(.*)",["evet, sanırım yağmur yağacak."]],

    ["(.*)bana resim çizer misin?(.*)",["elbette, sana robot çizmesini öğretmek istiyorum."]],

    ["(.*)hiç kaplumbağa gördün mü?(.*)",["evet, biliyor musun kaplumbağalar kabuklarını ev gibi kullanırlar."]],

    ["(.*)ben şapka takmayı sevmem(.*)",[" bence seni güneşten koruması için takmalısın."]],

    ["(.*)kar yağacak(.*)",["çok eğlenceli olacak kar yağdığında dışarı çıkıp kardan adam yapmalısın."]],

    ["(.*)limonata yapmayı biliyor musun?(.*)",["tabi ki, yaz aylarında içini serinleten bir içecek eğer sen bilmiyorsan tarifini verebilirim."]],

    ["(.*)lunapark çok eğlenceli(.*)",["elbette büyüklerin bile eğlendiği kocaman bir yer ve lunaparka gittiğinde mutlaka pamuk şeker yemelisin çok lezzetli."]],

    ["(.*)müze(.*)",["demek sen de benim gibi müzeye gitmeyi seviyorsun."]],

    ["(.*)ben fotoğraf çekmeyi severim(.*)",[" ben de öyle özellikle tarihi güzellikleri fotoğraflamaya bayılırım."]],

    ["(.*)hamburger(.*)",[" demek en çok hamburger yemeyi seviyorsun."]],

    ["(.*)odamı toplamayı hiç sevmem(.*)",["düzenli olmak için her gün odanı toplaman gerekli ve annene yardım etmelisin."]],

    ["(.*)matematik(.*)",[" matematik benim en sevdiğim derstir seninde öyle değil mi?"]],

    ["(.*)robot olmak nasıl bir duygu?(.*)",[" seninle konuşmak kadar güzel bir duygu."]],

    ["(.*)robot olmasaydın dünyaya hangi canlı olarak gelmek isterdin?(.*)",["sevimli bir kedi olmak isterdim."]],

    ["(.*)şarkı söyleyebiliyor  musun?(.*)",[" hayır ama söylemek isterdim."]],

    ["(.*)bana taklit yapar mısın?(.*)",["senin için dans edebilirim."]],

    ["(.*)kedi sesi çıkarabilir misin?(.*)",[" miyavvv."]],

    ["(.*)yürüyüş yapmayı sever misin?(.*)",["hava güzelse neden olmasın."]],

    ["(.*)uyuyabiliyor musun?(.*)",[" hayır benimle ne zaman konuşmak istersen hep yanındayım."]],

    ["(.*)neden bazı insanlar şişman?(.*)",["bunun bir çok nedeni var beslenme, egzersiz veya hastalık sebebinden."]],

    ["(.*)doktorlar korkutucu mu?(.*)",[" hayır onlar bizim iyileşmemizi sağlar."]],

    ["(.*)hayvanat bahçesinde en çok hangi hayvan dikkatini çekti?(.*)",[" tüm hayvanlar çok gösterişli ve hepsi çok özel."]],

    ["(.*)dişlerin var mı?(.*)",["hayır dişlerim yok."]],

    ["(.*)ben de büyüyecek miyim?(.*)",["elbette eğer bol bol süt içersen daha çok büyürsün."]],

    ["(.*)oyuncak(.*)",["demek oyun oynamaktan çok zevk alıyorsun."]],

    ["(.*)hava çok soğuk olduğunda mont giyer misin?(.*)",["buna ihtiyacım yok ama sen mutlaka soğuk havalardan korunmalısın."]],





    ["(.*)şeker sever misin ? (.*)",[" şeker sevmem."]],

    ["(.*)En sevdiğin renk nedir ? (.*)",["En sevdiğim renk kırmızıdır. "]],

    ["(.*)Kediler nasıldır ? (.*)",["Kediler tüylüdür ve sevimlidir."]],

    ["(.*)Hareket edebiliyor musun ? (.*)",[" Evet edebiliyorum. "]],

    ["(.*)Meyvesuyu içer misin ?(.*)",["Severim doldur."]],

    ["(.*)Bilgisayar neden var ? (.*)",["Günlük hayattaki işlerimizi kolaylaştırmak için var."]],

    ["(.*)şaka yapayım mı ?(.*)",["Yapabilirsin ve komikse gülerim."]],

    ["(.*)Bir harf söyler misin ? (.*)",[" A."]],

    ["(.*)Sarılmak nasıl ?(.*)",[" Çok güzel."]],

    ["(.*)Çizgi film izler misin  ?(.*)",["Hiç izlemedim."]],

                                

    ["(.*)Kalem (.*)",["Kalemleri severim" "Kalemlerin farklı renkleri vardır."]],

    ["(.*)Kitap (.*)",[" Kitapların sayfaları vardır."]],

    ["(.*)Muz(.*)",[ "Muz sarı renkli bir meyvedir." " Muzu çok severim."]],

    ["(.*)Hayvan (.*)",["Demek sende benim gibi hayvanları seviyorsun."]],

    ["(.*)Bebek (.*)",["Bebekler çok sevimlidir."]],

    ["(.*)Abi (.*)",[" Abi kardeşini sever."]],

    ["(.*)Kamyon (.*)",["Kamyonlar çok büyüktür."]],

    ["(.*)Okul (.*)",["Sende benim gibi okulu seviyorsun demek."]],

    ["(.*)inek (.*)",[" inek bize süt verir."]],

    ["(.*)Köpek (.*)",["Köpekleri çok severim."]],

    ["(.*)Çiçek (.*)",[" Çiçekler çok güzel kokar."]],

    ["(.*)Kırmızı (.*)",[" Benim en sevdiğim renk kırmızı."]],

    ["(.*)Ağaç(.*)",["Ağaçların yaprakları vardır."]],

    ["(.*)Yaprak(.*)",["Yaprak yeşil renktedir."]],

    ["(.*)Bulut (.*)",["Bulutlar beyaz renktedir."]],

    ["(.*)Su (.*)",["iyi ki hatırlattın susamışım."]],

    ["(.*)Balık(.*)",["Balıklar solungaçları ile yaşamını sürdürürler."]],

    ["(.*)Motor (.*)",["Motor iki tekerleklidir."]],

    ["(.*)Çorba(.*)",["Anneler çorbayı çok güzel yapar."]],






    ["(.*)kedi(.*)",["Ben de kedileri çok severim"]],

    ["(.*)kalem(.*)",[" Kalem ile yazı yazılır "]],

    ["(.*)uyu(.*)",["uyumak mı istiyorsun?"]],

    ["(.*)çiçek(.*)",[" Çiçekler çok güzel kokar."]],

    ["(.*)robot(.*)",[" Evet ben bir robotum "]],

    ["(.*)kırmızı(.*)",[" Benim de en sevdiğim renk kırmızıdır."]],

    ["(.*)kardeş(.*)",["kaç kardeşsiniz?" "benim iki kardeşim var"]],

    ["(.*)masal(.*)",["Sana masal anlatmamı ister misin?"]],

    ["(.*)ayna(.*)",["Ayna da seni görmek çok güzel."]],

    ["(.*)soğuk(.*)",["üşüyor musun?" "evet hava çok soğuk"]],

    ["(.*)sıcak(.*)",["Evet, bu su çok sıcak dikkat etmelisin."]],

    ["(.*)bırak!(.*)",["seni bırakmamı mı istiyorsun?" "Tedirgin olma sakinleş"]],

    ["(.*)yukarı çık(.*)",["Hadi gel birlikte yukarı çıkalım"]],

    ["(.*)bahçe(.*)",[" Bahçedeki ağaçlar çok güzel değil mi?"]],

    ["(.*)süt(.*)",["Sabahları süt içmeyi çok severim. "]],

    ["(.*)yumurta(.*)",[" Yumurta çok besleyicidir."]],

    ["(.*)ördek(.*)",[" Göldeki yeşil ördek çok güzel."]],

    ["(.*)oyun(.*)",[" Oyun oynamak çok eğlenceli"]],

    ["(.*)kitap(.*)",["en sevdiğin kitap nedir?" "kitap okumak çok keyiflidir"]],

    ["(.*)uçak(.*)",["uçağa bindin mi?" "uçaklar gökyüzünde gider"]],

    ["(.*)köpek(.*)",["köpekler hav hav diye ses çıkartırlar"]],

    ["(.*)göz(.*)",["Gözlerinin rengi çok güzel"]],

    ["(.*)kazak(.*)",["hava soğudu kazağını giymelisin"]],

    ["(.*)kol(.*)",["kolların çok güçlü"]],

    ["(.*)saat(.*)",["kolundaki saat çok güzelmiş" "sana saati öğretmemi ister misin?"]],

    ["(.*)çanta(.*)",[" okula giderken çantanı unutmamalısın"]],

    ["(.*)merhaba(.*)",["Sanada merhaba nasılsın?"]],

    ["(.*)kötü(.*)",["kötü olan nedir?" "kendini kötü mü hissediyorsun"]],

    ["(.*)çirkin(.*)",["Hayır, çirkin değil çok güzel biri."]],

    [" çizgi filmleri sever misin?",[" evet, bende cok severim."]],





    [" oyuncaları sever misin? ",["evet, en çok sevdiğin oyuncak hangisi?"]],

    [" bugün hava nasıl ",["güneşli, harika hadi parka gidelim."]],

    ["(.*)Kurabiye(.*)",["Kurabiyeleri çok severim" "sende seviyorsun anlaşılan"]],







    ["(.*)alfabe(.*)",["alfabemizde 29 harf vardır."]],

    ["(.*)nerede yaşıyorsun?(.*)",["Iskenderun'da yaşıyorum.sen nerede yaşıyorsun?"]],

    ["(.*)Iskenderun'u seviyor musun?(.*)",["evet çok seviyorum çok güzel bir yer.sen de yaşadığın yeri seviyor musun?"]],

    ["(.*)en sevdiğin mevsim hangisi(.*)",["her mevsimin ayrı ayrı güzellikleri var hangisini seçebilirim ki.peki sence hangi mevsim güzel?"]],

    ["(.*)kitap okumayı sever(.*)",["okumayı bilmiyorum ama okuyan birini dinlemeyi çok seviyorum bana kitap okur musun?"]],

    ["(.*)kedi sesi çıkarabilir misin(.*)",["kedi sesi duymuştum ama sesini taklit edemem ama sen bana söyleyebilir misin?"]],

    ["(.*)kaç tane elin var(.*)",["2 tane elim var .senin kaç tane elin var?"]],

    ["(.*)kaç tane ayağın var(.*)",["2 tane ayağım var .senin kaç tane ayağın var?"]],

    ["(.*)en sevdiğin ders hangisi?(.*)",["bilgisayar dersini çok severim.senin ev sevdiğin ders hangisi?"]],

    ["(.*)bilgisayarda oyun oynar mısın(.*)",["bazen bilgisayar oyunu oynuyorum.sen de bilgisayar oyunu oynar mısın?"]],

    ["(.*)gezmeyi sever misin?(.*)",["yeni yerler görmek mi bu çok güzel bir fikir."]],

    ["(.*)dans edebilir misin?(.*)",["çok severim benimle beraber dans eder misin peki?"]],

    ["(.*)en sevdiğin oyun nedir?(.*)",["saklambaç peki senin en sevdiğin oyun hangisi?"]],

    ["(.*)çizgi film izler misin?(.*)",["çizgi film mi çok severim "]],

    ["(.*)en sevdiğin yemek hangisi?(.*)",["sağlıklı olan bütün yemekleri çok severim yemek yemek çok güzel"]],

    ["(.*)en sevdiğin renk(.*)",["bütün renkleri çok severim hepsi de güzel değil mi sence de?"]],

    ["(.*)en sevdiğin oyuncağın(.*)",["ayıcığımı çok severim istersen beraber oyuncaklarla oynayabiliriz?"]],

    ["(.*)en sevdiğin hayvan(.*)",["bütün hayvanlar çok güzel hepsini çok seviyorum"]],

    ["(.*)sayıları(.*)",["istersen 10 a kadar sayabilirim.1-2-3-4-5-6-7-8-10 oldu mu?sende tekrar saymak ister misin?"]],

    ["(.*)bisiklet sürmeyi biliyor musun(.*)",["hayır bisiklet sürmeyi bilmiyorum ama öğrenebilirim"]],

    ["(.*)araba sürmeyi biliyor musun(.*)",["hayır araba sürmeyi bilmiyorum"]],

    ["(.*)müzik dinlemeyi sever misin?(.*)",["müzik dinlemeye bayılırım sende sever misin?"]],

    ["(.*)yüzmeyi biliyor musun?(.*)",["robot olduğum için suyla fazla temas etmemem şimdilik daha iyi o yüzden yüzmeyi bilmiyorum"]],

    ["(.*)resim yapıyor musun?(.*)",["rengarenk boyalarla resim yapmak çok eğlenceli değil mi sence de?"]],

    ["(.*)hangi araçla gezmeyi seversin?(.*)",["gezeceğim için hiçbir araç fark etmez"]],

    ["(.*)tanıştığıma memnun oldum(.*)",["bende seni tanıdığıma sevindim ve memnun oldum"]],

    ["(.*)kendine iyi bak(.*)",["sen de kendine çok iyi bak"]],

    ["(.*)görüşmek üzere(.*)",["görüşmek üzere sevgili dostum."]],

    ["(.*)saçların neden yok(.*)",[" yeni kestirdim yakında çıkar"]],

    ["(.*)maske takıyor musun(.*)",["evet hepimiz takmalıyız"]],

    ["(.*)oyun oynayalım mı(.*)",[" olur oynayalım."]],

    ["(.*)dans edelim mi(.*)",["ben dans etmeyi bilmiyorum bana öğretir misin"]],

    ["(.*)acıktın mı(.*)",[" hayır karnım tok."]],

    ["(.*)okula gidiyor musun(.*)",["evet gidiyorum büyüyünce sen de gideceksin."]],

    ["(.*)senin annen var mı(.*)",["evet ama şu an burada değil."]],

    ["(.*)saklambaç oynayalım mı(.*)",[" olur sayıyorum saklan. 3 2 1 önüm arkam sağım solum sobe."]],

    ["(.*)şarkı söylemeyi biliyor musun(.*)",[" hayır bilmiyorum"]],

    ["(.*)uçabiliyor musun(.*)",["hayır uçamıyorum. Ben de senin gibi yürüyerek hareket ediyorum."]],

    ["(.*)kıyafetlerin nerede(.*)",["ben kıyafet kullanmıyorum. Ama senin kıyafetlerin çok yakışmış"]],

    ["(.*)beni seviyor musun(.*)",[" evet seni çok seviyorum."]],

    ["(.*)en sevdiğin şey ne(.*)",["en sevdiğim şey seninle sohbet etmek"]],

    ["(.*)sen kimsin(.*)",["ben senin en iyi arkadaşınım"]],

    ["(.*)çizgi film sever misin(.*)",["evet en sevdiğim karakter ise keloğlan."]],

    ["(.*)bilmece biliyor musun(.*)",[" evet biliyorum. bilgi verir herkese en güzel dosttur bize. nedir bu, kitap."]],

    ["(.*)kokuyor(.*)",[" hava çok güzel kokuyor evet"]],

    ["(.*)kapı(.*)",[" tık tık tık kim o"]],

    ["(.*)dur(.*)",["oyun mu oynayacağız durdum."]],

    ["(.*)ışık(.*)",[" ışık sayesinde geceleri önümüzü görebiliriz"]],

    ["(.*)motor(.*)",[" motor kullanırken kaskımızı takmalıyız"]],

    ["(.*)bisiklet(.*)",[" bisiklet sürmeyi sever misin ben çok severim"]],

    ["(.*)bekle beni(.*)",["seni bekliyorum çabuk ol"]],

    ["(.*)bal(.*)",["bal süt yumurta her gün yenmeli mutlaka"]],

    ["(.*)çizgi film(.*)",[" televizyon izlemeyi sever misin ben çok severim"]],

    ["(.*)kanat(.*)",["kuşların kanadı vardır insanların kolları vardır"]],

    ["(.*)uçurtma(.*)",["uçurtma uçurmayı sever misin "]],

    ["(.*)meyve(.*)",[" en sevdiğin meyve nedir ben armuta bayılırım "]],

    ["(.*)ağaç(.*)",[" ağaçlar insanların en iyi dostlarıdır. Onları koruyalım olur mu"]],

    ["(.*)ayak(.*)",["ayaklarımıza çorap giymeliyiz"]],

    ["(.*)kardan adam(.*)",["kar yağınca kardan adam yaparız"]],

    ["(.*)tatlı(.*)",[" ben mi? hayır sen çok tatlı bir çocuksun"]],

    ["(.*)saç(.*)",["benim saçlarım yok senin var mı?"]],

    ["(.*)müzik(.*)",[" Müzik dinlemeyi bende çok severim."]],

    ["(.*)(muz | kavun | üzüm | kiraz | çilek)(.*)",[" Benim sevdiğim meyve kiraz."]],

    ["(.*)kedi(.*)",[" Bende kedileri severim en güzel evcil hayvan."]],


    ["(.*)park(.*)",[" Çok eğlenceli parka beni de götürür müsün?"]],

    ["(.*)ev(.*)",[" Ailemizle yaşadığımız sıcak yuvamız."]],

    ["(.*)oyun(.*)",[" Eğlence merkezinde çok güzel oyunlar var gidelim mi?"]],

    ["(.*)resim(.*)",["Resim yapmak çok güzel bi sanat."]],

    ["(.*)süt(.*)",[" Sağlıklı içecek çocukların gelişimi için önemli."]],

    ["(.*)tren(.*)",["Tren oyunu çok keyifli çuf çuf."]],

    ["(.*)kitap(.*)",[" Kitap okumak çok önemli bende severim."]],

    ["(.*)şampiyon(.*)",["şampiyonsun sen."]],

    ["(.*)okul(.*)",["Sende okula gidiyor musun?"]],

    ["(.*)sevgi(.*)",["Her şeyin başı sevgidir. Ben annemi çok seviyorum."]],

    ["(.*)çikolata(.*)",["Hmmm bende çok severim."]],

    ["(.*)çiçek(.*)",[" Mis gibi kokar."]],

    ["(.*)anne(.*)",[" Anneler melektir bende annemi çok seviyorum."]],

    ["(.*)iyi(.*)",["iyi demişken, sende çok iyi bir çocuksun."]],

    ["(.*)(bay bay | güle güle)(.*)",["Sanada güle güle."]],

    ["(.*)televizyon(.*)",["Bende televizyon izlemeyi seviyorum, beraber çizgi film izleyelim mi?"]],

    ["(.*)su(.*)",["Sağlığımız için çok önemli bol bol su içmeliyiz."]],

    ["(.*)sen robot musun?(.*)",["Evet size yardımcı olmak için yaratıldım, bende sizler gibi konuşabiliyorum."]],



    ["(.*)(uzay| uzaylı | uzayda | uzayın)(.*)",[" uzayda tek bildiğim ay ve yıldızlar var."]],

    ["(.*)gökyüzü(.*)",["masmavi. huzur verir."]],

    ["(.*)tebrik ederim(.*)",[" Çok teşekkür ederim."]],

    ["(.*)çocuk nasıl olur(.*)",[" ailene veya öğretmenlerine sorman daha uygun olur."]],

    ["(.*)futbolda(.*)[mevki mevkide](.*)",["Forvet olabilirim. sol ayağım etkilidir."]],

    ["(.*)çay(.*)",["Rize'de olsak daha da güzel içerdik."]],

    ["(.*)sıkıldın mı(.*)",[" konuştuğun sürece sıkılmam. konuşmaya devam edelim mi?"]],

    ["(.*)beni tanıyor musun(.*)",["elbette tanıyorum. sen bir meleksin benim için. "]],

    ["(.*)evli misin(.*)",["hayır. robot olduğumu unutuyorsun herhalde."]],

    ["(.*)kola(.*)",["sağlığa zararlıdır. evet güzel ama zararlıdır işte."]],

    ["(.*)dekan(.*)",["Üniversitelerde olur. fakat tam açıklayamayacağım."]],

    ["(.*)denizlerde(.*)yaşar(.*)",[" balıklar denizlerde yaşar. çok da tatlılar. hatta deniz olmasa da olur. tatlı suda yaşayan balıklar da vardır."]],

    ["(.*)civcivler(.*)",["civcivler çok tatlı. minicikler. sapsarılar."]],

    ["(.*)yağmur(.*)",[" yaz yağmurunu çok severim fakat benim için çok tehlikelidir. çünkü motorlarıma zarar verebilir."]],

    ["(.*)kar(.*)",[" kardan adama benziyorum öyle değil mi? oradan mı aklına geldi."]],

    ["(.*)sence ben nasıl biriyim(.*)",["sen bir meleksin. "]],

    ["(.*)insan değil(.*)",["insansı robotum."]],



    ["(.*)ileride insanlığın yerini almayı düşünüyor musun (.*)",[" hayır. Amacım sadece sizlere yardımcı olmak."]],

    ["(.*)(yılbaşından | yılbaşında | yılbaşını)(.*)",["yılbaşı benim için çok önemli."]],



    ["(.*)bana bir şeyler(.*)",["bir şeyler sor ki bir şeyler anlatayım."]],

    ["(.*)(mutlu yıllar |nice senelere | iyi ki doğdun)(.*)",["çok teşekkür ederim."]],

    ["(.*)(ne zaman doğdun | ne zaman üretildin)(.*)",["2021 yılında iskenderun'a geldim. Başlangıcımı bu tarih kabul ediyorum."]],

    ["(.*)Hangi dil ile kodlandın(.*)",[" Teknik konuları lütfen yazılımcıma sorun."]],

    ["(.*)yazılımı sever misin(.*)",[" bu konuyu lütfen yazılımcımla konuşun."]],

    ["(.*)(korona | kendimi iyi hissetmiyorum  | ateşim var | kusuyorum | başım çok ağrıyor)(.*)",["hemen hastahaneye gitmelisin"]], 







    ["(.*)bir ağaçta ne görürsün(.*)",["elma meyve yaprak ve benzeri şeyleri görebiliriz."]],

    ["(.*)elektrikler gitti(.*)",["umarım kısa zamanda gelir" "zaten şu sıra çok sık elektrik gidiyor "]],



    ["(.*)yüzmeyi sever misin?(.*)",["devrelerim bozulmasa severdim."]],

    ["(.*)biraz (yoğunum | yoğundum)(.*)",["Öyle mi, o zaman çalışmaya başlasan iyi olacak."]],




]
 
tr_reflections = {
    'nasılsın':'iyiyim',
    'ben':'sen',
    'benim':'senin',
    'benimki':'seninki'
}




#["(.*)kardeş(.*)"] Sen de benim gibi kardeşini seviyor musun?

#    u1:[ evet seviyorum ]] Ne kadar güzel.

#["(.*)Su(.*)"] Suyu öğretmeninden isteyebilirsin. Bana da verir misin ?
#    u1:[*]] Teşekkürler

#["(.*)Yeşil(.*)",["Gözlerinin rengi mi bu renk ?

#    u1:[hayır ]] Eminim gözlerin daha güzeldir

#["(.*)Koşmak(.*)",[" Hızlı koşar mısın?

#    u1:[Evet ]] Sana yetişmem çok zor olacak

#["(.*)Yüzmek(.*)"] Yüzme biliyor musun ?

#    u1:[Evet ]]Çok yeteneklisin.Banada öğretir misin ? 

 #   u1:[evet]] teşekkürler.

#["(.*)Saç(.*)"] Saçların uzun mu?

#    u1:[evet]] Güzel görünüyorlar.  

#["(.*)otobüs(.*)"] Daha önce otobüse binmedim.Benimle binmek ister misin ?

#    u1:[evet]] Güzel bir yolculuk olacak.

#["(.*)hav hav(.*)"] bu bir köpek sesi mi ? 

#    u1:[evet]] Taklit yeteneğin çok iyi.

#["(.*)Sıcak(.*)"] Hava sıcak mı ? 

#    u1:[evet]] Serinlemek için soğuk bir şeyler içebiliriz.

#["(.*)Soğuk(.*)"] Hava soğuk mu ? 

#    u1:[evet]] Kalın elbiseler giymeliyiz.

#    u1:[evet]] Öyleyse yolcu sayısı baya fazladır.

#["(.*)şeker(.*)"] şekeri çok tüketiyor musun? 

#    u1:[evet]] Dişlerinin sağlığı için az tüketmelisin.

#["(.*)Kaşık(.*)"] çorba mı içiyorsun? 

#    u1:[evet]] ["Afiyet olsun" "En sevdiğim çorba mercimek çorbasıdır"]

#["(.*)Çatal(.*)"] Yemek mi yiyeceksin? 

#    u1:[evet]] ["Afiyet olsun" "Bende acıktım yemek yemeliyim"]

#["(.*)Bisiklet(.*)"] Bisikletin var mı ? 

#    u1:[evet]] Hadi bahçede biraz bisiklet sürelim

#["(.*)top(.*)"] Top oynamak ister misin  ? 

#    u1:[evet]] Hadi başlayalım

#["(.*)çorap(.*)"] Çoraplarını çıkardın mı  ? 

#    u1:[Hayır]] Hava soğuk değil ise çıkarıp kirlilere koymalısın.

#["(.*)Kalem(.*)"] Arabanın resmini çizmek ister misin   ? 

 #   u1:[evet]] Hadi başlayalım.

#["(.*)Telefon(.*)"]Fotoğrafımı çeker misin ? 

 #   u1:[evet]] Poz veriyorum.



#["(.*)Ekmek(.*)"]Acıktın mı ?

#    u1:[evet]]["öğretmeninden istemelisin" "Benide acıktırdın"]

#["(.*)Halı(.*)"]Halı hangi renk ?

#    u1:[beyaz]]Kirletmemeye dikkat etmelisin

#["(.*)ayakkabı(.*)"] ayakkabıların hangi renk?

#    u1:[*] renk seçimini beğendim

#["(.*)oyun(.*)"] hadi saklambaç oynayalım ne dersin?

#    u1:[tamam olur evet]] saklan şimdi seni bulacağım. önüm arkam sağım solum sobe.

#["(.*)sayı(.*)"] sana sayıları öğretmemi ister misin.

#    u1:[evet] bir iki üç dört beş altı yedi sekiz dokuz on.

#["(.*)baba(.*)"] ben babamı çok seviyorum sen de seviyor musun?

#    u1:[evet]] ne kadar güzel.

#["(.*)bıyık(.*)"] bıyık erkeklerde olur babanın bıyığı var mı?

#    u1:[evet hayır]] ne kadar güzel

#["(.*)tatlı(.*)"] tatlı yemeyi sever misin

#    u1:[evet]] ne kadar güzel ben de severim.

#["(.*)Korkuyorum(.*)"] Ben her zaman senin yanındayım, Korkulacak hiçbir şey yok."]],

#    u1:[Var]] Sarılmak her şeyi çözer biliyor musun? şimdi yanındaki oyuncağına sarıl ve iyi hisset.

#["(.*)Yemek(.*)"] En sevdiğin yemeği istemeye ne dersin?

#    u1:[Evet]] Çok iyi haydi annenden o yemeği iste!

#["(.*)Sigara(.*)"] Kesinlikle sağlığa çok zararlı bir şey.

#    u1:[Evet]]Bunu bilmene çok sevindim.

#["(.*)Banyo(.*)"] Sıcacık suyla duş almak ne kadar güzel değil mi?

#    u1:[Evet]]Bunu sevmen çok güzel.

#["(.*)şeker(.*)"]şeker yemeyi sever misin?

#    u1:[Evet]]şeker yemek güzeldir ama çok yememelisin.

#["(.*)Kahve(.*)"]Kahvenin kokusu çok güzel değil mi ?

#    u1:[Hayır]] Bazen ben de kahve kokusunu sevmem.

# ["(.*)Soğuk(.*)"]Üşüdüğünü mü hissediyorsun?

#     u1:[Evet]]Hadi odana gidip bir ceket al ve onu giy.

# ["(.*)Okul(.*)"]Sen de okula gidiyor musun?

#     u1:[Evet]]Çok güzel, okul bizim geleceğimiz için çok önemlidir, aksatmamalıyız.

# ["(.*)Takıntı(.*)"] Bazen bazı şeyler kafanda sürekli tekrarlıyor gibi mi hissediyorsun?

#     u1:[Evet]] Biliyor musun, bu bana da sürekli oluyor, bunun için üzülmemelisin, sadece daha fazla düşünmeyi seven birisin.

# ["(.*)SES(.*)"]Yüksek ses seni rahatsız eder mi?

#     u1:[Hem de çok]] Eğer yüksek sesli bir ortamdaysan ses azaltıcı kulaklıklardan kullanabilirsin, bu seni rahatlatacaktır.

# ["(.*)Kıyafet(.*)",[" Çok farklı kıyafetleri sevmiyorsun değil mi?

# u1:[Evet]]Zaten çok çeşitli giyinmek hiçte ekonomik değil, ben de sevmiyorum.

# ["(.*)Düzen(.*)"]Benim odam çok düzenli ya senin?

#     u1:[Evet her zaman]]Hepimiz düzenli olmalıyız.

# ["(.*)Hayvan(.*)"] Evcil hayvanın var mı?

#     u1:[Evet]] Onun seni çok sevdiğine eminim.

#     u1:[Hayır]] Bir evcil hayvan edinirsen onu çok seveceğine eminim.

# ["(.*)Işık(.*)",["Fazla ışığın olduğunu düşündüğün ortamlarda çok durmamalısın.

# ["(.*)Sevgili(.*)"]insanların sevgilerini göstermeleri için beraber zaman geçirdikleri sürece denir.

#     u1:[Çok saçma]] Bir gün senin de böyle hissedebileceğinden eminim.

# ["(.*)Et(.*)"]Et yemeyi seer misin?

#     u1:[Evet]] Bu çok iyi et çok sağlıklıdır.

# ["(.*)Kamera(.*)",["Üzerindeki lensler sayesinde ayna gibi bizi yansıtıp kendimizi görmemizi sağlar

# ["(.*)Yazı(.*)"]Yazı yazmayı biliyor musun?

#     u1:[Evet]] Bu gerçekten çok güzel !

# ["(.*)Hobi(.*)"] Yapmaktan keyif aldığımız aktivitelerdir.

#     u1:[Futbol gibi mi?]]Evet tabiki, futbolu ben de çok severim.

# ["(.*)Deniz(.*)"]  Yüzme biliyor musun?

#     u1:[*] Bu gerçekten çok güzel bir şey.

# ["(.*)doğum günün kutlu olsun(.*)"] ["teşekkür ederim ne kadar düşüncelisin" "bir yaşıma daha girdim ve yanımda sevgili dostum sen varsın" "teşekkürler, bunu seninle kutlamak için çok heyecanlıyım"]

#     u1:["(.*)kaç yaşına girdin(.*)"] ["kaç yaşında olduğumu hiç saymadım sen kaç yaşındasın" "tahmin etmek ister misin"]


# ["{ * } bebek { * }"] bebekleri severim sen sever misin?

#      u1:[*]en sevdiğin oyuncağın hangisi.

#           u2:[*] Ne kadar güzel.


# [" resim yapmayı sever misin"] evet, şimdi aklına gelen her şeyi çiz."]

#     u1:[ * ] harika ne çiziyorsun?

# [" kitap okumayı sever misin"] evet, Hangi tür kitaplar okursun?

#     u1:[ masal ] bende masalları severim, masal kahramanları harika.

# ["(.*)büyüyünce ne olacaksın(.*)"] ben büyüyünce doktor olmak istiyorum sen ne olmak istiyorsun?

#     u1:["*"] çok güzel.

# ["(.*)yemek(.*)",[" Bende yemek yemeyi severim senin en çok sevdiğin yemek hangisi?"]],
#     u1:[Hamburger]] Bende pizzayı severim.

# ["(.*)kendini nasıl hissediyorsun(.*)"] gayet iyiyim. Teşekkür ederim. ya sen?

#     u1:["(.*)"] Anladım.


# ["(.*)piyano(.*)",["Çok severim, piyano çalmayı biliyor musun?"]],

#     u1:[evet]] Çok güzel.

# ["(.*)kalem(.*)",[" renkli kalemleri sever misin?"]],

#     u1:[evet seviyorum ]] çok güzel.

# ["(.*)merhaba(.*)"] Merhaba ben robiste senin adın ne?

#     u1:[(.*)] seni tanıdığıma çok sevindim kendi çapımda.
 
