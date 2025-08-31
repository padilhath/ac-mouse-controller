if starting:
    # =============================================================================================
    # Settings
    # =============================================================================================
    mouse_sensitivity = 10
    throttle_increase_time = 100
    throttle_decrease_time = 100
    braking_increase_time = 100
    braking_decrease_time = 100
    hand_braking_increase_time = 50
    hand_braking_decrease_time = 50
    clutch_increase_time = 50
    clutch_decrease_time = 50
    # =============================================================================================
    # Settings
    # =============================================================================================

    def calculate_rates(increase_time, decrease_time):
        if increase_time > 0:
            increase_time = int32_size / (increase_time / system.threadExecutionInterval)
        else:
            increase_time = int32_size

        if decrease_time > 0:
            decrease_time = int32_size / (decrease_time / system.threadExecutionInterval)
        else:
            decrease_time = int32_size

        return increase_time, -decrease_time

    def clamp(value):
        if value > int32_size:
            value = int32_size
        elif value < -int32_size:
            value = -int32_size
        return value
    
    def update_axis(current, target, increase_rate, decrease_rate):
        if current < target:
            current += increase_rate
            return min(current, target)
        elif current > target:
            current += decrease_rate
            return max(current, target)
        return current
    
    from ctypes import windll

    system.setThreadTiming(TimingTypes.HighresSystemTimer)
    system.threadExecutionInterval = 5
    mouse_lock = False
    int32_size = vJoy[0].axisMax
    
    v = vJoy[0]
    v.x, v.y, v.z, v.rx, v.ry, v.rz = (-int32_size,) * 6

    global steering
    steering = 0.0

    global throttle, throttle_increase_rate, throttle_decrease_rate
    throttle = -int32_size
    throttle_increase_rate, throttle_decrease_rate = calculate_rates(
        throttle_increase_time, throttle_decrease_time
    )

    global braking, braking_increase_rate, braking_decrease_rate
    braking = -int32_size
    braking_increase_rate, braking_decrease_rate = calculate_rates(
        braking_increase_time, braking_decrease_time
    )

    global hand_braking, hand_braking_increase_rate, hand_braking_decrease_rate
    hand_braking = -int32_size
    hand_braking_increase_rate, hand_braking_decrease_rate = calculate_rates(
        hand_braking_increase_time, hand_braking_decrease_time
    )

    global clutch, clutch_increase_rate, clutch_decrease_rate
    clutch = -int32_size
    clutch_increase_rate, clutch_decrease_rate = calculate_rates(
        clutch_increase_time, clutch_decrease_time
    )

    global mouse_sensitivity, v


# =================================================================================================
# Assign buttons
# =================================================================================================
v.setButton(0, mouse.leftButton)
v.setButton(1, mouse.rightButton)

# =================================================================================================
# Steering logic
# =================================================================================================
steering = steering + (
    (float(mouse.deltaX) * mouse_sensitivity)
)

steering = clamp(steering)
v.x = steering
# =================================================================================================
# Throttle logic with 33%, 66%, 100%
# =================================================================================================
if keyboard.getKeyDown(Key.W):
    target_throttle = int32_size
elif keyboard.getKeyDown(Key.E):
    target_throttle = -int32_size + (int32_size - -int32_size) * 0.66
elif keyboard.getKeyDown(Key.Q):
    target_throttle = -int32_size + (int32_size - -int32_size) * 0.33
else:
    target_throttle = -int32_size

throttle = update_axis(throttle, target_throttle, throttle_increase_rate, throttle_decrease_rate)
v.y = throttle

# =================================================================================================
# Braking logic with 33%, 66%, 100%
# =================================================================================================
if keyboard.getKeyDown(Key.S):
    target_braking = int32_size
elif keyboard.getKeyDown(Key.D):
    target_braking = -int32_size + (int32_size - -int32_size) * 0.66
elif keyboard.getKeyDown(Key.A):
    target_braking = -int32_size + (int32_size - -int32_size) * 0.33
else:
    target_braking = -int32_size

braking = update_axis(braking, target_braking, braking_increase_rate, braking_decrease_rate)
v.z = braking

# =================================================================================================
# Clutch logic
# =================================================================================================
if keyboard.getKeyDown(Key.C):
    target_clutch = int32_size
else:
    target_clutch = -int32_size

clutch = update_axis(clutch, target_clutch, clutch_increase_rate, clutch_decrease_rate)
v.rx = clutch

# =================================================================================================
# Hand Braking logic
# =================================================================================================
if keyboard.getKeyDown(Key.Space):
    target_hand_braking = int32_size
else:
    target_hand_braking = -int32_size

hand_braking = update_axis(hand_braking, target_hand_braking, hand_braking_increase_rate, hand_braking_decrease_rate)
v.ry = hand_braking

# =================================================================================================
# Mouse Lock logic
# =================================================================================================
if keyboard.getPressed(Key.Y):
    mouse_lock = not mouse_lock
if mouse_lock:
    windll.user32.SetCursorPos(500, 5000)

diagnostics.watch(steering)
diagnostics.watch(throttle)
diagnostics.watch(braking)
diagnostics.watch(clutch)
diagnostics.watch(hand_braking)
