# python compare hashes
script เพื่อใช้ตรวจสอบค่า hash ของ files ใน 2 folders ใช้ในกรณีเช่น ตรวจเจอ apk ที่มีค่า hash ของ apk ไม่ตรงกัน เมื่อ decompiled ออกมาแล้วใช้ตรวจสอบแยกแต่ละไฟล์ว่าระหว่าง 2 apks มีไฟล์ไหนไม่ตรงกันบ้าง

## Table of Contents

- [Usage](#usage)

## Usage
```sh
python ./compare_hashes.py './folder_1' './folder_2'
2023-01-30 12:56:00 :: Start comparison between ./folder_1 and folder_2
2023-01-30 12:56:01 :: End comparison
2023-01-30 12:56:01 :: Finished
```


| Name           | Version | Release          |
| -------------- | ------- | ---------------- |
| compare_hashes | v.0.1   | 2023-01-03 12:57 |
