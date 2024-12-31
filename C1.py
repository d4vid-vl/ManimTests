from manim import *

class Cube(Scene):
    def construct(self):
        box = Rectangle(stroke_color = GREEN_C, # Caja con borde de color verde
        stroke_opacity = 0.7, # Opacidad del borde
        fill_color = RED_B, # Color del cuerpo
        fill_opacity = 0.5, # Opacidad del cuerpo
        height = 1, width = 1) # Largo y ancho

        self.add(box) # Añadimos el objeto box al plano
        self.play(box.animate.shift(RIGHT*2), run_time=2) # Se mueve a la derecha 2 unidades en 2 segundos
        self.play(box.animate.shift(UP*3), run_time=2) # Arriba 3 unidades en 2 segundos
        self.play(box.animate.shift(DOWN*5+LEFT*5), run_time=2) # Abajo a la izquierda 5 unidades
        self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time=2) # Unidad y media arriba, y uno a la derecha

class Objects(Scene):
    def construct(self):
        axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], # Ejes de 3 unidades cada uno, 2D
        x_length=6, y_length=6) # Ambos ejes miden 6 unidades de video (Buscar)
        axes.to_edge(LEFT, buff=2) # Desde el borde izquierdo, mueve 2 unidades al lado contrario

        circle = Circle(stroke_width = 6, stroke_color = YELLOW, # Circulo con borde amarillo, ancho 6 unidades
                        fill_color = RED_C, fill_opacity = 0.8) # Color de cuerpo rojo, opacidad 0.8
        circle.set_width(2).to_edge(DR, buff=0) # Circulo de radio 2 unidades, al borde abajo a la derecha sin diferencias

        triangle = Triangle(stroke_color = ORANGE, stroke_width = 10,   # Triangulo de borde naranja, ancho 10 unidades
                            fill_color = GREY).set_height(2).shift(DOWN*3+RIGHT*3) # Color de cuerpo gris, altura 2, y 3 unidades abajo a la derecha
        
        self.play(Write(axes), run_time=2)  # Se muestran los ejes en 2 segundos
        self.play(DrawBorderThenFill(circle)) # Se dibuja el borde del circulo para después rellenarlo del color elegido
        self.play(circle.animate.set_width(1)) # Anima el cambio de radio de 2 -> 1
        self.play(Transform(circle, triangle), run_time=3) # El circulo se transforma en el triangulo en un lapso de 3 segundos