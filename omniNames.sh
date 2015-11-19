#!/bin/sh

killall omniNames [omniEvents]

rm /var/log/omniORB/omninames*

omniNames -start -logdir /var/log/omniORB/ &
