from manimlib.imports import *
from manimlib.constants import RED, GREEN, BLUE, YELLOW, PINK, ORANGE

class Transitions(Scene):
    def construct(self):
        headL = VGroup()
        headL.add(TextMobject("Línuleg algebra A (STÆ106G)"))
        headL.add(TextMobject("Rögnvaldur G. Möller"))
        headL.add(TextMobject("Háskóli Íslands"))
        headL.scale(0.67).arrange(DOWN, aligned_edge=LEFT, buff=SMALL_BUFF).to_corner(UL, buff=1)

        headR = VGroup()
        headR.add(TextMobject("Bjarki Baldursson Harksen"))
        headR.add(TextMobject("18. september 2020"))
        headR.add(TextMobject("Háskóli Íslands"))
        headR.scale(0.67).arrange(DOWN, aligned_edge=RIGHT, buff=SMALL_BUFF).to_corner(UR, buff=1)

        title = TextMobject("\\textbf{Skiladæmi 3}").scale(1.5)

        self.play(AnimationGroup(
            AnimationGroup(FadeInFrom(headL, 0.2*DOWN), FadeInFrom(headR, 0.2*DOWN)),
            FadeInFrom(title, 0.5*DOWN),
            lag_ratio=0.8,
            run_time=2
        ))
        self.wait(4)

        d9 = TextMobject("Dæmi 9").scale(1.2)
        d10 = TextMobject("Dæmi 10").scale(1.2)
        d11 = TextMobject("Dæmi 11").scale(1.2)
        d12 = TextMobject("Dæmi 12").scale(1.2)
        
        self.play(
            FadeOutAndShift(headL, 0.5*UP),
            FadeOutAndShift(headR, 0.5*UP),
            FadeOutAndShift(title, UP),
            FadeInFrom(d9, DOWN),
            run_time=2
        )
        self.wait(5)

        self.play(
            FadeOutAndShift(d9, UP),
            FadeInFrom(d10, DOWN),
            run_time=2
        )
        self.wait(5)

        self.play(
            FadeOutAndShift(d10, UP),
            FadeInFrom(d11, DOWN),
            run_time=2
        )
        self.wait(5)

        self.play(
            FadeOutAndShift(d11, UP),
            FadeInFrom(d12, DOWN),
            run_time=2
        )
        self.wait(5)



class D9_Intro(Scene):
    def construct(self):
        problem_text = TextMobject("Skoðum fylkið").to_corner(UL, buff=LARGE_BUFF)
        A_eq = TexMobject("A", "=")
        A_matrix = Matrix([
            [1, 3, -2], 
            [2, 5, -3], 
            [-3, 2, -4]
        ]).next_to(A_eq)
        A = VGroup(A_eq, A_matrix)
        A.move_to(ORIGIN)
        part_a_text = TextMobject("Eru dálkvigrar fylkisins línulega óháðir?")
        part_a_text.to_corner(DL, buff=LARGE_BUFF)

        self.play(AnimationGroup(
            Write(problem_text),
            Write(A),
            lag_ratio=0.7
        ))
        self.wait(1)
        self.play(Write(part_a_text))
        self.wait(1)

        self.play(*[ApplyMethod(mob.set_opacity, 0.3) for mob in 
            (A_eq, A_matrix.get_brackets(), A_matrix.get_columns()[1], A_matrix.get_columns()[2])])
        self.wait(1.5)
        self.play(
            ApplyMethod(A_matrix.get_columns()[0].set_opacity, 0.3),
            ApplyMethod(A_matrix.get_columns()[1].set_opacity, 1),
        )
        self.wait(1.5)
        self.play(
            ApplyMethod(A_matrix.get_columns()[1].set_opacity, 0.3),
            ApplyMethod(A_matrix.get_columns()[2].set_opacity, 1),
        )
        self.wait(4)
        self.play(*[ApplyMethod(mob.set_opacity, 1) for mob in 
            (A_eq, A_matrix.get_brackets(), A_matrix.get_columns()[0], A_matrix.get_columns()[1])])
        self.wait(3)


class D9_Method(Scene):
    def construct(self):
        iff = TextMobject("Dálkvigrarnir eru línulega óháðir ef og aðeins ef").to_edge(UP, buff=2.5)
        only_zero = TexMobject("A\\va{x} = \\va{0} \\Rightarrow \\va{x} = \\va{0}")
        no_free_vars = TextMobject("Engar frjálsar breytur í $A\\va{x}$!").to_edge(DOWN, buff=2.5)
        self.play(Write(iff))
        self.wait(3)
        self.play(Write(only_zero))
        self.wait(8)
        self.play(Write(no_free_vars))
        self.wait(1)

class D9_Stallform(Scene):
    def construct(self):
        stall_text = TextMobject("Komum $A$ á efra stallaform:").to_corner(UL, buff=LARGE_BUFF)
        A0 = Matrix([
            [1, 3, -2], 
            [2, 5, -3], 
            [-3, 2, -4]
        ]).scale(0.8)

        sim1 = TexMobject("\\sim").next_to(A0)
        A1 = Matrix([
            [1, 3, -2], 
            [2, 5, -3], 
            [-3, 2, -4]
        ]).scale(0.8).next_to(sim1)
        A2 = Matrix([
            [1, 3, -2], 
            [0, -1, 1], 
            [0, 11, -10]
        ]).scale(0.8).next_to(A1, DOWN, aligned_edge=RIGHT)
        sim2 = TexMobject("\\sim").set_x(sim1.get_x()).set_y(A2.get_y())
        VGroup(A0, sim1, A1, sim2, A2).center()

        linop1 = TexMobject("L_2 - 2L_1").scale(0.8).next_to(A1)
        linop2 = TexMobject("L_3 + 3L_1").scale(0.8).next_to(A1, aligned_edge=DOWN).shift(0.14*UP)
        linop3 = TexMobject("L_3 + 11L_2").scale(0.8).next_to(A2, aligned_edge=DOWN).shift(0.14*UP)

        A1_changes = [0, -1, 1, 0, 11, -10]
        for i in range(3, 9):
            A1.elements[i].generate_target()
            A1.elements[i].target = TexMobject(str(A1_changes[i-3])).scale(0.8).move_to(A1.elements[i], aligned_edge=RIGHT)

        A2_changes = [0, 1]
        for i in range(7, 9):
            A2.elements[i].generate_target()
            A2.elements[i].target = TexMobject(str(A2_changes[i-7])).scale(0.8).move_to(A2.elements[i], aligned_edge=RIGHT)

        self.play(Write(stall_text))
        self.play(Write(A0))
        self.wait(1)
        self.play(AnimationGroup(Write(sim1), Write(A1), lag_ratio=0.5))
        self.wait(0.5)
        self.play(FadeInFrom(linop1, 0.2*LEFT))
        self.wait(1)
        self.play(AnimationGroup(*[MoveToTarget(num) for num in A1.elements[3:6]], lag_ratio=0.3))
        self.wait(1.5)
        self.play(FadeInFrom(linop2, 0.2*LEFT))
        self.wait(1)
        self.play(AnimationGroup(*[MoveToTarget(num) for num in A1.elements[6:]], lag_ratio=0.3))

        self.wait(2.5)
        self.play(AnimationGroup(Write(sim2), Write(A2), lag_ratio=0.5))
        self.wait(0.5)
        self.play(FadeInFrom(linop3, 0.2*LEFT))
        self.wait(1)
        self.play(AnimationGroup(*[MoveToTarget(num) for num in A2.elements[7:]], lag_ratio=0.3))
        self.wait(5)
        
        stall_coords = A2.get_center() + 1.5*DOWN
        self.play(
            *[FadeOutAndShift(mob, -stall_coords) for mob in (stall_text, A0, A1, sim1, sim2, linop1, linop2, linop3)],
            ApplyMethod(A2.shift, -stall_coords)
        )
        self.wait(1)

        yesss1 = TextMobject("Forystustuðull í hverri línu").next_to(A2, DOWN, buff=0.8)
        yesss2 = TextMobject("Engar frjálsar breytur í $A\\va{x}=\\va{0}$").next_to(yesss1, DOWN, buff=MED_LARGE_BUFF-0.1)
        yesss3 = TextMobject("Dálkvigrar $A$ línulega óháðir!").next_to(yesss2, DOWN, buff=MED_LARGE_BUFF)

        self.play(
            *[ApplyMethod(A2.elements[i].set_opacity, 0.3) for i in (1, 2, 3, 5, 6, 7)],
            FadeInFrom(yesss1, 0.2*UP)
        )
        self.wait(1)
        self.play(FadeInFrom(yesss2, 0.2*UP))
        self.wait(1)
        self.play(FadeInFrom(yesss3, 0.2*UP))
        self.wait(1)

        self.play(*[ApplyMethod(A2.elements[i].set_opacity, 1) for i in (1, 2, 3, 5, 6, 7)])
        self.wait(2)

        
class D9_Geometric(ThreeDScene):
    def construct(self):
        A_eq = TexMobject("A", "=")
        A_matrix = Matrix([
            [1, 3, -2], 
            [2, 5, -3], 
            [-3, 2, -4]
        ]).next_to(A_eq)
        A_matrix.set_column_colors(GREEN, RED, BLUE)
        A = VGroup(A_eq, A_matrix).scale(0.6)
        A.to_corner(UL)
        A.set_opacity(0)
        self.add_fixed_in_frame_mobjects(A)
        # self.play(A.set_opacity, 1)

        self.set_camera_orientation(0.8*PI/2, -0.8*PI/2)
        axes = ThreeDAxes(
            x_axis_config={"tick_frequency": 0.5}, 
            y_axis_config={"tick_frequency": 0.5}, 
            z_axis_config={"tick_frequency": 0.5}
        )
        x_label = TexMobject("x").scale(0.8).move_to(5.5*RIGHT+0.5*DOWN).rotate(PI/2, axis=RIGHT)
        y_label = TexMobject("y").scale(0.8).move_to(5.5*UP+0.5*LEFT).rotate(PI/2, axis=RIGHT)
        z_label = TexMobject("z").scale(0.8).move_to(3.5*OUT+0.5*LEFT).rotate(PI/2, axis=RIGHT)
        labels = VGroup(x_label, y_label, z_label)
        self.play(
            A.set_opacity, 1,
            ShowCreation(axes),
            Write(labels)
        )
        self.wait(3)

        a1 = Vector(np.array([1/2, 2/2, -3/2])).set_color(GREEN).set_shade_in_3d(True)
        a2 = Vector(np.array([3/2, 5/2, 2/2])).set_color(RED).set_shade_in_3d(True)
        a3 = Vector(np.array([-2/2, -3/2, -4/2])).set_color(BLUE).set_shade_in_3d(True)

        for a in (a1, a2, a3):
            self.play(ShowCreation(a))
            a.generate_target()
            a.target = Sphere(
                checkerboard_colors=[a.get_color(), a.get_color()], 
                stroke_color=a.get_color(),
                radius=0.04,
                shade_in_3d=False
            ).move_to(a.get_end())
            self.wait(1)
            self.play(MoveToTarget(a))
            self.wait(2)

        plane = ParametricSurface(
            lambda y, z: np.array([(11*y + z)/19, y, z]),
            u_min=-3,
            u_max=3,
            v_min=-3,
            v_max=3,
            resolution=1,
            fill_opacity=0.6,
            checkerboard_colors=[YELLOW, YELLOW],
            stroke_color=YELLOW,
            stroke_width=0
        ).set_shade_in_3d(True)
        self.play(ShowCreation(plane))
        self.wait(4)
        self.move_camera(1.1*PI/2, -1.335*PI/2)
        self.wait(6)

        question = TextMobject("Spanna vigrarnir allt $\\mathbb{R}^3$?")
        question.scale(0.9).to_corner(DR, buff=LARGE_BUFF).set_opacity(0)
        # question.add_background_rectangle()
        self.add_fixed_in_frame_mobjects(question)

        self.play(question.set_opacity, 1)
        self.wait(1)


class D9_SpanR3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(0.8*PI/2, -0.8*PI/2)
        axes = ThreeDAxes(
            x_axis_config={"tick_frequency": 0.5}, 
            y_axis_config={"tick_frequency": 0.5}, 
            z_axis_config={"tick_frequency": 0.5}
        )
        self.add(axes)
        # self.begin_ambient_camera_rotation()

        v1 = Vector(np.array([4/2, -2/2, -1/2])).set_color(GREEN).set_shade_in_3d(True)
        v2 = Vector(np.array([-3/2, -1/2, 1/2])).set_color(RED).set_shade_in_3d(True)

        norm = np.cross(v1.get_end(), v2.get_end())
        plane = ParametricSurface(
            lambda x, y: np.array([x, y, (-norm[0]*x - norm[1]*y)/norm[2]]),
            u_min=-4,
            u_max=4,
            v_min=-4,
            v_max=4,
            resolution=1,
            fill_opacity=0.6,
            checkerboard_colors=[YELLOW, YELLOW],
            stroke_color=YELLOW,
            stroke_width=0
        )

        self.play(ShowCreation(v1), ShowCreation(v2))

        self.wait(2)

        self.play(ShowCreation(plane))
        self.wait(5)

        v3 = Vector(np.array([3/2, 1/2, 2/2])).set_color(BLUE).set_shade_in_3d(True)
        v3.org = v3.get_end()
        self.play(ShowCreation(v3))
        self.wait(1.5)
        self.play(plane.move_to, v3.get_end())
        
        plane.add_updater(lambda p: p.move_to(v3.get_end()))
        self.wait(3)

        scale_val = ValueTracker(1)
        def v3_updater(v):
            s = scale_val.get_value()
            if abs(s) < 0.01:
                v.put_start_and_end_on(ORIGIN, 1e-9*RIGHT)
            else:
                v.put_start_and_end_on(ORIGIN, s*v.org, account_for_3d=True)

        v3.add_updater(v3_updater)

        self.play(scale_val.set_value, 2, run_time=2)
        self.play(scale_val.set_value, -2, run_time=2)
        self.play(scale_val.set_value, 1, run_time=2)
        self.wait(4)

        v3.clear_updaters()
        plane.clear_updaters()

        v3.generate_target()
        v3.target = Vector(1.5*v1.get_end() + v2.get_end())
        v3.target.set_color(BLUE).set_shade_in_3d(True)
        self.play(
            ReplacementTransform(v3, v3.target),
            ApplyMethod(plane.center)
        )
        self.wait(1)
        v3 = v3.target
        v3.org = v3.get_end()
        v3.add_updater(v3_updater)

        v3.resume_updating()

        self.play(scale_val.set_value, 2, run_time=2)
        self.play(scale_val.set_value, -2, run_time=2)
        self.play(scale_val.set_value, 1, run_time=2)
        self.wait(4)


class D9_Formal(Scene):
    def construct(self):
        formal = TextMobject("Formlega:").to_corner(UL, buff=LARGE_BUFF)
        formal.set_color(YELLOW)
        rule = VGroup(
            TextMobject("Ef $A$ er $3 \\times 3$ fylki með línulega óháða dálkvigra"),
            TextMobject("og $\\va{b}\\in\\mathbb{R}^3$ ", "þá hefur"),
            TexMobject("A\\va{x} = \\va{b}"),
            TextMobject("nákvæmlega eina lausn.")
        )
        rule.arrange(DOWN, aligned_edge=LEFT)
        rule[0].shift(0.3*UP)
        rule[1].shift(0.4*UP)
        rule[2].set_x(0)
        rule[3].shift(0.4*DOWN)

        self.play(FadeInFrom(formal, LEFT))
        self.wait(1)
        self.play(Write(rule[0]))
        self.wait(0.5)
        self.play(Write(rule[1][0]))
        self.play(AnimationGroup(Write(rule[1][1]), Write(rule[2]), lag_ratio=0.5))
        self.play(Write(rule[3]))
        self.wait(1)


class D10_TransformDefs(Scene):
    def construct(self):
        lets_def = TextMobject("Skilgreinum eftirfarandi varpanir:")
        T1_tex = TexMobject("T_1: \\mathbb{R}^3 \\to \\mathbb{R}\\phantom{^2},\\quad T(x_1, x_2, x_3) = x_1 - x_2 + 3x_3 + 1")
        T2_tex = TexMobject("T_2: \\mathbb{R}^3 \\to \\mathbb{R}^2,\\quad T(x_1, x_2, x_3) = (x_1,\\, x_1 + x_2 + x_3)")
        T1_tex.scale(0.8)
        T2_tex.scale(0.8)
        VGroup(lets_def, T1_tex, T2_tex).arrange(DOWN, aligned_edge=LEFT).to_corner(UL, buff=LARGE_BUFF)
        for T in (T1_tex, T2_tex):
            T.shift(0.5*DOWN)
            T.set_x(0)

        self.play(Write(lets_def))
        self.wait(1)
        self.play(Write(T1_tex), Write(T2_tex))
        self.wait(3)

        left_rect = Rectangle(height=2.5, width=2.5*16/9, fill_color="#00FF00", fill_opacity=1)
        right_rect = left_rect.copy()
        VGroup(left_rect, right_rect).arrange(buff=0.8).next_to(T2_tex, DOWN, buff=LARGE_BUFF)

        self.play(DrawBorderThenFill(left_rect))
        self.wait(5)
        self.play(DrawBorderThenFill(right_rect))
        self.wait(5)

        question = TextMobject("Eru varpanirnar línulegar?").move_to(lets_def, aligned_edge=LEFT)
        self.play(
            FadeInFrom(question, 0.8*DOWN),
            FadeOutAndShift(lets_def, 0.8*UP)
        )
        self.wait(1)

class D10_R3toR(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(0.85*PI/2, -0.8*PI/2)
        axes = ThreeDAxes().scale(0.8)

        label = TexMobject("T_1:").to_corner(UL).set_opacity(0)
        self.add_fixed_in_frame_mobjects(label)
        self.play(
            ApplyMethod(label.set_opacity, 1),
            FadeIn(axes)
        )
        self.wait(1)
        
        R3 = Prism(dimensions=[8, 8, 5], fill_color=YELLOW, fill_opacity=0.4)
        R1 = Prism(dimensions=[8, 0.05, 0.05], fill_color=YELLOW, fill_opacity=0.8)
        R1.set_shade_in_3d(False)

        self.play(FadeIn(R3))
        self.wait(2)
        self.play(ReplacementTransform(R3, R1))
        self.wait(1)


class D10_R3toR2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(0.85*PI/2, -0.8*PI/2)
        axes = ThreeDAxes().scale(0.8)

        label = TexMobject("T_2:").to_corner(UL).set_opacity(0)
        self.add_fixed_in_frame_mobjects(label)
        self.play(
            ApplyMethod(label.set_opacity, 1),
            FadeIn(axes)
        )
        self.wait(1)
        
        R3 = Prism(dimensions=[8, 8, 5], fill_color=YELLOW, fill_opacity=0.4)
        R2 = Prism(dimensions=[8, 8, 0.1], fill_color=YELLOW, fill_opacity=0.6)

        self.play(FadeIn(R3))
        self.wait(2)
        self.play(ReplacementTransform(R3, R2))
        self.wait(1)


class D10_T1Only2D(LinearTransformationScene):
    CONFIG = {
        "function": lambda z: complex(z.real - z.imag + 1, 0),
        "show_basis_vectors": False,
        "foreground_plane_kwargs": {
            "x_max": FRAME_WIDTH,
            "x_min": -FRAME_WIDTH,
            "y_max": FRAME_WIDTH,
            "y_min": -FRAME_WIDTH,
            "faded_line_ratio": 0
        },
    }

    def construct(self):
        label = TexMobject("T_1:").to_corner(UL)
        label.add_background_rectangle()
        self.add(label)

        self.setup()
        self.plane.prepare_for_nonlinear_transform(100)
        self.wait(3)
        self.play(ApplyMethod(
            self.plane.apply_complex_function, self.function,
            run_time = 5,
        ))
        self.wait(3)
        
        zero_vector = Dot(color=RED)
        zero_tex = TexMobject("\\va{0}", "\\mapsto", "1")
        zero_tex.next_to(zero_vector, UP, buff=0.29).shift(-zero_tex[0].get_x()*RIGHT)
        zero_tex[0].set_color(RED)
        zero_tex[1].set_x(0.525)
        zero_tex[2].set_x(1)
        zero_tex.add_background_rectangle_to_submobjects()

        self.play(ShowCreation(zero_vector))
        self.play(Write(zero_tex[0]))
        self.wait(0.5)
        self.play(
            FadeInFrom(zero_tex[1], 0.1*LEFT),
            ApplyMethod(zero_vector.shift, RIGHT), 
            run_time=2
        )
        self.play(Write(zero_tex[2]))
        self.wait(3)

        ohno = TexMobject("T_1(c\\, \\va{x})", "\\neq", "c\\, T_1(\\va{x})")
        ohno.move_to(2.5*UP)
        ohno[1].set_color(RED)
        ohno.add_background_rectangle()
        self.play(Write(ohno))
        self.wait(1)


class D10_T2Only2D(LinearTransformationScene):
    CONFIG = {
        "show_basis_vectors": False,
        "foreground_plane_kwargs": {
            "x_max": FRAME_WIDTH,
            "x_min": -FRAME_WIDTH,
            "y_max": FRAME_WIDTH,
            "y_min": -FRAME_WIDTH,
            "faded_line_ratio": 0
        },
    }

    def construct(self):
        label = TexMobject("T_2:").to_corner(UL)
        label.add_background_rectangle()
        self.add(label)
        matrix = [
            [1, 0],
            [1, 1]
        ]
        self.apply_matrix(matrix)
        self.wait(1)


class D10_T2Confirm(Scene):
    def construct(self):
        lets_confirm = TextMobject("Staðfestum að $T_2$ sé línuleg vörpun:")
        lets_confirm.scale(0.8).to_corner(UL)
        make_vects = TextMobject("Látum $\\va{x} \coloneqq (x_1, x_2, x_3)$ og $\\va{y} \coloneqq (y_1, y_2, y_3)$.")
        make_vects.scale(0.8).next_to(lets_confirm, DOWN, aligned_edge=LEFT)
        self.play(Write(lets_confirm))
        self.wait(0.5)
        self.play(Write(make_vects))
        self.wait(1)

        prod_check = TexMobject(
            "T_2(c\\, \\va{x})",  
            "= T_2(cx_1, cx_2, cx_3)", "= (cx_1,\\, cx_1 + cx_2 + cx_3)", 
            "= c(x_1,\\, x_1 + x_2 + x_3)", "= c\\, T_2(\\va{x})")
        prod_check.scale(0.8)
        prod_check[3].next_to(prod_check[1], DOWN, aligned_edge=LEFT)
        prod_check[4].next_to(prod_check[3])
        prod_check.move_to(UP)
        one = TextMobject("(i)").scale(0.8).next_to(prod_check[0], LEFT, buff=0.5)
        self.play(Write(one))
        self.play(Write(prod_check))
        self.wait(1.5)

        sum_check = TexMobject(
            "T_2(\\va{x} + \\va{y})",
            "= T_2(x_1+y_1,\\, x_2+y_2,\\, x_3+y_3)", "= (x_1+y_1,\\, x_1+y_1+x_2+y_2+x_3+y_3)",
            "= (x_1,\\, x_1+x_2+x_3) + (y_1,\\, y_1+y_2+y_3)", "= T_2(\\va{x})+T_2(\\va{y})"
        )
        sum_check.scale(0.8)
        for i in range(2, 5):
            sum_check[i].next_to(sum_check[i-1], DOWN, aligned_edge=LEFT)
        sum_check.move_to(1.5*DOWN)
        two = TextMobject("(ii)").scale(0.8).next_to(sum_check[0], LEFT, buff=0.5)
        self.play(Write(two))
        self.play(Write(sum_check))
        self.wait(1)


class D10_FindBasisVectors(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(0.67*PI/2, -0.8*PI/2)
        axes = ThreeDAxes(
            x_axis_config={"tick_frequency": 2}, 
            y_axis_config={"tick_frequency": 2}, 
            z_axis_config={"tick_frequency": 2}
        )
        x_label = TexMobject("x").move_to(5.5*RIGHT+0.5*DOWN)
        y_label = TexMobject("y").move_to(5.5*UP+0.5*LEFT)
        z_label = TexMobject("z").move_to(3.5*OUT+0.5*LEFT).rotate(PI/2, axis=RIGHT)
        labels = VGroup(x_label, y_label, z_label)
        self.add(axes, labels)
        self.wait(1)

        e1 = Vector(2*RIGHT).set_color(GREEN).set_shade_in_3d(False)
        e2 = Vector(2*UP).set_color(RED).set_shade_in_3d(False)
        e3 = Vector(2*OUT+1e-9*UP).set_color(BLUE).set_shade_in_3d(False)
        e1.generate_target()
        e2.generate_target()
        e3.generate_target()
        e1.target = Vector(2*RIGHT+2*UP).set_color(GREEN).set_shade_in_3d(False)
        e2.target = e2
        e3.target = Vector(2*UP).set_color(BLUE).set_shade_in_3d(False)

        e1.tex = TexMobject("\\va{e}_1", "= (1, 0, 0)", "\\mapsto", "(", "1", "," ,"1", ")")
        e2.tex = TexMobject("\\va{e}_2", "= (0, 1, 0)", "\\mapsto", "(", "0", "," ,"1", ")")
        e3.tex = TexMobject("\\va{e}_3", "= (0, 0, 1)", "\\mapsto", "(", "0", "," ,"1", ")")
        VGroup(e1.tex, e2.tex, e3.tex).scale(0.8).arrange(DOWN, aligned_edge=LEFT).to_corner(UL).set_opacity(0)
        self.add_fixed_in_frame_mobjects(e1.tex, e2.tex, e3.tex)
        for et, c in zip([e1.tex, e2.tex, e3.tex], [GREEN, RED, BLUE]):
            et[0].set_color(c)
        
        for e in (e1, e2, e3):
            e.tex[:2].set_opacity(1)
            self.play(
                Write(e.tex[:-1]),
                ShowCreation(e)
            )
            self.wait(2)
            e.tex[2:].set_opacity(1)
            self.play(
                Write(e.tex[2:]),
                MoveToTarget(e)
            )
            self.wait(3)

        self.wait(5)
        self.play(*[FadeOut(mob) for mob in (axes, labels, e1, e2, e3)])
        self.set_camera_orientation(0, -PI/2)
        self.wait(1)
        
        T2_tex = TexMobject("T_2(\\va{x}) =", "\\va{x}")
        T2_matrix_with_T = Matrix([
            ["T_2(\\va{e}_1)", "T_2(\\va{e}_2)", "T_2(\\va{e}_3)"]
        ], h_buff=2, bracket_v_buff=0.1)
        T2_matrix_with_T.elements.set_opacity(0)
        Te1 = TexMobject("T_2(", "\\va{e}_1", ")").move_to(T2_matrix_with_T.elements[0])
        Te2 = TexMobject("T_2(", "\\va{e}_2", ")").move_to(T2_matrix_with_T.elements[1])
        Te3 = TexMobject("T_2(", "\\va{e}_3", ")").move_to(T2_matrix_with_T.elements[2])
        Te1[1].set_color(GREEN).set_opacity(0)
        Te2[1].set_color(RED).set_opacity(0)
        Te3[1].set_color(BLUE).set_opacity(0)
        T2_matrix_with_T.add(Te1, Te2, Te3)

        T2_matrix_with_nums = Matrix([
            [1, 0, 0],
            [1, 1, 1]
        ], h_buff=2, bracket_v_buff=0.1, bracket_h_buff=0.8309648769)
        T2_matrix_with_nums.set_column_colors(GREEN, RED, BLUE)
        T2_eq = VGroup(T2_tex[0], T2_matrix_with_T, T2_tex[1]).arrange()
        T2_matrix_with_nums.move_to(T2_matrix_with_T)
        T2_tex[-1].shift(0.1*LEFT)

        cops = VGroup(
            Te1[1].copy().set_opacity(1), 
            Te2[1].copy().set_opacity(1), 
            Te3[1].copy().set_opacity(1)
        )

        self.play(Write(T2_eq))
        self.play(AnimationGroup(
            ReplacementTransform(e1.tex[0].copy(), cops[0]),
            ReplacementTransform(e2.tex[0].copy(), cops[1]),
            ReplacementTransform(e3.tex[0].copy(), cops[2]),
            lag_ratio=0.2
        ))
        self.wait(2)

        self.play(AnimationGroup(
            *[FadeOut(mob) for mob in (cops, VGroup(Te1, Te2, Te3))],
            ReplacementTransform(e1.tex[-4].copy(), T2_matrix_with_nums.elements[0]),
            ReplacementTransform(e1.tex[-2].copy(), T2_matrix_with_nums.elements[3]),
            ReplacementTransform(e2.tex[-4].copy(), T2_matrix_with_nums.elements[1]),
            ReplacementTransform(e2.tex[-2].copy(), T2_matrix_with_nums.elements[4]),
            ReplacementTransform(e3.tex[-4].copy(), T2_matrix_with_nums.elements[2]),
            ReplacementTransform(e3.tex[-2].copy(), T2_matrix_with_nums.elements[5]),
            ReplacementTransform(T2_matrix_with_T.brackets, T2_matrix_with_nums.brackets),
            lag_ratio=0.25
        ), run_time=3)
        self.wait(0.5)

        T2_matrix_final = Matrix([
            [1, 0, 0],
            [1, 1, 1]
        ], h_buff=0.75, bracket_v_buff=0.1)
        T2_matrix_final.move_to(T2_matrix_with_nums)

        T2_tex[0].generate_target()
        T2_tex[0].target.next_to(T2_matrix_final, LEFT)

        T2_tex[-1].generate_target()
        T2_tex[-1].target.next_to(T2_matrix_final).shift(0.1*LEFT)


        self.play(
            *[FadeOut(e) for e in (e1.tex, e2.tex, e3.tex)],
            *[ApplyMethod(
                T2_matrix_with_nums.elements[i].move_to, 
                T2_matrix_final.elements[i]) 
                for i in range(6)
            ],
            ReplacementTransform(T2_matrix_with_nums.brackets, T2_matrix_final.brackets),
            MoveToTarget(T2_tex[0]),
            MoveToTarget(T2_tex[-1]),
            run_time=3
        )
        self.wait(2)

        brace = BraceText(T2_matrix_final, "Fylki vörpunarinnar")
        self.play(Write(brace), run_time=2)
        self.wait(1)


class D11_FirstMethod(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_axis_config={"tick_frequency": 0.5}, 
            y_axis_config={"tick_frequency": 0.5}, 
            z_axis_config={"tick_frequency": 0.5}
        ).scale(2)
        self.add(axes)
        axes.z_axis.set_opacity(0)

        e1 = Vector(RIGHT).set_color(GREEN)
        e2 = Vector(UP).set_color(RED)
        self.play(
            ShowCreation(e1), 
            ShowCreation(e2)
        )
        self.wait(2)

        self.play(*[ApplyMethod(mob.shift, 3/2*LEFT) for mob in self.get_mobjects()])
        e1.ghost = e1.copy().scale(3, about_point=e1.get_start()).set_opacity(0.7)
        self.play(
            ShowCreation(e1.ghost),
            run_time=2
        )
        self.wait(1)

        self.play(*[ApplyMethod(mob.shift, 5/2*UP) for mob in self.get_mobjects()])
        e2.ghost = e2.copy().scale(-5, about_point=e2.get_start()).set_opacity(0.7)
        self.play(
            ShowCreation(e2.ghost),
            run_time=2
        )
        self.wait(1)
        self.play(e2.ghost.shift, 3*RIGHT)
        self.wait(2)
        
        v = Vector(np.array([3, -5, 0])).set_color(YELLOW)
        v.shift(3/2*LEFT+5/2*UP)
        self.play(ShowCreation(v))
        self.wait(3)

        v_tex = TexMobject("(3, -5) = 3\\, ", "\\va{e}_1",  "-5\\, ", "\\va{e}_2")
        v_tex.next_to(v.get_end())
        v_tex[-3].set_color(GREEN)
        v_tex[-1].set_color(RED)
        self.play(Write(v_tex))
        self.wait(5)

        self.play(
            *[FadeOutAndShift(g, 3/2*RIGHT+5/2*DOWN) for g in (e1.ghost, e2.ghost, v_tex)],
            *[ApplyMethod(mob.shift, 3/2*RIGHT+5/2*DOWN) 
                for mob in self.get_mobjects() if mob not in (e1.ghost, e2.ghost, v_tex)
            ],
            run_time=2
        )
        self.wait(0.5)

        e1.generate_target()
        e2.generate_target()
        v.generate_target()
        e1.target = Vector(0.45*np.array([1, 2, 3])).set_color(GREEN)
        e2.target = Vector(0.45*np.array([-1, 0, 1])).set_color(RED)
        v.target = Vector(0.45*np.array([8, 6, 4])).set_color(YELLOW)

        T_domain = TexMobject("T: \\mathbb{R}^2 \\to \\mathbb{R}^3")
        T_e1 = TexMobject("T(", "\\va{e}_1", ") = (1, 2, 3)")
        T_e2 = TexMobject("T(", "\\va{e}_2", ") = (-1, 0, 1)")
        T_e1[1].set_color(GREEN)
        T_e2[1].set_color(RED)
        T_def = VGroup(T_domain, T_e1, T_e2).scale(0.8).arrange(DOWN, aligned_edge=LEFT)
        T_def.to_corner(UL).set_opacity(0).add_background_rectangle()
        self.add_fixed_in_frame_mobjects(T_def)
        self.play(T_def.set_opacity, 1)
        self.wait(5)

        self.play(ApplyMethod(axes.z_axis.set_opacity, 1))
        self.wait(1)
        self.move_camera(0.9*PI/2, -0.7*PI/2)

        self.play(
            MoveToTarget(e1),
            MoveToTarget(e2),
            MoveToTarget(v),
            ApplyMethod(axes.scale, 0.45)
        )
        self.wait(3)

        e1.ghost = e1.copy().scale(3, about_point=e1.get_start()).set_opacity(0.7)
        self.play(
            ShowCreation(e1.ghost),
            run_time=2
        )
        self.wait(1)

        e2.ghost = e2.copy().scale(-5, about_point=e1.get_start()).set_opacity(0.7)
        self.play(
            ShowCreation(e2.ghost),
            run_time=2
        )
        self.wait(1)
        self.play(e2.ghost.shift, e1.ghost.get_end())

        Tv_tex = TexMobject(
            "T(3, -5)",  
            "= 3\\, T(", 
            "\\va{e}_1", 
            ") + 5\\, T(", 
            "\\va{e}_2", 
            ")",  
            "= 3(1, 2, 3) - 5(-1, 0, 1)", 
            "= (8, 6, 4)"
        )
        Tv_tex[2].set_color(GREEN)
        Tv_tex[4].set_color(RED)
        Tv_tex.scale(0.7).next_to(T_def, DOWN, aligned_edge=LEFT)
        Tv_tex[6].next_to(Tv_tex[1], DOWN, aligned_edge=LEFT)
        Tv_tex[7].next_to(Tv_tex[6], DOWN, aligned_edge=LEFT)
        Tv_tex.set_opacity(0).add_background_rectangle()
        self.add_fixed_in_frame_mobjects(Tv_tex)

        Tv_tex[:7].set_opacity(1)
        self.play(Write(Tv_tex[:7]))
        self.wait(2)
        Tv_tex[7:].set_opacity(1)
        self.play(Write(Tv_tex[7:]))

        self.wait(1)


class D11_AlternativeMethod(Scene):
    def construct(self):
        alt = TextMobject("Önnur aðferð:").to_corner(UL, buff=0.67).set_color(YELLOW)
        Tv = TexMobject("T(3, -5)", "=")
        T_matrix = Matrix([["T(\\va{e}_1)", "T(\\va{e}_2)"]], h_buff=1.8, bracket_h_buff=SMALL_BUFF)
        vector = Matrix([[3], [-5]], bracket_h_buff=SMALL_BUFF)
        eq = VGroup(Tv, T_matrix, vector).scale(0.8).arrange().center()

        self.play(FadeInFrom(alt, 0.5*LEFT))
        self.wait(1)

        self.play(Write(eq))
        self.wait(3)

        T_matrix_new = Matrix([
            [1, -1],
            [2, 0],
            [3, 1]
        ], bracket_h_buff=SMALL_BUFF).scale(0.8).move_to(T_matrix)

        Tv.generate_target()
        Tv.target.next_to(T_matrix_new, LEFT)
        vector.generate_target()
        vector.target.next_to(T_matrix_new)

        self.play(
            *[ReplacementTransform(o, n) 
                for o, n in zip(
                    [T_matrix.brackets, T_matrix.get_columns()[0], T_matrix.get_columns()[1]], 
                    [T_matrix_new.brackets, T_matrix_new.get_columns()[0], T_matrix_new.get_columns()[1]]
                )
            ],
            MoveToTarget(Tv),
            MoveToTarget(vector)
        )
        eq.remove(T_matrix)
        eq.add(T_matrix_new)

        self.wait(2)

        self.play(eq.shift, 1.5*UP)

        mat_vec_mult = Matrix([
            ["3 \\cdot 1 + (-5) \\cdot (-1)"],
            ["3 \\cdot 2 + (-5) \\cdot 0"],
            ["3 \\cdot 3 + (-5) \\cdot 1"]
        ], bracket_h_buff=SMALL_BUFF, element_alignment_corner=DL)

        next_eq = VGroup(TexMobject("="), mat_vec_mult)
        next_eq.scale(0.8).arrange().next_to(Tv[1], DOWN, aligned_edge=LEFT, buff=1.5)

        self.play(Write(next_eq))

        self.wait(4)
        
        mat_vec_res = Matrix([[8], [6], [4]], bracket_h_buff=SMALL_BUFF).scale(0.8)
        mat_vec_res.move_to(mat_vec_mult, aligned_edge=LEFT)

        self.play(
            *[ReplacementTransform(mat_vec_mult.elements[i], mat_vec_res.elements[i]) for i in range(3)],
            ReplacementTransform(mat_vec_mult.brackets, mat_vec_res.brackets)
        )
        self.wait(1)


class D11_Part2D(LinearTransformationScene, MovingCameraScene):
    CONFIG = {
        "show_basis_vectors": False,
        "foreground_plane_kwargs": {
            "x_max": 1.5*FRAME_WIDTH,
            "x_min": -1.5*FRAME_WIDTH,
            "y_max": 1.5*FRAME_WIDTH,
            "y_min": -1.5*FRAME_WIDTH,
            "faded_line_ratio": 0
        },
        "background_plane_kwargs": {
            "x_max": 1.5*FRAME_WIDTH,
            "x_min": -1.5*FRAME_WIDTH,
            "y_max": 1.5*FRAME_WIDTH,
            "y_min": -1.5*FRAME_WIDTH,
        },
    }

    def construct(self):
        v1 = Vector(RIGHT+UP).set_color(YELLOW)
        v2 = Vector(RIGHT+DOWN).set_color(PINK)
        self.add_vector(v1)
        self.add_vector(v2)
        self.wait(2)

        T_domain = TexMobject("T: \\mathbb{R}^2 \\to \\mathbb{R}^2")
        T_e1 = TexMobject("T(", "1, 1", ") = (2, 3)")
        T_e2 = TexMobject("T(", "1, -1", ") = (1, 0)")
        T_e1[1].set_color(YELLOW)
        T_e2[1].set_color(PINK)
        T_def = VGroup(T_domain, T_e1, T_e2).scale(0.8).arrange(DOWN, aligned_edge=LEFT)
        T_def.to_corner(UL).add_background_rectangle()
        self.play(FadeIn(T_def))
        self.wait(4)

        transformation_matrix = [[1.5, 0.5], [1.5, 1.5]]
        self.apply_matrix(transformation_matrix, run_time=3)
        self.wait(3)
        self.apply_inverse(transformation_matrix, run_time=1)
        self.wait(1)

        v3 = Vector(3*RIGHT-5*UP).set_color(ORANGE)
        self.play(self.camera.frame.set_width, 20)
        self.add_vector(v3)
        self.wait(2)

        ghost_expl1 = TexMobject("(", "3, -5", ") =", "c_1", "(", "1, 1", ") +", "c_2", "(", "1, -1", ")")
        ghost_expl2 = TexMobject("c_1 + c_2 = 3 \\quad \\wedge \\quad c_1 - c_2 = -5")
        ghost_expl3 = TexMobject("2c_1 = -2 \\quad \\wedge \\quad 2c_2 = 8")
        ghost_expl4 = TexMobject("c_1 =", "-1", "\\quad \\wedge \\quad", "c_2 =", "4")

        VGroup(ghost_expl1, ghost_expl2, ghost_expl3, ghost_expl4) \
            .arrange(DOWN, aligned_edge=LEFT) \
            .next_to(T_def, DOWN, buff=0.8)

        for g in (ghost_expl1, ghost_expl2, ghost_expl3, ghost_expl4):
            g.add_background_rectangle()

        ghost_expl1[2].set_color(ORANGE)
        ghost_expl1[6].set_color(YELLOW)
        ghost_expl1[10].set_color(PINK)

        self.play(Write(ghost_expl1))
        self.wait(2)
        self.play(Write(ghost_expl2))
        self.wait(2)
        self.play(Write(ghost_expl3))
        self.wait(2)
        self.play(Write(ghost_expl4))
        self.wait(3)

        v1.ghost = v1.copy().scale(-1, about_point=ORIGIN).set_opacity(0.75)
        v2.ghost = v2.copy().scale(4, about_point=ORIGIN).set_opacity(0.75)
        self.play(
            ShowCreation(v1.ghost),
            ShowCreation(v2.ghost),
            run_time=2.5
        )
        self.wait(0.5)
        self.play(v2.ghost.shift, v1.ghost.get_end())

        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in (ghost_expl1, ghost_expl2, ghost_expl3, ghost_expl4, v1.ghost, v2.ghost)]
        )
        self.apply_matrix(transformation_matrix)
        self.wait(2)

        v1.ghost = v1.copy().scale(-1, about_point=ORIGIN).set_opacity(0.75)
        v2.ghost = v2.copy().scale(4, about_point=ORIGIN).set_opacity(0.75)
        self.play(
            ShowCreation(v1.ghost),
            ShowCreation(v2.ghost),
            run_time=2.5
        )
        self.wait(0.5)
        self.play(v2.ghost.shift, v1.ghost.get_end())
        self.wait(3)

        get_it = TexMobject(
            "T(", "3, -5", ")", "= -T(", "1, 1", ") + 4T(", "1, -1", ")",
            "= -(2, 3) + 4(1, 0)", "= (2, -3)"
        )
        get_it[1].set_color(ORANGE)
        get_it[4].set_color(YELLOW)
        get_it[6].set_color(PINK)
        get_it[8].next_to(get_it[3], DOWN, aligned_edge=LEFT)
        get_it[9].next_to(get_it[8], DOWN, aligned_edge=LEFT)
        get_it.to_corner(UL).shift(1.5*UL+0.5*LEFT).add_background_rectangle()

        self.play(
            FadeOut(T_def),
            Write(get_it)
        )
        self.wait(1)


class D12_Question(Scene):
    def construct(self):
        A = Matrix([
            [1, 2, 3],
            [-1, 0, 0]
        ])

        B = Matrix([
            [1, 2],
            ["\\tfrac{1}{2}", 3]
        ])

        C = Matrix([
            [-1, 0],
            [2, 5],
            [0, 3]
        ])

        A.tex = TexMobject("A", "=")
        B.tex = TexMobject("B", "=")
        C.tex = TexMobject("C", "=")
        A.tex[0].set_color(RED)
        B.tex[0].set_color(BLUE)
        C.tex[0].set_color(YELLOW)

        VGroup(
            VGroup(A.tex, A).scale(0.8).arrange(),
            VGroup(B.tex, B).scale(0.8).arrange(),
            VGroup(C.tex, C).scale(0.8).arrange()
        ).arrange(buff=1.2).to_edge(UP, buff=1)

        question1 = TextMobject("Eru eftirfarandi fylkjamargfeldi skilgreind?").scale(0.8)
        question2 = TextMobject("Hver er útkoman?").scale(0.8)

        AB = TexMobject("A", "B")
        BB = TexMobject("B", "^2")
        CB = TexMobject("C", "B")
        AB[0].set_color(RED)
        AB[1].set_color(BLUE)
        BB[0].set_color(BLUE)
        BB[1].set_color(BLUE)
        CB[0].set_color(YELLOW)
        CB[1].set_color(BLUE)

        VGroup(AB, BB, CB).arrange(buff=1).next_to(question1, DOWN, buff=0.75)
        question2.next_to(BB, DOWN, buff=0.75)

        self.play(AnimationGroup(
            ShowCreation(A), ShowCreation(A.tex), 
            ShowCreation(B), ShowCreation(B.tex), 
            ShowCreation(C), ShowCreation(C.tex),
            lag_ratio=0.1,
            run_time=2
        ))
        self.wait(2)

        self.play(Write(question1))
        self.play(AnimationGroup(
            Write(AB), Write(BB), Write(CB),
            lag_ratio=0.1
        ))

        self.wait(20)

        A_size = TexMobject("2", "\\times", "3").scale(0.8).next_to(A, DOWN).set_color(RED)
        B_size = TexMobject("2", "\\times", "2").scale(0.8).next_to(B, DOWN).set_color(BLUE)
        C_size = TexMobject("3", "\\times", "2").scale(0.8).next_to(C, DOWN).set_color(YELLOW)

        self.play(Write(A_size))
        self.wait(1)
        self.play(Write(B_size))
        self.wait(1)
        self.play(Write(C_size))
        self.wait(5)

        for m in (AB, BB, CB):
            m.rect = SurroundingRectangle(m)

        self.play(ShowCreation(AB.rect))
        self.wait(1)
        self.play(
            ShowCreationThenDestructionAround(B_size[0]),
            ShowCreationThenDestructionAround(A_size[2]), 
            run_time=5,
            rate_func=double_smooth
        )
        self.wait(2)
        AB.cross = Cross(AB)
        self.play(AnimationGroup(
            Uncreate(AB.rect),
            ShowCreation(AB.cross),
            lag_ratio=0.5,
            run_time=1.5
        ))
        self.wait(4)
        self.play(ShowCreation(BB.rect))
        self.wait(0.5)
        self.play(
            ShowCreationThenDestructionAround(B_size[0]), 
            ShowCreationThenDestructionAround(B_size[2]),
            run_time=4,
            rate_func=double_smooth
        )
        self.play(Uncreate(BB.rect))
        self.wait(2)

        self.play(ShowCreation(CB.rect))
        self.wait(0.5)
        self.play(
            ShowCreationThenDestructionAround(B_size[0]),
            ShowCreationThenDestructionAround(C_size[2]), 
            run_time=4,
            rate_func=double_smooth
        )
        self.play(Uncreate(CB.rect))
        self.wait(5)

        self.play(Write(question2))



class D12_WhatDoesItMean(LinearTransformationScene):
    CONFIG = {
        "show_basis_vectors": False,
        "foreground_plane_kwargs": {
            "x_max": 1.5*FRAME_WIDTH,
            "x_min": -1.5*FRAME_WIDTH,
            "y_max": 1.5*FRAME_WIDTH,
            "y_min": -1.5*FRAME_WIDTH,
            "faded_line_ratio": 0
        },
    }

    def construct(self):
        question = TextMobject("Hvað þýðir fylkjamargföldun?") \
            .scale(0.8).to_corner(UL).add_background_rectangle()
        self.play(FadeInFrom(question, 0.5*LEFT))
        self.wait(2)

        vector = Vector(RIGHT+2*UP).set_color(YELLOW)
        self.add_vector(vector)
        self.wait(2)

        first_matrix = [[0, -1], [1, 0]]
        second_matrix = [[1, 1], [0, 1]]
        mat_mult = np.matmul(second_matrix, first_matrix)

        first_then = TextMobject("Fyrst ", "$B$", "svo ", "$A$") \
            .scale(0.8).next_to(question, DOWN, buff=1, aligned_edge=LEFT) \
            .shift(0.5*RIGHT)
        first_then[-2:].next_to(first_then[:-2], DOWN, aligned_edge=RIGHT)
        first_then[-2:].add_background_rectangle()
        first_then[:-2].add_background_rectangle()
        AB = TexMobject("A", "B") \
            .scale(0.8).next_to(first_then, buff=1.2)
        brace = Brace(first_then, RIGHT, buff=0.4)

        self.play(Write(first_then[:2]))
        self.apply_matrix(first_matrix)
        self.wait(0.5)

        self.play(Write(first_then[2:]))
        self.apply_matrix(second_matrix)
        self.wait(2)
        ghost = vector.copy().set_opacity(0.5)
        self.add(ghost)

        self.apply_inverse(mat_mult, run_time=1.2)
        self.wait(1)

        self.play(ShowCreation(brace))
        self.play(
            ReplacementTransform(first_then[1].copy(), AB[1]),
            ReplacementTransform(first_then[3].copy(), AB[0]),
            run_time=1.5
        )
        self.wait(0.5)
        self.apply_matrix(mat_mult)
        self.wait(1)


class D12_WhenDefined(Scene):
    def construct(self):
        question = TextMobject("Hvenær er fylkjamargföldun skilgreind?") \
            .scale(0.8).to_corner(UL)

        A = TexMobject("A", "n \\times m")
        A[0].move_to(2*LEFT+UP)
        A[1].scale(0.8).next_to(A[0], DOWN, buff=0.2)

        B = TexMobject("B", "p \\times q")
        B[0].move_to(2*RIGHT+UP)
        B[1].scale(0.8).next_to(B[0], DOWN, buff=0.2)

        self.play(FadeInFrom(question, 0.5*LEFT))
        self.wait(1)

        self.play(Write(A[0]))
        self.wait(0.5)
        self.play(Write(A[1]))
        self.wait(3)

        self.play(Write(B[0]))
        self.wait(0.5)
        self.play(Write(B[1]))
        self.wait(3)

        vec = TexMobject("\\va{x}")
        vec.next_to(A[0], buff=SMALL_BUFF)

        self.play(FadeInFrom(vec, 0.1*RIGHT))
        self.wait(1)

        Rm_to_Rn = TexMobject("\\mathbb{R}^m", "\\to", "\\mathbb{R}^n")
        Rm_to_Rn.scale(0.8).next_to(A, DOWN)
        self.play(Write(Rm_to_Rn))

        self.wait(1)
        self.play(FadeOutAndShift(vec, 0.1*RIGHT))
        self.wait(3)
        vec.next_to(B[0], buff=SMALL_BUFF)

        self.play(FadeInFrom(vec, 0.1*RIGHT))
        self.wait(1)

        Rq_to_Rp = TexMobject("\\mathbb{R}^q", "\\to", "\\mathbb{R}^p")
        Rq_to_Rp.scale(0.8).next_to(B, DOWN)
        self.play(Write(Rq_to_Rp))

        self.wait(1)
        self.play(FadeOutAndShift(vec, 0.1*RIGHT))
        self.wait(5)

        AB = TexMobject("A", "B").move_to(UP)

        self.play(
            ReplacementTransform(A[0].copy(), AB[0]),
            ReplacementTransform(B[0].copy(), AB[1])
        )
        self.wait(1)

        vec.next_to(AB, buff=SMALL_BUFF)

        self.play(FadeInFrom(vec, 0.1*RIGHT))
        self.wait(1)

        self.play(
            MoveAlongPath(
                vec, 
                ArcBetweenPoints(
                    vec.get_center(), 
                    Rq_to_Rp.get_left()+0.5*DOWN+0.2*RIGHT,
                )
            ),
        )
        self.wait(1)
        vec.generate_target()
        vec.target = TexMobject("B\\va{x}").scale(0.8).move_to(Rq_to_Rp.get_right()+0.5*DOWN-0.2*RIGHT)
        self.play(MoveToTarget(vec), run_time=2)
        self.wait(3)

        self.play(
            MoveAlongPath(
                vec, 
                ArcBetweenPoints(
                    vec.get_center(), 
                    Rm_to_Rn.get_left()+0.5*DOWN+0.2*RIGHT,
                    angle=-PI/2
                )
            )
        )
        self.wait(1)
        vec.generate_target()
        vec.target = TexMobject("A", "B", "\\va{x}").scale(0.8).move_to(Rm_to_Rn.get_right()+0.5*DOWN-0.2*RIGHT)
        self.play(MoveToTarget(vec), run_time=2)
        self.wait(4)

        vec_bef = vec[-1].copy().move_to(Rq_to_Rp.get_left()+0.5*DOWN+0.2*RIGHT)
        self.play(
            ReplacementTransform(vec[-1].copy(), vec_bef)
        )
        self.wait(0.5)
        Rq_rect = SurroundingRectangle(Rq_to_Rp[0])
        Rm_rect = SurroundingRectangle(Rm_to_Rn[-1])
        self.play(
            ShowCreationThenDestructionAround(Rq_to_Rp[0]),
            run_time=2
        )
        self.wait(1)
        self.play(
            ShowCreationThenDestructionAround(Rm_to_Rn[-1]),
            run_time=2
        )
        self.wait(4)

        AB_size = TexMobject("n \\times q").scale(0.8).next_to(AB, DOWN, buff=0.2)

        self.play(Write(AB_size))
        self.wait(3)

        vec.generate_target()
        vec.target = TexMobject("B\\va{x}").scale(0.8).move_to(Rm_to_Rn.get_left()+0.5*DOWN+0.2*RIGHT)

        vec_bef.generate_target()
        vec_bef.target = TexMobject("B\\va{x}").scale(0.8).move_to(Rq_to_Rp.get_right()+0.5*DOWN-0.2*RIGHT)

        self.play(
            MoveToTarget(vec),
            MoveToTarget(vec_bef),
            run_time=1.5
        )

        self.wait(2)
        self.play(
            ShowCreationThenDestructionAround(Rq_to_Rp[-1]),
            run_time=2
        )
        self.wait(1)
        self.play(
            ShowCreationThenDestructionAround(Rm_to_Rn[0]),
            run_time=2
        )
        self.wait(3)

        result = TextMobject("Aðeins skilgreind ef ", "$m=p$").scale(0.8).move_to(2*DOWN)
        result[1].set_color(YELLOW)

        self.play(Write(result))
        self.wait(1)


class D12_Multiply(Scene):
    def construct(self):
        calculate = TextMobject("Reiknum margfeldin:").scale(0.8).to_corner(UL)

        BB_tex = TexMobject(
            "B^2", 
            "= \\begin{bmatrix} 1 & 2 \\\\ \\tfrac{1}{2} & 3 \\end{bmatrix}",
            "\\begin{bmatrix} 1 & 2 \\\\ \\tfrac{1}{2} & 3 \\end{bmatrix}",
            """ = \\begin{bmatrix} 
                1 \\cdot 1 + 2 \\cdot \\nicefrac{1}{2} & 1 \\cdot 2 + 2 \\cdot 3 \\\\
                \\nicefrac{1}{2} \\cdot 1 + 3 \\cdot \\nicefrac{1}{2} & \\nicefrac{1}{2} \\cdot 2 + 3 \\cdot 3
            \\end{bmatrix}""",
            "= \\begin{bmatrix} 2 & 8 \\\\ 2 & 10 \\end{bmatrix}"
        )
        BB_tex[0].set_color(BLUE)
        BB_tex[3].next_to(BB_tex[1], DOWN, aligned_edge=LEFT)
        BB_tex[4].next_to(BB_tex[3], DOWN, aligned_edge=LEFT)
        BB_tex.scale(0.75).move_to(0.5*LEFT+2.5*UP, aligned_edge=UR)

        self.play(FadeInFrom(calculate, 0.5*LEFT))
        self.wait(2.5)

        self.play(Write(BB_tex[:3]))
        self.wait(1)
        self.play(Write(BB_tex[3]))
        self.wait(1.5)
        self.play(Write(BB_tex[4]))
        self.wait(5)

        CB_tex = TexMobject(
            "C", "B", 
            "= \\begin{bmatrix} -1 & 0 \\\\ 2 & 5 \\\\ 0 & 3 \\end{bmatrix}",
            "\\begin{bmatrix} 1 & 2 \\\\ \\tfrac{1}{2} & 3 \\end{bmatrix}",
            """ = \\begin{bmatrix} 
                -1 \\cdot 1 + 0 \\cdot \\nicefrac{1}{2} & -1 \\cdot 2 + 0 \\cdot 3 \\\\
                2 \\cdot 1 + 5 \\cdot \\nicefrac{1}{2} & 2 \\cdot 2 + 5 \\cdot 3 \\\\
                0 \\cdot 1 + 3 \\cdot \\nicefrac{1}{2} & 0 \\cdot 2 + 3 \\cdot 3
            \\end{bmatrix}""",
            "= \\begin{bmatrix} -1 & -2 \\\\ \\nicefrac{9}{2} & 19 \\\\ \\nicefrac{3}{2} & 9 \\end{bmatrix}"
        )
        CB_tex[0].set_color(YELLOW)
        CB_tex[1].set_color(BLUE)
        CB_tex[4].next_to(CB_tex[2], DOWN, aligned_edge=LEFT)
        CB_tex[5].next_to(CB_tex[4], DOWN, aligned_edge=LEFT)
        CB_tex.scale(0.75).move_to(0.5*RIGHT+2.5*UP, aligned_edge=UL)

        self.play(Write(CB_tex[:4]))
        self.wait(1)
        self.play(Write(CB_tex[4]))
        self.wait(1.5)
        self.play(Write(CB_tex[5]))
        self.wait(5)


class D12_Invertible(Scene):
    def construct(self):
        A_def = TextMobject("Látum ", "$A \\coloneqq \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}$.")
        A_def.scale(0.8).to_corner(UL)
        question = TextMobject("Hvenær er $A$ víxlið við $\\begin{bmatrix} 0 & 1 \\\\ 0 & 0 \\end{bmatrix}$?")
        question.scale(0.8).next_to(A_def)

        first_mult = TexMobject(
            """\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} 
            \\begin{bmatrix} 0 & 1 \\\\ 0 & 0 \\end{bmatrix}""",
            """\\begin{bmatrix} 
                a \\cdot 0 + b \\cdot 0 & a \\cdot 1 + b \\cdot 0 \\\\ 
                c \\cdot 0 + d \\cdot 0 & c \\cdot 1 + d \\cdot 0 
            \\end{bmatrix}""",
            "\\begin{bmatrix} 0 & a \\\\ 0 & c \\end{bmatrix}"
        )
        first_mult.arrange(DOWN, aligned_edge=LEFT)
        first_mult.scale(0.75).move_to(LEFT+1.5*UP, aligned_edge=UR)

        second_mult = TexMobject(
            """\\begin{bmatrix} 0 & 1 \\\\ 0 & 0 \\end{bmatrix} 
            \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}""",
            """\\begin{bmatrix} 
                0 \\cdot a + 1 \\cdot c & 0 \\cdot b + 1 \\cdot d \\\\ 
                0 \\cdot a + 0 \\cdot c & 0 \\cdot b + 0 \\cdot d
            \\end{bmatrix}""",
            "\\begin{bmatrix} c & d \\\\ 0 & 0 \\end{bmatrix}"
        )
        second_mult.arrange(DOWN, aligned_edge=LEFT)
        second_mult.scale(0.75).move_to(RIGHT+1.5*UP, aligned_edge=UL)

        eqs = VGroup()
        for m in (first_mult[1], second_mult[1], first_mult[2], second_mult[2]):
            eqs.add(TexMobject("=").next_to(m, LEFT))

        self.play(Write(A_def))
        self.wait(1)
        self.play(Write(question))
        self.wait(3)

        self.play(
            ShowCreation(first_mult[0]),
            ShowCreation(second_mult[0])
        )
        self.wait(1)

        self.play(
            Write(eqs[0]),
            Write(eqs[1]),
            ShowCreation(first_mult[1]),
            ShowCreation(second_mult[1]),
            run_time=1.5
        )
        self.wait(1)

        self.play(
            Write(eqs[2]),
            Write(eqs[3]),
            ShowCreation(first_mult[2]),
            ShowCreation(second_mult[2]),
            run_time=1.5
        )
        self.wait(3)

        mat1 = first_mult[-1].copy().scale(1/0.8).move_to(LEFT)
        mat2 = second_mult[-1].copy().scale(1/0.8).move_to(RIGHT)
        self.play(
            *[FadeOut(mob) for mob in (first_mult[:-1], second_mult[:-1], eqs)],
            ReplacementTransform(first_mult[-1], mat1),
            ReplacementTransform(second_mult[-1], mat2),
            run_time=2.5
        )
        self.wait(1)

        eq = TexMobject("=").rotate(PI)
        self.play(Write(eq))
        self.wait(3)

        a_is_d = TexMobject("a = d").shift(1.5*DOWN)
        c_is_zero = TexMobject("c = 0").next_to(a_is_d, DOWN)

        self.play(FadeInFrom(a_is_d, 0.2*UP))
        self.wait(1)
        self.play(FadeInFrom(c_is_zero, 0.2*UP))
        self.wait(1)


class D12_SquareMatrices(Scene):
    def construct(self):
        question1 = TextMobject("Látum $A$, $B$ og $C$ vera fylki þannig að $AB=C$.")
        question2 = TextMobject("Ef tvö fylkjana eru ferningsfylki er það síðasta það líka?")
        question1.scale(0.8).to_corner(UL)
        question2.scale(0.8).next_to(question1, DOWN, aligned_edge=LEFT)

        self.play(Write(question1))
        self.wait(1)
        self.play(Write(question2))
        self.wait(1)

        A = TexMobject("A").shift(1.5*LEFT+0.5*UP)
        B = TexMobject("B").shift(0.5*UP)
        C = TexMobject("C").shift(1.5*RIGHT+0.5*UP)
        cdot = TexMobject("\\cdot").move_to(mid(A.get_center(), B.get_center()))
        eq = TexMobject("=").move_to(mid(B.get_center(), C.get_center()))

        n_cross_n = TexMobject("n", "\\times", "n").scale(0.8)
        m_cross_m = TexMobject("m", "\\times", "m").scale(0.8)
        buwah = TexMobject("?\\, \\, ", "\\times", "\\, \\, ?").scale(0.8)
        buwah[1].move_to(buwah.get_center())

        self.play(AnimationGroup(
            Write(A), 
            FadeInFrom(cdot, 0.2*DOWN),
            Write(B), 
            FadeInFrom(eq, 0.2*DOWN),
            Write(C),
            lag_ratio=0.2
        ))
        self.wait(1)

        part1 = TextMobject("(i)")
        part2 = TextMobject("(ii)")
        part3 = TextMobject("(iii)")
        VGroup(part1, part2, part3).scale(0.7).arrange(DOWN, buff=0.4) \
            .next_to(A, LEFT, aligned_edge=UR).shift(DL)

        self.play(Write(part1))
        n1 = n_cross_n.copy().set_x(A.get_x()).set_y(part1.get_y())
        m1 = m_cross_m.copy().set_x(B.get_x()).set_y(part1.get_y())
        b1 = buwah.copy().set_x(C.get_x()).set_y(part1.get_y())
        self.play(AnimationGroup(
            Write(n1),
            Write(m1),
            Write(b1),
            lag_ratio=0.5
        ))
        self.wait(2)

        self.play(Write(part2))
        n2 = n_cross_n.copy().set_x(A.get_x()).set_y(part2.get_y())
        m2 = m_cross_m.copy().set_x(C.get_x()).set_y(part2.get_y())
        b2 = buwah.copy().set_x(B.get_x()).set_y(part2.get_y())
        self.play(AnimationGroup(
            Write(n2),
            Write(m2),
            Write(b2),
            lag_ratio=0.5
        ))
        self.wait(2)

        self.play(Write(part3))
        n3 = n_cross_n.copy().set_x(B.get_x()).set_y(part3.get_y())
        m3 = m_cross_m.copy().set_x(C.get_x()).set_y(part3.get_y())
        b3 = buwah.copy().set_x(A.get_x()).set_y(part3.get_y())
        self.play(AnimationGroup(
            Write(n3),
            Write(m3),
            Write(b3),
            lag_ratio=0.5
        ))
        self.wait(5)

        self.play(
            ShowCreationThenDestructionAround(n1[2]),
            ShowCreationThenDestructionAround(m1[0]),
            run_time=4,
            rate_func=double_smooth
        )
        self.wait(1)
        m1.generate_target()
        m1.target = n1.copy().move_to(m1)
        self.play(ReplacementTransform(m1, m1.target))
        self.wait(1)

        self.play(AnimationGroup(
            FadeOut(b1[0]),
            FadeOut(b1[2]),
            MoveAlongPath(n1[0].copy(), ArcBetweenPoints(n1[0].get_center(), b1[0].get_center(), aligned_edge=DOWN, angle=PI/4)),
            MoveAlongPath(m1[2].copy(), ArcBetweenPoints(m1[2].get_center(), b1[2].get_center(), aligned_edge=DOWN, angle=PI/4)),
            lag_ratio=0.2,
            run_time=2
        ))
        self.wait(5)

        self.play(
            ShowCreationThenDestructionAround(n2[0]),
            ShowCreationThenDestructionAround(m2[0]),
            run_time=4,
            rate_func=double_smooth
        )
        self.wait(1)
        m2.generate_target()
        m2.target = n2.copy().move_to(m2)
        self.play(ReplacementTransform(m2, m2.target))
        self.wait(1)

        self.play(AnimationGroup(
            FadeOut(b2[0]),
            FadeOut(b2[2]),
            MoveAlongPath(n2[2].copy(), ArcBetweenPoints(n2[2].get_center(), b2[0].get_center(), aligned_edge=DOWN, angle=PI/4)),
            MoveAlongPath(m2[2].copy(), ArcBetweenPoints(m2[2].get_center(), b2[2].get_center(), aligned_edge=DOWN, angle=-PI/4)),
            lag_ratio=0.2,
            run_time=2
        ))
        self.wait(5)

        self.play(
            ShowCreationThenDestructionAround(n3[2]),
            ShowCreationThenDestructionAround(m3[2]),
            run_time=4,
            rate_func=double_smooth
        )
        self.wait(1)
        m3.generate_target()
        m3.target = n3.copy().move_to(m3)
        self.play(ReplacementTransform(m3, m3.target))
        self.wait(1)

        self.play(AnimationGroup(
            FadeOut(b3[0]),
            FadeOut(b3[2]),
            MoveAlongPath(m3[0].copy(), ArcBetweenPoints(m3[0].get_center(), b3[0].get_center(), aligned_edge=DOWN, angle=-PI/4)),
            MoveAlongPath(n3[0].copy(), ArcBetweenPoints(n3[0].get_center(), b3[2].get_center(), aligned_edge=DOWN, angle=-PI/4)),
            lag_ratio=0.2,
            run_time=2
        ))
        self.wait(5)
        



