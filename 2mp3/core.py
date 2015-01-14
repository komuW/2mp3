# -*- coding: utf-8 -*-

"""
2mp3.core
~~~~~~~~~~
The main module that converts your files to awesome mp3's.
"""

import envoy


cwd = None

# check whether ffmpeg is installed
ffmpeg = envoy.run('ffmpeg')

if 'No such file or directory' in ffmpeg.std_err:
    # ffmpeg isn't installed, install it.
    out = envoy.run("echo It seems like you dont have ffmpeg installed. \
                     Dont worry, 2mp3 will install it in a giffy").std_out
    print out

    y1 = envoy.run('sudo apt-add-repository -y ppa:jon-severinsson/ffmpeg') 
    y2 = envoy.run('sudo apt-get -y update')
    y3 = envoy.run('sudo apt-get -y install ffmpeg')

    out = "\n ffmpeg has been succesfully installed. continuing with conversion...\n"
    print out



the_cmd = 'for i in *.*; do ffmpeg -i "$i" -f mp3 "$i".mp3; done'
convert = envoy.run(the_cmd)

cwd = '/vagrant/2mp3/test_songs'
list_all_in_dir = envoy.run('ls', cwd=cwd).std_out
split_em = list_all_in_dir.split('\n')
# remove empty items from list
split_em = filter(None, split_em)

print "BEGINNING CONVERSION, this may take a while.\n"
for song in split_em:
    the_cmd = 'ffmpeg -i "{0}" -f mp3 "{1}".mp3'.format(song, song)
    print "CONVERTING: {0} : INTO AN MP3 FILE...".format(song)
    convert = envoy.run(the_cmd, cwd=cwd)

import pdb;pdb.set_trace()
print "ok"
print "ok"
print "ok"
print "cool"

#run(command, data=None, timeout=None, kill_timeout=None, env=None, cwd=None)