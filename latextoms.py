import latex2mathml.converter

latex_input = r"\begin{array}{c}{{\frac{\partial I}{\partial x}\delta x+\frac{\partial I}{\partial y}\delta y+\frac{\partial I}{\partial z}\delta z+\frac{\partial I}{\partial t}\delta t=0}}\\ {{\frac{\partial I}{\partial x}V_{x}+\frac{\partial I}{\partial y}V_{y}+\frac{\partial I}{\partial z}V_{z}+\frac{\partial I}{\partial t}=0}}\end{array}"
mathml_output = latex2mathml.converter.convert(latex_input)
print(mathml_output)