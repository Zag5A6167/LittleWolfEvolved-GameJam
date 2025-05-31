import pygame

class CenteredText:
    def __init__(self, text_content, font_size, color=(0, 0, 0), font_name=None, screen_width=800, screen_height=600):
        """
        สร้างวัตถุข้อความที่อยู่กลางจอ.

        Args:
            text_content (str): ข้อความที่ต้องการแสดง
            font_size (int): ขนาดตัวอักษร
            color (tuple): สีของข้อความ (RGB tuple เช่น (255, 255, 255) สำหรับสีขาว). ค่าเริ่มต้นคือสีดำ.
            font_name (str, optional): ชื่อไฟล์ฟอนต์ .ttf (เช่น "font.ttf") ถ้าไม่ระบุ จะใช้ฟอนต์เริ่มต้นของ Pygame.
            screen_width (int): ความกว้างของหน้าจอ Pygame (จำเป็นสำหรับการคำนวณจุดกึ่งกลาง)
            screen_height (int): ความสูงของหน้าจอ Pygame (จำเป็นสำหรับการคำนวณจุดกึ่งกลาง)
        """
        self.text_content = text_content
        self.font_size = font_size
        self.color = color
        self.font_name = font_name
        self.screen_width = screen_width
        self.screen_height = screen_height

        # โหลดฟอนต์ (ต้องเรียก pygame.init() ก่อนใช้งาน Class นี้)
        self.font = pygame.font.Font(self.font_name, self.font_size)

        # สร้าง Surface ของข้อความและ Rect พร้อมจัดกลางทันที
        self._update_surface()

    def _update_surface(self):
        """
        (เมธอดภายใน) สร้าง Surface ของข้อความขึ้นใหม่และปรับขนาด Rect พร้อมจัดกลางจอ.
        จะถูกเรียกอัตโนมัติเมื่อข้อความหรือสีเปลี่ยน.
        """
        self.surface = self.font.render(self.text_content, True, self.color)
        self.rect = self.surface.get_rect()
        # กำหนดให้จุดกึ่งกลางของ Rect อยู่กลางจอเสมอ
        self.rect.center = (self.screen_width // 2, self.screen_height // 2)

    def set_text(self, new_text):
        """เปลี่ยนข้อความที่แสดงและจัดกลางใหม่."""
        if self.text_content != new_text:
            self.text_content = new_text
            self._update_surface()

    def set_color(self, new_color):
        """เปลี่ยนสีของข้อความและจัดกลางใหม่."""
        if self.color != new_color:
            self.color = new_color
            self._update_surface()

    def draw(self, surface):
        """
        วาดข้อความลงบน Surface ที่กำหนด.

        Args:
            surface (pygame.Surface): Surface ที่ต้องการวาดข้อความลงไป (เช่น หน้าจอหลักของเกม).
        """
        surface.blit(self.surface, self.rect)

    def get_rect(self):
        """
        ส่งคืน Rect ของข้อความ เพื่อให้สามารถปรับตำแหน่งเพิ่มเติมได้ภายนอกคลาส.
        """
        return self.rect