#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:59:33 2022

@author: muntazirabidi
"""

class Codec:
    def encode(self, strs):
        
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)
        else:
            return chr(257).join(x.encode('utf-8') for x in strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        if s == chr(258):
            return []
        else:
            return s.split(chr(257))


# Your Codec object will be instantiated and called as such:
strs = ["Hello","World"]
codec = Codec()
print(codec.decode(codec.encode(strs)))

