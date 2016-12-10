
def toggle(self, context):

  addon = context.user_preferences.addons[__name__.partition('.')[0]].preferences

  if context.space_data.viewport_shade == 'SOLID' or context.scene.silhouette.show_silhouette:

    layout = self.layout

    layout.prop(context.scene.silhouette, 'show_silhouette')

    if context.scene.silhouette.show_silhouette:

      layout.prop(addon, 'background_color', text='')
