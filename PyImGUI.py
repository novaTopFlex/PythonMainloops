import imgui

imgui.create_context()
ingui.get_io().display_size = 100, 100
imgui.get_io().fonts.get_tex_data_as_rgba32()
imgui.new_frame()
imgui.begin("Your first window!", True)
imgui.text("Hello world!")
imgui.end()
imgui.render()
imgui.end_frame()
