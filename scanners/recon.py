#!/usr/bin/env python3

# MIT License
#
# Copyright (C) 2019-2020, Entynetproject. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
from lib.args import args
from lib.output import *
from lib.googlesearch import search


def phone_us_format(phone_number, delimiter):
    clean_phone_number = re.sub('[^0-9]+', '', phone_number)
    formatted_phone_number = re.sub(
        "(\d)(?=(\d{3})+(?!\d))", r"\1" + delimiter, "%d" % int(clean_phone_number[:-1])) + clean_phone_number[-1]
    return formatted_phone_number


def phone_format(phone_number, delimiter):
    clean_phone_number = re.sub('[^0-9]+', '', phone_number)
    formatted_phone_number = re.sub(
        "(\d)(?=(\d{2})+(?!\d))", r"\1" + delimiter, "%d" % int(clean_phone_number[:-1])) + clean_phone_number[-1]
    return formatted_phone_number


def scan(number):
    if not args.recon:
        return -1

    test('Running custom format reconnaissance...')

    cc = number['countryCode'].replace('+', '')
    nb = number['local']

    if number['countryIsoCode'] == 'US' or number['countryIsoCode'] == 'CA':
        segments = phone_us_format(cc + nb, ' ').split(' ')

        seg1 = segments[-3]
        seg2 = segments[-2]
        seg3 = segments[-1]

        formats = [
            '%s%s%s' % (seg1, seg2, seg3),
            '%s %s%s%s' % (cc, seg1, seg2, seg3),
            '%s %s %s%s' % (cc, seg1, seg2, seg3),
            '%s %s%s' % (seg1, seg2, seg3),
            '%s-%s%s' % (seg1, seg2, seg3),
            '%s-%s-%s' % (seg1, seg2, seg3),
            '+%s %s-%s-%s' % (cc, seg1, seg2, seg3),
            '(+%s)%s-%s-%s' % (cc, seg1, seg2, seg3),
            '+%s/%s-%s-%s' % (cc, seg1, seg2, seg3),
            '(%s) %s%s' % (seg1, seg2, seg3),
            '(%s) %s-%s' % (seg1, seg2, seg3),
            '(%s) %s.%s' % (seg1, seg2, seg3),
            '(%s)%s%s' % (seg1, seg2, seg3),
            '(%s)%s-%s' % (seg1, seg2, seg3),
            '(%s)%s.%s' % (seg1, seg2, seg3)
        ]
    else:
        formated_number = number['international'].replace(number['countryCode'] + ' ', '').split(' ')

        segments = []
        
        for seg in formated_number:
          segments.append(seg)
        
        formats = [
            '+%s0%s' % (cc, nb),
            '(00%s)0%s' % (cc, number['local']),
            '+%s/0%s' % (cc, nb),
            '+%s0%s' % (cc, '-'.join(segments)),
            '(+%s)0%s' % (cc, '-'.join(segments)),
            '(00%s)0%s' % (cc, '-'.join(segments)),
            '(00%s)0%s' % (cc, '-'.join(segments)),
            '+%s/0%s' % (cc, ' '.join(segments)),
            '+%s0%s' % (cc, ' '.join(segments)),
            '(00%s)0%s' % (cc, ' '.join(segments)),
            '(+%s)0%s' % (cc, ''.join(segments)),
            '(+%s)0%s' % (cc, ' '.join(segments)),
            '+%s/0%s' % (cc, '-'.join(segments)),
            '+%s/0%s' % (cc, ' '.join(segments)),
        ]
        
    for format in formats:
        info('Footprint reconnaissance for %s' % (format))
        for result in search('"%s"' % (format), stop=5):
            info("URL: " + result)
