[app]
title = Offline Speech
package.name = offlinespeech
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# المتطلبات الأساسية (مهمة جداً للعمل أوفلاين)
requirements = python3,kivy,kivymd,vosk,pyaudio

orientation = portrait
fullscreen = 0

# أذونات الأندرويد المطلوبة
android.permissions = RECORD_AUDIO, INTERNET, READ_EXTERNAL_STORAGE

# إعدادات الأندرويد
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
