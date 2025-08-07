import cadquery as cq

# Cube 10x10x10
result_cube = cq.Workplane("XY").box(10, 10, 10)

# cylinder
result_cylinder = cq.Workplane("XY").circle(5).extrude(20)

# cut_sphere
cube = cq.Workplane("XY").box(20, 20, 20)
sphere = cq.Workplane("XY").sphere(11)
result_cut_sphere = cube.cut(sphere)

# plate_with_hole
result_plate_with_hole = (
    cq.Workplane("XY")
    .box(60, 40, 5)
    .faces(">Z")
    .workplane()
    .hole(10)
)
# Show object
show_object(result_cut_sphere)
