import time
import random
import argparse
from DrissionPage import ChromiumPage, ChromiumOptions

URL = 'https://www.twitch.tv/qqros/clip/DaintyGenerousDiamondDBstyle-kAJROjnc4LP6kuHV'
TOTAL_BATCHES = 15
MIN_WAIT = 2
MAX_WAIT = 7

parser = argparse.ArgumentParser()
parser.add_argument('batch', type=int, help='Batch number (0-14)')
args = parser.parse_args()

if not 0 <= args.batch < TOTAL_BATCHES:
    raise ValueError('batch must be between 0 and 14')

print(f'Batch {args.batch + 1} / {TOTAL_BATCHES}')

options = ChromiumOptions()
options.headless()
options.set_argument('--no-sandbox')
options.set_argument('--disable-dev-shm-usage')
options.set_argument('--blink-settings=imagesEnabled=false')
options.set_user_agent(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/120.0.0.0 Safari/537.36'
)

page = ChromiumPage(options)

try:
    print('Opening Twitch clip...')
    page.get(URL)

    wait_time = random.uniform(MIN_WAIT, MAX_WAIT)
    print(f'Staying on page for {wait_time:.2f} seconds')
    time.sleep(wait_time)

finally:
    page.quit()
    print('Done.')
