
'''
Toggle Silhouette Addon
Copyright (c) 2016 Trentin Frederick (proxe) All Rights Reserved.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# addon info
bl_info = {
  'name': 'Toggle Silhouette',
  'author': 'Trentin Frederick (proxe)',
  'version': (0, 4, 9),
  'blender': (2, 75, 0),
  'location': '3D View \N{Rightwards Arrow} Properties Shelf \N{Rightwards Arrow} Shading',
  'description': 'Quickly toggle the viewport into a silhouette mode.',
  # 'wiki_url': '',
  # 'tracker_url': '',
  'category': '3D View'
}

# imports
import bpy
from bpy.utils import register_module, unregister_module

from .addon import preferences, properties, interface


def register():


def unregister():
