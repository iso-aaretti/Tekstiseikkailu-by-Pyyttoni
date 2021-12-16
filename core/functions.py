def get_scene_from_id(idf, scenes):
    for scene in scenes:
        if idf == scene.id:
            return scene


def try_scene_change(active_scene, scenes, command, player):
    changed_scene = False
    if command == "a":
        if active_scene.exit_a is not None:
            active_scene.set_leave_scene()
            active_scene = get_scene_from_id(active_scene.exit_a, scenes)
            changed_scene = True
    elif command == "b":
        if active_scene.exit_b is not None:
            active_scene.set_leave_scene()
            active_scene = get_scene_from_id(active_scene.exit_b, scenes)
            changed_scene = True
    elif command == "c":
        if active_scene.exit_c is not None:
            active_scene.set_leave_scene()
            active_scene = get_scene_from_id(active_scene.exit_c, scenes)
            changed_scene = True
    if changed_scene:
        description = active_scene.get_description(player)
    else:
        description = "Väärä syöttö"
    return active_scene, description


def activate_object(scene, inventory, object_name, player):
    description = ""
    for scene_object in scene.objects:
        if object_name == scene_object.name:
            result = scene.activate_object(scene_object, player)
            scene = result[0]
            description = result[1]
            player = result[2]
        else:
            for alias in scene_object.aliases:
                if object_name == alias:
                    result = scene.activate_object(scene_object, player)
                    scene = result[0]
                    description = result[1]
                    player = result[2]

    for inv_object in inventory:
        if object_name == inv_object.name:
            description = inv_object.activate_description
            player = inv_object.set_player_flag_on_activate(player)
            if inv_object.change_on_activate_object is not None:
                new_object = inv_object.change_on_activate_object
                inventory[:] = [x for x in inventory if not (x.name == inv_object.name)]
                inventory.append(new_object)
            elif inv_object.should_remove_on_activate:
                inventory[:] = [x for x in inventory if not (x.name == inv_object.name)]

        else:
            for alias in inv_object.aliases:
                if object_name == alias:
                    description = inv_object.activate_description
                    player = inv_object.set_player_flag_on_activate(player)
                    if inv_object.change_on_activate_object is not None:
                        new_object = inv_object.change_on_activate_object
                        inventory[:] = [x for x in inventory if not (x.name == inv_object.name)]
                        inventory.append(new_object)
                    elif inv_object.should_remove_on_activate:
                        inventory[:] = [x for x in inventory if not (x.name == inv_object.name)]

    return scene, inventory, player, description
