import bpy

# Function to ensure correct context for conversion
def convert_to_mesh(obj):
    bpy.ops.object.mode_set(mode='OBJECT')  # Ensure we're in object mode
    bpy.ops.object.select_all(action='DESELECT')  # Deselect all objects
    bpy.context.view_layer.objects.active = obj  # Set the active object to our target
    obj.select_set(True)  # Select the object
    bpy.ops.object.convert(target='MESH')  # Convert the selected object to a mesh

# Function to clear existing mesh objects
def clear_mesh_objects():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

# Function to create an egg
def create_egg():
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
    egg = bpy.context.object
    egg.scale = (0.7, 0.7, 1)
    egg.name = 'Egg'
    return egg

# Function to create a simple chicken model
def create_chicken():
    # Body
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(-2, 0, 0))
    chicken_body = bpy.context.object
    chicken_body.scale = (1, 1.2, 1)
    chicken_body.name = 'ChickenBody'

    # Head
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.6, location=(-3, 0, 1))
    chicken_head = bpy.context.object
    chicken_head.name = 'ChickenHead'

    # Beak
    bpy.ops.mesh.primitive_cone_add(radius1=0.2, depth=0.4, location=(-3.5, 0, 1))
    chicken_beak = bpy.context.object
    chicken_beak.rotation_euler = (0, 0, 1.5708)  # Rotate to face forward
    chicken_beak.name = 'ChickenBeak'

    # Tail
    bpy.ops.mesh.primitive_cone_add(radius1=0.5, depth=0.8, location=(-1.2, 0, 0.5))
    chicken_tail = bpy.context.object
    chicken_tail.rotation_euler = (0, 0, -1.5708)  # Rotate to face backward
    chicken_tail.name = 'ChickenTail'

    # Joining parts
    for obj in [chicken_head, chicken_beak, chicken_tail]:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = chicken_body
    bpy.ops.object.join()  # Join selected objects into one

    return chicken_body

# Main function to run the script
def main():
    clear_mesh_objects()
    egg = create_egg()
    chicken = create_chicken()

    # Material assignments (optional)
    # Egg material
    egg_material = bpy.data.materials.new(name="EggMaterial")
    egg_material.diffuse_color = (1, 1, 0.8, 1)  # Soft yellow
    egg.data.materials.append(egg_material)

    # Chicken material
    chicken_material = bpy.data.materials.new(name="ChickenMaterial")
    chicken_material.diffuse_color = (1, 0.8, 0.5, 1)  # Soft orange
    chicken.data.materials.append(chicken_material)

# Execute the main function
main()
