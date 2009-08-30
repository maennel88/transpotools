"""
/***************************************************************************
TestPlugin
A QGIS plugin
ahmed's test plugin to finally develop apython plugin
                             -------------------
begin                : 2009-03-08 
copyright            : (C) 2009 by dassouki
email                : dassouki@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "Travel Demand Modeling" 
def description():
  return "Plugin to perform a standard four step procedure"
def version(): 
  return "Version .0.1 - alpha" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load TestPlugin class from file TestPlugin
  from TranspoPlugin import TranspoPlugin 
  return TranspoPlugin(iface)


