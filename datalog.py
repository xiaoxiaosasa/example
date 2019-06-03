import logging
from logging import handlers,Formatter
import time
log = logging.getLogger()


logging.basicConfig(level=logging.INFO,
                filename=str(time.strftime('%Y%m%d%H%M%S',time.localtime())+'.log'),
                filemode='w',
                format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                )


while True:
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
