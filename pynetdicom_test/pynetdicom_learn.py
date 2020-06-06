#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pynetdicom.presentation import PresentationContext
from pynetdicom import build_context

cx = PresentationContext()
cx.context_id = 1
# 1.2.840.10008.1.1 - Verification SOP Class
# 1.2.840.10008.5.1.4.1.1 - CT Image Storage
cx.abstract_syntax = '1.2.840.10008.1.1'
# 1.2.840.10008.1.2 - Implicit VR Little Endian
# 1.2.840.10008.1.2.4.50 - JPEG Baseline
cx.transfer_syntax = ['1.2.840.10008.1.2', '1.2.840.10008.1.2.4.50']
print(cx)

cx1 = build_context(
    '1.2.840.10008.1.1', ['1.2.840.10008.5.1.4.1.1.3.1']
)
print(cx1)
cx2 = build_context('1.2.840.10008.1.1')
print(cx2)
