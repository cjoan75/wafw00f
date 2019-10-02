#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'AliYunDun (Alibaba Cloud Computing)'


def is_waf(self):
    schemes = [
        self.matchContent(r'error(s)?.aliyun.(com|net)?'),
        self.matchStatus(405)
        ]
    if all(i for i in schemes):
        return True
    return False