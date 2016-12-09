
def toggle(self, context):

  if context.space_data.viewport_shade in {'SOLID'} or context.scene.silhouette.show_silhouette:

    layout = self.layout

    layout.prop(context.scene.silhouette, 'show_silhouette')
