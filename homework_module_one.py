import cadquery as cq


def generate_flashcase(
    length=60,
    width=20,
    height=10,
    wall_thickness=1.5,
    fillet_radius=2,
    usb_width=12,
    usb_height=5
):
    # Step 1: Building the Basic Hull
    model = cq.Workplane("XY").box(length, width, height)

    # Step 2: Cut out the inner cavity (shell)
    model = model.faces(">Z").shell(-wall_thickness)

    # Step 3: Filleting the vertical edges
    model = model.edges("|Z").filter(
        lambda e: e.Length() > 5).fillet(fillet_radius)

    # Step 4: Cutout for USB port
    usb_offset_x = -length / 2 + wall_thickness / 2
    usb_offset_z = height / 2 - usb_height / 2

    usb_cut = (
        cq.Workplane("XY")
        .transformed(offset=(usb_offset_x, 0, usb_offset_z))
        .box(wall_thickness + 1, usb_width, usb_height)
    )

    model = model.cut(usb_cut)

    return model


model = generate_flashcase(
    length=70,
    width=24,
    height=12,
    wall_thickness=2,
    fillet_radius=3,
    usb_width=13,
    usb_height=5.5
)

# show_object(model)
