# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
mapillary.utils.time
~~~~~~~~~~~~~~~~~~~~

This module contains the time utilies for the UNIX epoch seconds, the time and the date range, and
the date filtering logic.

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Package imports
import datetime


def date_to_unix_timestamp(date: str):
    """A utility function that converts the given date
    into its UNIX epoch timestamp equivalent. It accepts the formats, ranging from
    YYYY-MM-DDTHH:MM:SS, to simply YYYY, and a permutation of the fields in between as well

    Has a special argument, '*', which returns current timestamp

    :param date: The date to get the UNIX timestamp epoch of
    :type date: str

    Usage::
        >>> from utils.time_utils import date_to_unix_timestamp
        >>> date_to_unix_timestamp('2020-10-23')
        "1603393200"
    """

    # Returns the epoch current timestamp in milliseconds
    if date == "*":
        return int(datetime.datetime.now().timestamp()) * 1000

    # Return the epoch timestamp in miliseconds
    return int(datetime.datetime.fromisoformat(date).timestamp()) * 1000
