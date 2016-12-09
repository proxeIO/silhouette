import bpy
from bpy.types import AddonPreferences

from .config import defaults

class toggle_silhouette(AddonPreferences):

  default = defaults

  background_color = FloatVectorProperty(
    name = 'Background Color',
    description = 'The background color to use when displaying silhouettes.',
    subtype = 'COLOR',
    size = 3,
    min = 0.0,
    max = 1.0,
    default = default['background_color']
  )
