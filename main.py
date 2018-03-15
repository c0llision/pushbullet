#!/usr/bin/env python3
from pushbullet import Pushbullet


def main():
    ''' main'''
    from keys import api_key, encrypt_key
    pb = Pushbullet(api_key, encrypt_key)
    pb.push_note("This is the title", "This is the body")


if __name__ == '__main__':
    main()
