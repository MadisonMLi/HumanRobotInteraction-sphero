async def start_program():
    set_main_led({'r': 20, 'g': 255, 'b': 14})
    await speak('Hi, do you want to play a game? Kick me to start ', True)
    set_heading(0)
async def on_charging():
    pass
register_event(EventType.ON_CHARGING, on_charging)
async def on_collision():
    while not (get_ambient_light() <= 20):
        set_main_led({'r': 85, 'g': 101, 'b': 255})
        set_speed(120)
        await Sound.Effects.BeepDouble.play(True)
        await delay(2)
        set_main_led({'r': 255, 'g': 13, 'b': 0})
        set_heading(get_heading() + 180)
        set_speed(get_speed() + 10)
        await delay(1)
        await delay(0.025)
    stop_roll()
    await speak('too dark, i can\'t see', True)
    await delay(0.2)
    play_matrix_animation(0, False)
    await delay(1)
    await speak('I am going to sleep', True)
    await delay(1)
    exit_program()
register_event(EventType.ON_COLLISION, on_collision)
register_matrix_animation({'frames': [[[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1]],
    [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1]],
    [[1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]],
    [[1, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]], 'palette': [{'r': 255, 'g': 255, 'b': 255},
    {'r': 0, 'g': 0, 'b': 0},
    {'r': 255, 'g': 0, 'b': 0},
    {'r': 255, 'g': 64, 'b': 0},
    {'r': 255, 'g': 128, 'b': 0},
    {'r': 255, 'g': 191, 'b': 0},
    {'r': 255, 'g': 255, 'b': 0},
    {'r': 185, 'g': 246, 'b': 30},
    {'r': 0, 'g': 255, 'b': 0},
    {'r': 185, 'g': 255, 'b': 255},
    {'r': 0, 'g': 255, 'b': 255},
    {'r': 0, 'g': 0, 'b': 255},
    {'r': 145, 'g': 0, 'b': 211},
    {'r': 157, 'g': 48, 'b': 118},
    {'r': 255, 'g': 0, 'b': 255},
    {'r': 204, 'g': 27, 'b': 126}], 'fps': 4, 'transition': MatrixAnimationTransition.NONE})