#!/usr/bin/python3
def element_at(passions, idx):
    if idx < 0 or idx >= len(passions):
        return None
    return passions[idx]
