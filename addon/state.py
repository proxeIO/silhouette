import bpy

def toggle_silhouette(self, context):

  option = context.scene.silhouette
  light = context.user_preferences.system.solid_lights
  space_data = context.space_data

  if not bpy.context.scene.silhouette.toggle:

    option.first_light_diffuse = light[0].diffuse_color
    option.first_light_specular = light[0].specular_color
    option.second_light_diffuse = light[1].diffuse_color
    option.second_light_specular = light[1].specular_color
    option.third_light_diffuse = light[2].diffuse_color
    option.third_light_specular = light[2].specular_color

    
