# anytime-fitness-gym-booker
All of the appointments at my gym kept getting booked so I made a Python script to book it automatically at midnight.

# How to use
This uses selenium and the Gecko driver for Mozilla Firefox. Setup a cron job to run this script on a Linux/Unix box with a GUI.


You have to add your keyfob, lastname, the member authentication page, your club page, and your desired time to the environment variables at the top of `joiner.py`. This script books 2 days in advance.


Run ``python joiner.py`` to use the script.

Enjoy!
