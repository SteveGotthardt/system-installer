#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  disable.py
#
#  Copyright 2021 Thomas Castleman <contact@draugeros.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
"""Disable DE/WM or DE/WM features"""
import subprocess

def immersion():
    """disable Immersion within DE.

    This may involve enabliong desktop icons, re-adding panels, and more.
    """
    # restart panel
    subprocess.Popen(["xfce4-panel"])
    # bring back desktop icons
    subprocess.Popen(["xfconf-query", "--channel", "xfce4-desktop",
                      "--property", "/desktop-icons/style", "--set", "2"])
