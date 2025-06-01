import pygame

# 1. เริ่มต้น Pygame
pygame.init()

# 2. ตั้งค่าหน้าจอ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Tooltip Example")

# 3. กำหนดสี
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GREY = (200, 200, 200)
DARK_GREY = (100, 100, 100)

# 4. กำหนด Font
main_font = pygame.font.Font(None, 36)
tooltip_font = pygame.font.Font(None, 24)

# 5. สร้างองค์ประกอบ UI ที่ต้องการให้มี Tooltip
# ในที่นี้คือปุ่มสี่เหลี่ยมผืนผ้า
button_rect = pygame.Rect(300, 250, 200, 50) # ตำแหน่ง x, y, กว้าง, สูง
button_text = main_font.render("Hover Me", True, WHITE)
button_text_rect = button_text.get_rect(center=button_rect.center)

# ข้อความสำหรับ Tooltip
tooltip_message = "Test"

# 6. ฟังก์ชันสำหรับวาด Tooltip (แยกออกมาเพื่อให้จัดการง่าย)
def draw_tooltip(surface, text, mouse_pos):
    """
    วาด tooltip บน surface ที่กำหนด
    :param surface: surface ที่จะวาด tooltip ลงไป (ปกติคือหน้าจอหลัก)
    :param text: ข้อความสำหรับ tooltip
    :param mouse_pos: ตำแหน่งปัจจุบันของเมาส์ (x, y)
    """
    # สร้าง Surface สำหรับข้อความ Tooltip
    rendered_tooltip = tooltip_font.render(text, True, BLACK) # สีข้อความเป็นสีดำ
    tooltip_rect = rendered_tooltip.get_rect()

    # กำหนดตำแหน่งของ Tooltip (ให้เยื้องจากเมาส์เล็กน้อย)
    # 15, 15 คือ offset เพื่อไม่ให้ tooltip บังเมาส์หรือปุ่ม
    tooltip_rect.topleft = (mouse_pos[0] + 15, mouse_pos[1] + 15)

    x = 20


    # วาดพื้นหลังของ Tooltip (สีขาว) และขอบ (สีแดง)
    # inflate(10, 10) คือการขยายขนาด Rect ออกไปอีก 10px รอบด้าน เพื่อทำเป็น padding ของพื้นหลัง
    pygame.draw.rect(surface, WHITE, tooltip_rect.inflate(x, x))
    pygame.draw.rect(surface, RED, tooltip_rect.inflate(x, x), 2) # 2 คือความหนาของเส้นขอบ

    # วาดข้อความ Tooltip
    surface.blit(rendered_tooltip, tooltip_rect)


# 7. ลูปหลักของเกม
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 8. การวาดภาพบนหน้าจอ
    screen.fill(DARK_GREY) # เติมพื้นหลังด้วยสีเทาเข้ม

    # วาดปุ่ม
    pygame.draw.rect(screen, BLUE, button_rect) # วาดสี่เหลี่ยมสีน้ำเงิน
    screen.blit(button_text, button_text_rect) # วาดข้อความบนปุ่ม

    # 9. ตรรกะของ Tooltip
    mouse_pos = pygame.mouse.get_pos() # รับตำแหน่งปัจจุบันของเมาส์

    # ตรวจสอบว่าเมาส์อยู่เหนือปุ่มหรือไม่
    if button_rect.collidepoint(mouse_pos):
        draw_tooltip(screen, tooltip_message, mouse_pos) # ถ้าอยู่ ให้วาด tooltip

    # 10. อัปเดตหน้าจอ
    pygame.display.flip()

# 11. ออกจาก Pygame
pygame.quit()