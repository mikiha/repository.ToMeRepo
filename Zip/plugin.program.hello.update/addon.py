# -*- coding: utf-8 -*-
import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('Name')
 
line1 = "נא לעדכן את המערכת לגרסה 2.0.5"
line2 = "יש עדכונים בשרת לגרסה חדשה יותר"
line3 = "הוראות התקנה:גשו לאריח-מערכת-מרכז העדכונים-בחרו גרסה מתאימה"


xbmcgui.Dialog().ok(addonname, line1, line2, line3)
