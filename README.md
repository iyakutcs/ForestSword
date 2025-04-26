# Forest⚔️Sword #
FOREST SWORD nam-ı diğer ormanın kalbinden dövülmüş çelik! Ormanın derinliklerinde, kadim zamanlardan kalma bir koruyucu kılıç yeniden uyanır. Bu silah, ormanın huzurunu tehdit eden lanetli ağaç yaratıklarını yok etmek
için dövülmüştür… Bu kılıç, ormanı istila eden lanetli odun yaratıklarını keserek ormanın dengesini korumakla görevli. Ancak zamanla kılıcın keskinliği azalıyor. Ormanda yer yer beliren su damlaları kılıca hayat ve
güç veriyor.
Python Pgzero ile yazılmış kılıçla odun kesme oyunu. Görevin, kılıcın keskinliğini koruyarak mümkün olduğunca fazla odun kesmek ve ormanın dengesini sağlamak. Fakat dikkat et: Eğer kılıç oduna zamanında müdahale edemezse, ormanın ruhu zarar görüyor (ıska sayın düşüyor) ve nihayetinde görev başarısız oluyor…
## Kod üzerine notlar: ##
* Satır#8: game_state = "start"  # start, play, gameover. // Oyunun 3 farklı durumu var.
* Satır#28: screen.blit("background", (0, 0)) //Verilen konumdaki görüntüyü ekrana çizin.
* Satır#49: screen.draw.text(f"Skorun: {score:.2f}", center=(WIDTH // 2, HEIGHT // 2 + 20), fontsize=50, color="white") //{score:.2f} virgülden sonra 2 basamak. f for float.
* Satır#59: sword.pos = pygame.mouse.get_pos() //# Kılıcı mouse ile takip ettiriyoruz
* Satır$69: if wood.direction == "down": //odunun hareket yönü direction özelliği ile belirleniyor.
* Satır#94: closest = min(targets, key=lambda t: sword.distance_to(t))//targets listesindeki nesneler arasından, sword objesine en yakın olanı buluyor.
* Satır#101: wood.timer = getattr(wood, "timer", 30) - 1. //wood nesnesinin timer adında bir özelliği (değişkeni) var mı diye bakar. Eğer varsa, o değeri alır. Eğer yoksa, varsayılan olarak 30 kullanır.
* Satır#177: def on_key_down(key): ve sonrasında if key == keys.SPACE: //klavyeden tuş okutmak istiyorsak bunu kullanıyoruz. keys.SPACE (Boşluk tuşunun basıldığını algılıyor.)
