import random
import pygame

WIDTH = 800
HEIGHT = 1000

# Oyunun durumları
game_state = "start"  # start, play, gameover

# Kılıç
sword = Actor("sword", center=(WIDTH // 2, HEIGHT // 2))

# Skor ve oyun durum değişkenleri
score = 0.00
sharpness = 10
miss = 5

# Objeler listeleri
woods = []
waters = []

# Zamanlayıcılar
spawn_timer = 0

def draw():
    screen.clear()
    if game_state == "start":
        screen.blit("background", (0, 0))
        screen.draw.text("<FOREST SWORD>", center=(WIDTH // 2, HEIGHT // 2 - 150), fontsize=75, color="orange", owidth=2)
        screen.draw.text("Baslamak icin SPACE'e bas", center=(WIDTH // 2, HEIGHT // 2 + 20), fontsize=40, color="white")
    elif game_state == "play":
        screen.clear()
        screen.blit("background", (0, 0))

        for wood in woods:
            wood.draw()
        for water in waters:
            water.draw()

        sword.draw()

        screen.draw.text(f"Skor: {score:.2f}", (10, 10), fontsize=30, color="yellow")
        screen.draw.text(f"Keskinlik: {sharpness}", (10, 50), fontsize=30, color="lightblue")
        screen.draw.text(f"Iska: {miss}", (10, 90), fontsize=30, color="red")

    elif game_state == "gameover":
        screen.blit("gameover", (WIDTH//2-250, HEIGHT//2-250))
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2 - 50), fontsize=80, color="red", owidth=3)
        screen.draw.text(f"Skorun: {score:.2f}", center=(WIDTH // 2, HEIGHT // 2 + 20), fontsize=50, color="white")
        screen.draw.text("Tekrar baslamak icin SPACE", center=(WIDTH // 2, HEIGHT // 2 + 80), fontsize=40, color="white")

def update():
    global spawn_timer, game_state, miss, score, sharpness

    if game_state != "play":
        return

    # Kılıcı mouse ile takip ettiriyoruz
    sword.pos = pygame.mouse.get_pos()

    # Odun ve su üretimi
    spawn_timer += 1
    if spawn_timer > 60:
        spawn_timer = 0
        spawn_random_object()

    # Odunları hareket ettir
    for wood in woods[:]:
        if wood.direction == "down":
            wood.y += wood.speed
        elif wood.direction == "up":
            wood.y -= wood.speed
        elif wood.direction == "left":
            wood.x -= wood.speed
        elif wood.direction == "right":
            wood.x += wood.speed

        if sword.colliderect(wood) and wood.image == "wood":
            score += sharpness
            wood.image = "wood_broken"
        elif (wood.x < -50 or wood.x > WIDTH + 50 or wood.y < -50 or wood.y > HEIGHT + 50) and wood.image == "wood":
            woods.remove(wood)
            miss -= 1

    # Sularla çarpışma
    for water in waters[:]:
        if sword.colliderect(water) and water.image == "water":
            sharpness += 1
            water.image = "water_splash"

    # En yakın hedefe yönelme
    targets = [obj for obj in woods + waters if obj.image in ["wood", "water"]]
    if targets:
        closest = min(targets, key=lambda t: sword.distance_to(t))
        angle = sword.angle_to(closest)
        sword.angle = angle

    # Kırık odunları ve sıçrayan suları temizle
    for wood in woods[:]:
        if wood.image == "wood_broken":
            wood.timer = getattr(wood, "timer", 30) - 1
            if wood.timer <= 0:
                woods.remove(wood)

    for water in waters[:]:
        if water.image == "water_splash":
            water.timer = getattr(water, "timer", 30) - 1
            if water.timer <= 0:
                waters.remove(water)

    # Oyun bitti mi?
    if miss <= 0:
        game_state = "gameover"

    # Nesne hareketleri
def spawn_random_object():
    global sharpness
    obj_type = random.choice(["wood", "water"])

    if obj_type == "wood":
        direction = random.choice(["down", "up", "left", "right"])
        speed = random.randint(2, 5)

        if direction == "down":
            pos = (random.randint(50, WIDTH - 50), -50)
        elif direction == "up":
            pos = (random.randint(50, WIDTH - 50), HEIGHT + 50)
        elif direction == "left":
            pos = (WIDTH + 50, random.randint(50, HEIGHT - 50))
        else:  # right
            pos = (-50, random.randint(50, HEIGHT - 50))

        wood = Actor("wood", pos=pos)
        wood.direction = direction
        wood.speed = speed
        woods.append(wood)

    else:
        x = random.randint(100, WIDTH - 100)
        y = random.randint(100, HEIGHT - 100)
        water = Actor("water", pos=(x, y))
        water.speed = 0
        waters.append(water)


    for water in waters:
        water.y += water.speed
        if sword.colliderect(water) and water.image == "water":
            sharpness += 1
            water.image = "water_splash"
        elif water.y > HEIGHT:
            waters.remove(water)
        # En yakın hedefi bul (su veya odun)
    targets = [obj for obj in woods + waters if obj.image in ["wood", "water"]]
    if targets:
        closest = min(targets, key=lambda t: sword.distance_to(t))
        angle = sword.angle_to(closest)
        sword.angle = angle
    #Kırıkları temizle
    for wood in woods[:]:
        if wood.image == "wood_broken":
            wood.timer = getattr(wood, "timer", 30) - 1
            if wood.timer <= 0:
                woods.remove(wood)

    for water in waters[:]:
        if water.image == "water_splash":
            water.timer = getattr(water, "timer", 30) - 1
            if water.timer <= 0:
                waters.remove(water)

    # Oyun bitti mi?
    if miss <= 0:
        game_state = "gameover"


def on_key_down(key):
    global game_state, score, sharpness, miss, woods, waters
    if key == keys.SPACE:
        if game_state in ["start", "gameover"]:
            game_state = "play"
            score = 0.00
            sharpness = 10
            miss = 5
            woods = []
            waters = []

# Write your code here :-)
