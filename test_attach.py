import allure
import pytest

#附件
def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段html body块</body>","html测试块",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("C:/Users/wang/Desktop/截图/7F0A53C8-CC5C-41b2-86EB-D22C2DD88654.png",name="这是一个图片",attachment_type=allure.attachment_type.PNG)

def test_attach_video():
    allure.attach.file("D:/旧电脑文件/Photo/照片/2020.6.5-6.7青岛/IMG_0406.MP4",name="",attachment_type=allure.attachment_type.MP4)