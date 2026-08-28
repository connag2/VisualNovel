# 서진의 봄 일기 시스템
default diary_pages = []

init python:
    def add_diary(text):
        diary_pages.append(text)
