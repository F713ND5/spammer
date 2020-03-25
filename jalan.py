#!/usr/bin/python

import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
mengetik(' Selamat datang di tools spammer sms')
mengetik(' Saya sudah mendapatkan persetujuan dari team black coder crush untuk menyatukan ulang tools ini')
print "\033[96m[√] TUNGGU SEBENTAR..."
