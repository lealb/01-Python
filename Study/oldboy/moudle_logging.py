# -*- coding: utf-8 -*-
# Author:leali
# Description: logging
# Version:v1.0
# Date:4/19/2018-12:09 AM

import logging as log

if __name__ == "__main__":
    # 通过下面的方式进行简单配置输出方式与日志级别
    log.basicConfig(filename='logger.log', level=log.INFO)

    log.debug('debug message')
    log.info('info message')
    log.warn('warn message')
    log.error('error message')
    log.critical('critical message')

