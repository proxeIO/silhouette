import bpy

def toggle_silhouette(self, context):

  option = context.scene.silhouette
  gradient = context.user_preferences.themes['Default'].view_3d.space.gradients
  light = context.user_preferences.system.solid_lights
  space_data = context.space_data
  addon = context.user_preferences.addons[__name__.partition('.')[0]]

  if not bpy.context.scene.silhouette.show_silhouette:

    option.first_light_diffuse = light[0].diffuse_color
    option.first_light_specular = light[0].specular_color
    option.second_light_diffuse = light[1].diffuse_color
    option.second_light_specular = light[1].specular_color
    option.third_light_diffuse = light[2].diffuse_color
    option.third_light_specular = light[2].specular_color

    option.using_gradient = gradient.show_grad
    option.using_matcap = space_data.use_matcap
    option.using_ambient_occlusion = space_data.use_ssao
    option.using_render_only = space_data.show_only_render

    for i in range(0, 2):

      light[i].diffuse_color = (0.0, 0.0, 0.0)
      light[i].specular_color = (0.0, 0.0, 0.0)

    gradient.show_grad = False
    gradient.high_gradient = addon.background_color
