import xbmcaddon
import xbmcgui
import os
import os.path

def signalhibernate(setpath, resetpath):
    if os.path.isfile(resetpath):
        os.remove(resetpath)
    open(setpath, 'a').close()

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

text = "A recording has been finished, Kodi will be shutdown now!" 
 
selectedVal = xbmcgui.Dialog().yesno(heading="Confirm Hibernation",
                                     line1=text,
                                     yeslabel="cancel",
                                     nolabel="OK",
                                     autoclose=5000)

stop_hibernate = '/tmp/kodi_stopshutdown'
do_hibernate = '/tmp/kodi_doshutdown'

if selectedVal:
    signalhibernate(stop_hibernate, do_hibernate)
else:
    signalhibernate(do_hibernate, stop_hibernate)

