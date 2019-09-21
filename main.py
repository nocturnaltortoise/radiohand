import vlc
import skywriter

i = vlc.Instance("--aout=alsa")
player = i.media_player_new()
player.set_mrl('bbc_radio_five_live.m3u8')

airwheel_pos = 10000

@skywriter.flick()
def flick(start,finish):
    print("Flick: ", start, finish)
    if start == 'south' and finish == 'north':
        player.play()
    elif start == 'north' and finish == 'south':
        player.stop()

@skywriter.airwheel()
def airwheel(delta):
    global airwheel_pos
    airwheel_pos += delta * 4
    if airwheel_pos < 0:
        airwheel_pos = 0
    
    if airwheel_pos > 10000:
        airwheel_pos = 10000
    
    print("airwheel_pos: ", airwheel_pos, "volume set to: ", int(airwheel_pos / 100))
    player.audio_set_volume(int(airwheel_pos / 100))
    print("actual volume: ", player.audio_get_volume())
     


input("Enter to quit")
