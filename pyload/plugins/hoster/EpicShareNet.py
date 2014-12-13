# -*- coding: utf-8 -*-

from pyload.plugins.internal.DeadHoster import DeadHoster, create_getInfo


class EpicShareNet(DeadHoster):
    __name    = "EpicShareNet"
    __type    = "hoster"
    __version = "0.02"

    __pattern = r'https?://(?:www\.)?epicshare\.net/\w{12}'

    __description = """EpicShare.net hoster plugin"""
    __license     = "GPLv3"
    __authors     = [("t4skforce", "t4skforce1337[AT]gmail[DOT]com")]


getInfo = create_getInfo(EpicShareNet)