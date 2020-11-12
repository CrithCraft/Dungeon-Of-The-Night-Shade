#Dungeon of the NightShade by CrithCraft Feb. 2019 (C)

import pygame
import os, random
pygame.init()

#base of bases varibles
win = pygame.display.set_mode((832, 648))
mixer = pygame.mixer

#directions
main_dir = os.path.split(os.path.abspath('__file__'))[0]  # Program's diretory


#load_textures_start

icon_texture = os.path.join(main_dir, 'images/icon.png')
pygame.display.set_icon(pygame.image.load(icon_texture))
#mobs

#slime
slime_texture_1 = os.path.join(main_dir, 'images/mobs/slime/slime_1.png')
slime_texture_2 = os.path.join(main_dir, 'images/mobs/slime/slime_2.png')

#bonny
bonny_texture_1 = os.path.join(main_dir, 'images/mobs/bonny/bonny_1.png')
bonny_texture_2 = os.path.join(main_dir, 'images/mobs/bonny/bonny_2.png')

#monkey
monkey_texture_1 = os.path.join(main_dir, 'images/mobs/monkey/monkey_1.png')
monkey_texture_2 = os.path.join(main_dir, 'images/mobs/monkey/monkey_2.png')

#down
player_down_1_texture = os.path.join(main_dir, 'images/player/player_down_1.png')
player_down_2_texture = os.path.join(main_dir, 'images/player/player_down_2.png')

#up
player_up_1_texture = os.path.join(main_dir, 'images/player/player_up_1.png')
player_up_2_texture = os.path.join(main_dir, 'images/player/player_up_2.png')

#left
player_left_1_texture = os.path.join(main_dir, 'images/player/player_left_1.png')
player_left_2_texture = os.path.join(main_dir, 'images/player/player_left_2.png')

#right
player_right_1_texture = os.path.join(main_dir, 'images/player/player_right_1.png')
player_right_2_texture = os.path.join(main_dir, 'images/player/player_right_2.png')

#player died
player_died_texture = os.path.join(main_dir, 'image/player/player_died.png')

#player get sword
player_get_sword_texture = os.path.join(main_dir, 'images/player/player_get_sword.png')

#player attack

#up
player_attack_up_3 = os.path.join(main_dir, 'images/player/player_up_attack_3.png')
player_attack_up_2 = os.path.join(main_dir, 'images/player/player_up_attack_2.png')
player_attack_up_1 = os.path.join(main_dir, 'images/player/player_up_attack_1.png')

#down
player_attack_down_3 = os.path.join(main_dir, 'images/player/player_down_attack_3.png')
player_attack_down_2 = os.path.join(main_dir, 'images/player/player_down_attack_2.png')
player_attack_down_1 = os.path.join(main_dir, 'images/player/player_down_attack_1.png')

#map


#map_animation

#map animation end

#center
map_0000_texture = os.path.join(main_dir, 'images/map/map_0000.png')
map_0000_dark_awake_texture = os.path.join(main_dir, 'images/map/map_0000_dark_awake.png')
map_0000_night_texture = os.path.join(main_dir, 'images/map/map_0000_night.png')
map_0000_bloodsun_texture = os.path.join(main_dir, 'images/map/map_0000_bloodsun.png')

#left
map_0010_texture = os.path.join(main_dir, 'images/map/map_0010.png')
map_0010_dark_awake_texture = os.path.join(main_dir, 'images/map/map_0010_dark_awake.png')
map_0010_night_texture = os.path.join(main_dir, 'images/map/map_0010_night.png')
map_0010_bloodsun_texture = os.path.join(main_dir, 'images/map/map_0010_bloodsun.png')

map_0020_texture = os.path.join(main_dir, 'images/map/map_0020.png')
map_0020_dark_awake_texture = os.path.join(main_dir, 'images/map/map_0020_dark_awake.png')
map_0020_night_texture = os.path.join(main_dir, 'images/map/map_0020_night.png')
#down
map_0100_texture = os.path.join(main_dir, 'images/map/map_0100.png')
map_0100_dark_awake_texture = os.path.join(main_dir, 'images/map/map_0100_dark_awake.png')
map_0100_night_texture = os.path.join(main_dir, 'images/map/map_0100_night.png')

map_0120_texture = os.path.join(main_dir, 'images/map/map_0120.png')
map_0120_dark_awake_texture = os.path.join(main_dir, 'images/map/map_0120_dark_awake.png')
map_0120_night_texture = os.path.join(main_dir, 'images/map/map_0120_night.png')
#sub_rotates
map_0110_texture = os.path.join(main_dir, 'images/map/map_0110.png')
map_0110_dark_awake_texture = os.path.join(main_dir, 'images/map/map_0110_dark_awake.png')
map_0110_night_texture = os.path.join(main_dir, 'images/map/map_0110_night.png')

map_0220_texture = os.path.join(main_dir, 'images/map/map_0220.png')
map_0220_dark_awake_texture = os.path.join(main_dir, 'images/map/map_0220_dark_awake.png')
map_0220_night_texture = os.path.join(main_dir, 'images/map/map_0220_night.png')


#map others
evil_tree_1 = os.path.join(main_dir, 'images/map/other/tree_1.png')
evil_tree_2 = os.path.join(main_dir, 'images/map/other/tree_2.png')
evil_tree_3 = os.path.join(main_dir, 'images/map/other/tree_3.png')
evil_tree_4 = os.path.join(main_dir, 'images/map/other/tree_4.png')

#load textures_end


#load sound_start

sound_exit = os.path.join(main_dir, 'sound/sound_exit.wav')
sound_get_item = os.path.join(main_dir, 'sound/sound_get_item.wav')
sound_attack = os.path.join(main_dir, 'sound/sound_attack.wav')
sound_hurt = os.path.join(main_dir, 'sound/sound_hurt.wav')
sound_evil_destroy = os.path.join(main_dir, 'sound/sound_evil_destroy.wav')

#mob sound

#slime
sound_slime_attack = os.path.join(main_dir, 'sound/sound_slime_attack.wav')
sound_slime_death = os.path.join(main_dir, 'sound/sound_slime_death.wav')

#load sound_end

#load music_start
music_fill_1 = os.path.join(main_dir, 'music/Greenfield.ogg')
music_fill_2 = os.path.join(main_dir, 'music/DarkAwake.ogg')
music_fill_3 = os.path.join(main_dir, 'music/BloodSun.ogg')
#load music_end

#GUI load_texture_start
heart_texture_1 = os.path.join(main_dir, 'images/GUI/heart/heart_1.png')
heart_status = pygame.image.load(heart_texture_1)

event_texture_1 = os.path.join(main_dir, 'images/GUI/event_label/event_1.png')
event_texture_2 = os.path.join(main_dir, 'images/GUI/event_label/event_2.png')
event_texture_3 = os.path.join(main_dir, 'images/GUI/event_label/event_3.png')
event_status = pygame.image.load(event_texture_1)

GUI_texture_get = os.path.join(main_dir, 'images/GUI/GUI.png')
GUI_texture = pygame.image.load(GUI_texture_get)
#GUI load_texture_end

#inicilization music_start
sound = mixer.Sound(sound_exit)
channel = sound.play()

music = mixer.Sound(sound_exit)
channel_music = music.play()
#inicilization music_end


#Game varibles
player_texture = pygame.image.load(player_down_1_texture)

screen_width = 832
screen_height = 576
pygame.display.set_caption("Dungeon")

width = 64
height = 64
x = screen_width/2-width/2
y = screen_height/2-height/2
vel = 8
player_dir = "down"
last_player_dir = "down"
key_press = None


prev_x = x
prev_y = y
t = 0

live_player = 90

#EVENTS
event = "GET_SWORD_EVENT"

#MAP EVENT
map_event = "Normal"
map_texture = pygame.image.load(map_0000_texture)
map_level = 0000
play_sound_event = 0

#MOB VARIBLES

#mob list
#0-2 - Slime
#3-5 - Skeleton

#slime varibles
animation_mob = 0
kol_vo_mobs = 6
mob_exist = []

for i in range(0,kol_vo_mobs):
    mob_exist.append(1)

#slime varibles
slime_x = []
slime_y = []
slime_prev_x = []
slime_prev_y = []
slime_radius = 256
speed_slime = 6

#skeleton varibles
skeleton_x = []
skeleton_y = []
skeleton_prev_x = []
skeleton_prev_y = []
skeleton_radius = 192
speed_skeleton = 6

for i in range(0,kol_vo_mobs+1):
    mob_exist.append(1)
    #slime
    slime_x.append(1)
    slime_y.append(1)
    #skeleton
    skeleton_x.append(1)
    skeleton_y.append(1)
    #slime
    slime_prev_x.append(1)
    slime_prev_y.append(1)
    #skeleton
    skeleton_prev_x.append(1)
    skeleton_prev_y.append(1)

#map mobs cordinate

#slime - 1
slime_x[1] = (64+64)
slime_y[1] = (128+64)

#slime - 2
slime_x[2] = (128+64)
slime_y[2] = (192+64)

#slime - 3
slime_x[3] = (512)
slime_y[3] = (256+64)

#skeleton - 4
skeleton_x[4] = 64+64
skeleton_y[4] = 128+64

#skeleton - 5
skeleton_x[5] = 128+64
skeleton_y[5] = 192+64

#skeleton - 6
skeleton_x[6] = 512
skeleton_y[6] = 256+64





# map cordinate - 0 - up , 0 - down, 0 - left, 0 - right.
map_level = 0000
tick = 0
animation = 0

#map_tick
animation_tick_map = 1

#write time in tick
Exit_time = 150

#Map events
map_0000_event = "Dark Awake"
map_0010_event = "Dark Awake"
map_0020_event = "Dark Awake"
map_0100_event = "Dark Awake"
map_0110_event = "Dark Awake"
map_0120_event = "Dark Awake"
map_0220_event = "Dark Awake"



#Functions
def Collision(first_x, first_y, first_width, first_height,  second_x, second_y, second_width, second_height):
    if (first_x + first_width >= second_x) and (first_x <= second_x + second_width) and (first_y + first_height >= second_y) and (first_y <= second_y + second_height):
        return True
    else:
        return False



def MapCheck(Number_Map, Direction):
    #Up
    if Number_Map == 0110 and Direction == "Up":
        return True
    elif Number_Map == 0100 and Direction == "Up":
        return True
    elif Number_Map == 0120 and Direction == "Up":
        return True
    elif Number_Map == 0220 and Direction == "Up":
        return True
    #Down
    elif Number_Map == 0000 and Direction == "Down":
        return True
    elif Number_Map == 0010 and Direction == "Down":
        return True
    elif Number_Map == 0020 and Direction == "Down":
        return True
    elif Number_Map == 0120 and Direction == "Down":
        return True
    #Left
    elif Number_Map == 0110 and Direction == "Left":
        return True
    elif Number_Map == 0100 and Direction == "Left":
        return True
    elif Number_Map == 0000 and Direction == "Left":
        return True
    elif Number_Map == 0010 and Direction == "Left":
        return True
    #Right
    elif Number_Map == 0110 and Direction == "Right":
        return True
    elif Number_Map == 0120 and Direction == "Right":
        return True
    elif Number_Map == 0020 and Direction == "Right":
        return True
    elif Number_Map == 0010 and Direction == "Right":
        return True
    else:
        return False



def MapGetNumber(Number_Map, Direction):
    #Up
    if Number_Map == 0110 and Direction == "Up":
        return 0010
    if Number_Map == 0100 and Direction == "Up":
        return 0000
    #Up
    if Number_Map == 0120 and Direction == "Up":
        return 0020
    if Number_Map == 0220 and Direction == "Up":
        return 0120
    #Down
    if Number_Map == 0000 and Direction == "Down":
        return 0100
    if Number_Map == 0020 and Direction == "Down":
        return 0120
    if Number_Map == 0010 and Direction == "Down":
        return 0110
    if Number_Map == 0120 and Direction == "Down":
        return 0220
    #Left
    if Number_Map == 0100 and Direction == "Left":
        return 0110
    if Number_Map == 0110 and Direction == "Left":
        return 0120
    if Number_Map == 0000 and Direction == "Left":
        return 0010
    if Number_Map == 0010 and Direction == "Left":
        return 0020
    #Right
    if Number_Map == 0110 and Direction == "Right":
        return 0100
    if Number_Map == 0120 and Direction == "Right":
        return 0110
    if Number_Map == 0010 and Direction == "Right":
        return 0000
    if Number_Map == 0020 and Direction == "Right":
        return 0010


def MapGetTexture(Number_Map):
    if Number_Map == 0000:
        if map_0000_event == "Normal":
            return pygame.image.load(map_0000_texture), "Normal"
        elif map_0000_event == "Dark Awake":
            return pygame.image.load(map_0000_dark_awake_texture), "Dark Awake"
        elif map_0000_event == "Night":
            return pygame.image.load(map_0000_night_texture), "Night"
        elif map_0000_event == "Blood Sun":
            return pygame.image.load(map_0000_bloodsun_texture), "Blood Sun"

    if Number_Map == 0100:
        if map_0100_event == "Normal":
            return pygame.image.load(map_0100_texture), "Normal"
        elif map_0100_event == "Dark Awake":
            return pygame.image.load(map_0100_dark_awake_texture), "Dark Awake"
        elif map_0100_event == "Night":
            return pygame.image.load(map_0100_night_texture), "Night"
        elif map_0100_event == "Blood Sun":
            return pygame.image.load(map_0100_bloodsun_texture), "Blood Sun"

    if Number_Map == 0010:
        if map_0010_event == "Normal":
            return pygame.image.load(map_0010_texture), "Normal"
        elif map_0010_event == "Dark Awake":
            return pygame.image.load(map_0010_dark_awake_texture), "Dark Awake"
        elif map_0010_event == "Night":
            return pygame.image.load(map_0010_night_texture), "Night"
        elif map_0010_event == "Blood Sun":
            return pygame.image.load(map_0010_bloodsun_texture), "Blood Sun"

    if Number_Map == 0020:
        if map_0020_event == "Normal":
            return pygame.image.load(map_0020_texture), "Normal"
        elif map_0020_event == "Dark Awake":
            return pygame.image.load(map_0020_dark_awake_texture), "Dark Awake"
        elif map_0020_event == "Night":
            return pygame.image.load(map_0020_night_texture), "Night"
        elif map_0020_event == "Blood Sun":
            return pygame.image.load(map_0020_bloodsun_texture), "Blood Sun"

    if Number_Map == 0110:
        if map_0110_event == "Normal":
            return pygame.image.load(map_0110_texture), "Normal"
        elif map_0110_event == "Dark Awake":
            return pygame.image.load(map_0110_dark_awake_texture), "Dark Awake"
        elif map_0110_event == "Night":
            return pygame.image.load(map_0110_night_texture), "Night"
        elif map_0110_event == "Blood Sun":
            return pygame.image.load(map_0110_bloodsun_texture), "Blood Sun"

    if Number_Map == 0120:
        if map_0120_event == "Normal":
            return pygame.image.load(map_0120_texture), "Normal"
        elif map_0120_event == "Dark Awake":
            return pygame.image.load(map_0120_dark_awake_texture), "Dark Awake"
        elif map_0120_event == "Night":
            return pygame.image.load(map_0120_night_texture), "Night"
        elif map_0120_event == "Blood Sun":
            return pygame.image.load(map_0120_bloodsun_texture), "Blood Sun"

    if Number_Map == 0220:
        if map_0220_event == "Normal":
            return pygame.image.load(map_0220_texture), "Normal"
        elif map_0220_event == "Dark Awake":
            return pygame.image.load(map_0220_dark_awake_texture), "Dark Awake"
        elif map_0220_event == "Night":
            return pygame.image.load(map_0220_night_texture), "Night"
        elif map_0220_event == "Blood Sun":
            return pygame.image.load(map_0220_bloodsun_texture), "Blood Sun"



#Load texture in first time
map_texture, map_event = MapGetTexture(map_level)


run = True
while run:
    pygame.time.delay(50)
    #quit event


    if not (channel_music.get_busy()):
        if map_event == "Normal":
            music = mixer.Sound(music_fill_1)
        if map_event == "Dark Awake":
            music = mixer.Sound(music_fill_2)
        if map_event == "Blood Sun":
            music = mixer.Sound(music_fill_3)
        if map_event == "Night":
            music = mixer.Sound(music_fill_1)
        channel_music = music.play()



    #slime UI start
    for i in range(1,3+1):
        if mob_exist[i] == 1:
            if (x-slime_radius < slime_x[i]) and (x+slime_radius > slime_x[i]):
                if (x - 64 > slime_x[i]):
                    slime_prev_y[i] = slime_y[i]
                    slime_prev_x[i] = slime_x[i]
                    if (y-slime_radius < slime_y[i]) and (y+slime_radius > slime_y[i]):
                        slime_x[i] += 1
                    if x - slime_x[i] != 0:
                        slime_y[i] = ((y - slime_y[i]) * ((slime_x[i] + 1) - slime_x[i]) / (x - slime_x[i])) + slime_y[i]
                if (x + 64 < slime_x[i]):
                    slime_prev_y[i] = slime_y[i]
                    slime_prev_x[i] = slime_x[i]
                    if (y-slime_radius < slime_y[i]) and (y+slime_radius > slime_y[i]):
                        slime_x[i] -= 1
                    if x - slime_x[i] != 0:
                        slime_y[i] = ((slime_y[i] - y) * ((slime_x[i] - 1) - x))/(slime_x[i] - x) + y
                if (x + 64 >= slime_x[i]) and (x - 64 <= slime_x[i]) and (y-slime_radius < slime_y[i]) and (y+slime_radius > slime_y[i]):
                    if slime_y[i] < y + 64:
                        slime_y[i] += speed_slime/2
                    if slime_y[i] > y - 64:
                        slime_y[i] -= speed_slime/2
    #slime UI end

    #skeleton UI start
    for i in range(4,6+1):
        if mob_exist[i] == 1:
            if (x-skeleton_radius < skeleton_x[i]) and (x+skeleton_radius > skeleton_x[i]):
                if (x - 64 > skeleton_x[i]):
                    skeleton_prev_y[i] = skeleton_y[i]
                    skeleton_prev_x[i] = skeleton_x[i]
                    if (y-skeleton_radius < skeleton_y[i]) and (y+skeleton_radius > skeleton_y[i]):
                        skeleton_x[i] += 1
                    if x - skeleton_x[i] != 0:
                        skeleton_y[i] = ((y - skeleton_y[i]) * ((skeleton_x[i] + 1) - skeleton_x[i]) / (x - skeleton_x[i])) + skeleton_y[i]
                if (x + 64 < skeleton_x[i]):
                    skeleton_prev_y[i] = skeleton_y[i]
                    skeleton_prev_x[i] = skeleton_x[i]
                    if (y-skeleton_radius < skeleton_y[i]) and (y+skeleton_radius > skeleton_y[i]):
                        skeleton_x[i] -= 1
                    if x - skeleton_x[i] != 0:
                        skeleton_y[i] = ((skeleton_y[i] - y) * ((skeleton_x[i] - 1) - x))/(skeleton_x[i] - x) + y
                if (x + 64 >= skeleton_x[i]) and (x - 64 <= skeleton_x[i]) and (y-skeleton_radius < skeleton_y[i]) and (y+skeleton_radius > skeleton_y[i]):
                    if skeleton_y[i] < y + 64:
                        skeleton_y[i] += speed_skeleton/2
                    if skeleton_y[i] > y - 64:
                        skeleton_y[i] -= speed_skeleton/2
        #skeleton UI end





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #set up control_start

    if live_player == 0:
        run = False

    keys = pygame.key.get_pressed()

    #attack
    if keys[pygame.K_LSHIFT] and keys[pygame.K_UP] and not (keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT]):
        if player_dir != "attack_up":
            animation = 0
            sound = mixer.Sound(sound_attack)
            channel = sound.play()
            last_player_texture = player_texture
            player_dir = last_player_dir
            y -= 64
            player_texture = pygame.image.load(player_attack_up_1)
            player_dir = "attack_up"
        else:
            #animation_start
            if player_dir != "attack_up":
                player_dir = "attack_up"

            if animation == 0:
                player_texture = pygame.image.load(player_attack_up_1)
                animation += 1
            elif animation == 1:
                player_texture = pygame.image.load(player_attack_up_2)
                animation += 1
            elif animation == 2:
                player_texture = pygame.image.load(player_attack_up_3)
                animation += 1
            elif animation != 3:
                animation += 1
    elif player_dir == "attack_up":
        y += 64
        player_texture = last_player_texture
        player_dir = last_player_dir

    if keys[pygame.K_LSHIFT] and keys[pygame.K_DOWN] and not (keys[pygame.K_UP] and keys[pygame.K_LSHIFT]):
        if player_dir != "attack_down":
            animation = 0
            sound = mixer.Sound(sound_attack)
            channel = sound.play()
            last_player_texture = player_texture
            player_dir = last_player_dir
            x -= 64
            player_texture = pygame.image.load(player_attack_down_1)
            player_dir = "attack_down"
        else:
            #animation_start
            if player_dir != "attack_down":
                player_dir = "attack_down"

            if animation == 0:
                player_texture = pygame.image.load(player_attack_down_1)
                animation += 1
            elif animation == 1:
                player_texture = pygame.image.load(player_attack_down_2)
                animation += 1
            elif animation == 2:
                player_texture = pygame.image.load(player_attack_down_3)
                animation += 1
            elif animation != 3:
                animation += 1
    elif player_dir == "attack_down":
        x += 64
        player_texture = last_player_texture
        player_dir = last_player_dir

    #movement

    if keys[pygame.K_UP] and y > vel and not (keys[pygame.K_RIGHT]) and not (keys[pygame.K_LEFT]) and not(keys[pygame.K_LSHIFT]):
        #animation_start
        if player_dir != "up":
            animation = 0
            player_dir = "up"

        if animation == 0:
            player_texture = pygame.image.load(player_up_1_texture)
            animation += 1
        elif animation == 5:
            player_texture = pygame.image.load(player_up_2_texture)
            animation += 1
        elif animation == 10:
            animation = 0
        else:
            animation += 1
        #animation_end
        prev_y = y
        y -= vel

        # down map
        if y <= vel:
            if MapCheck(map_level, "Up") == True:
                sound = mixer.Sound(sound_exit)
                channel = sound.play()
                pygame.time.delay(Exit_time)
                #map_texture = pygame.image.load(map_1_texture)
                y = screen_height - height - vel
                map_level = MapGetNumber(map_level, "Up")
                map_texture, map_event = MapGetTexture(map_level)


    if keys[pygame.K_DOWN] and y < screen_height - height - vel and not (keys[pygame.K_RIGHT]) and not (keys[pygame.K_LEFT]) and not(keys[pygame.K_LSHIFT]):
        #animation_start
        if player_dir != "down":
            animation = 0
            player_dir = "down"

        if animation == 0:
            player_texture = pygame.image.load(player_down_1_texture)
            animation += 1
        elif animation == 5:
            player_texture = pygame.image.load(player_down_2_texture)
            animation += 1
        elif animation == 10:
            animation = 0
        else:
            animation += 1
        #animation_end
        prev_y = y
        y += vel

        # down map
        if y >= screen_height - height - vel:
            if MapCheck(map_level, "Down") == True:
                sound = mixer.Sound(sound_exit)
                channel = sound.play()
                pygame.time.delay(Exit_time)
                y = vel
                map_level = MapGetNumber(map_level, "Down")
                map_texture, map_event = MapGetTexture(map_level)


    if keys[pygame.K_LEFT] and x > vel and not (keys[pygame.K_DOWN])  and not (keys[pygame.K_UP]) and not(keys[pygame.K_LSHIFT]):

        #set key pressed
        key_press = "left"

        #animation_start
        if player_dir != "left":
            animation = 0
            player_dir = "left"

        if animation == 0:
            player_texture = pygame.image.load(player_left_1_texture)
            animation += 1
        elif animation == 5:
            player_texture = pygame.image.load(player_left_2_texture)
            animation += 1
        elif animation == 10:
            animation = 0
        else:
            animation += 1
        #animation_end
        prev_x = x
        x -= vel

        #left map
        if x <= vel:
            if MapCheck(map_level, "Left") == True:
                sound = mixer.Sound(sound_exit)
                channel = sound.play()
                pygame.time.delay(Exit_time)
                x = screen_width - width - vel
                map_level = MapGetNumber(map_level, "Left")
                map_texture, map_event = MapGetTexture(map_level)




    if keys[pygame.K_RIGHT] and not (keys[pygame.K_DOWN])  and not (keys[pygame.K_UP]) and x < screen_width - width - vel and not(keys[pygame.K_LSHIFT]):
        #animation_start
        if player_dir != "right":
            animation = 0
            player_dir = "right"

        if animation == 0:
            player_texture = pygame.image.load(player_right_1_texture)
            animation += 1
        elif animation == 5:
            player_texture = pygame.image.load(player_right_2_texture)
            animation += 1
        elif animation == 10:
            animation = 0
        else:
            animation += 1
        #animation_end
        prev_x = x
        x += vel

        #right map
        if x >= screen_width - width - vel:
            if MapCheck(map_level, "Right") == True:
                sound = mixer.Sound(sound_exit)
                channel = sound.play()
                pygame.time.delay(Exit_time)
                x = vel
                map_level = MapGetNumber(map_level, "Right")
                map_texture, map_event = MapGetTexture(map_level)


    #animation enemies
    if animation_mob % 7 >= 0 and animation_mob % 7 <= 3:
        #slime
        slime_texture = pygame.image.load(slime_texture_1)
        #bonny
        bonny_texture = pygame.image.load(bonny_texture_1)
        #monkey
        monkey_texture = pygame.image.load(monkey_texture_1)
        animation_mob += 1
    else:
        #slime
        slime_texture = pygame.image.load(slime_texture_2)
        #bonny
        bonny_texture = pygame.image.load(bonny_texture_2)
        #monkey
        monkey_texture = pygame.image.load(monkey_texture_2)
        animation_mob += 1

    if animation_mob == 9:
        animation_mob = 0




    #set up control_end

    #map color-fill start
    if map_event == "Normal":
        win.fill((192, 248, 56))
    elif map_event == "Dark Awake":
        win.fill((169, 123, 181))
    elif map_event == "Night":
        win.fill((138, 176, 128))
    elif map_event == "Blood Sun":
        win.fill((181, 123, 125))
    #map color-fill end

    #map texture
    win.blit(map_texture, (0, 0))



    #collision_box
    #pygame.draw.rect(win, (0, 0, 255), (0, 0, screen_width, 128))
    #pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    #pygame.draw.rect(win, (0, 255, 0), (352, 224, 128, 128))

    # Collision Map_start
    if map_level == 0000:
        if Collision(x, y, width, height, 0, 0, screen_width, 128):
            x = prev_x
            y = prev_y
        #for mobs

        #for slime
        for i in range(1,3+1):
            for k in range(1,3+1):
                if Collision(slime_x[i], slime_y[i], width, height, 0, 0, screen_width, 128):
                    if mob_exist[i] == 1 and mob_exist[k] == 1:
                        slime_x[i] = slime_prev_x[i]
                        slime_y[i] = slime_prev_y[i]
                if Collision(slime_x[i], slime_y[i], width, height, slime_x[k], slime_y[k], width, height) and k != i:
                    if mob_exist[i] == 1 and mob_exist[k] == 1:
                        slime_x[i] = slime_prev_x[i]
                        slime_y[i] = slime_prev_y[i]

        for i in range(4,6+1):
            for k in range(4,6+1):
                if Collision(skeleton_x[i], skeleton_y[i], width, height, 352, 224, 128, 128):
                    if mob_exist[i] == 1 and mob_exist[k] == 1:
                        skeleton_x[i] = skeleton_prev_x[i]
                        skeleton_y[i] = skeleton_prev_y[i]
                if Collision(skeleton_x[i], skeleton_y[i], width, height, skeleton_x[k], skeleton_y[k], width, height) and k != i:
                    if mob_exist[i] == 1 and mob_exist[k] == 1:
                        skeleton_x[i] = skeleton_prev_x[i]
                        skeleton_y[i] = skeleton_prev_y[i]
                        

    if map_level == 0100:
        if Collision(x, y, width, height, 0*4, 70*4, 88*4, 74*4) or Collision(x, y, width, height, 120*4, 70*4, 88*4, 74*4):
            x = prev_x
            y = prev_y

    if map_level == 0010:
        if Collision(x, y, width, height, 0, 0, screen_width, 128):
            x = prev_x
            y = prev_y
        elif Collision(x, y, width, height, 0, 0, screen_width - 256, 448):
            x = prev_x
            y = prev_y

    if map_level == 0020:
        if Collision(x, y, width, height, 0, 0, screen_width, 448):
            x = prev_x
            y = prev_y

    if map_level == 0120:
        if Collision(x, y, width, height, 352, 224, 128, 128):
            x = prev_x
            y = prev_y
    if map_level == 0110:
        if Collision(x, y, width, height, 97*4, 70*4, 111*4, 71*4):
            x = prev_x
            y = prev_y





    # Collision Map_end

    #slime generation

    #write self varibles

    if map_level == 0000:
        for i in range(1,3+1):
            if mob_exist[i] == 1:
                if random.randint(1,100) == 10:
                    sound = mixer.Sound(sound_slime_attack)
                    channel = sound.play()

                if live_player % 10 == 0 and live_player != 0 and live_player != 90:
                        sound = mixer.Sound(sound_hurt)
                        channel = sound.play()
                if Collision(x, y, width, height, slime_x[i], slime_y[i], 64, 64) and player_dir != "attack_up" and player_dir != "attack_down":
                    live_player -= 1
                    slime_x[i] = slime_prev_x[i]
                    slime_y[i] = slime_prev_y[i]
                    if live_player % 5 == 0 and live_player != 0:
                        sound = mixer.Sound(sound_hurt)
                        channel = sound.play()
                    x = prev_x
                    y = prev_y
                win.blit(slime_texture, (slime_x[i], slime_y[i]))

            else:
                pass


            if animation == 0 and mob_exist[i] == 1:
                if Collision(x+64, y+64, width, height, slime_x[i], slime_y[i], 64, 64) and player_dir == "attack_up":
                    sound = mixer.Sound(sound_slime_death)
                    channel = sound.play()
                    mob_exist[i] = 0
                if Collision(x+64, y+64, width, height, slime_x[i], slime_y[i], 64, 64) and player_dir == "attack_down":
                    sound = mixer.Sound(sound_slime_death)
                    channel = sound.play()
                    mob_exist[i] = 0
            

            if animation == 2 and mob_exist[i] == 1:
                if Collision(x, y, width+64, height+64, slime_x[i], slime_y[i], 64, 64) and player_dir == "attack_up":
                    mob_exist[i] = 0
                    sound = mixer.Sound(sound_slime_death)
                    channel = sound.play()
                if Collision(x, y, width, height, slime_x[i], slime_y[i], 64, 64) and player_dir == "attack_down":
                    mob_exist[i] = 0
                    sound = mixer.Sound(sound_slime_death)
                    channel = sound.play()
            #if Collision(x, y, width, height, slime_x[i], slime_y[i], 64, 64)

    if map_level == 0120:
        for i in range(4,6+1):
            if mob_exist[i] == 1:

                if live_player % 10 == 0 and live_player != 0 and live_player < 90 :
                    sound = mixer.Sound(sound_hurt)
                    channel = sound.play()

                if Collision(x, y, width, height, skeleton_x[i], skeleton_y[i], 64, 64) and player_dir != "attack_up" and player_dir != "attack_down":
                    if map_event == "Normal":
                        live_player += 1
                    elif map_event == "Dark Awake":
                        live_player -= 1

                    skeleton_x[i] = skeleton_prev_x[i]
                    skeleton_y[i] = skeleton_prev_y[i]
                    x = prev_x
                    y = prev_y
                if map_event == "Normal":
                    #skeleton texture needed
                    win.blit(bonny_texture, (skeleton_x[i], skeleton_y[i]))
                elif map_event == "Dark Awake":
                    win.blit(monkey_texture, (skeleton_x[i], skeleton_y[i]))
            else:
                pass

            if animation == 0 and mob_exist[i] == 1:
                if Collision(x+64, y+64, width, height, skeleton_x[i], skeleton_y[i], 64, 64) and player_dir == "attack_up":
                    sound = mixer.Sound(sound_slime_death)
                    channel = sound.play()
                    mob_exist[i] = 0
                if Collision(x+64, y+64, width, height, skeleton_x[i], skeleton_y[i], 64, 64) and player_dir == "attack_down":
                    sound = mixer.Sound(sound_slime_death)
                    channel = sound.play()
                    mob_exist[i] = 0


            if animation == 2 and mob_exist[i] == 1:
                if Collision(x, y, width+64, height+64, skeleton_x[i], skeleton_y[i], 64, 64) and player_dir == "attack_up":
                    mob_exist[i] = 0
                    sound = mixer.Sound(sound_slime_death)
                    channel = sound.play()
            if Collision(x, y, width, height, skeleton_x[i], skeleton_y[i], 64, 64) and player_dir == "attack_down":
                mob_exist[i] = 0
                sound = mixer.Sound(sound_slime_death)
                channel = sound.play()

    #clear map 0000
    mob_map = 0
    for i in range(1,3):
        mob_map += mob_exist[i]
    #after calculate mobs on map 0000
    if mob_map == 0 and play_sound_event == 0:
        map_0000_event = "Normal"
        sound = mixer.Sound(sound_evil_destroy)
        channel = sound.play()
        play_sound_event = 1



    #player draw
    win.blit(player_texture, (x, y))




    #GUI Draw
    win.blit(GUI_texture, (0, screen_height))

    if live_player <= 90 and live_player > 60:
        win.blit(heart_status, (32, screen_height))
        win.blit(heart_status, (32+64, screen_height))
        win.blit(heart_status, (32+128, screen_height))
    elif live_player <= 60 and live_player > 30:
        win.blit(heart_status, (32+64 , screen_height))
        win.blit(heart_status, (32+128, screen_height))
    elif live_player <= 30 and live_player > 0:
        win.blit(heart_status, (32+128, screen_height))

    if map_event == "Normal":
        event_status = pygame.image.load(event_texture_1)
        win.blit(event_status, (256 - 18, screen_height + 4))
    elif map_event == "Dark Awake":
        event_status = pygame.image.load(event_texture_3)
        win.blit(event_status, (256 - 18, screen_height + 4))
    elif map_event == "Night":
        event_status = pygame.image.load(event_texture_2)
        win.blit(event_status, (256 - 14, screen_height + 4))
    elif map_event == "Blood Sun":
        event_status = pygame.image.load(event_texture_3)
        win.blit(event_status, (256 - 14, screen_height + 4))

    
    pygame.display.update()

pygame.quit()
